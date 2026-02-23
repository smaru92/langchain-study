from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo")

# 1. 블로그 글 생성 Chain
blog_prompt = ChatPromptTemplate.from_template(
    """
        다음 주제로 블로그 글을 작성해줘.
        
        주제: {topic}
        타겟 독자: {audience}
        글자 수: {length}자 내외
        톤: {tone}
    """
)

blog_chain = blog_prompt | chat | StrOutputParser()

result = blog_chain.invoke({
    "topic": "Python 백엔드 개발자가 되는 방법",
    "audience": "프로그래밍 입문자",
    "length": "300",
    "tone": "친근하고 격려하는"
})

print("=== 블로그 글 ===")
print(result)
print()

# 2. 면접 질문 생성 Chain
interview_prompt = ChatPromptTemplate.from_template(
    """
        다음 기술에 대한 면접 질문 {count}개를 만들어줘.
        난이도: {level}
        기술: {tech}
        
        형식:
        1. 질문
        2. 질문
        ...
    """
)

interview_chain = interview_prompt | chat | StrOutputParser()

result = interview_chain.invoke({
    "tech": "FastAPI",
    "count": "5",
    "level": "중급",
})

print("=== 면접 질문 ===")
print(result)