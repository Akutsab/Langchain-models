from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
llm=OpenAI(model='gpt-4o-mini')
res=llm.invoke("What is the capital of India?")
print(res)