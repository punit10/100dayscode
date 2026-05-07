from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
import random
import string

app = FastAPI()
URL_LIST = []
@app.get("/")
def create_url(request: Request):
    params_dict = dict(request.query_params)
    long_url = params_dict.get("long_url")
    if long_url.split(":")[0] not in ["http", "https"]:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Invalid URL format"},
        )
    random_key = ''.join(random.choices(string.ascii_lowercase, k=5))
    short_url = f"http://127.0.0.1:8000/{random_key}"
    URL_LIST.append({"long_url": long_url, "short_url": short_url, "key": random_key, "visits":0})
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"short_url": short_url, "long_url": long_url, "urls": URL_LIST}
    )


@app.get("/url/{short_url}")
def get_url(short_url: str, request: Request):
    print(short_url)
    for url in URL_LIST:
        if url.get("short_url") == short_url:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"long_url": url.get("long_url"), "list": URL_LIST}
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"long_url": "Not Found THIS"}
            )
