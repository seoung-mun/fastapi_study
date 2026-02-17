# routers/user.py

from fastapi import APIRouter
from pydantic import BaseModel

class CreatePostBodyDto(BaseModel):
    name : str
    age : int
    height : int
    weight : int



user_router = router = APIRouter()

@router.get("/")
async def getUser(nickname : str, age : int):
    return {"nickname" : nickname, "age" : age}
 

@router.post("/")
async def createUserByUsername(body : CreatePostBodyDto, username : str, age : int):
    height = body.height
    weight = body.weight

    processed_heigth = f"{height}cm"
    processed_weigth = f"{weight}kg"

    return {"username" : username, "age" : age, "height" : processed_heigth, "weight" : processed_weigth}

