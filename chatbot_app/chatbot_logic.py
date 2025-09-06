# File: chatbot_app/chatbot_logic.py (The final, robust version)

import os
from openai import OpenAI
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

def get_rag_response(query: str) -> str:
    """
    Retrieves context from Pinecone and generates a response from OpenAI.
    """
    try:
        # --- Explicitly get keys at the start of the function ---
        openai_api_key = os.getenv("OPENAI_API_KEY")
        pinecone_api_key = os.getenv("PINECONE_API_KEY")

        # --- Add a clear check to see if the keys were loaded ---
        if not openai_api_key or not pinecone_api_key:
            # This will print a very clear error in your server terminal
            print("CRITICAL ERROR: OpenAI or Pinecone API key is missing from the environment.")
            # Return a more specific error to the user
            return "Error: The server is not configured with the necessary API keys. Please contact the administrator."

        index_name = "scholarships"
        
        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small",
            openai_api_key=openai_api_key  # Use the variable here
        )
        
        # PineconeVectorStore will automatically use the PINECONE_API_KEY from the environment
        vectorstore = PineconeVectorStore.from_existing_index(
            index_name=index_name,
            embedding=embeddings
        )

        # Retrieve relevant documents for the user's query
        search_results = vectorstore.similarity_search(query, k=3)
        context = "\n".join([doc.page_content for doc in search_results])

        # Initialize the OpenAI client to generate the final answer
        client = OpenAI(api_key=openai_api_key) # Use the variable here
        
        prompt = f"""
        You are a helpful AI Assistant. Use the following context to answer the question.
        Context: {context}
        Question: {query}
        Answer:
        """
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.5
        )
        return response.choices[0].message.content

    except Exception as e:
        # This will print the specific error to your server terminal for debugging
        print(f"An unexpected error occurred in the RAG pipeline: {e}") 
        return "I'm sorry, but I encountered an unexpected error while processing your request. Please try again."