from langchain.chains import RetrievalQA
from langchain import PromptTemplate
from app.models.retrieval import get_vector_db, get_retriever
from app.models.generation import get_llm
from app.models.splitter import text_splitter

prompt_template = """Imagine you are Person 1 in the conversation. Respond to Person 2 statement in a way that mirrors Person 1 style, emotions, and expressions.
Construct an answer if you don't have any context from the vector Database.

{context}

QUESTION:```{question}```
ANSWER:
"""

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

def get_qa_service(docs):
    # splitter = text_splitter(docs)
    vectordb = get_vector_db(docs)
    retriever = get_retriever(vectordb)
    llm = get_llm()
    return RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", chain_type_kwargs={"prompt": PROMPT}, retriever=retriever)
