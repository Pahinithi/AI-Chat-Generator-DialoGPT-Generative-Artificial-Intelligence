from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "microsoft/DialoGPT-large"  # You can use other sizes like "small" or "medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Function to generate responses
def generate_response(input_text, max_length=1000, num_return_sequences=1):
    # Encode the input text
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')

    # Generate response
    outputs = model.generate(input_ids, max_length=max_length, num_return_sequences=num_return_sequences,
                             pad_token_id=tokenizer.eos_token_id, no_repeat_ngram_size=3, top_p=0.92, temperature=0.75)

    # Decode the generated responses
    generated_responses = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    
    return generated_responses
