from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

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
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request,
                                      "index.html",
                                      {"posts":posts, "title": "Home"})

@app.get("/api/posts")
def get_posts():
    return posts


# pip install "fastapi[standard]"
# for dev env with auto load and debug
# fastapi dev main.py
# for prod setup more optimised and fast
# fastapi run main.py