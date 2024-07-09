from langchain.text_splitter import CharacterTextSplitter

def text_splitter(docs):
    text_splitter = CharacterTextSplitter(separator='\n', chunk_size=1000, chunk_overlap=10)
    return text_splitter.split_documents(docs)