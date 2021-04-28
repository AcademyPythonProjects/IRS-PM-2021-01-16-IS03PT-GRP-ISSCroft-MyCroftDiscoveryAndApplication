from fastapi import FastAPI
import uvicorn
import requests
from get_next_address import get_next_address


app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Please tell me vehicle number and current postal code'}

@app.post('/get_address')
def get_address(vehicle_num: str, current_postalCode: int):
    return get_next_address(vehicle_num, current_postalCode)



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)