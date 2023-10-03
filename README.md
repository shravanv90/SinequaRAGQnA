# **Retrieval Augmented Generation (RAG) Enterprise Search Q&A**

This application employs RAG (Retrieval-Augmented Generation) methodology combined with the FLAN-T5 model from Hugging Face and Sinequa. Users can pose questions and receive detailed, context-aware answers sourced from the sinequa SBA App.

\[!RAG\](assets/ragimage.png)

## **Why RAG?**

---

The RAG approach bridges the gap between extractive question-answering models and generative language models. By using RAG:

- **Efficient Information Retrieval**: Extracts relevant snippets from large databases, such as PharmaApp, ensuring the most relevant information is considered for the answer.
- **Contextual Understanding**: Generatively crafts a human-like response by fusing the knowledge from the retrieved snippets and the nuances of the posed question.
- **Scalability**: Instead of fine-tuning large models on every dataset, RAG can dynamically pull from databases, making it adaptable and versatile across different domains.

---

## **Features**

- **Powerful Question-Answering System**: Utilizes RAG for precise, context-rich answers.
- **Sinequa Integration**: Seamlessly searches the PharmaApp database for pertinent information.
- **FLAN-T5 Transformer Model**: Capitalizes on the transformer model for detailed response generation.
- **Streamlit Interface**: A sleek, user-friendly GUI for posing questions and viewing answers.
- **Completely Free**: No hidden costs or fees, making it a cost-effective solution for enterprises.
- **Local Execution**: Ensures data security as the application can be run locally, minimizing the risk associated with external data breaches.
- **Cost Savings**: Avoid expensive cloud-based solutions and reduce costs by leveraging this local, powerful Q&A system.

---

## **Installation**

1.  **Clone the repository:**

```
git clone https://github.com/shravanv90/SinequaRAGQnA.git
```

1.  Install required libraries:

```
pip install streamlit transformers requests
```

1.  Run the Streamlit application:

```
streamlit run app.py
```

## **Usage**

1.  Enter your question in the input field.
2.  Press "Enter".
3.  Enjoy a context-rich answer.
