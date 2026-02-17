# routers/house.py

from fastapi import APIRouter
from pydantic import BaseModel
from src.services.house import runModel, runModel2
from src.dtos.house import GetPredictionOfHousePrice2BodyDto

house_router = router = APIRouter()

@router.get("/price/predict")
async def getPredictionOfHousePrice(crim : float, room : float):
    price = await runModel(crim, room)

    return price

@router.post("/price/predict")
async def getPredictionOfHousePrice2(body: GetPredictionOfHousePrice2BodyDto):
  price = await runModel2(body)
  
  return price