from sentence_transformers import SentenceTransformer, util
import torch
from FE_TEST_STRING.FE_TEST_STRING import docs
from components.sort_n_show import sort_n_show

# Load the pre-trained model from Hugging Face
model = SentenceTransformer("jinaai/jina-embeddings-v2-base-en", trust_remote_code= True)

# Define the query and extend it with other documents
# input_texts = ["I see two boxes. They look like computers. What might they be and what do they do?"]
input_texts = ["I don't under stand all the valve system. How does it work?"]
input_texts.extend(docs)

# Encode all texts to embeddings
embeddings = model.encode(input_texts, convert_to_tensor=True)

# Compute cosine similarities
# The query is the first element; compare it with all other documents.
cosine_scores = util.cos_sim(embeddings[0], embeddings[1:])

sort_n_show(input_texts, cosine_scores, 0.7)