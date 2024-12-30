from fastapi import FastAPI
import socket
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"hostname": hostname, "current_time": current_time}
