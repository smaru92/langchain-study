from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

# 1. 검색도구
search = DuckDuckGoSearchRun()

# 2. LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 3. Agent 생성
tools = [search]
agent = create_react_agent(llm, tools)

# 4. 대화형 검색
print("=== 검색 Agent ===")
print("질문을 입력하세요. (종료: q)\n")

while True:
    question = input("질문: ")
    if question.lower() == 'q':
        print("종료합니다.")
        break

    result = agent.invoke({"messages": [("human", question)]})
    answer = result["messages"][-1].content
    print(f"답변: {answer}\n")