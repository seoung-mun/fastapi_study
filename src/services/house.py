# services/house.py

from typing import List
import xgboost as xgb
import pandas as pd

from src.dtos.house import GetPredictionOfHousePrice2BodyDto

loaded_model = xgb.XGBRegressor()

loaded_model.load_model('src/models/xgb_model.json')

async def runModel(crim : float, room : float) -> List[float]:
  
  dic = {
    "CRIM": [crim],
    "ZN": [18.0],
    "INDUS": [22.37],
    "CHAS": [0],
    "NOX": [0.145],
    "RM": [room],
    "AGE": [66.7],
    "DIS": [4.291],
    "RAD": [13],
    "TAX": [333.333],
    "PTRATIO": [21.0],
    "B": [197.6],
    "LSTAT": [23.4],
  }
    
  input = pd.DataFrame.from_dict(dic, orient='columns')
  
  z = loaded_model.predict(input)

  result: List[float] = z.tolist()
  
  return result

async def runModel2(input : GetPredictionOfHousePrice2BodyDto) -> List[float]:
  
  dic = {
    "CRIM": [input.crim],
    "ZN": [input.zn],
    "INDUS": [input.indus],
    "CHAS": [input.chas],
    "NOX": [input.nox],
    "RM": [input.room],
    "AGE": [input.age],
    "DIS": [input.dis],
    "RAD": [input.rad],
    "TAX": [input.tax],
    "PTRATIO": [input.ptratio],
    "B": [input.b],
    "LSTAT": [input.lstat],
  }
    
  input = pd.DataFrame.from_dict(dic, orient='columns')
  
  z = loaded_model.predict(input)

  result: List[float] = z.tolist()
  
  return result