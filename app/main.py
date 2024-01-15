from fastapi import FastApi

app = FastApi()

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

