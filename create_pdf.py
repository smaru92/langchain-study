from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 한글 폰트 등록 (Windows)
pdfmetrics.registerFont(TTFont('Malgun', 'C:/Windows/Fonts/malgun.ttf'))

# PDF 생성
c = canvas.Canvas("company_info.pdf", pagesize=letter)

# 한글 폰트 설정
c.setFont('Malgun', 12)

# 내용 작성
content = [
    "회사 소개서",
    "",
    "1. 회사 개요",
    "회사명: 테크스타트",
    "설립일: 2020년 3월 15일",
    "대표이사: 김철수",
    "직원수: 50명",
    "위치: 서울시 강남구 테헤란로 123",
    "",
    "2. 주요 서비스",
    "- AI 챗봇 솔루션 개발",
    "- 자연어 처리 API 제공",
    "- 기업용 문서 검색 시스템",
    "",
    "3. 기술 스택",
    "- 백엔드: Python, FastAPI",
    "- AI: LangChain, OpenAI",
    "- 데이터베이스: PostgreSQL, Redis",
    "- 클라우드: AWS",
    "",
    "4. 채용 정보",
    "현재 백엔드 개발자를 채용 중입니다.",
    "- 경력: 3년 이상",
    "- 필수: Python, FastAPI",
    "- 우대: LangChain, AI 경험",
    "- 연봉: 5000만원 ~ 7000만원",
    "",
    "5. 복리후생",
    "- 점심 식대 지원",
    "- 간식 무제한",
    "- 자기개발비 연 100만원",
    "- 재택근무 주 2회",
    "- 유연 출퇴근제",
]

y = 750
for line in content:
    c.drawString(50, y, line)
    y -= 20

c.save()
print("company_info.pdf 생성 완료!")