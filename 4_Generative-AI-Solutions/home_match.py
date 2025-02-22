# A starter file for the HomeMatch application if you want to build your solution in a Python program instead of a notebook.

###########################################
# Step 1: Setting Up the Python Application
###########################################

import os
import pandas as pd
import shutil

os.environ["OPENAI_API_KEY"] = "YOUR API KEY"
os.environ["OPENAI_API_BASE"] = "https://openai.vocareum.com/v1"

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate

from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field, NonNegativeInt
from fastapi.encoders import jsonable_encoder

MODEL_NAME = "gpt-3.5-turbo"
CHROMA_PATH = "chroma"
CSV_PATH = "property_listing.csv"

# Load LLM
llm = ChatOpenAI(model_name=MODEL_NAME, temperature=0.0)

#########################################
# Step 2: Generating Real Estate Listings
#########################################

# Property Pydantic Model
class Property(BaseModel):
    """
    A property definition.

    Attributes:
    - suburb: str
    - postcode: NonNegativeInt
    - suburb_description: str
    - price_guide: NonNegativeInt
    - bedrooms_count: NonNegativeInt
    - bathrooms_count: NonNegativeInt
    - buildup_area_sqm: NonNegativeInt
    - land_area_sqm: NonNegativeInt
    - frontage_m: NonNegativeInt
    - property_description: str
    """
    suburb: str = Field(description="The suburb or council where the property is located.")
    postcode: NonNegativeInt = Field(description="Suburb postcode for handling mails.")
    suburb_description: str = Field(description="A description of the suburb or locality.")
    price_guide: NonNegativeInt = Field(description="The price of the property in AUD.")
    bedrooms_count: NonNegativeInt = Field(description="The number of bedrooms in the property.")
    bathrooms_count: NonNegativeInt = Field(description="The number of bathrooms in the property.")
    buildup_area_sqm: NonNegativeInt = Field(description="The size of the house in square meter.")
    land_area_sqm: NonNegativeInt = Field(description="The size of the land in square meter.")
    frontage_m: NonNegativeInt = Field(description="Property frontage length in meters.")
    property_description: str = Field(description="A description of the property.")


class PropertyListing(BaseModel):
    """
    A collection of properties: real estate listing.

    Attributes:
    - listings: List[Property]
    """
    listings: list[Property] = Field(description="A list of properties.")


instruction = f"Generate a CSV file with at least 15 (fifteen) real estate property listings of different suburbs."

sample_listing = \
"""
Suburb: North Adelaide
Postcode: 5006
Price Guide: $975,000
Bedrooms Count: 3
Bathrooms Count: 2
Buildup Area: 240 sqm
Land Area: 350 sqm
Frontage: 12 m
Property Description: Tucked away in North Adelaide's leafy streets and laneways, nestling gracefully among heritage buildings, a masterclass in terraced townhouse design. This townhouse is bespoke. Showcasing the finest fixtures, fittings and technology: from the engineered oak floors to the feature lighting, from the bespoke cabinetry to the tasteful palette of stone benchtops and tiles, from state-of-the-art appliances to the home security system.
Suburb Description: North Adelaide is a predominantly residential precinct and suburb of the City of Adelaide in South Australia, situated, close to Central Business District, north of the River Torrens and within the Adelaide Park Lands. Laid out in a grid plan in three sections by Colonel William Light in 1837, the suburb contains many grand old mansions. North Adelaide is well served by road, although in peak hour some roads, particularly O'Connell Street and Melbourne Street, are quite congested.
"""

# Generate Parsed Output
parser = PydanticOutputParser(pydantic_object=PropertyListing)

# Printing the Prompt
prompt = PromptTemplate(
    template="{instruction}\n{sample}\n{format_instructions}\n",
    input_variables=["instruction", "sample"],
    partial_variables={"format_instructions": parser.get_format_instructions},
)

query = prompt.format(
    instruction=instruction,
    sample=sample_listing,
)
print(query)

# Get the response
response = llm.invoke(query)

# create a dataframe from the response
result = parser.parse(response.content)
df = pd.DataFrame(jsonable_encoder(result.listings))
print(df.head())

# save the dataframe to a csv file
df.to_csv(CSV_PATH, index_label = 'id')

###############################################
# Step 3: Storing Listings in a Vector Database
###############################################

embedding_function = OpenAIEmbeddings

df = pd.read_csv(CSV_PATH)
documents = []
for index, row in df.iterrows():

    page_content = "|".join([
        f"suburb: {row['suburb']}",
        f"postcode: {row['postcode']}",
        f"suburb_description: {row['suburb_description']}",
        f"price_guide: {row['price_guide']}",
        f"bedrooms_count: {row['bedrooms_count']}",
        f"bathrooms_count: {row['bathrooms_count']}",
        f"buildup_area_sqm: {row['buildup_area_sqm']}",
        f"land_area_sqm: {row['land_area_sqm']}",
        f"frontage_m: {row['frontage_m']}",
        f"property_description: {row['property_description']}",
    ])

    documents.append(
        Document(
            page_content=page_content, metadata={'id': str(index)}
        )
    )

# Split Text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100,
    length_function=len,
    add_start_index=True,
)
chunks = text_splitter.split_documents(documents)
print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

if chunks:
    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

# Save to Chroma
if os.path.exists(CHROMA_PATH):
    shutil.rmtree(CHROMA_PATH)

db = Chroma.from_documents(
    chunks, embedding_function(), persist_directory=CHROMA_PATH
)
db.persist()
print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

################################################
# Step 4: Building the User Preference Interface
################################################

questions = [
    "How big do you want your house to be?"
    "What are 3 most important things for you in choosing this property?",
    "Which amenities would you like?",
    "Which transportation options are important to you?",
    "How urban do you want your suburb to be?",
]

buyer_preference_1 = [
    "A comfortable three-bedroom house with a spacious kitchen and a cozy living room.",
    "A quiet suburb, good local schools, and convenient shopping options.",
    "A backyard for gardening, a two-car garage, and a modern, energy-efficient heating system.",
    "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.",
    "A balance between suburban tranquility and access to urban amenities like restaurants and theaters."
]

buyer_preference_2 = [
    "A modern four-bedroom family house with scenic hills view and a open plan living.",
    "Should be under 700000 price, at least 10 m frontage, and a family-friendly community.",
    "A three-car garage, a barbeque pit and a modern, outdoor seating area.",
    "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.",
    "Growing suburb, nature and access to city public transport like buses and railway."
]

buyer_preference_3 = [
    "A stylish two-bedroom apartment with possibly a lake view and a modern kitchen.",
    "At least 100 sqm buildup area, planned community, and children play area or parks.",
    "Access to facilities such as a gym and swimming pool.",
    "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.",
    "A balance between suburban tranquility and access to urban amenities like restaurants and theaters."
]

buyer_preference_4 = [
    "A luxurious home with at least five bedrooms. Walking distance to prestigious schools.",
    "More than 400 sqm build up area, exclusive suburb with leafy streets and under 2 million price.",
    "A tennis court, swimming pool, home theater, and landscaped gardens.",
    "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.",
    "A balance between suburban tranquility and access to urban amenities like restaurants and theaters."
]

PROMPT_TEMPLATE = \
"""
Based on the following context:

{context}

---
Select a property listing: 

{preference}
"""

########################################
# Step 5: Searching Based on Preferences
########################################

def retrieve_property_listing(query_text: str, prompt_template: str) -> str:
    """
    Retrieve relevant property listings
    :param query_text: Buyer preferences.
    :param prompt_template: Prompt template
    :return: formatted property listings.
    """
    openai_embedding_function = OpenAIEmbeddings()
    chroma_db = Chroma(persist_directory=CHROMA_PATH, embedding_function=openai_embedding_function)

    # Search the DB.
    results = chroma_db.similarity_search_with_relevance_scores(query_text, k = 5)
    if len(results) == 0 or results[0][1] < 0.7:
        return "Unable to find matching results."
    else:
        context = "\n---\n".join([doc.page_content for doc, _score in results])
        chat_prompt_template = ChatPromptTemplate.from_template(prompt_template)
        prompt = chat_prompt_template.format(context=context, preference=query_text)
        print(f"\nGenerated Prompt: {prompt}")

        response_text = llm.invoke(prompt)
        sources = [doc.metadata.get("id", None) for doc, _score in results]
        formatted_response = f"\nResponse: {response_text}\nSources: {sources}"
        return formatted_response


buyer_preferences = [
    "\n".join(buyer_preference_1),
    "\n".join(buyer_preference_2),
    "\n".join(buyer_preference_3),
    "\n".join(buyer_preference_4),
]

for preference in buyer_preferences:
    print(retrieve_property_listing(preference, PROMPT_TEMPLATE))

############################################
# Step 6: Personalizing Listing Descriptions
############################################

AUGMENT_PROMPT_TEMPLATE = \
"""
Based on the following context:

{context}

---
Buyer Preferences:

{preference}

Craft a response that not only justifies the selection, but also ensures that your explanation is distinct, captivating, and customized to align with the specified preferences. This involves subtly emphasizing aspects of the property that align with what the buyer is looking for.
"""

print("\n---\nAUGMENT_PROMPT_RESPONSES\n")
for preference in buyer_preferences:
    print(retrieve_property_listing(preference, AUGMENT_PROMPT_TEMPLATE))
