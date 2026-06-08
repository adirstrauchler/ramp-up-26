from fastapi import FastAPI, HTTPException
import redis

app = FastAPI()

@app.get("/")
def getMessage():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    text = r.get("message")
    r.close()
    return text