from langchain_community.document_loaders import WhatsAppChatLoader

def load_documents(file_path):
    loader = WhatsAppChatLoader(file_path)
    return loader.load()
