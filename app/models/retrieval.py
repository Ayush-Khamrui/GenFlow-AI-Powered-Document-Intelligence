from app.config import Config
from langchain.vectorstores import Chroma
from app.models.embedding import get_embeddings

def get_vector_db(docs):
    embeddings = get_embeddings()
    vectordb = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory=Config.DB_DIR)
    vectordb.persist()
    return vectordb

def get_retriever(vectordb):
    return vectordb.as_retriever(search_kwargs={"k": 3})
