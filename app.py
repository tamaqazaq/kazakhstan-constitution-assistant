import streamlit as st
import subprocess
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb
import json

client = chromadb.Client()
collection_name = "constitution_kz"

if collection_name in [c.name for c in client.list_collections()]:
    collection = client.get_collection(collection_name)
else:
    collection = client.create_collection(collection_name)

def load_and_index(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    client.delete_collection(name=collection_name)
    global collection
    collection = client.create_collection(name=collection_name)

    collection.add(documents=chunks, ids=ids)

def search_docs(query, k=3):
    results = collection.query(query_texts=[query], n_results=k)
    return results['documents'][0]

def ask_ollama(prompt):
    process = subprocess.Popen(
        ["ollama", "run", "llama2"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=prompt + "\n")
    if process.returncode != 0:
        return f"Error: {stderr}"
    lines = stdout.splitlines()
    answer_lines = [line for line in lines if not line.strip().startswith(">>>")]
    return "\n".join(answer_lines).strip()

st.title("AI Assistant: Constitution of Kazakhstan")

json_path = r"C:\Users\Asus\Documents\ai-assistant\konstitutsiya_kz.json"

try:
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    st.write("JSON file successfully loaded from path:", json_path)

    # Extract text from sections and articles
    texts = []
    for section_key, section_value in data.items():
        if isinstance(section_value, dict) and "статьи" in section_value:
            articles = section_value["статьи"]
            for article_num, article_text in articles.items():
                texts.append(article_text)
        else:
            if isinstance(section_value, str):
                texts.append(section_value)

    text = "\n\n".join(texts)

    if text:
        load_and_index(text)
        st.success("Text from JSON has been indexed.")
    else:
        st.error("Failed to extract text from JSON.")
except Exception as e:
    st.error(f"Error reading JSON: {e}")

# Ask the user for a question
question = st.text_input("Ask a question:")

if question:
    try:
        docs = search_docs(question)
        context = "\n\n".join(docs)

        # Create the prompt in English for Ollama
        prompt = f"""You are an AI assistant working with only the text of the Constitution of Kazakhstan.
Your task is to answer questions based solely on the text of the Constitution.

Constitution text:
{context}

Question: {question}

Answer:
"""
        answer = ask_ollama(prompt)
        st.markdown("### Answer:")
        st.write(answer)
    except Exception as e:
        st.error(f"Error processing the question: {e}")
