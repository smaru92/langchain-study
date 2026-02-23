from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo")

# 대화 기록 리스트
messages = [
    SystemMessage(content="너는 친절한 AI 비서야")
]

# 1. 첫번째 대화
messages.append(HumanMessage(content="내 이름은 광연이야"))
response1 = chat.invoke(messages)
print("AI:", response1.content)
messages.append(AIMessage(content=response1.content))

# 2. 두번째 대화
messages.append(HumanMessage(content="내 이름이 뭐라고 했지?"))
response2 = chat.invoke(messages)
print("AI:", response2.content)
messages.append(AIMessage(content=response2.content))

# 세 번째 대화
messages.append(HumanMessage(content="내 이름을 거꾸로 말해봐"))
response3 = chat.invoke(messages)
print("AI:", response3.content)

print()
print("대화기록")
print(messages)