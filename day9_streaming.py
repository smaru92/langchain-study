from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", streaming=True)

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 AI 어시스턴트입니다."),
    ("human", "{input}")
])

chain = prompt | llm

# 스트리밍 출력
print("=== 스트리밍 테스트 ===\n")
print("종료: q\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'q':
        break

    print("AI: ", end="", flush=True)

    # 스트리밍 출력
    for chunk in chain.stream({"input": user_input}):
        # print(f"받은 데이터: {chunk.content}")
        print(chunk.content, end="", flush=True)

    print("\n")