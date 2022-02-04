from fastapi import FastAPI

# create a FastAPI "instance"
app = FastAPI()


# tell FastAPI that the function right below is in charge of handling Get request that go to '/'
@app.get('/')
async def root() -> str:
    return 'Hello. How are you doin? ^_^!'
  
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000)