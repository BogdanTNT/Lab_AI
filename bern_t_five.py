import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, AutoModelForSeq2SeqLM

# https://huggingface.co/google/flan-t5-base

# Initialize the tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")

# Check if CUDA is available and then set the device appropriately
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Function to encode the conversation history and generate a response
def generate_response(input_text, chat_history):
    # Append the new input text to the chat history
    if chat_history:
        new_input = f"{chat_history} {input_text}"
    else:
        new_input = input_text
    
    # Tokenize the updated conversation
    input_ids = tokenizer.encode(new_input, return_tensors="pt").to(device)
    
    # Generate a response
    outputs = model.generate(input_ids, max_length=512)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Main chat loop
chat_history = ""
print("AI is ready to chat! Type 'quit' to exit.")
while True:
    input_text = input("You: ")
    if input_text.lower() == 'quit':
        break
    # Generate and print the response from the AI
    chat_history = generate_response(input_text, chat_history)
    print("AI:", chat_history)
