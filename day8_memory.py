from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

chat_history = []

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 AI 어시스턴트입니다."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

chain = prompt | llm

def chat(user_input):
    response = chain.invoke({
        "history": chat_history,
        "input": user_input,
    })

    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response.content))

    return response.content

# 테스트
print("=== 메모리 테스트 ===\n")
print("종료: q\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'q':
        break

    response = chat(user_input)
    print(f"AI: {response}\n")