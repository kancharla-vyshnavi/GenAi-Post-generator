from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Create Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

# Ask question
response = llm.invoke("Two most important ingredients in samosa are")

# Print output
print(response.content)





