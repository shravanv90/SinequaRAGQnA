import streamlit as st
import requests
from transformers import GPT2LMHeadModel, GPT2Tokenizer,AutoTokenizer, AutoModelForSeq2SeqLM

# Load the GPT-2 model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
MAX_TOKENS = model.config.n_positions - 10  # Keeping a buffer for generated content

# --- Sinequa Interface ---
def query_sinequa(question):
    SINEQUA_ENDPOINT = 'http://<API_URL>/api/v1/query'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "app": "<Appname>",
        "user": "<user>",
        "password": "<passw>",
        "query": {
            "name": "<query_name>",
            "text": question
        }
    }
    response = requests.post(SINEQUA_ENDPOINT, headers=headers, json=data)

    records = response.json().get('records', [])
    highlighted_texts = [extract['highlighted'] for record in records 
                         for extract in record.get('extracts', []) 
                         if 'highlighted' in extract]
    
    return highlighted_texts

# --- GPT-2 Response Generation ---
def generate_answer(question):
    # Get passages from Sinequa
    passages = query_sinequa(question)

    # Combine question and passages for context
    context = question + " " + " ".join(passages)

    # Tokenize context and truncate if needed
    input_ids = tokenizer.encode(context, return_tensors="pt", truncation=True, max_length=MAX_TOKENS)

    # Generate response
    outputs = model.generate(input_ids, max_length=MAX_TOKENS, pad_token_id=tokenizer.eos_token_id)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer

def format_answer(answer):
    # Use set to avoid duplicates
    unique_sentences = set()

    # Split by '.' to get individual sentences and iterate
    for sentence in answer.split('.'):
        stripped_sentence = sentence.strip()
        if stripped_sentence and stripped_sentence not in unique_sentences:
            unique_sentences.add(stripped_sentence)

    # Convert set back to list to maintain order
    ordered_sentences = list(unique_sentences)

    # Rejoin sentences and format bold tags
    cleaned_answer = '. '.join(ordered_sentences)
    cleaned_answer = cleaned_answer.replace('{b}', '**').replace('{nb}', '**')  # Markdown bold format

    return cleaned_answer


# --- Streamlit Interface ---
st.title("RAG Enterprise Search Q&A")

user_input = st.text_input("Ask a question:")
if user_input:
    raw_answer = generate_answer(user_input)
    formatted_answer = format_answer(raw_answer)
    st.markdown(formatted_answer)

