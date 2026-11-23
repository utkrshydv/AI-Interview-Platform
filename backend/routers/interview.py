from fastapi import APIRouter

router = APIRouter(
  prefix="/interview",
  tags=["interview"]
)

@router.get("/")
async def hello():
  return "AI Interview Platform"