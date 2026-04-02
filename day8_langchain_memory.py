from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

memory = MemorySaver()

agent = create_react_agent(
    model=llm,
    tools=[],
    checkpoint=memory,
)

# 대화 설정 (thread_id로 구분)
config = {"configurable": {
    "thread_id": "user-1"
}}

# 대화 함수
def chat(user_input):
    result = agent.invoke(
        {"message": [("human", user_input)]},
        config=config,
    )
    return result["message"][-1].content

# 테스트
print("=== LangGraph 메모리 테스트 ===\n")
print("종료: q\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'q':
        break

    response = chat(user_input)
    print(f"AI: {response}")