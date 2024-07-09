# GenFlow-AI-Powered-Document-Intelligence

Currently This project leverages Generative AI to replicate a person's words and feelings based on their WhatsApp data. By uploading the WhatsApp chat data, the chatbot can respond to queries as if it were the person themselves. This project utilizes a Language Learning Model (LLM) and Flask to generate API requests.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload WhatsApp chat data
- Generate responses mimicking the person in the chat data
- Use Flask to handle API requests
- Modular code structure for easy maintenance and extension

## Project Structure

The project is organized as follows:

```
app/
├── models/
│   ├── __init__.py
│   ├── embedding.py
│   ├── generation.py
│   ├── retrieval.py
│   ├── splitter.py
├── routes/
│   ├── __init__.py
│   ├── api_routes.py
├── services/
│   ├── __init__.py
│   ├── document_service.py
│   ├── query_service.py
├── __init__.py
├── config.py
├── main.py
data/
├── .env
.gitignore
LICENSE
README.md
requirements.txt
```

### Description of Key Files

- **models/**: Contains the core functionality for embedding, generation, retrieval, and splitting of chat data.
  - `embedding.py`: Handles the embedding of chat data.
  - `generation.py`: Generates responses based on embeddings.
  - `retrieval.py`: Retrieves relevant data based on queries.
  - `splitter.py`: Splits the chat data into manageable chunks.
- **routes/**: Manages the API endpoints.
  - `api_routes.py`: Defines the routes for API requests.
- **services/**: Contains service-related code.
  - `document_service.py`: Manages document uploads and processing.
  - `query_service.py`: Handles query processing and response generation.
- **`config.py`**: Contains configuration settings.
- **`main.py`**: The main entry point for the application.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the `data/` directory and add the necessary environment variables.

## Usage

1. **Run the application:**

   ```bash
   python app/services/main.py
   ```

2. **Upload WhatsApp chat data:**
   Use the provided API endpoint to upload the chat data.

3. **Interact with the chatbot:**
   Send queries to the chatbot and receive responses that mimic the person's words and feelings based on the chat data.

## API Endpoints

### Query the Chatbot

- **Endpoint:** `/api/ask`
- **Method:** `POST`
- **Description:** Send a query to the chatbot and receive a response.

### Example Request

**Upload Chat Data:**

```bash
curl -X POST -F "file=@path_to_your_file" http://localhost:5000/api/upload
```

**Query the Chatbot:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"query": "Your query here"}' http://localhost:5000/api/query
```

## Future Scope

1. Addition of Advanced RAG features
2. LLM-RAG Scoring Techniques
3. More methods to retrieve information from internet and using it in Software Engineering Lifecycle.

## Contributing

Contributions are welcome!.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
