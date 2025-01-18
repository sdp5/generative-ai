# Custom Chatbot Project

# DATA WRANGLING
# Load your chosen dataset into a `pandas` dataframe with a column named "text".
# This column should contain all of your text data, separated into at least 20 rows.

# ! pip install -q "pandas"
# ! pip install sodapy

import pandas as pd
from sodapy import Socrata
from torch.ao.nn.quantized.functional import threshold

# client = Socrata("data.cityofnewyork.us", None)
# results = client.get("if26-z6xq", limit=200)
# results_df = pd.DataFrame.from_records(results)
#
# results_df.info()
# print(results_df.head())

results_df = pd.read_csv("data/nyc_food_scrap_drop_off_sites.csv")
results_df.info()

print(results_df.iloc[0]["borough"])
print(results_df.iloc[0]["ntaname"])
print(results_df.iloc[0]["food_scrap_drop_off_site"])
print(results_df.iloc[0]["operation_day_hours"])
print(results_df.iloc[0]["notes"])

results_text = []
not_accepted_row_count_min = 192
for (i, row) in results_df.iterrows():
    food_scrap_drop_off_site = row['food_scrap_drop_off_site']
    # clean food_scrap_drop_off_site text
    if ":" in row["food_scrap_drop_off_site"]:
        food_scrap_drop_off_site = row['food_scrap_drop_off_site'].split(': ')[1]

    notes = row['notes']
    if not isinstance(notes, str):
        continue
    # Ensure to have some rows with not_accepted info in the notes
    if 'Not accepted' not in row['notes'] and not_accepted_row_count_min > 0:
        continue
    else:
        not_accepted_row_count_min -= 1

    results_text.append({
        "text":
            f"area - {row['borough']} | "
            f"suburb - {row['ntaname']} | "
            f"food_scrap_drop_off_site - {food_scrap_drop_off_site} | "
            f"operation_day_hours - {row['operation_day_hours']} | "
            f"accepted / not_accepted - {notes}"
    })

df = pd.DataFrame.from_records(results_text)
df.info()

print(df.head())

# CUSTOM QUERY COMPLETION
# Compose a custom query using your chosen dataset and retrieve results from an OpenAI
# Completion model. You may copy and paste any useful code from the course materials.

import openai

openai.api_base = "https://openai.vocareum.com/v1"
openai.api_key = "YOUR API KEY"

que_1 = "List some of the food scarp drop off sites in Brooklyn area which operate 24/7?"
prompt_1 = f"""
Question: {que_1}
Answer:
"""
initial_answer_1 = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt_1,
    max_tokens=200
)["choices"][0]["text"].strip()
print("\n" + prompt_1 + "\n" + initial_answer_1)

que_2 = "What items are not accepted in the bins at some of the locations?"
prompt_2 = f"""
Question: {que_2}
Answer:
"""
initial_answer_2 = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt_2,
    max_tokens=200
)["choices"][0]["text"].strip()
print("\n" + prompt_2 + "\n" + initial_answer_2)

# Generating Embeddings
EMBEDDING_MODEL_NAME = "text-embedding-ada-002"
batch_size = 100
embeddings = []
for i in range(0, len(df), batch_size):
    # Send text data to OpenAI model to get embeddings
    response = openai.Embedding.create(
        input=df.iloc[i:i + batch_size]["text"].tolist(),
        engine=EMBEDDING_MODEL_NAME
    )

    # Add embeddings to list
    embeddings.extend([data["embedding"] for data in response["data"]])

# Add embeddings list to dataframe
df["embeddings"] = embeddings
print(df)

df.to_csv("embeddings.csv")

# Create a Function that Finds Related Pieces of Text for a Given Question
from openai.embeddings_utils import get_embedding, distances_from_embeddings

def get_rows_sorted_by_relevance(question, df):
    """
    Function that takes in a question string and a dataframe containing
    rows of text and associated embeddings, and returns that dataframe
    sorted from least to most relevant for that question
    """

    # Get embeddings for the question text
    question_embeddings = get_embedding(question, engine=EMBEDDING_MODEL_NAME)

    # Make a copy of the dataframe and add a "distances" column containing
    # the cosine distances between each row's embeddings and the
    # embeddings of the question
    df_copy = df.copy()
    df_copy["distances"] = distances_from_embeddings(
        question_embeddings,
        df_copy["embeddings"].values,
        distance_metric="cosine"
    )

    # Sort the copied dataframe by the distances and return it
    # (shorter distance = more relevant so we sort in ascending order)
    df_copy.sort_values("distances", ascending=True, inplace=True)
    return df_copy


get_rows_sorted_by_relevance(que_1, df)
get_rows_sorted_by_relevance(que_2, df)

# Create a Function that Composes a Text Prompt
import tiktoken

def create_prompt(question, df, max_token_count):
    """
    Given a question and a dataframe containing rows of text and their
    embeddings, return a text prompt to send to a Completion model
    """
    # Create a tokenizer that is designed to align with our embeddings
    tokenizer = tiktoken.get_encoding("cl100k_base")

    # Count the number of tokens in the prompt template and question
    prompt_template = """
Answer the question based on the context below, and if the question
can't be answered based on the context, say "I don't know"

Context: 

{}

---

Question: {}
Answer:"""

    current_token_count = len(tokenizer.encode(prompt_template)) + \
                          len(tokenizer.encode(question))

    context = []
    for text in get_rows_sorted_by_relevance(question, df)["text"].values:

        # Increase the counter based on the number of tokens in this row
        text_token_count = len(tokenizer.encode(text))
        current_token_count += text_token_count

        # Add the row of text to the list if we haven't exceeded the max
        if current_token_count <= max_token_count:
            context.append(text)
        else:
            break

    return prompt_template.format("\n\n###\n\n".join(context), question)


print(create_prompt(que_1, df, 1800))
print(create_prompt(que_2, df, 1800))

# Create a Function that Answers a Question
COMPLETION_MODEL_NAME = "gpt-3.5-turbo-instruct"


def answer_question(
        question, df, max_prompt_tokens=1800, max_answer_tokens=500
):
    """
    Given a question, a dataframe containing rows of text, and a maximum
    number of desired tokens in the prompt and response, return the
    answer to the question according to an OpenAI Completion model

    If the model produces an error, return an empty string
    """

    prompt = create_prompt(question, df, max_prompt_tokens)

    try:
        response = openai.Completion.create(
            model=COMPLETION_MODEL_NAME,
            prompt=prompt,
            max_tokens=max_answer_tokens
        )
        return response["choices"][0]["text"].strip()
    except Exception as e:
        print(e)
        return ""

# CUSTOM PERFORMANCE DEMONSTRATION
# Demonstrate the performance of your custom query using at least 2 questions. For each question,
# show the answer from a basic `Completion` model query as well as the answer from your custom query.

# Question 1

custom_answer_1 = answer_question(que_1, df)
print("Custom Answer 1: " + custom_answer_1)

# Question 2

custom_answer_2 = answer_question(que_2, df)
print("Custom Answer 2: " + custom_answer_2)

# Comparisons of answers with and without context

print(f"""
{que_1}

Original Answer: {initial_answer_1}
\n\nCustom Answer:   {custom_answer_1}

---

{que_2}
Original Answer: {initial_answer_2}
\n\nCustom Answer:   {custom_answer_2}
""")
