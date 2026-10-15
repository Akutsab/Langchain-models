from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding=GoogleGenerativeAIEmbeddings(model="mgemini-embedding-2", dimensions=32)
res=embedding.embed_query("Delhi is the capital of India")
print(str(res))