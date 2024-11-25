from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI(
    title="My API",
    description="This is a simple API for demonstration purposes.",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "url": "https://yourwebsite.com",
        "email": "your_email@example.com",
    },
)

# Define routes
@app.get("/", summary="Root Endpoint", description="This is the root endpoint of the API.")
async def root():
    return {"message": "Welcome to my API!"}

@app.get("/users", summary="Get All Users", description="Retrieve a list of all users.")
async def get_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
