from flask import Blueprint, request, jsonify
from app.services.document_service import load_documents
from app.services.query_service import get_qa_service

api_bp = Blueprint('api', __name__)

@api_bp.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')
    docs = load_documents('E:\GenFlow-AI-Powered-Document-Intelligence\GenFlow-AI-Powered-Document-Intelligence\data\chat\chatArman.txt')  # Or wherever your file is located
    qa_service = get_qa_service(docs)
    response = qa_service(question)
    return jsonify(response)
