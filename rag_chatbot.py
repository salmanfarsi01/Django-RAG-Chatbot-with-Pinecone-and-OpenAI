# chatbot_app/rag_chatbot.py
import os
from openai import OpenAI
from pinecone import Pinecone

# The variables are already loaded by settings.py, so you just need to access them.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# For Pinecone, you'll similarly use the API key from the environment.
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Your function
def get_chatbot_response(query):
    # ... your chatbot logic here
    # You will use the 'client' and 'pc' instances initialized above.
    # ...
    return response


