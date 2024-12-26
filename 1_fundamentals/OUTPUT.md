Dataset loaded successfully.

Subset of the dataset created successfully.

Train split of dataset:

```
Dataset({
    features: ['text', 'label'],
    num_rows: 100
})
```

Test split of dataset:

```
Dataset({
    features: ['text', 'label'],
    num_rows: 100
})
```

Let's take a look at first data in the set:

```
{'text': "As soon as I heard about this film I knew I had to check it out. Well, I heard about it, then I found the trailer. After that, that's when I knew I had to see it. And I am so glad I did. You want to see classic television mixed with zombies? No? Then get lost.<br /><br />FIDO is a movie unlike anything I've ever seen. Well, actually, it kind of is. It's kind of like a Lassie episode and a Zombie film. Though when combined, it feels completely new and original. FIDO is about a little boy named Timmy and his new pet Fido. Well this new pet ain't no squawking parakeet or some potty-trained puppy. It's a re-animated dead guy...a zombie. A large radiation cloud engulfed Earth which led to all of the dead rising, which ensued the Zombie Wars. Though through the genius of Reinhold Giger, lead scientist of ZomCon, he discovered that if you destroy the brain, the zombie will perish, thus giving us the edge and the win in the Zombie War. Though due to lingering radiation, whoever dies becomes a zombie. Which can be a problem especially with the elderly. Though Zomcom steps up again with more breakthroughs, especially with the Domestication Collar. The collar stops the zombie's need for human flesh and thus making it harmless as a household pet. But not all is perfect in this Zombie Utopia, collars break, old people die and....well I'll just let you watch this incredibly unique flick.<br /><br />FIDO is a fantastic idea brought to fruition. With an all-star cast, and great writing FIDO rises above most in the comedy/horror genre. There are plenty of funny and original situations that really had me entertained. Though after seeing the film, I personally think the movie would have been better in black and white. At less than 90 minutes, the movie doesn't go on for too long and moves from scene to scene at a good rate. It'll probably end up being a cult-classic of sorts, since it's not really a laugh out loud comedy or even a horror movie. It's a comedy/family/zombie film immersed in the 1950 vibe. If you thought anything I said here was interesting by all means check this film out. But if you're still on the fence, swing your leg back over and stay there. 8.5 outta 10", 'label': 1}`
```

Tokenizers loaded successfully.

Map: 100%|██████████████████████████████████████████████████████████████████████████████| 100/100 [00:00<00:00, 1703.45 examples/s]
Map: 100%|██████████████████████████████████████████████████████████████████████████████| 100/100 [00:00<00:00, 1707.02 examples/s]

<br>Some weights of DistilBertForSequenceClassification were not initialized from the model checkpoint at distilbert-base-uncased and are newly initialized: `['classifier.bias', 'classifier.weight', 'pre_classifier.bias', 'pre_classifier.weight']`
<br>You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.

Dataset tokenized successfully.

Show the first example of tokenized training set:

`[101, 2004, 2574, 2004, 1045, 2657, 2055, 2023, 2143, 1045, 2354, 1045, 2018, 2000, 4638, 2009, 2041, 1012, 2092, 1010, 1045, 2657, 2055, 2009, 1010, 2059, 1045, 2179, 1996, 9117, 1012, 2044, 2008, 1010, 2008, 1005, 1055, 2043, 1045, 2354, 1045, 2018, 2000, 2156, 2009, 1012, 1998, 1045, 2572, 2061, 5580, 1045, 2106, 1012, 2017, 2215, 2000, 2156, 4438, 2547, 3816, 2007, 14106, 1029, 2053, 1029, 2059, 2131, 2439, 1012, 1026, 7987, 1013, 1028, 1026, 7987, 1013, 1028, 10882, 3527, 2003, 1037, 3185, 4406, 2505, 1045, 1005, 2310, 2412, 2464, 1012, 2092, 1010, 2941, 1010, 2009, 2785, 1997, 2003, 1012, 2009, 1005, 1055, 2785, 1997, 2066, 1037, 27333, 2666, 2792, 1998, 1037, 11798, 2143, 1012, 2295, 2043, 4117, 1010, 2009, 5683, 3294, 2047, 1998, 2434, 1012, 10882, 3527, 2003, 2055, 1037, 2210, 2879, 2315, 27217, 1998, 2010, 2047, 9004, 10882, 3527, 1012, 2092, 2023, 2047, 9004, 7110, 1005, 1056, 2053, 5490, 6692, 26291, 2075, 11498, 20553, 2102, 2030, 2070, 8962, 3723, 1011, 4738, 17022, 1012, 2009, 1005, 1055, 1037, 2128, 1011, 6579, 2757, 3124, 1012, 1012, 1012, 1037, 11798, 1012, 1037, 2312, 8249, 6112, 24692, 3011, 2029, 2419, 2000, 2035, 1997, 1996, 2757, 4803, 1010, 2029, 18942, 1996, 11798, 5233, 1012, 2295, 2083, 1996, 11067, 1997, 27788, 12640, 15453, 2121, 1010, 2599, 7155, 1997, 1062, 5358, 8663, 1010, 2002, 3603, 2008, 2065, 2017, 6033, 1996, 4167, 1010, 1996, 11798, 2097, 2566, 4509, 1010, 2947, 3228, 2149, 1996, 3341, 1998, 1996, 2663, 1999, 1996, 11798, 2162, 1012, 2295, 2349, 2000, 15304, 8249, 1010, 9444, 8289, 4150, 1037, 11798, 1012, 2029, 2064, 2022, 1037, 3291, 2926, 2007, 1996, 9750, 1012, 2295, 1062, 5358, 9006, 4084, 2039, 2153, 2007, 2062, 12687, 2015, 1010, 2926, 2007, 1996, 4968, 3370, 9127, 1012, 1996, 9127, 6762, 1996, 11798, 1005, 1055, 2342, 2005, 2529, 5771, 1998, 2947, 2437, 2009, 19741, 2004, 1037, 4398, 9004, 1012, 2021, 2025, 2035, 2003, 3819, 1999, 2023, 11798, 26425, 1010, 9127, 2015, 3338, 1010, 2214, 2111, 3280, 1998, 1012, 1012, 1012, 1012, 2092, 1045, 1005, 2222, 2074, 2292, 2017, 3422, 2023, 11757, 4310, 17312, 1012, 1026, 7987, 1013, 1028, 1026, 7987, 1013, 1028, 10882, 3527, 2003, 1037, 10392, 2801, 2716, 2000, 5909, 3258, 1012, 2007, 2019, 2035, 1011, 2732, 3459, 1010, 1998, 2307, 3015, 10882, 3527, 9466, 2682, 2087, 1999, 1996, 4038, 1013, 5469, 6907, 1012, 2045, 2024, 7564, 1997, 6057, 1998, 2434, 8146, 2008, 2428, 2018, 2033, 21474, 1012, 2295, 2044, 3773, 1996, 2143, 1010, 1045, 7714, 2228, 1996, 3185, 2052, 2031, 2042, 2488, 1999, 2304, 1998, 2317, 1012, 2012, 2625, 2084, 3938, 2781, 1010, 1996, 3185, 2987, 1005, 1056, 2175, 2006, 2005, 2205, 2146, 1998, 5829, 2013, 3496, 2000, 3496, 2012, 1037, 2204, 3446, 1012, 2009, 1005, 2222, 2763, 2203, 2039, 2108, 1037, 8754, 1011, 4438, 1997, 11901, 1010, 2144, 2009, 1005, 1055, 2025, 2428, 1037, 4756, 2041, 5189, 4038, 2030, 2130, 1037, 5469, 3185, 1012, 2009, 1005, 1055, 1037, 4038, 1013, 2155, 1013, 11798, 2143, 26275, 1999, 1996, 3925, 21209, 1012, 2065, 2017, 2245, 2505, 1045, 2056, 2182, 2001, 5875, 2011, 2035, 2965, 4638, 2023, 2143, 2041, 1012, 2021, 2065, 102]`

Pretrained Model loaded successfully.

Fine tuned Model loaded successfully.

Pretrained Model classifiers:

`Linear(in_features=768, out_features=2, bias=True)`

Inspect Pretrained Model:

```
DistilBertForSequenceClassification(
  (distilbert): DistilBertModel(
    (embeddings): Embeddings(
      (word_embeddings): Embedding(30522, 768, padding_idx=0)
      (position_embeddings): Embedding(512, 768)
      (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
      (dropout): Dropout(p=0.1, inplace=False)
    )
    (transformer): Transformer(
      (layer): ModuleList(
        (0-5): 6 x TransformerBlock(
          (attention): DistilBertSdpaAttention(
            (dropout): Dropout(p=0.1, inplace=False)
            (q_lin): Linear(in_features=768, out_features=768, bias=True)
            (k_lin): Linear(in_features=768, out_features=768, bias=True)
            (v_lin): Linear(in_features=768, out_features=768, bias=True)
            (out_lin): Linear(in_features=768, out_features=768, bias=True)
          )
          (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
          (ffn): FFN(
            (dropout): Dropout(p=0.1, inplace=False)
            (lin1): Linear(in_features=768, out_features=3072, bias=True)
            (lin2): Linear(in_features=3072, out_features=768, bias=True)
            (activation): GELUActivation()
          )
          (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
        )
      )
    )
  )
  (pre_classifier): Linear(in_features=768, out_features=768, bias=True)
  (classifier): Linear(in_features=768, out_features=2, bias=True)
  (dropout): Dropout(p=0.2, inplace=False)
)
Fine Tuned Model classifiers:
Linear(in_features=768, out_features=2, bias=True)
Inspect Fine Tuned Model:
DistilBertForSequenceClassification(
  (distilbert): DistilBertModel(
    (embeddings): Embeddings(
      (word_embeddings): Embedding(30522, 768, padding_idx=0)
      (position_embeddings): Embedding(512, 768)
      (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
      (dropout): Dropout(p=0.1, inplace=False)
    )
    (transformer): Transformer(
      (layer): ModuleList(
        (0-5): 6 x TransformerBlock(
          (attention): DistilBertSdpaAttention(
            (dropout): Dropout(p=0.1, inplace=False)
            (q_lin): Linear(in_features=768, out_features=768, bias=True)
            (k_lin): Linear(in_features=768, out_features=768, bias=True)
            (v_lin): Linear(in_features=768, out_features=768, bias=True)
            (out_lin): Linear(in_features=768, out_features=768, bias=True)
          )
          (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
          (ffn): FFN(
            (dropout): Dropout(p=0.1, inplace=False)
            (lin1): Linear(in_features=768, out_features=3072, bias=True)
            (lin2): Linear(in_features=3072, out_features=768, bias=True)
            (activation): GELUActivation()
          )
          (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
        )
      )
    )
  )
  (pre_classifier): Linear(in_features=768, out_features=768, bias=True)
  (classifier): Linear(in_features=768, out_features=2, bias=True)
  (dropout): Dropout(p=0.2, inplace=False)
)
```

Evaluate pre-trained foundation_model.

100%|██████████████████████████████████████████████████████████████████████████████████████████████| 25/25 [00:16<00:00,  1.47it/s]

`{'eval_loss': 0.6987037658691406, 'eval_model_preparation_time': 0.0008, 'eval_accuracy': 0.49, 'eval_runtime': 17.6588, 'eval_samples_per_second': 5.663, 'eval_steps_per_second': 1.416}`

Evaluate fine-tuned pre-trained model.

100%|██████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [00:17<00:00,  2.92it/s]

`{'eval_loss': 0.18837317824363708, 'eval_model_preparation_time': 0.0011, 'eval_accuracy': 0.94, 'eval_runtime': 17.4414, 'eval_samples_per_second': 5.733, 'eval_steps_per_second': 2.867}`

Full train the foundation_model.

100%|██████████████████████████████████████████████████████████████████████████████████████████████| 25/25 [01:43<00:00,  4.13s/it]

`{'eval_loss': 0.6914172172546387, 'eval_model_preparation_time': 0.0008, 'eval_accuracy': 0.53, 'eval_runtime': 17.3029, 'eval_samples_per_second': 5.779, 'eval_steps_per_second': 1.445, 'epoch': 1.0}`

`{'train_runtime': 103.3356, 'train_samples_per_second': 0.968, 'train_steps_per_second': 0.242, 'train_loss': 0.9415467834472656, 'epoch': 1.0}`

Evaluate post-trained foundation_model.

100%|██████████████████████████████████████████████████████████████████████████████████████████████| 25/25 [00:16<00:00,  1.50it/s]

`{'eval_loss': 0.6914172172546387, 'eval_model_preparation_time': 0.0008, 'eval_accuracy': 0.53, 'eval_runtime': 17.3453, 'eval_samples_per_second': 5.765, 'eval_steps_per_second': 1.441, 'epoch': 1.0}`

100%|██████████████████████████████████████████████████████████████████████████████████████████████| 25/25 [00:16<00:00,  1.49it/s]

The installed version of bitsandbytes was compiled without GPU support. 8-bit optimizers, 8-bit multiplication, and GPU quantization are unavailable.

```
                                                text  label  predicted_label
0  I've seen this amusing little 'brit flick'many...      1                0
1  Yep, Edward G. gives us a retro view of the cr...      0                0
2  Has there ever been an Angel of Death like MIM...      1                0
3  This is one of the worst Sandra Bullock movie ...      0                0
4  Dr Steven Segal saves the world from a deadly ...      0                0
5  An interesting concept turned into carnage... ...      0                0
6  Not good. Mostly because you don't give a damn...      0                0
7  The opening scene makes you feel like you're w...      0                0
8  I've watched a number of Wixel Pixel and Sub R...      0                0
9  Continuing in the string of "stalker/slasher" ...      0                0
```

Look at some of the incorrect predictions.

```
                                                 text  label  predicted_label
0   I've seen this amusing little 'brit flick'many...      1                0
2   Has there ever been an Angel of Death like MIM...      1                0
12  I gave this a 10 because it's the best film of...      1                0
15  Korean "romance" about the owner of a camera s...      1                0
17  Ostensibly a story about the young child of Ji...      1                0
20  The rise of punk music was scarcely documented...      1                0
21  I love this film (dont know why it is called P...      1                0
23  I just saw this movie tonight(5th Nov. 2005)fo...      1                0
24  As a longtime admirer of the 2001 film "Moulin...      1                0
25  So funny is the perfect way to describe this 1...      1                0
```

`trainable params: 739,586 || all params: 67,694,596 || trainable%: 1.0925`

PEFT SEQ_CLS MODEL:

```
PeftModelForSequenceClassification(
  (base_model): LoraModel(
    (model): DistilBertForSequenceClassification(
      (distilbert): DistilBertModel(
        (embeddings): Embeddings(
          (word_embeddings): Embedding(30522, 768, padding_idx=0)
          (position_embeddings): Embedding(512, 768)
          (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
          (dropout): Dropout(p=0.1, inplace=False)
        )
        (transformer): Transformer(
          (layer): ModuleList(
            (0-5): 6 x TransformerBlock(
              (attention): DistilBertSdpaAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): lora.Linear(
                  (base_layer): Linear(in_features=768, out_features=768, bias=True)
                  (lora_dropout): ModuleDict(
                    (default): Dropout(p=0.1, inplace=False)
                  )
                  (lora_A): ModuleDict(
                    (default): Linear(in_features=768, out_features=8, bias=False)
                  )
                  (lora_B): ModuleDict(
                    (default): Linear(in_features=8, out_features=768, bias=False)
                  )
                  (lora_embedding_A): ParameterDict()
                  (lora_embedding_B): ParameterDict()
                  (lora_magnitude_vector): ModuleDict()
                )
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): lora.Linear(
                  (base_layer): Linear(in_features=768, out_features=768, bias=True)
                  (lora_dropout): ModuleDict(
                    (default): Dropout(p=0.1, inplace=False)
                  )
                  (lora_A): ModuleDict(
                    (default): Linear(in_features=768, out_features=8, bias=False)
                  )
                  (lora_B): ModuleDict(
                    (default): Linear(in_features=8, out_features=768, bias=False)
                  )
                  (lora_embedding_A): ParameterDict()
                  (lora_embedding_B): ParameterDict()
                  (lora_magnitude_vector): ModuleDict()
                )
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
          )
        )
      )
      (pre_classifier): ModulesToSaveWrapper(
        (original_module): Linear(in_features=768, out_features=768, bias=True)
        (modules_to_save): ModuleDict(
          (default): Linear(in_features=768, out_features=768, bias=True)
        )
      )
      (classifier): ModulesToSaveWrapper(
        (original_module): Linear(in_features=768, out_features=2, bias=True)
        (modules_to_save): ModuleDict(
          (default): Linear(in_features=768, out_features=2, bias=True)
        )
      )
      (dropout): Dropout(p=0.2, inplace=False)
    )
  )
)
```

100%|████████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:16<00:00,  2.32s/it]

`peft_seq_cls_pre_train_results: {'eval_loss': 0.6914173364639282, 'eval_model_preparation_time': 0.0013, 'eval_accuracy': 0.53, 'eval_runtime': 19.3401, 'eval_samples_per_second': 5.171, 'eval_steps_per_second': 0.362}`

100%|██████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [02:38<00:00,  9.00s/it]

`{'eval_loss': 0.6913836598396301, 'eval_model_preparation_time': 0.0013, 'eval_accuracy': 0.53, 'eval_runtime': 19.291, 'eval_sampl100%|██████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [02:59<00:00, 12.83s/it]`

`{'eval_loss': 0.6913579702377319, 'eval_model_preparation_time': 0.0013, 'eval_accuracy': 0.53, 'eval_runtime': 19.9834, 'eval_samples_per_second': 5.004, 'eval_steps_per_second': 0.35, 'epoch': 2.0}`

`{'train_runtime': 179.6275, 'train_samples_per_second': 1.113, 'train_steps_per_second': 0.078, 'train_loss': 0.692131655556815, 'epoch': 2.0}`

100%|████████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:16<00:00,  2.34s/it]

`peft_seq_cls_post_train_results: {'eval_loss': 0.6913579702377319, 'eval_model_preparation_time': 0.0013, 'eval_accuracy': 0.53, 'eval_runtime': 19.6632, 'eval_samples_per_second': 5.086, 'eval_steps_per_second': 0.356, 'epoch': 2.0}`

100%|████████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:16<00:00,  2.34s/it]

<br>Some weights of DistilBertForSequenceClassification were not initialized from the model checkpoint at distilbert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight', 'pre_classifier.bias', 'pre_classifier.weight']
<br>You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.

```
                                                text  label  predicted_label
0  I've seen this amusing little 'brit flick'many...      1                0
1  Yep, Edward G. gives us a retro view of the cr...      0                0
2  Has there ever been an Angel of Death like MIM...      1                0
3  This is one of the worst Sandra Bullock movie ...      0                0
4  Dr Steven Segal saves the world from a deadly ...      0                0
5  An interesting concept turned into carnage... ...      0                0
6  Not good. Mostly because you don't give a damn...      0                0
7  The opening scene makes you feel like you're w...      0                0
8  I've watched a number of Wixel Pixel and Sub R...      0                0
9  Continuing in the string of "stalker/slasher" ...      0                0
```

Reconstructed model from saved PEFT:

```
PeftModelForSequenceClassification(
  (base_model): LoraModel(
    (model): DistilBertForSequenceClassification(
      (distilbert): DistilBertModel(
        (embeddings): Embeddings(
          (word_embeddings): Embedding(30522, 768, padding_idx=0)
          (position_embeddings): Embedding(512, 768)
          (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
          (dropout): Dropout(p=0.1, inplace=False)
        )
        (transformer): Transformer(
          (layer): ModuleList(
            (0-5): 6 x TransformerBlock(
              (attention): DistilBertSdpaAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): lora.Linear(
                  (base_layer): Linear(in_features=768, out_features=768, bias=True)
                  (lora_dropout): ModuleDict(
                    (default): Dropout(p=0.1, inplace=False)
                  )
                  (lora_A): ModuleDict(
                    (default): Linear(in_features=768, out_features=8, bias=False)
                  )
                  (lora_B): ModuleDict(
                    (default): Linear(in_features=8, out_features=768, bias=False)
                  )
                  (lora_embedding_A): ParameterDict()
                  (lora_embedding_B): ParameterDict()
                  (lora_magnitude_vector): ModuleDict()
                )
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): lora.Linear(
                  (base_layer): Linear(in_features=768, out_features=768, bias=True)
                  (lora_dropout): ModuleDict(
                    (default): Dropout(p=0.1, inplace=False)
                  )
                  (lora_A): ModuleDict(
                    (default): Linear(in_features=768, out_features=8, bias=False)
                  )
                  (lora_B): ModuleDict(
                    (default): Linear(in_features=8, out_features=768, bias=False)
                  )
                  (lora_embedding_A): ParameterDict()
                  (lora_embedding_B): ParameterDict()
                  (lora_magnitude_vector): ModuleDict()
                )
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
          )
        )
      )
      (pre_classifier): ModulesToSaveWrapper(
        (original_module): Linear(in_features=768, out_features=768, bias=True)
        (modules_to_save): ModuleDict(
          (default): Linear(in_features=768, out_features=768, bias=True)
        )
      )
      (classifier): ModulesToSaveWrapper(
        (original_module): Linear(in_features=768, out_features=2, bias=True)
        (modules_to_save): ModuleDict(
          (default): Linear(in_features=768, out_features=2, bias=True)
        )
      )
      (dropout): Dropout(p=0.2, inplace=False)
    )
  )
)
```

```
Dataset({
    features: ['text', 'label', 'input_ids', 'attention_mask'],
    num_rows: 12
})
```

`[101, 1045, 1005, 2310, 2464, 2023, 19142, 2210, 1005, 28101, 17312, 1005, 2116, 2335, 1012, 1996, 2069, 3291, 2003, 2049, 2747, 20165, 2006, 2678, 2030, 4966, 1012, 1045, 1005, 24529, 5121, 1037, 20127, 2005, 1037, 4966, 2713, 1012, 1996, 2172, 4771, 2957, 5207, 3248, 1005, 5061, 2100, 1005, 2019, 4654, 1011, 6986, 2137, 1010, 3005, 2074, 2042, 2207, 2013, 3827, 1010, 2002, 4858, 2370, 1037, 3105, 2004, 2019, 3751, 2937, 1999, 1037, 2924, 1010, 2009, 2035, 3632, 2092, 2127, 2002, 4858, 2370, 7861, 12618, 18450, 1999, 1037, 2924, 2002, 2923, 2007, 2010, 4654, 13675, 10698, 2229, 1010, 2585, 9152, 8159, 3248, 1996, 3040, 23356, 7332, 1010, 2049, 2019, 22249, 2210, 17083, 2361, 1010, 11504, 2996, 5033, 2030, 8133, 3016, 1010, 2097, 2272, 2000, 1996, 5343, 1012, 2298, 2041, 2005, 2198, 13919, 9082, 2077, 2002, 4930, 2009, 2502, 2007, 1005, 26822, 12734, 1005, 10642, 1997, 1996, 2439, 15745, 1005, 2935, 1997, 1996, 7635, 1005, 1999, 1037, 2235, 2535, 2004, 1037, 19805, 1010, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`

```
{'text': "I've seen this amusing little 'brit flick'many times. The only problem is Its currently unavailable on video or DVD. I'ts certainly a contender for a DVD release. The much missed Richard Jordan plays 'pinky' an Ex-pat American, whose Just been released from prison,he finds himself A job as an Electrician in a bank, it all goes well until he finds Himself Embroiled in a bank heist with his ex cronies, David Niven Plays the mastermind Ivan, Its an enjoyable little romp, hopefully studio canal or anchor bay, will come to the Rescue. Look out for john Rhys Davies Before he struck it big with 'shogun' Raiders of the lost Ark 'Lord Of The Rings' In a small role as a barrister,", 'label': 1, 'input_ids': [101, 1045, 1005, 2310, 2464, 2023, 19142, 2210, 1005, 28101, 17312, 1005, 2116, 2335, 1012, 1996, 2069, 3291, 2003, 2049, 2747, 20165, 2006, 2678, 2030, 4966, 1012, 1045, 1005, 24529, 5121, 1037, 20127, 2005, 1037, 4966, 2713, 1012, 1996, 2172, 4771, 2957, 5207, 3248, 1005, 5061, 2100, 1005, 2019, 4654, 1011, 6986, 2137, 1010, 3005, 2074, 2042, 2207, 2013, 3827, 1010, 2002, 4858, 2370, 1037, 3105, 2004, 2019, 3751, 2937, 1999, 1037, 2924, 1010, 2009, 2035, 3632, 2092, 2127, 2002, 4858, 2370, 7861, 12618, 18450, 1999, 1037, 2924, 2002, 2923, 2007, 2010, 4654, 13675, 10698, 2229, 1010, 2585, 9152, 8159, 3248, 1996, 3040, 23356, 7332, 1010, 2049, 2019, 22249, 2210, 17083, 2361, 1010, 11504, 2996, 5033, 2030, 8133, 3016, 1010, 2097, 2272, 2000, 1996, 5343, 1012, 2298, 2041, 2005, 2198, 13919, 9082, 2077, 2002, 4930, 2009, 2502, 2007, 1005, 26822, 12734, 1005, 10642, 1997, 1996, 2439, 15745, 1005, 2935, 1997, 1996, 7635, 1005, 1999, 1037, 2235, 2535, 2004, 1037, 19805, 1010, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}`
```

`[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`

```
                                                 text  predictions  labels
0   I've seen this amusing little 'brit flick'many...            1       1
1   Yep, Edward G. gives us a retro view of the cr...            1       0
2   When you watch low budget horror movies as muc...            1       0
3   So funny is the perfect way to describe this 1...            1       1
4   THE CELL fascinated me at first glance. I was ...            1       1
5   I never comment on a film, but I have to say t...            1       0
6   Wesley Snipes is perfectly cast as Blade, a ha...            1       1
7   This is the best work i have ever seen on tele...            1       1
8   Mean spirited, and down right degrading adapta...            1       0
9   Possibly the worst movie I ever saw. The perso...            1       0
10  There won't be one moment in this film where y...            1       1
11  Persuaded by the 7.0 points in IMDb, which is ...            1       0
```

`{'accuracy': 0.5}`

```
                              stage                                    details  eval_loss
0  Foundation model before training                    distilbert-base-uncased  0.698704
1   Foundation model after training                    distilbert-base-uncased  0.691417
2        PEFT model before training                    PEFT LoRA SEQ_CLS Model  0.691417
3         PEFT model after training                    PEFT LoRA SEQ_CLS Model  0.691358
4          Fine tuned trained model  tashrifmahmud/sentiment_analysis_model_v2  0.188373

[5 rows x 3 columns]
```
