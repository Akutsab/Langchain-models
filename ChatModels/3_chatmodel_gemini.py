from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="models/gemini-3-flash-preview")
res=model.invoke("what is the capital of france?")
print(res.content[0]['text'])