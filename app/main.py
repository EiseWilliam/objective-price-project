from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from typing import Annotated
import uvicorn
from db.database import db


from routers import auth, user, core, history, dashboard

app = FastAPI()

origins = [
   config('CLIENT_ORIGIN'),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)


app.include_router(auth.router, tags=['Auth'], prefix='/auth')
app.include_router(core.router, tags=['Core'], prefix='/api')
app.include_router(user.router, tags=['User'], prefix='/user')
app.include_router(dashboard.router, tags=['SuperUser'], prefix='/admin')
app.include_router(history.router, tags=['History'], prefix='/user/history')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to Pricely API"}

@app.get("/api/test-mongodb-connection")
async def test_mongodb_connection():
    try:
        # Attempt to perform a simple database operation, like listing collections
        collection_names = await db.list_collection_names()
        
        # If the operation succeeds, return a success message
        return {"message": "MongoDB connection successful!",
                "collection_names": collection_names}
    except Exception as e:
        # If an error occurs, return an error message
        raise HTTPException(status_code=500, detail=f"MongoDB connection failed: {str(e)}")
    


@app.post("/create-collection/{collection_name}")
async def create_collection(collection_name: Annotated[str | None, "collection_name"] = "nill_collection"):
    try:
        # Use the MongoDB create_collection method to create a new collection
        await db.create_collection(collection_name)
        
        # If the operation succeeds, return a success message
        return {"message": f"Collection '{collection_name}' created successfully!"}
    except Exception as e:
        # If an error occurs, return an error message
        raise HTTPException(status_code=500, detail=f"Failed to create collection: {str(e)}")
    
    

# start uvicorn server
if __name__ == "__main__":
    uvicorn.run(app = "main:app", port=8000, reload=True)



