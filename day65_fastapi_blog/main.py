import uvicorn
from fastapi import FastAPI

app = FastAPI()

posts: list[dict] =[
    {"id":1,
     "author": "Punit Sharma",
     "title": "Fast api is easy to learn",
     "content": "This framework is easy to learn and super fast",
     "date_posted": "April 01, 2025"
     },
    {"id":2,
     "author": "John Doe",
     "title": "Python is awesome",
     "content": "Python is a great language and web development is easy with it ",
     "date_posted": "April 01, 2025"
     },
]
@app.get("/")
def home():
    return {"message": "hello world!"}

@app.get("/api/posts")
def get_posts():
    return posts


# pip install "fastapi[standard]"
# for dev env with auto load and debug
# fastapi dev main.py
# for prod setup more optimised and fast
# fastapi run main.py