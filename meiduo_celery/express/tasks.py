from meiduo_express import MeiduoExp
from ..main import app

@app.task
def meiduo_place_order(data):
    return MeiduoExp.place_order(data)