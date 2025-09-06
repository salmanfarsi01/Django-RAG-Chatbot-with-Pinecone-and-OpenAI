# Django RAG Chatbot with Pinecone & OpenAI

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0+-green?style=for-the-badge&logo=django&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-blueviolet?style=for-the-badge&logo=openai&logoColor=white)
![Pinecone](https://img.shields.io/badge/Pinecone-Vector_DB-orange?style=for-the-badge&logo=pinecone&logoColor=white)

A full-stack AI chatbot application that uses a Retrieval-Augmented Generation (RAG) pipeline to answer questions from a custom knowledge base of PDF and DOCX files. This project provides an interactive web interface for users to chat with an AI that has specialized knowledge from documents you provide.
<img width="635" height="791" alt="image" src="https://github.com/user-attachments/assets/af164e29-4906-4ca6-bad0-a878e4e0af90" />

## About The Project

This project addresses a common limitation of standard LLMs: their lack of access to private, specific, or up-to-the-minute information. By implementing a RAG pipeline, this application allows you to create a "knowledge base" from your own documents. The chatbot then uses this knowledge base as its primary source of truth, enabling it to provide accurate, context-aware answers and significantly reduce the risk of AI "hallucination."

The entire application is built with a robust Django backend and a simple, interactive vanilla JavaScript frontend.

## Key Features

-   **Custom Knowledge Base**: Ingests your own PDF and DOCX documents to create a specialized knowledge base.
-   **Interactive Web UI**: A clean and simple chat interface for real-time interaction.
-   **RAG Pipeline**: Leverages LangChain to orchestrate the retrieval of relevant context from a vector database before generating a response.
-   **Accurate & Contextual Answers**: The AI is instructed to answer questions based on the provided documents, ensuring responses are relevant and factual.
-   **Scalable Vector Storage**: Uses Pinecone as a highly efficient and scalable vector database for storing document embeddings.
-   **Secure API Key Management**: Utilizes `.env` files to securely manage sensitive API keys.

## Tech Stack

-   **Backend**: Django, Django REST Framework
-   **AI / ML**:
    -   **LLM**: OpenAI GPT-3.5-Turbo
    -   **Orchestration**: LangChain
    -   **Vector Database**: Pinecone
    -   **Embeddings**: OpenAI `text-embedding-3-small`
-   **Frontend**: HTML, CSS, Vanilla JavaScript (with AJAX/Fetch API)
-   **Database**: SQLite (for Django's core needs)
-   **Tooling**: `python-dotenv` for environment management

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.9+
-   Git
-   A Pinecone account and API key
-   An OpenAI account and API key

### Installation and Setup

1.  **Clone the Repository**
    ```sh
    git clone https://github.com/your-username/Django-RAG-Chatbot-with-Pinecone-and-OpenAI.git
    cd Django-RAG-Chatbot-with-Pinecone-and-OpenAI
    ```

2.  **Create and Activate a Virtual Environment**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    *(First, ensure you have a `requirements.txt` file by running `pip freeze > requirements.txt` in your project's terminal)*
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables**
    -   Create a file named `.env` in the project's root directory.
    -   Copy the contents of `.env.example` into `.env`.
    -   Fill in your actual secret keys and API keys.

    ```env
    # .env file
    SECRET_KEY='your-django-secret-key-goes-here'
    OPENAI_API_KEY='your-openai-api-key'
    PINECONE_API_KEY='your-pinecone-api-key'
    ```

5.  **Run Django Migrations**
    ```sh
    python manage.py migrate
    ```

6.  **Ingest Your Documents**
    -   Place your PDF and/or DOCX files into the `source_documents/` folder.
    -   Run the custom Django management command to process and embed them into Pinecone.
    ```sh
    python manage.py process_documents
    ```
    *(You only need to run this command when you add, remove, or change files in the `source_documents` folder.)*

7.  **Run the Development Server**
    ```sh
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/chat/`.

## Future Improvements

-   [ ] Implement user authentication to support multiple users.
-   [ ] Store chat history in the database for each user.
-   [ ] Switch to a more robust frontend framework like React or Vue.js.
-   [ ] Implement response streaming for a more interactive "typing" effect.
-   [ ] Add support for more document types (e.g., .txt, .csv).

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Before you commit and push:**

1.  Create a file named `.env.example` and copy the *structure* (not the values) of your `.env` file into it. This shows other users what variables they need.
2.  Make sure your `.gitignore` file includes `.env`, `db.sqlite3`, and the `venv/` directory.
3.  Run `pip freeze > requirements.txt` in your terminal to create the list of dependencies for others to install.

You are now ready to showcase your project professionally on GitHub!
