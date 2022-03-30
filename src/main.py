from fastapi import FastAPI
import uvicorn
import api



if __name__ == "__main__":
    app = FastAPI()
    app.include_router(api.router)
    uvicorn.run(app, host="0.0.0.0", port=5000)




