import os
from django.core.management.base import BaseCommand
from django.conf import settings
from dotenv import load_dotenv

# Langchain imports
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

class Command(BaseCommand):
    help = 'Loads, chunks, embeds, and adds documents to the Pinecone index.'

    def handle(self, *args, **options):
        # --- Loading .env File ---
        self.stdout.write("Attempting to load .env file...")
        env_path = os.path.join(settings.BASE_DIR, '.env')
        
        if os.path.exists(env_path):
            self.stdout.write(self.style.SUCCESS(".env file found."))
            load_dotenv(dotenv_path=env_path)
        else:
            self.stdout.write(self.style.ERROR(".env file NOT found at expected path."))
            return

        # --- DEBUG SECTION ---
        self.stdout.write("--- Checking Environment Variables ---")
        openai_api_key = os.getenv("OPENAI_API_KEY")
        pinecone_api_key = os.getenv("PINECONE_API_KEY")

        if openai_api_key:
            self.stdout.write(self.style.SUCCESS("   [✓] OPENAI_API_KEY is loaded."))
        else:
            self.stdout.write(self.style.ERROR("   [✗] OPENAI_API_KEY is NOT loaded."))

        if pinecone_api_key:
            self.stdout.write(self.style.SUCCESS("   [✓] PINECONE_API_KEY is loaded."))
        else:
            self.stdout.write(self.style.ERROR("   [✗] PINECONE_API_KEY is NOT loaded."))
        self.stdout.write("------------------------------------")
        
        if not openai_api_key or not pinecone_api_key:
            self.stdout.write(self.style.ERROR("Processing stopped because one or more API keys are missing."))
            return
        # --- END DEBUG SECTION ---

        self.stdout.write("\nStarting document processing...")
        folder_path = os.path.join(settings.BASE_DIR, 'source_documents')
        
        # ... (rest of the code is the same)
        documents = []
        for filename in os.listdir(folder_path):
            path = os.path.join(folder_path, filename)
            try:
                if filename.endswith(".pdf"):
                    loader = PyPDFLoader(path)
                    documents.extend(loader.load())
                elif filename.endswith(".docx"):
                    loader = Docx2txtLoader(path)
                    documents.extend(loader.load())
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to load {filename}: {e}"))
                continue
        
        self.stdout.write(f"Loaded {len(documents)} document pages.")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(documents)
        self.stdout.write(f"Split documents into {len(splits)} chunks.")

        index_name = "scholarships"
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=openai_api_key)
        
        self.stdout.write(f"Adding {len(splits)} document chunks to the Pinecone index '{index_name}'...")
        try:
            PineconeVectorStore.from_documents(
                documents=splits,
                embedding=embeddings,
                index_name=index_name
            )
            self.stdout.write(self.style.SUCCESS("Document chunks successfully added to the index."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while adding documents to Pinecone: {e}"))