from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

from day8_memory import chat_history

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", streaming=True)

chat_history = []

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 AI 어시스턴트입니다."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

chain = prompt | llm

# 스트리밍 + 메모리
def chat(user_input):
    print("AI: ", end="", flush=True)

    full_response = ""
    for chunk in chain.stream({"history": chat_history, "input": user_input}):
        print(chunk.content, end="", flush=True)
        full_response += chunk.content

    print("\n")

    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=full_response))


# 테스트
print("=== 메모리 + 스트리밍 ===\n")
print("종료: q\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'q':
        break
    chat(user_input)