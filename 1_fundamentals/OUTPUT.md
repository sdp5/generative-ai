Train split of dataset:
```
Dataset({
    features: ['text', 'label'],
    num_rows: 200
})
```

Test split of dataset:
```
Dataset({
    features: ['text', 'label'],
    num_rows: 200
})
```

Let's take a look at first data in the set:
```
{'text': "As soon as I heard about this film I knew I had to check it out. Well, I heard about it, then I found the trailer. After that, that's when I knew I had to see it. And I am so glad I did. You want to see classic television mixed with zombies? No? Then get lost.<br /><br />FIDO is a movie unlike anything I've ever seen. Well, actually, it kind of is. It's kind of like a Lassie episode and a Zombie film. Though when combined, it feels completely new and original. FIDO is about a little boy named Timmy and his new pet Fido. Well this new pet ain't no squawking parakeet or some potty-trained puppy. It's a re-animated dead guy...a zombie. A large radiation cloud engulfed Earth which led to all of the dead rising, which ensued the Zombie Wars. Though through the genius of Reinhold Giger, lead scientist of ZomCon, he discovered that if you destroy the brain, the zombie will perish, thus giving us the edge and the win in the Zombie War. Though due to lingering radiation, whoever dies becomes a zombie. Which can be a problem especially with the elderly. Though Zomcom steps up again with more breakthroughs, especially with the Domestication Collar. The collar stops the zombie's need for human flesh and thus making it harmless as a household pet. But not all is perfect in this Zombie Utopia, collars break, old people die and....well I'll just let you watch this incredibly unique flick.<br /><br />FIDO is a fantastic idea brought to fruition. With an all-star cast, and great writing FIDO rises above most in the comedy/horror genre. There are plenty of funny and original situations that really had me entertained. Though after seeing the film, I personally think the movie would have been better in black and white. At less than 90 minutes, the movie doesn't go on for too long and moves from scene to scene at a good rate. It'll probably end up being a cult-classic of sorts, since it's not really a laugh out loud comedy or even a horror movie. It's a comedy/family/zombie film immersed in the 1950 vibe. If you thought anything I said here was interesting by all means check this film out. But if you're still on the fence, swing your leg back over and stay there. 8.5 outta 10", 'label': 1}
```
<br>Map: 100%|██████████| 200/200 [00:00<00:00, 4842.05 examples/s]
<br>Map: 100%|██████████| 200/200 [00:00<00:00, 5047.66 examples/s]

Show the first example of tokenized training set:
```
[101, 2004, 2574, 2004, 1045, 2657, 2055, 2023, 2143, 1045, 2354, 1045, 2018, 2000, 4638, 2009, 2041, 1012, 2092, 1010, 1045, 2657, 2055, 2009, 1010, 2059, 1045, 2179, 1996, 9117, 1012, 2044, 2008, 1010, 2008, 1005, 1055, 2043, 1045, 2354, 1045, 2018, 2000, 2156, 2009, 1012, 1998, 1045, 2572, 2061, 5580, 1045, 2106, 1012, 2017, 2215, 2000, 2156, 4438, 2547, 3816, 2007, 14106, 1029, 2053, 1029, 2059, 2131, 2439, 1012, 1026, 7987, 1013, 1028, 1026, 7987, 1013, 1028, 10882, 3527, 2003, 1037, 3185, 4406, 2505, 1045, 1005, 2310, 2412, 2464, 1012, 2092, 1010, 2941, 1010, 2009, 2785, 1997, 2003, 1012, 2009, 1005, 1055, 2785, 1997, 2066, 1037, 27333, 2666, 2792, 1998, 1037, 11798, 2143, 1012, 2295, 2043, 4117, 1010, 2009, 5683, 3294, 2047, 1998, 2434, 1012, 10882, 3527, 2003, 2055, 1037, 2210, 2879, 2315, 27217, 1998, 2010, 2047, 9004, 10882, 3527, 1012, 2092, 2023, 2047, 9004, 7110, 1005, 1056, 2053, 5490, 6692, 26291, 2075, 11498, 20553, 2102, 2030, 2070, 8962, 3723, 1011, 4738, 17022, 1012, 2009, 1005, 1055, 1037, 2128, 1011, 6579, 2757, 3124, 1012, 1012, 1012, 1037, 11798, 1012, 1037, 2312, 8249, 6112, 24692, 3011, 2029, 2419, 2000, 2035, 1997, 1996, 2757, 4803, 1010, 2029, 18942, 1996, 11798, 5233, 1012, 2295, 2083, 1996, 11067, 1997, 27788, 12640, 15453, 2121, 1010, 2599, 7155, 1997, 1062, 5358, 8663, 1010, 2002, 3603, 2008, 2065, 2017, 6033, 1996, 4167, 1010, 1996, 11798, 2097, 2566, 4509, 1010, 2947, 3228, 2149, 1996, 3341, 1998, 1996, 2663, 1999, 1996, 11798, 2162, 1012, 2295, 2349, 2000, 15304, 8249, 1010, 9444, 8289, 4150, 1037, 11798, 1012, 2029, 2064, 2022, 1037, 3291, 2926, 2007, 1996, 9750, 1012, 2295, 1062, 5358, 9006, 4084, 2039, 2153, 2007, 2062, 12687, 2015, 1010, 2926, 2007, 1996, 4968, 3370, 9127, 1012, 1996, 9127, 6762, 1996, 11798, 1005, 1055, 2342, 2005, 2529, 5771, 1998, 2947, 2437, 2009, 19741, 2004, 1037, 4398, 9004, 1012, 2021, 2025, 2035, 2003, 3819, 1999, 2023, 11798, 26425, 1010, 9127, 2015, 3338, 1010, 2214, 2111, 3280, 1998, 1012, 1012, 1012, 1012, 2092, 1045, 1005, 2222, 2074, 2292, 2017, 3422, 2023, 11757, 4310, 17312, 1012, 1026, 7987, 1013, 1028, 1026, 7987, 1013, 1028, 10882, 3527, 2003, 1037, 10392, 2801, 2716, 2000, 5909, 3258, 1012, 2007, 2019, 2035, 1011, 2732, 3459, 1010, 1998, 2307, 3015, 10882, 3527, 9466, 2682, 2087, 1999, 1996, 4038, 1013, 5469, 6907, 1012, 2045, 2024, 7564, 1997, 6057, 1998, 2434, 8146, 2008, 2428, 2018, 2033, 21474, 1012, 2295, 2044, 3773, 1996, 2143, 1010, 1045, 7714, 2228, 1996, 3185, 2052, 2031, 2042, 2488, 1999, 2304, 1998, 2317, 1012, 2012, 2625, 2084, 3938, 2781, 1010, 1996, 3185, 2987, 1005, 1056, 2175, 2006, 2005, 2205, 2146, 1998, 5829, 2013, 3496, 2000, 3496, 2012, 1037, 2204, 3446, 1012, 2009, 1005, 2222, 2763, 2203, 2039, 2108, 1037, 8754, 1011, 4438, 1997, 11901, 1010, 2144, 2009, 1005, 1055, 2025, 2428, 1037, 4756, 2041, 5189, 4038, 2030, 2130, 1037, 5469, 3185, 1012, 2009, 1005, 1055, 1037, 4038, 1013, 2155, 1013, 11798, 2143, 26275, 1999, 1996, 3925, 21209, 1012, 2065, 2017, 2245, 2505, 1045, 2056, 2182, 2001, 5875, 2011, 2035, 2965, 4638, 2023, 2143, 2041, 1012, 2021, 2065, 102]
```

> Some weights of DistilBertForSequenceClassification were not initialized from the model checkpoint at distilbert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight', 'pre_classifier.bias', 'pre_classifier.weight']
> You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.

Model classifiers:
`Linear(in_features=768, out_features=2, bias=True)`

Inspect Model:
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
```

<br>FutureWarning: `evaluation_strategy` is deprecated and will be removed in version 4.46 of 🤗 Transformers. Use `eval_strategy` instead
<br>FutureWarning: `tokenizer` is deprecated and will be removed in version 5.0.0 for `Trainer.__init__`. Use `processing_class` instead.

```
100%|██████████| 50/50 [02:29<00:00,  2.96s/it]
  0%|          | 0/50 [00:00<?, ?it/s]
  4%|▍         | 2/50 [00:00<00:15,  3.02it/s]
  6%|▌         | 3/50 [00:01<00:22,  2.14it/s]
  8%|▊         | 4/50 [00:01<00:24,  1.85it/s]
 10%|█         | 5/50 [00:02<00:26,  1.72it/s]
 12%|█▏        | 6/50 [00:03<00:26,  1.65it/s]
 14%|█▍        | 7/50 [00:03<00:26,  1.60it/s]
 16%|█▌        | 8/50 [00:04<00:26,  1.57it/s]
 18%|█▊        | 9/50 [00:05<00:26,  1.55it/s]
 20%|██        | 10/50 [00:05<00:26,  1.54it/s]
 22%|██▏       | 11/50 [00:06<00:25,  1.53it/s]
 24%|██▍       | 12/50 [00:07<00:24,  1.53it/s]
 26%|██▌       | 13/50 [00:07<00:24,  1.52it/s]
 28%|██▊       | 14/50 [00:08<00:23,  1.52it/s]
 30%|███       | 15/50 [00:09<00:23,  1.50it/s]
 32%|███▏      | 16/50 [00:09<00:22,  1.50it/s]
 34%|███▍      | 17/50 [00:10<00:21,  1.51it/s]
 36%|███▌      | 18/50 [00:11<00:21,  1.51it/s]
 38%|███▊      | 19/50 [00:11<00:20,  1.50it/s]
 40%|████      | 20/50 [00:12<00:19,  1.51it/s]
 42%|████▏     | 21/50 [00:13<00:19,  1.51it/s]
 44%|████▍     | 22/50 [00:13<00:18,  1.51it/s]
 46%|████▌     | 23/50 [00:14<00:17,  1.51it/s]
 48%|████▊     | 24/50 [00:15<00:17,  1.52it/s]
 50%|█████     | 25/50 [00:15<00:16,  1.52it/s]
 52%|█████▏    | 26/50 [00:16<00:15,  1.52it/s]
 54%|█████▍    | 27/50 [00:17<00:15,  1.52it/s]
 56%|█████▌    | 28/50 [00:17<00:14,  1.52it/s]
 58%|█████▊    | 29/50 [00:18<00:13,  1.52it/s]
 60%|██████    | 30/50 [00:19<00:13,  1.52it/s]
 62%|██████▏   | 31/50 [00:19<00:12,  1.52it/s]
 64%|██████▍   | 32/50 [00:20<00:11,  1.52it/s]
 66%|██████▌   | 33/50 [00:21<00:11,  1.52it/s]
 68%|██████▊   | 34/50 [00:21<00:10,  1.52it/s]
 70%|███████   | 35/50 [00:22<00:09,  1.51it/s]
 72%|███████▏  | 36/50 [00:23<00:09,  1.51it/s]
 74%|███████▍  | 37/50 [00:23<00:08,  1.51it/s]
 76%|███████▌  | 38/50 [00:24<00:07,  1.51it/s]
 78%|███████▊  | 39/50 [00:25<00:07,  1.52it/s]
 80%|████████  | 40/50 [00:25<00:06,  1.52it/s]
 82%|████████▏ | 41/50 [00:26<00:05,  1.52it/s]
 84%|████████▍ | 42/50 [00:27<00:05,  1.52it/s]
 86%|████████▌ | 43/50 [00:27<00:04,  1.52it/s]
 88%|████████▊ | 44/50 [00:28<00:03,  1.52it/s]
 90%|█████████ | 45/50 [00:29<00:03,  1.52it/s]
 92%|█████████▏| 46/50 [00:29<00:02,  1.52it/s]
 94%|█████████▍| 47/50 [00:30<00:01,  1.52it/s]
 96%|█████████▌| 48/50 [00:31<00:01,  1.52it/s]
 98%|█████████▊| 49/50 [00:31<00:00,  1.52it/s]
{'eval_loss': 0.7500608563423157, 'eval_accuracy': 0.51, 'eval_runtime': 33.0015, 'eval_samples_per_second': 6.06, 'eval_steps_per_second': 1.515, 'epoch': 1.0}
                                               
100%|██████████| 50/50 [03:03<00:00,  2.96s/it]
100%|██████████| 50/50 [00:32<00:00,  1.52it/s]
100%|██████████| 50/50 [03:04<00:00,  3.69s/it]
{'train_runtime': 184.4309, 'train_samples_per_second': 1.084, 'train_steps_per_second': 0.271, 'train_loss': 0.9098149871826172, 'epoch': 1.0}
100%|██████████| 50/50 [00:32<00:00,  1.55it/s]
100%|██████████| 50/50 [00:32<00:00,  1.55it/s]
```

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

PEFT MODEL:
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

<br>FutureWarning: `evaluation_strategy` is deprecated and will be removed in version 4.46 of 🤗 Transformers. Use `eval_strategy` instead
<br>FutureWarning: `tokenizer` is deprecated and will be removed in version 5.0.0 for `Trainer.__init__`. Use `processing_class` instead.

```
 50%|█████     | 13/26 [02:10<01:53,  8.76s/it]
  0%|          | 0/13 [00:00<?, ?it/s]
 15%|█▌        | 2/13 [00:02<00:15,  1.41s/it]
 23%|██▎       | 3/13 [00:05<00:19,  2.00s/it]
 31%|███       | 4/13 [00:08<00:20,  2.30s/it]
 38%|███▊      | 5/13 [00:11<00:19,  2.49s/it]
 46%|████▌     | 6/13 [00:14<00:18,  2.59s/it]
 54%|█████▍    | 7/13 [00:16<00:16,  2.67s/it]
 62%|██████▏   | 8/13 [00:19<00:13,  2.73s/it]
 69%|██████▉   | 9/13 [00:22<00:11,  2.76s/it]
 77%|███████▋  | 10/13 [00:25<00:08,  2.78s/it]
 85%|████████▍ | 11/13 [00:28<00:05,  2.79s/it]
 92%|█████████▏| 12/13 [00:31<00:02,  2.80s/it]
```

`{'eval_loss': 0.7317150831222534, 'eval_accuracy': 0.51, 'eval_runtime': 35.3084, 'eval_samples_per_second': 5.664, 'eval_steps_per_second': 0.368, 'epoch': 1.0}`

```                                               
 50%|█████     | 13/26 [02:46<01:53,  8.76s/it]
100%|██████████| 13/13 [00:32<00:00,  2.37s/it]
100%|██████████| 26/26 [04:57<00:00,  8.95s/it]
  0%|          | 0/13 [00:00<?, ?it/s]
 15%|█▌        | 2/13 [00:02<00:15,  1.41s/it]
 23%|██▎       | 3/13 [00:05<00:20,  2.01s/it]
 31%|███       | 4/13 [00:08<00:20,  2.31s/it]
 38%|███▊      | 5/13 [00:11<00:19,  2.49s/it]
 46%|████▌     | 6/13 [00:14<00:18,  2.60s/it]
 54%|█████▍    | 7/13 [00:16<00:16,  2.67s/it]
 62%|██████▏   | 8/13 [00:19<00:13,  2.73s/it]
 69%|██████▉   | 9/13 [00:22<00:11,  2.76s/it]
 77%|███████▋  | 10/13 [00:25<00:08,  2.78s/it]
 85%|████████▍ | 11/13 [00:28<00:05,  2.79s/it]
 92%|█████████▏| 12/13 [00:31<00:02,  2.81s/it]
```

`{'eval_loss': 0.7257698774337769, 'eval_accuracy': 0.51, 'eval_runtime': 35.3612, 'eval_samples_per_second': 5.656, 'eval_steps_per_second': 0.368, 'epoch': 2.0}`

```                                              
100%|██████████| 26/26 [05:32<00:00,  8.95s/it]
100%|██████████| 13/13 [00:32<00:00,  2.39s/it]
100%|██████████| 26/26 [05:33<00:00, 12.83s/it]
{'train_runtime': 333.5721, 'train_samples_per_second': 1.199, 'train_steps_per_second': 0.078, 'train_loss': 0.7359374853280874, 'epoch': 2.0}
100%|██████████| 13/13 [00:32<00:00,  2.50s/it]
100%|██████████| 50/50 [00:33<00:00,  1.50it/s]
```

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

<br>Some weights of DistilBertForSequenceClassification were not initialized from the model checkpoint at distilbert-base-uncased and are newly initialized: `['classifier.bias', 'classifier.weight', 'pre_classifier.bias', 'pre_classifier.weight']`
<br>You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.

```
Reconstructed model from saved PEFT:
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
    num_rows: 18
})
```

`[101, 1045, 1005, 2310, 2464, 2023, 19142, 2210, 1005, 28101, 17312, 1005, 2116, 2335, 1012, 1996, 2069, 3291, 2003, 2049, 2747, 20165, 2006, 2678, 2030, 4966, 1012, 1045, 1005, 24529, 5121, 1037, 20127, 2005, 1037, 4966, 2713, 1012, 1996, 2172, 4771, 2957, 5207, 3248, 1005, 5061, 2100, 1005, 2019, 4654, 1011, 6986, 2137, 1010, 3005, 2074, 2042, 2207, 2013, 3827, 1010, 2002, 4858, 2370, 1037, 3105, 2004, 2019, 3751, 2937, 1999, 1037, 2924, 1010, 2009, 2035, 3632, 2092, 2127, 2002, 4858, 2370, 7861, 12618, 18450, 1999, 1037, 2924, 2002, 2923, 2007, 2010, 4654, 13675, 10698, 2229, 1010, 2585, 9152, 8159, 3248, 1996, 3040, 23356, 7332, 1010, 2049, 2019, 22249, 2210, 17083, 2361, 1010, 11504, 2996, 5033, 2030, 8133, 3016, 1010, 2097, 2272, 2000, 1996, 5343, 1012, 2298, 2041, 2005, 2198, 13919, 9082, 2077, 2002, 4930, 2009, 2502, 2007, 1005, 26822, 12734, 1005, 10642, 1997, 1996, 2439, 15745, 1005, 2935, 1997, 1996, 7635, 1005, 1999, 1037, 2235, 2535, 2004, 1037, 19805, 1010, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
`{'text': "I've seen this amusing little 'brit flick'many times. The only problem is Its currently unavailable on video or DVD. I'ts certainly a contender for a DVD release. The much missed Richard Jordan plays 'pinky' an Ex-pat American, whose Just been released from prison,he finds himself A job as an Electrician in a bank, it all goes well until he finds Himself Embroiled in a bank heist with his ex cronies, David Niven Plays the mastermind Ivan, Its an enjoyable little romp, hopefully studio canal or anchor bay, will come to the Rescue. Look out for john Rhys Davies Before he struck it big with 'shogun' Raiders of the lost Ark 'Lord Of The Rings' In a small role as a barrister,", 'label': 1, 'input_ids': [101, 1045, 1005, 2310, 2464, 2023, 19142, 2210, 1005, 28101, 17312, 1005, 2116, 2335, 1012, 1996, 2069, 3291, 2003, 2049, 2747, 20165, 2006, 2678, 2030, 4966, 1012, 1045, 1005, 24529, 5121, 1037, 20127, 2005, 1037, 4966, 2713, 1012, 1996, 2172, 4771, 2957, 5207, 3248, 1005, 5061, 2100, 1005, 2019, 4654, 1011, 6986, 2137, 1010, 3005, 2074, 2042, 2207, 2013, 3827, 1010, 2002, 4858, 2370, 1037, 3105, 2004, 2019, 3751, 2937, 1999, 1037, 2924, 1010, 2009, 2035, 3632, 2092, 2127, 2002, 4858, 2370, 7861, 12618, 18450, 1999, 1037, 2924, 2002, 2923, 2007, 2010, 4654, 13675, 10698, 2229, 1010, 2585, 9152, 8159, 3248, 1996, 3040, 23356, 7332, 1010, 2049, 2019, 22249, 2210, 17083, 2361, 1010, 11504, 2996, 5033, 2030, 8133, 3016, 1010, 2097, 2272, 2000, 1996, 5343, 1012, 2298, 2041, 2005, 2198, 13919, 9082, 2077, 2002, 4930, 2009, 2502, 2007, 1005, 26822, 12734, 1005, 10642, 1997, 1996, 2439, 15745, 1005, 2935, 1997, 1996, 7635, 1005, 1999, 1037, 2235, 2535, 2004, 1037, 19805, 1010, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}`

```
{'input_ids': tensor([[  101,  1045,  1005,  2310,  2464,  2023, 19142,  2210,  1005, 28101,
         17312,  1005,  2116,  2335,  1012,  1996,  2069,  3291,  2003,  2049,
          2747, 20165,  2006,  2678,  2030,  4966,  1012,  1045,  1005, 24529,
          5121,  1037, 20127,  2005,  1037,  4966,  2713,  1012,  1996,  2172,
          4771,  2957,  5207,  3248,  1005,  5061,  2100,  1005,  2019,  4654,
          1011,  6986,  2137,  1010,  3005,  2074,  2042,  2207,  2013,  3827,
          1010,  2002,  4858,  2370,  1037,  3105,  2004,  2019,  3751,  2937,
          1999,  1037,  2924,  1010,  2009,  2035,  3632,  2092,  2127,  2002,
          4858,  2370,  7861, 12618, 18450,  1999,  1037,  2924,  2002,  2923,
          2007,  2010,  4654, 13675, 10698,  2229,  1010,  2585,  9152,  8159,
          3248,  1996,  3040, 23356,  7332,  1010,  2049,  2019, 22249,  2210,
         17083,  2361,  1010, 11504,  2996,  5033,  2030,  8133,  3016,  1010,
          2097,  2272,  2000,  1996,  5343,  1012,  2298,  2041,  2005,  2198,
         13919,  9082,  2077,  2002,  4930,  2009,  2502,  2007,  1005, 26822,
         12734,  1005, 10642,  1997,  1996,  2439, 15745,  1005,  2935,  1997,
          1996,  7635,  1005,  1999,  1037,  2235,  2535,  2004,  1037, 19805,
          1010,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101, 15624,  1010,  3487,  1043,  1012,  3957,  2149,  1037, 22307,
          3193,  1997,  1996,  4735,  3639,  2088,  1012,  2034,  2002,  1005,
          1055,  2019,  2058,  4371, 23067,  2271, 12478,  2040, 10255,  1996,
          3308,  2158,  2000,  1996,  3242,  1006,  2209, 13459,  2135,  1010,
         12167,  4780,  2011, 13366,  2953, 28533,  5163,  1007,  1010,  2059,
          2002,  1005,  1055,  2061,  3561,  2007, 23124,  2010,  2069, 14017,
         10732,  2003,  1996,  5835,  1012,  5466,  1999,  1037, 12323,  2094,
          7472,  1010,  1037, 15958,  5915,  6934,  2046,  7279, 13098,  1998,
          2053, 24209,  2389,  5244,  2055,  2040,  2002,  6985,  2015,  1010,
          1998,  2279,  2518,  2017,  2113,  1011,  1011, 21146, 20722,   999,
          2304,  4190,  5160,  1006,  2643,  1045,  2293,  2008,  7655,  1007,
          1012,  2002,  5927,  1996,  2422,  2074,  1999,  2051,  2000,  3828,
          2010, 12323,  2094, 11419,  2013,  1996,  3242,  1012,  8038,  7962,
          1012,  1026,  7987,  1013,  1028,  1026,  7987,  1013,  1028,  2021,
          2428,  1010,  1996, 20747,  2895,  2003,  5760, 11463,  7716, 14672,
          1012,  2156,  2032,  8595,  2041,  1037,  7409,  1010,  2156,  2032,
          4392,  9947,  1010,  2156,  2032,  7475, 13459,  2135,  2004,  2002,
         29497,  1037,  7960,  4920,  1999,  2010,  7388,  1012,  2022,  4810,
          2005, 11463,  7716, 14672,  1012,  1026,  7987,  1013,  1028,  1026,
          7987,  1013,  1028,  1996,  7570,  4140,  1997,  1996,  2143,  2295,
          1010,  2003, 24408,  5735,  1012,  2007, 10543, 13366, 14147,  1996,
          4277,  1997,  8992,  1998,  2019, 26264,  5411,  7619,  5717,  1010,
          2016,  2003,  2242,  2000,  2156,  1012,  2130, 10955,  1037,  2978,
          1012,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  2043,  2017,  3422,  2659,  5166,  5469,  5691,  2004,  2172,
          2004,  1045,  2079,  1010,  2017,  2131,  2000,  2073,  2017,  2064,
          2425,  2040,  2001,  2920,  1999,  4526,  1996,  3185,  1010,  2004,
          2169,  2143,  1011,  9338,  9909,  2010,  2219, 14894,  2000,  1996,
          8808,  1012,  2107,  2003,  1996,  2553,  2007,  2990,  1011,  1051,
          1012,  2043,  1045,  3427,  2023,  5621,  9643,  3185,  1010,  1045,
          2001,  2187,  2007,  1996,  6151, 19825,  3468,  3110,  2008,  5965,
         15589,  2078,  4097,  2001,  2920,  1010,  2672,  2025,  2004,  2472,
          2021,  1999,  2070,  4827,  1010,  1998,  2004,  1045, 18800,  1010,
          1045,  2179,  2008,  1045,  2001,  6149,  1012,  2069,  5965,  1998,
          1037,  9210,  2140,  1997,  2500,  2071,  4339,  2242,  2023, 17203,
          1010,  1998,  2023,  3185,  2074,  2128, 23941,  2094,  1997,  5965,
         15589,  2078,  4097,  1012,  4983,  2017,  2066,  5965, 15589,  2078,
          4097,  1006,  1998,  2643,  2069,  4282,  2339,  3087,  2052,  1007,
          4468,  2023,  3185,  1012,  2065,  2017,  1005,  2128,  2183,  2000,
          9278,  2019, 15589,  2078,  4097, 27263,  1010,  9278,  5365,  8859,
         10376, 17074,  2015,  1010,  2009,  1005,  1055,  1996,  2069,  4408,
          9716,  2732,  1999, 15589,  2078,  4097,  1005,  1055,  2601,  8808,
          2100,  5304,  1997,  6659,  5691,  1012,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  2061,  6057,  2003,  1996,  3819,  2126,  2000,  6235,  2023,
          2260,  2781, 11867, 21511,  1997,  1996,  2434,  2732,  5233,  1012,
          8051,  5233,  2003, 11757,  6057,  1012,  2009,  2003,  3591,  2004,
          1996,  9117,  1997,  1996,  2686,  8680,  8051,  5233,  1012,  1996,
          8257,  2003,  2023,  1024,  5674,  2732,  5233,  2209,  2011,  2919,
          5889,  1998, 11757,  2919,  2569,  3896,  1012,  1996,  3494,  2421,
          1996,  1000,  6970,  9692, 28804,  2879,  1011,  4687,  1000, 19857,
          3489,  2732, 24204,  2121,  1010,  1996,  1000,  9078, 22146,  1998,
          6970,  9692, 28804,  7968,  3124,  1000, 10654, 16521,  1010, 18243,
          8458, 23233,  2121,  1010,  1000, 12700,  1000,  1998,  1037,  3677,
          1997,  2060, 10392,  3494,  1012,  2009,  2003,  5263,  2025,  2000,
          4756,  2004,  2017,  3422,  2023,  2260,  2781,  8813,  1012,  2009,
          1005,  1055,  5236,  2021,  2009,  1005,  1055,  4569,  1012,  2017,
          2097,  4756,  2013,  1996,  2707,  2000,  1996,  2203,  1010,  1998,
          2017,  2097,  2514,  1996,  2342,  2000,  3422,  2009,  2153,  1010,
          1998,  2153,  1010,  1998,  2153,  1010,  1998,  2153,  1012,  1012,
          1012,  1998,  2017,  2097,  4756,  2296,  2051,  2017,  2156,  2009,
           999,   999,   999,  1026,  7987,  1013,  1028,  1026,  7987,  1013,
          1028,  2184,  2041,  1997,  2184,  1012,  1996,  4569, 15580,  2102,
          2260,  2781,  2412,  2081,  1012,  2017,  2097,  2903,  2009,  6354,
          1037,  3371,   999,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  1996,  3526, 15677,  2033,  2012,  2034,  6054,  1012,  1045,
          2001,  1037,  2978,  4527,  2055,  2008,  2755,  1010,  2138,  1996,
          2466,  1997,  2008,  3185,  2003,  7078, 11771,  1012,  2065,  2009,
          2018,  2053,  2466,  1010,  1996,  2143,  2052,  2022,  2488,  1012,
         21122, 16284,  2015,  1000,  4895,  9610,  2368,  1998, 23067,  2226,
          1000,  3310,  2000,  2026,  2568,  1011,  1037,  2143,  2302,  2466,
          1010,  2021,  2036,  2007, 17160,  1998,  2823, 14888,  4871,  1012,
          2021,  1996,  3526,  2003,  2012,  2034,  1037,  5365,  1011,  3185,
          1010,  1998,  2069,  2117,  1037,  3538,  1997,  2396,  1012,  1045,
          1005,  1049,  2200,  4699,  1999, 16985,  3366,  2213,  1005,  1055,
          2279,  2622,  1012,  8429,  2006,  2796,  2071,  2022,  2200,  5875,
          1010,  2926,  2043,  2009,  2038,  1996,  2168,  3504,  2004,  1996,
          3526,  1012,  1026,  7987,  1013,  1028,  1026,  7987,  1013,  1028,
          2005,  2143,  2189, 20305,  1024,  4922,  5370,  1005,  1055,  3556,
          2005,  1996,  3526,  2003,  7078, 28851,  1010,  2021,  1037,  2524,
          5962,  3325,  1010,  2138,  1997,  2049,  2200, 19770,  2594,  2806,
          1012,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  1045,  2196,  7615,  2006,  1037,  2143,  1010,  2021,  1045,
          2031,  2000,  2360,  2008,  2023,  2001,  2028,  1997,  1996,  5409,
          3152,  2008,  1045,  2031,  2412,  2464,  1012,  1045,  2514,  2009,
          2001,  2081,  2011,  1037,  4088,  3678,  2143,  3076,  1998,  2025,
          2000,  2404,  2091, 10904,  2143,  2493,  1010,  2021,  2023,  2001,
          9202,   999,  1045,  2106,  2025,  4965,  1996,  2599,  3883,  1998,
          2371,  1045,  2001,  1999,  3772,  2465,  2007,  2014,  2096,  2016,
          2001,  2006,  2143,  1012,  2014,  6567,  2020,  2200,  3647,  1998,
          1045,  2514,  2016,  2001, 23150,  6834,  2060, 19910,  1999,  3152,
          1998,  2025,  3772,  1998,  2437,  2014,  2219,  6567,  1012,  1996,
          3257,  2001,  2200, 16801,  1998,  1996,  2614,  2001, 10989,  2084,
          1996,  5889,  3209,  1012,  1996,  2203,  2089,  2031,  2081,  1037,
          2210,  2062,  3168,  2065,  2045,  2001,  2619,  6583, 11335,  3436,
          1996,  2824,  1998,  2025,  1037,  2299,  1012,  1045,  2293, 25382,
         18856,  3170,  2021,  2016,  2014,  2774,  3711,  3243,  4703,  1999,
          3152,  1012,  2672,  1996,  2299,  4989,  2071,  2031,  2042,  1037,
          2210,  2062,  2434,  1012,  1996,  2299,  1000,  4689,  1000,  2001,
          2107,  1037, 18856, 17322,  1012,  2004,  1045,  2056,  2077,  1045,
          2196,  7615,  2006,  3152,  1998,  2031,  2464,  2026,  3745,  1997,
          2204,  1998,  2919,  1010,  2021,  2023,  2001,  1996,  5409,  1012,
          3374,  1012,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101, 11482,  1055,  3490, 10374,  2003,  6669,  3459,  2004,  6085,
          1010,  1037,  2431,  2529,  1010,  2431,  4393,  2124,  1996,  2154,
         26965,  1012,  2002,  2038,  2035,  2037, 20828,  1998,  2010,  2069,
         11251,  2003,  1996, 21810,  2005,  2668,  1012,  2144,  2002, 12597,
          2039,  2007, 13300,  2099,  1006, 19031, 19031,  3406, 12494,  3385,
          1007,  2002,  2038, 14682,  2091,  6144,  2040,  2031,  2973,  5921,
          2149, 22719,  2005,  4693,  1010,  2021, 18168,  3490, 11008,  4765,
          2058, 19980, 14845, 10097,  1006,  4459,  2079, 12881,  2546,  1007,
          2003,  5458,  1997,  2542,  1999,  9396,  2007,  1996,  4286,  1006,
          2833,  2004,  2002,  4455,  2068,  1007,  1998,  2002,  3488,  2000,
          5256,  2078,  1996,  2668,  2643,  1998,  2202,  2491,  1997,  1996,
          2088,  1012,  1026,  7987,  1013,  1028,  1026,  7987,  1013,  1028,
          2023,  3185,  2003,  2092,  3459,  1010,  2517,  1998,  2856,  1025,
         12725,  1996, 13972,  2038,  1037, 26162,  4536,  2013,  2707,  2000,
          3926,  1012,  8966,  2007,  2307,  2954, 10071,  1998, 13554,  7982,
          1010,  6085,  2003,  5121,  2062,  2895,  2084,  5469,  1010,  2021,
          2009,  5791, 18058,  1012,  1026,  7987,  1013,  1028,  1026,  7987,
          1013,  1028,  1022,  1013,  2184,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  2023,  2003,  1996,  2190,  2147,  1045,  2031,  2412,  2464,
          2006,  2547,  1012,  1996,  2466,  2003, 17075,  1011,  1011,  2035,
          1996,  2062,  2061,  2138,  2009,  2003,  2995,  1012,  1996,  4898,
          2106,  2037, 19453,  1011,  1011,  1996, 10640,  1997,  2824,  2003,
          2092,  8832,  1012,  1996,  3772,  2003,  2307,  1012,  2023,  2038,
          2000,  2022,  1996,  2190,  2535,  3520,  5380,  2669,  2038,  2412,
          2018,  1012,  1998,  1996,  2304,  1998,  2317, 16434,  2001, 11813,
          1012,  2026,  2069,  9038,  2003,  2008,  2009,  2003,  2025,  2800,
          2000,  4965,  1012,  1037,  2261,  2086,  3283,  1045, 11925,  2619,
          2920,  2007,  1996,  2537,  1006,  2593,  2007, 13683,  2030,  1999,
          2563,  1007,  1998,  2001,  2409,  2027,  2018,  2053,  3488,  2000,
          2713,  2009,  2006, 17550,  1006,  2012,  1996,  2051,  1007,  1012,
          2023,  2001,  1037,  4035,  2537,  1998,  2743,  1999,  1996,  1057,
          1012,  1055,  1012,  2006,  2137, 17408,  1012,  2045,  2003,  2107,
          2019,  3037,  1999,  3773,  2023,  1011,  1011,  2074,  2524,  2000,
          2903,  2053,  2028,  2064,  2191,  2009,  2800,  1012,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  2812, 24462,  1010,  1998,  2091,  2157,  2139, 16307,  2075,
          6789,  2000,  1996,  4438,  2336,  1005,  1055,  6925,  2025,  2069,
         14087,  1996, 11084,  1997,  2049, 18921, 27753,  5886,  2021, 14087,
          2151,  5848,  2054,  2061,  2412,  1012,  3505, 13854,  2323,  2025,
          2069,  2022, 14984,  1997,  2370,  2005,  2010,  9202,  2836,  2008,
          2003,  1037,  3154, 10973,  2125,  1997,  2054,  3958, 12385,  3240,
          2106,  2021,  2002,  2323,  2507,  2039,  3772,  2035,  2362,  1012,
          2002,  2003,  2061, 15703,  2008,  2017,  2052,  2215,  2000,  3786,
          1996, 10231,  2041,  1997,  2032,  2065,  2017,  2020,  2583,  2000,
          5376,  2157,  1999,  1996,  2143,  1012,  1996,  4520,  2024,  9200,
          1998,  1996, 16434,  2003,  2200,  3532,  1012,  1045,  2031,  2464,
          1037,  2843,  1997,  2919,  2143,  2023,  2095,  1010,  2021,  2023,
          2025,  2069,  3138,  1996,  9850,  2021,  2009,  2003,  2007,  2041,
          1037,  4797,  2028,  1996,  4788,  3152,  2412,  2081,  1012,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  1045,  2064,  3305,  2129, 15377,  2064,  2022, 15703,  2000,
          2070,  1010,  2021,  1996, 11150,  2002,  4152,  2003,  2200,  9951,
          1012, 15377,  2001,  2081,  3432,  2157,  2013,  1996,  2927,  1998,
         17839,  3475,  1005,  1056,  2919,  1010,  2926,  2005,  1996,  2402,
          3924,  2002, 20432,  2015,  1012,  1045,  7714,  2424,  2023,  2265,
          2000,  2022,  2200,  2104,  9250,  2558,  1012, 15377,  1004,  2814,
          2003,  1037,  2200,  4547,  2265,  1999,  2026,  5448,  1998,  2130,
          2459,  2086,  2044,  2049,  2834,  1006,  1998,  3053,  2538,  2086,
          2044,  1996,  2839,  1005,  1055,  2834,  2006,  2188,  2678,  1007,
          1010,  2002, 16481,  2051,  1998,  2051,  2153,  2008,  2002,  2145,
          9023,  2000,  2402,  2336,  1012,  2672,  2625,  2061,  2084,  1999,
          1996,  2220,  3938,  1005,  1055,  2073, 15377,  2001,  1996,  8410,
          8124,  1997,  1996,  2051,  1010,  2021,  2002,  1005,  1055,  2145,
          1037,  4438,  1012,  2004,  1037,  5470,  1997, 15377,  2870,  1010,
          1045,  2514,  2008,  1045,  2323,  6985,  2032,  1999,  1037,  2126,
          2008,  2987,  1005,  1056,  4025,  2066, 12403,  2213,  1012,  1996,
          2126,  1996,  6379,  3124, 12011,  2477,  2089,  2022,  2200, 21934,
         24759,  6553,  1998,  4895, 22852,  6553,  1010,  2021,  2052,  2017,
          2738,  2031,  2068,  4994,  2055,  2162,  1029,  2022, 18836,  2070,
          2028,  1006,  1037,  9427,  2094, 15799,  1010,  2021,  2145,  1007,
          2003,  2045,  2000,  7216,  4268,  1998,  2292,  2068,  2022,  4268,
          3432,  1012,  1999,  2023,  2154,  1998,  2287,  1010,  1045,  2514,
          2008,  2057,  5481,  2256,  4268,  2000,  4982,  2039,  1998, 15377,
          2003,  2045,  2000,  2360,  2017,  2064,  2145,  2022,  1037,  2775,
          2012,  2540,  1012,  1999,  2804,  1010,  2116,  1997, 15377,  1005,
          1055,  8220,  2006,  2783,  4178,  2055, 20228, 22974, 23061,  2213,
          1010,  2108,  7481,  1010,  1998,  2748,  1012,  1012,  1012,  2130,
          2331,  1010,  2071,  5574,  2000,  3071,  1010,  2025,  2074,  2010,
          4539,  4378,  1012,  4661,  1010,  2256,  2336,  2342,  2000,  4553,
          2000,  2022,  2785,  1998,  4847,  2500,  2005,  2040,  2027,  2024,
          1010,  1998,  2002,  7126,  2068,  2079,  2008,  1012,  1999,  2460,
          1010, 15377,  2089,  2022, 15703,  2000,  2070,  2111,  1998,  1045,
          3294,  3305,  2339,  1010,  2021,  3013,  2032,  2070, 19840,  1012,
          2035,  2002,  1998,  2010,  2814,  1006,  2247,  2007,  2718,  4024,
          1010,  2010,  2537,  2194,  1007,  2024,  2667,  2000,  2079,  2003,
          2393,  4268,  2025,  2069,  4553,  4072,  4813,  1010,  2021,  2000,
          2031,  4569,  1998,  2000,  2036,  2298,  2012,  1996,  3893,  3033,
          1997,  2166,  1012,  2065,  2062,  2111,  7791,  2000,  2037,  2336,
          1005,  1055,  5440,  2839,  1998,  7021,  2032,  2083,  2037,  2159,
          1010,  2672,  2057,  2876,  1005,  1056,  2022,  2061,  4997,  2055,
          2032,  1998,  4298,  2166,  2993,  1012,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  2076,  1037,  6480,  1997,  3773,  1998,  9107,  5190,  1997,
          3152,  1010,  3110,  5135,  2003,  7078,  1996,  5409,  1006,  1008,
          1008,  2350,  2143,  2007,  1037,  1011,  2862,  3340,  1007,  2008,
          1045,  2031,  2412,  2464,  1012,  3347,  3904,  1012,  2023,  3185,
          6135, 11896,  2006,  2296,  2504,  1012,  2009,  1005,  1055,  9996,
         16164,  1998,  5493,  1012,  2045,  1005,  1055,  4895,  7076, 21649,
          3772,  1010,  1996,  2785,  2073,  1996,  5889,  3711, 11471,  2041,
          1997,  2037,  9273,  1012,  2074,  9334,  3477,  5403, 10603,  1010,
          3383,  1029,  1998,  5409,  1997,  2035,  1010,  1996, 22889,  6784,
          6292,  5896,  3544,  2000,  2031,  2042,  2517,  2104,  1996,  3747,
          1997,  2070, 16010,  9415,  2179,  2069,  1999, 22365,  2015,  1012,
          1045,  2064,  1005,  1056,  2130,  4088,  2000, 22346,  2129,  1996,
          3213,  1013,  2472,  2071,  2412,  2031,  2179,  3087,  2000,  5446,
          2023,  2622,  1010,  2292,  2894,  9958,  2151,  1997,  1996,  3340,
          2008,  2009,  2106,  1012,  1045,  5621,  4299,  1045,  2071,  2131,
          2067,  1996,  2051,  2008,  1045, 13842,  3666,  2023,  3538,  1997,
         13044,  1012,  2065,  2825,  1010,  1045,  2052,  2031,  2445,  2023,
          2143,  1037,  3694,  1997,  5717,  1012,  2488,  2664,  1010,  1037,
          4997,  2193,  1012,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  2043,  1045,  2001,  1999,  5504,  3694,  1006,  2067,  1999,
          3355,  1007,  1010,  1045,  2001,  2356,  2000,  3191,  1996,  3117,
          2008,  2023,  2001,  2241,  2006,  2004,  2112,  1997,  2026,  2394,
          2465,  2913,  1012,  1045,  2064,  3342,  2108,  2200,  5028,  2011,
          2009,  1998,  7568,  2043,  1037,  2694,  2544,  2234,  2041,  1037,
          2095,  2101,  1012,  1026,  7987,  1013,  1028,  1026,  7987,  1013,
          1028, 19031,  3723, 11338,  8713, 14854,  2001,  1037,  2759,  2694,
          3883,  2043,  2023,  2143,  2001,  2550,  1998,  2001,  2525,  2652,
          1037,  2684,  1999,  1037, 28466,  2389,  2155,  2006,  1996,  2718,
          2694,  2186,  1000,  2155,  1000,  1012,  2009,  2001,  3154,  2008,
          2016,  2018,  1996,  2846,  1998,  3754,  2000,  4139,  2125,  2023,
          2112,  1012,  1045,  9131,  2014,  2004,  2108,  1037,  2978,  1000,
         10551,  1000,  2012,  2335,  1010,  2021,  2058,  2035,  2016,  2515,
          1037,  2204,  3105,  1012,  2016,  7883,  1996,  3185,  2092,  1012,
          1026,  7987,  1013,  1028,  1026,  7987,  1013,  1028, 14631,  4897,
          2063,  2003, 10392,  2004,  1996,  4968,  2040,  3544,  2000,  2022,
          1996,  2069,  2028,  1999,  1996,  4398,  2008,  3849,  2000,  5621,
          2729,  2005,  2014,  1012,  6437, 24953,  2004,  1996,  5399, 10363,
          1998,  3621, 11265, 10976,  4588,  2388,  2003,  2036,  2204,  1010,
          2004,  2003,  2402,  5863, 17133,  1006,  2040,  2052,  2776,  3711,
          2004,  1996,  2304,  7794, 16554, 22622,  1999,  1000,  5519, 11373,
          1000,  1007,  2004,  1996,  4086,  3920,  2905,  2040,  3849,  2000,
          2022,  1996,  3579,  1997,  1996,  6687,  1005,  1055, 12242,  1012,
          5503, 12017,  2003,  2036, 23263, 16004,  2004,  1996,  2446,  5268,
          1997,  1996,  2516,  1026,  7987,  1013,  1028,  1026,  7987,  1013,
          1028,  1996,  2190,  2836,  1010,  2174,  1010,  7460,  2000,  2745,
         12790,  1012,  2009,  2003,  5621,  3928,  1998,  7857,  2098,  2062,
          5038,  2084,  2009,  2288,  2012,  1996,  2051,  1012,  1996, 22364,
          1998,  3147,  2791,  2002, 16783,  3084,  1996,  5019,  1999,  2029,
          2002,  3544,  3697,  2000,  3422,  1010,  2021,  3084,  2009,  2172,
          6082,  2000,  3305,  1996,  4251, 15561,  1997,  1996,  5837,  2684,
          1012, 12790,  3957,  2673,  1996,  2157,  8015,  1998,  3849,  2000,
          2031,  1037,  2204,  4824,  1997,  1996, 10318,  8317, 14354,  2015,
          1012,  1026,  7987,  1013,  1028,  1026,  7987,  1013,  1028,  1996,
          2143, 12980,  2013,  1996,  2338,  2069,  1999,  2070,  2235,  3971,
          1012,  2009,  2003,  6919,  1998, 18988,  2000,  3422,  1010,  1998,
          1045,  3246,  2008,  2009,  4152,  2207,  2153,  2006,  2000,  2678,
          2030,  4966,  1012,  1026,  7987,  1013,  1028,  1026,  7987,  1013,
          1028,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  2009,  1005,  1055, 16267,  5793,  2008,  1996,  2111,  2040,
          2081,  2023,  1000,  3185,  1000,  2031,  2196,  2464,  2107,  8235,
         11867, 21511,  2015,  2004,  1000,  1996,  6248,  3282,  1000,  1998,
          1000,  2980,  7171,  1000,  1012,  2023,  3185,  2003,  6659,  1010,
          1998,  2061,  2024,  1996,  5889,  1012,  2027,  2876,  1005,  1056,
          2113,  3772,  2130,  2065,  2009,  2718,  2068,  1999,  1996,  2227,
          1010,  2004,  1045,  2371,  2066,  2725,  2096,  3666,  2023,  2561,
          8632,  1997, 29132,  1012,  1026,  7987,  1013,  1028,  1026,  7987,
          1013,  1028,  1996,  3185,  2003,  5236,  1998,  2038,  2053,  8562,
          1999,  2009,  2054,  2061,  2412,  1012,  1045,  1005,  1049,  2469,
          2008,  1045,  2071,  2191,  1037,  2488,  3185,  2007,  2026,  2814,
          1012,  2000,  2033,  2009,  1005,  1055,  6429,  2008,  1037,  3185,
          2064,  8246,  2023,  2172,  1012,  2025,  1037,  2309, 12266,  2030,
          6057,  2240,  1012,  2053,  7637,  1997,  4454,  2369,  2009,  1012,
          2009,  1005,  1055,  1037, 17203,  3185,  1998,  1045,  1005,  1040,
          2066,  2000,  3113,  1996,  2711,  2040,  2941,  7777,  2023,  3185,
          1012,  9805,  3600,   999,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  2023,  2265,  2038,  2000,  2022,  2026,  5440,  2041,  1997,
          2035,  1996,  3770,  1005,  1055,  5469,  2694,  3065,  1012,  2066,
          7122,  2013,  1996,  2601,  7363,  1010,  2036,  2013,  1996,  2168,
         17277,  1010,  2023,  2265,  2003,  1037,  4678, 17070,  1012,  2065,
          2017,  5993,  2007,  2033,  1010,  3531,  3696,  2023,  9964,  1045,
          2318,  1010,  2000,  2131,  1996,  2773,  2041,  2005,  9219,  1998,
          2131,  2009,  2041,  2006,  4966,  1012,  2182,  2003,  1996,  9964,
          4769,  1024,  7479,  1012,  9964,  2239,  4179,  1012,  4012,  1013,
          3301, 22932, 22932,  1013,  9964,  1012, 16129,  2070,  1997,  2026,
          5440,  4178,  2052,  2031,  2000,  2022,  1043, 17960,  1043, 17960,
          1010,  1998,  4542,  3153,  1012,  1045,  2036,  3866,  1996,  3098,
         17174,  2007,  1996,  6071,  2155,  1012,  2008,  2109,  2000, 19815,
          2033,  2041,   999,  2028,  1997,  1996,  2477,  1045,  2052,  2031,
          2000,  3198,  1996,  4966, 17277,  2000,  2421,  2052,  2022,  1996,
          5812,  2614,  2657,  2157,  2077,  2073,  1996,  3293,  3338,  2052,
          2022,  1012,  1045,  2123,  1005,  1056,  2113,  2065,  2151,  1997,
          2017,  3342,  2008,  2112,  2021,  2008,  1005,  1055,  2028,  1997,
          1996,  2364,  2477,  2008,  7545,  2067,  5758,  2000,  2033,  1012,
          1045,  2812,  1010,  2272,  2006,   999,  2162,  1997,  1996,  8484,
          1996,  2694,  2186,  2525,  2038,  2042,  2207,  2006,  4966,  1010,
          2061,  1045,  2360,  9219,  1010,  1998,  2036,  7122,  2013,  1996,
          2601,  7363,  1010,  1998,  5958,  1996,  6122,  1996,  2186,  2323,
          2022,  2207,  2205,   999,  2057,  1996,  4599,  2342,  2000,  3713,
          2256,  9273,   999,  2057,  2342,  2023, 12476,  2265,  2006,  4966,
          2061,  3531,  3659,  1996,  2773,   999,   999,   999,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  2023,  2003,  1996,  2028,  2350,  3291,  2007,  2023,  2143,
          1010,  2247,  2007,  1037,  2204,  3066,  1997,  5447, 10054,  1005,
          5221,  5691,  1024,  2589,  1999,  1037,  3653,  6528, 20771,  2126,
          2011,  3653,  6528, 20771,  2111,  1012,  1026,  7987,  1013,  1028,
          1026,  7987,  1013,  1028,  2009,  1005,  1055,  2428,  6517,  1010,
          2021,  1000,  2502,  7171,  1000,  3185, 11153,  1006,  4439, 11898,
          2358,  8609,  2271,  1012,  1012,  1012,  1007,  2013,  2023,  2874,
          7164,  2027,  2288,  1996, 27046,  2705,  1010,  2027,  2113,  2054,
          1996,  2210,  2111,  2066,  1012,  1026,  7987,  1013,  1028,  1026,
          7987,  1013,  1028,  2057,  1005,  2128,  2025,  1037,  4138,  2874,
          1010,  2296,  2051,  1037,  2502,  3185,  2066,  2023,  1006,  2382,
          8817,  1029,   999,   999,  1029,  1007,  2003,  2081,  1010,  2009,
          1005,  1055,  6276,  2125,  1037,  2843,  1997,  2500,  2040,  2180,
          1005,  1056,  2156,  2037,  3185,  2081,  2138,  1997,  3768,  1997,
         10605,  2393,  1012,  2061,  2009, 19421, 19960,  3695, 26775,  3012,
          1025,  2069,  5691,  2013,  1000,  2814,  1997,  1996,  2155,  1000,
          2024,  2183,  2000,  2022,  2081,  1012,  1026,  7987,  1013,  1028,
          1026,  7987,  1013,  1028,  1045,  2614,  4854,  1998,  1045,  2572,
          1012,  1045,  2253,  2156, 25207,  1011,  2605,  8074,  1037,  4990,
          1999,  1996,  3268,  1997,  2026, 10748,  1010,  2021,  1045,  2179,
          2870,  5881,  1999,  1037,  4770,  1997,  4297,  5644, 27870, 14767,
          1024,  2413,  9669,  1006,  2057, 10657,  3531,  2256, 12334,  1010,
          2061,  1042,  1008,  1008,  1008,  2256,  5447, 10054,  1005,  2653,
          1007,  1998,  3768,  1997,  3439,  2470,  2003,  2069,  1037,  2261,
          1012,  5587,  1037,  3409,  2100,  2293,  2466,  1998,  1996,  2168,
          2189,  3556,  2652,  2153,  1998,  2153,  1998, 12873,  5447, 10054,
          1005, 13972,  2003,  6069,  2330,  2039,  1998,  3198,  2005,  2062,
          1012,  1045,  1005,  1049,  5580,  2023,  3653,  6528, 20771,  3538,
          1997,  1055,  1008,  1008,  1008,  2134,  1005,  1056,  2079,  2004,
          3740,  2011,  1996, 11898,  2358,  8609,  2271,  2502,  7171,  1012,
          1012,  1012,  2009,  1005,  1055,  6069,  2393,  3185, 11153,  2040,
          4995,  1005,  1056,  1999,  1996,  2200, 19868,  1000,  3185,  2449,
          1000,  1997,  5447,  1012,  1026,  7987,  1013,  1028,  1026,  7987,
          1013,  1028,  9278, 22206,  3347,  2612,  1998,  2031,  1037,  2613,
          2204,  2051,  1012,  1026,  7987,  1013,  1028,  1026,  7987,  1013,
          1028,  8827,  1024,  1045,  1005,  2222,  2196,  9641,  2068,  2005,
         27853,  2107,  2019, 12476,  2516,  1012,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  1045,  2572,  2200,  4699,  1999,  4111,  2336,  1998,  1045,
          2031,  3191,  2116,  3341,  2099,  5785, 25991,  6002,  1011,  1011,
          2021,  2023,  9643,  3185,  2481,  1005,  1056,  2562,  2033,  4699,
          1010,  4496,  2071,  1045,  4308,  2035,  1996, 18691,  1010,  4895,
         22852,  6553,  5019,  1012,  1045,  2069,  3266,  2000,  4133,  2083,
          1996,  3088,  2112,  1998,  2198,  1005,  1055,  2034,  2261,  2420,
          1999,  3885,  1012,  2292,  1005,  1055,  2831,  2055,  1005,  4895,
         22852,  6553,  1005,  1998,  1005,  2091, 15950, 10021,  1005,   999,
          1996,  5889,  1999, 23957, 11072,  2246,  2066,  4469,  2312,  9610,
         25370,  1010,  2738,  2084,  2307, 27754,  1006,  2045,  2003,  1037,
          4489,  1007,  1012,  2027,  2106,  2025,  2693,  2007,  1996,  4519,
          2008,  1037,  3748,  4111,  2052,  1012,  1006,  2005,  7831,  1010,
          2156,  2070,  1997,  1996,  2488,  4774,  1997,  1996, 27754,  5691,
          2073,  2027,  4738,  2037,  5889,  2000,  2693,  1999, 28684,  2319,
          4827,  1007,  1012,  1996, 27754,  4521,  2312,  5292,  4609,  8376,
          1997,  6240,  1011,  1011,  2025,  1037,  2691, 23957,  3218,  2004,
          2521,  2004,  1045,  2113,  1012,  1045,  2572,  1037, 26476,  2005,
          4111,  3441,  2021,  1996,  5896,  2106,  2025,  2191,  2033,  2729,
          2055,  1996, 27754,  1012,  1996,  2307,  2317,  9624,  1997,  1996,
          5590,  2008,  4858,  2198, 11811,  2024, 25869,  5555, 20689,  4509,
          4498,  1012,  1996,  3008,  1997, 11811,  2020,  2911, 13088, 11012,
          2098,  2006,  2019,  4153,  3509,  1010,  2021,  5064,  2009,  2003,
          1037,  2200,  2146,  4440,  2091,  1996,  2314,  2000,  2131,  2000,
          1996,  3023,  1011,  1011,  2507,  2033,  1037,  3338,   999,  2292,
          1005,  1055,  2831,  2055,  1005,  4030,  1005,  1012,  2130,  1996,
         12455,  2040,  2228,  2023,  2003,  2019,  6581,  3185,  6449,  2008,
          2009,  2003,  2025,  2019,  2895,  3185,  1012,  2521,  2013,  2009,
          1012,  2009,  5363,  2000,  2022,  1037,  2839,  2817,  1011,  1011,
          6854,  1996,  2091, 15950, 10021,  2112,  3653,  9527, 28184,   999,
          1045,  2106,  2025,  3191, 25991,  1005, 24566,  2808,  1010,  2021,
          2116,  1997,  2010,  2060,  2186,  1011,  1011,  2027,  2020,  8966,
          2007, 15902,  2895,  1998, 14779,  3800,   999,  2023,  2143,  2074,
          3475,  1005,  1056,  2045,  1012,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101,  1996,  1000,  2204,  2739,  1000,  2003,  2008,  1996,  9661,
          2003,  1999,  2237,  1012,  1996,  1000,  2919,  2739,  1000,  2003,
          2008,  1005,  1055,  2157,  2058, 12883, 16291,  1005,  1055,  5230,
          2188,  1012,  2002, 17507,  2039,  2004,  2010,  2173, 10854,  2066,
          2019,  8372,  2718,  2009,  1010,  2043,  3667,  9044,  7533,  2046,
          1996,  2598,  1998, 16825,  2358, 25377,  2011,  1010,  4385,  1012,
          1026,  7987,  1013,  1028,  1026,  7987,  1013,  1028,  2000,  2022,
          2062,  3563,  1010,  1996,  7212,  1005,  7980,  2003,  2173,  3599,
          2058, 12883,  1005,  4920,  1012,  1996,  7006, 27907,  2015,  2833,
          1010,  1998,  2011,  2832,  1997,  9614,  1010,  4481,  2041,  2009,
          1005,  1055,  1037, 10442,  1012, 12883,  1010,  8025,  2054,  2035,
          1996, 14513,  3388,  2003,  2055,  1010,  7266,  2010,  2126,  2083,
          1996,  5234,  1998,  7266,  2039,  1999,  1996,  7006,  1005,  1055,
          2677,  1012,  1026,  7987,  1013,  1028,  1026,  7987,  1013,  1028,
          1045,  1005,  2222,  2360,  2005,  2518,  2005, 22861,  1024,  2002,
          2003,  6135, 22518,  1010,  2012,  2560,  1999,  2023,  9476,  1010,
          1998,  2012,  2560,  2005,  2382,  3823,  1012,  2043,  2002,  3310,
          2000,  2010,  9456,  1010,  2002,  3216,  2066,  4689,  1998,  2057,
          2131,  1037,  7006,  1011,  6431,  1011,  1037, 10442,  2645,  1996,
          2717,  1997,  1996,  2126,  1012,  2320,  2153,  1010, 12883,  5344,
         12873,  7116,  1010,  2028,  2002,  4455,  1000, 19212,  1010,  1000,
          2021,  7006,  2003,  9205,  1998, 12883,  2097,  2342,  2035,  2010,
         25433,  1998,  5399,  1011,  8275, 11655,  3567,  3527,  2000, 21713,
          2094,  2125,  2023,  6841,  1012,  1026,  7987,  1013,  1028,  1026,
          7987,  1013,  1028,  2055,  2431,  1996, 18201,  2015,  2024,  5236,
          1998,  1996,  2060,  2431,  6057,  1010,  2021,  2467,  3435,  1011,
          3048,  1010, 14231,  1998,  2204,  2438,  2000, 16755,  1012,  1045,
          2812,  1010,  2009,  1005,  1055,  2025, 10126,  2017,  2064,  2156,
          1037,  7006,  2006,  1037,  8132,  9351,  2063,  1010,  2030,  2725,
          1037, 15876,  2721,  3153,   999,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1]])}
{'input_ids': tensor([[  101, 11771,  1010, 12580, 21425,  7815,  3850,  1012,  2984,  7482,
          5405,  2003,  2496,  2000,  6945, 18033,  2239,  2040,  1005,  1055,
          2383,  2019,  6771,  2007, 10941,  2474, 11039,  2072,  1012,  5405,
          2003,  2814,  2007,  2474, 11039,  2072,  1998,  2987,  1005,  1056,
          2113,  2055,  1996, 16789,  1012, 18033,  2239,  8289,  1999,  2019,
          4926,  1998,  2474, 11039,  2072,  2003,  6875,  2007,  2010,  3336,
          1012,  8038,  7962,   999,  1026,  7987,  1013,  1028,  1026,  7987,
          1013,  1028,  1045,  1005,  1049, 14984,  2000,  6449,  1045,  3825,
          2769,  2000,  2156,  2023,  1999,  1037,  3004,  1999,  3069,  1012,
          1045,  4669,  2035,  2093,  3340,  2021,  2130,  2037,  6196, 11725,
          2481,  1005,  1056,  4139,  2023,  2125,  1012,  1045,  7887,  2354,
          2054,  2001,  2183,  2000,  4148,  1012,  2066,  2178, 13082,  2056,
          1011,  1011,  2023,  3248,  2066,  1037, 18720,  1011,  6758,  6480,
          3185,  1012,  1026,  7987,  1013,  1028,  1026,  7987,  1013,  1028,
          2009,  2515,  2031,  2474, 11039,  2072, 25082, 25493,  2012,  2028,
          2391,  1998,  2130,  5405, 11082,  6065,  2320,   999,  2036,  2045,
          1005,  1055,  1037, 23100,  7171,  1997,  2327,  3238,  2308,  2652,
          2374,  1006,   999,   999,   999,  1007,  1012,  2060,  2084,  2008,
          2009,  1005,  1055,  2694,  5379,  1012,  1996,  2069,  2204,  2518,
          2055,  2023,  2001, 10805, 15659,  2652,  5405,  1998, 18033,  2239,
          1005,  1055,  9454,  2365,  1012,  2200,  8502,  1998,  3243,  1037,
          2204,  3364,  1012,  2008,  4998,  2045,  1005,  1055,  2498,  2000,
         16755,  2023,  1012,  2017,  1005,  2310,  2464,  2009,  2077,  1012,
          1012,  1012,  1998,  2589,  2488,  1012,  2009,  1005,  1055,  5525,
          2042,  6404,  1012, 13558,  2009,  1012,   102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1]])}
```

`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`

```
                                                 text  predictions  labels
0   I've seen this amusing little 'brit flick'many...            0       1
1   Yep, Edward G. gives us a retro view of the cr...            0       0
2   When you watch low budget horror movies as muc...            0       0
3   So funny is the perfect way to describe this 1...            0       1
4   THE CELL fascinated me at first glance. I was ...            0       1
5   I never comment on a film, but I have to say t...            0       0
6   Wesley Snipes is perfectly cast as Blade, a ha...            0       1
7   This is the best work i have ever seen on tele...            0       1
8   Mean spirited, and down right degrading adapta...            0       0
9   I can understand how Barney can be annoying to...            0       1
10  During a lifetime of seeing and enjoying thous...            0       0
11  When I was in 7th grade(back in 1977), I was a...            0       1
12  It's painfully obvious that the people who mad...            0       0
13  This show has to be my favorite out of all the...            0       1
14  This is the one major problem with this film, ...            0       0
15  I am very interested in animal children and I ...            0       0
16  The "good news" is that the circus is in town....            0       1
17  Boring, utterly predictable soap opera. Mary T...            0       0
```

`{'accuracy': 0.5}`

`Process finished with exit code 0`
