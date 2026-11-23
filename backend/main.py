from fastapi import FastAPI
from routers.interview import router as interview_router

app = FastAPI(
  version='0.0.1',
  title="ai interview platform",
  description = "ai interview platform using fastapi"
)

app.include_router(interview_router)

