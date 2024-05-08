import torch.nn.functional as F
from torch import Tensor
from transformers import AutoTokenizer, AutoModel
from FE_TEST_STRING.FE_TEST_STRING import docs
from components.sort_n_show import sort_n_show

# https://huggingface.co/thenlper/gte-large

def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]

tokenizer = AutoTokenizer.from_pretrained("thenlper/gte-large")
model = AutoModel.from_pretrained("thenlper/gte-large")

input_texts = [
    "What cylinders does the stand have?",
    # "What are the blue tubes coming from the cylinder for?",
]
input_texts.extend(docs)

# Tokenize the input texts
batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors='pt')

outputs = model(**batch_dict)
embeddings = average_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

# (Optionally) normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:1] @ embeddings[1:].T)

sort_n_show(input_texts, scores, 0.75)