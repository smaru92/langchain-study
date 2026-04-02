from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

from day8_memory import chat_history

load_dotenv()

# 설정
MAX_HISTORY = 6 # 최근 6개 메시지만 유지(3턴)
MAX_TOKEN = 500

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    streaming=True,
    max_tokens=MAX_TOKEN,
)

chat_history = []

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 AI 어시스턴트입니다."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm

def chat(user_input):
    global chat_history


    print("AI: ", end="", flush=True)

    full_response = ""
    for chunk in chain.stream({"history": chat_history, "input": user_input}):
        print(chunk.content, end="", flush=True)
        full_response += chunk.content

    print("\n")

    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=full_response))

    chat_history = chat_history[-MAX_HISTORY:]

# 스트리밍 출력
print("=== 최적화 버전 ===\n")
print(f"설정: 최근 {MAX_HISTORY//2}턴, 최대 {MAX_TOKENS} 토큰\n")
print("종료: q\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'q':
        break
    chat(user_input)