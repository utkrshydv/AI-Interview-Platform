from enum import Enum
from pydantic import BaseModel
from typing import Optional

class InterviewEnumStatus(str, Enum):
  IN_PROGRESS = "in_progress"
  COMPLETED = "completed"

class Answer(BaseModel):
  question: str
  answer: Optional[str]
  skip: bool = False


class InterviewSession(BaseModel):
  session_id: str
  questions: list[str] = []
  status: InterviewEnumStatus = InterviewEnumStatus.IN_PROGRESS
  answers: list[Answer] = []
  current_index: int = 0
