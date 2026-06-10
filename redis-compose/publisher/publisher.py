from fastapi import FastAPI, HTTPException
import redis

app = FastAPI()

@app.post("/publish/")
def addMessage(message:str):
    r = redis.Redis(host='redis', port=6379, decode_responses=True)
    text = r.set("message", message)
    r.close()
    return text