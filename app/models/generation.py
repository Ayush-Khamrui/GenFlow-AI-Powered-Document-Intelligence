from langchain_community.llms import Ollama

def get_llm():
    return Ollama(model="gemma:2b")
