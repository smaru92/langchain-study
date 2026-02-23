from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo")

# 1. 첫번째 대화
response1 = chat.invoke("내 이름은 광연이야")
print("AI:", response1.content)

# 2. 두번째 대화
response2 = chat.invoke("내 이름이 뭐라고 했지?")
print("AI:", response2.content)