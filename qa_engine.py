from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

def get_llm_answer(question, docs_data):
   
    cont = "\n".join(doc['content'] for doc in docs_data)
    prpt = f"You are a financial analyst AI. Based on the following documents, answer the user's question concisely:\n\n{cont}\n\nQuestion: {question}\nAnswer:"
    llm = Ollama(model="llama3")
    ans = llm(prpt)
    return ans