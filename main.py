
import time
import uvicorn
from fastapi import FastAPI
import pickle



app=FastAPI()
pickle_in=open("svc.pkl","rb")
svc1=pickle.load(pickle_in)
@app.post('/')
def Diagnose(Symptoms:str):
  user =Symptoms
  arr =list(map(int,user))
  diagnos=svc1.predict([arr])

  data_set = {'Page': 'Home','Message': f'{diagnos}','Time': time.time()}
  return data_set





if(__name__ == '__main__'):
    uvicorn.run(app , host='127.0.0.1',port=8800)
