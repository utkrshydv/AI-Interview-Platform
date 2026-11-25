from fastapi import APIRouter,HTTPException, status
from services.interview_services import create_session, get_session, save_answer
from request_model.AnswerRequest import AnswerRequest
from models.interview import InterviewEnumStatus
from response_model.AnswerResponse import AnswerResponse


router = APIRouter(
  prefix="/interview",
  tags=["interview"]
)

@router.get("/")
async def hello():
  return "AI Interview Platform"

@router.get("/start")
async def start_interview():
  questions = [
    "add 1 and 2",
    "what is javascript?",
    "what is inheritance?"
  ]

  session = create_session()

  session.questions = questions

  return {
    "introText": "welcome to the interview",
    "session_id": session.session_id,
    "firstQuestion": session.questions[0]
  }

@router.post("/submit", response_model=AnswerResponse)
async def submit_answer(answerReq: AnswerRequest):
  session = get_session(answerReq.session_id)
  if not session or session.status == InterviewEnumStatus.COMPLETED:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="interview session not found")


  save_answer(answerReq.answer, answerReq.skip, session)

  if session.status == InterviewEnumStatus.COMPLETED:
    return{
      "interviewEnded": True
    }

  return {
    "interviewEnded": False,
    "nextQuestion": session.questions[session.current_index] 
  }

@router.put("/end/{session_id}")
async def end_interview(session_id:str):
   session = get_session(session_id)
   if not session or session.status == InterviewEnumStatus.COMPLETED:
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="interview session not found")

   session.status = InterviewEnumStatus.COMPLETED

   return{
     "interviewEnded": True
   }


@router.get("/report/{session_id}")
async def report(session_id: str):
   session = get_session(session_id)
   if not session or session.status == InterviewEnumStatus.COMPLETED:
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="interview session not found")

   return{
     "result": "Your interview result"
   }