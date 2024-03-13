import openai
from crud import create_problem, create_answer
# from models import Problem, Answer
from schemas import Problem, Answer
from database import SessionLocal

openai.api_key = ''

completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': 'assistant는 수학 선생님이다.'},
        {'role': 'user', 'content': '내가 말하는 것을 수학문제로 만들고 python dict 형식으로 문제는 title키에 저장하고 질문은 question에, 정답은 answer 키에 저장하고 해설은 explain 키에 저장해줘.'},
        {'role': 'assistant', 'content': '물론이죠! 어떤 문제를 만들어드릴까요? 원하는 난이도나 주제를 알려주세요.'},
        {'role': 'user', 'content': '중학교 1학년 과정의 중간 난이도로 거듭제곱에 대한 문제를 만들어줘.'},
    ]
)

res = completion['choices'][0]['message']['content']


problem = Problem(title='거듭제곱', content=res, explanation='거듭제곱에 대한 문제입니다.', category_id=1, category_detail_id=1)
create_problem(db=SessionLocal(), problem=problem)