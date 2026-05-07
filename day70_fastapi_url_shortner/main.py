from fastapi import FastAPI, HTTPException, status, Path, Query
from pydantic import BaseModel, HttpUrl, field_validator
import random
import string

app = FastAPI()

# In-memory store: short_code -> long_url
url_store = {}
BASE_URL = "http://company.com"


# Request Model
class URLRequest(BaseModel):
    long_url: HttpUrl

    @field_validator("long_url")
    def validate_url(cls, v):
        # Example: only allow http/https explicitly
        if not (str(v).startswith("http://") or str(v).startswith("https://")):
            raise ValueError("URL must start with http:// or https://")
        return v
random_string_len = 5


def generate_short_code(length: int = 5) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def create_short_logic(long_url: str):
    short_code = generate_short_code()

    while short_code in url_store:
        short_code = generate_short_code()

    url_store[short_code] = {
        "url": long_url,
        "visits": 0
    }
    return {"short_url": f"{BASE_URL}/{short_code}"}


@app.get("/")
def home():
    return {
        "message": "Welcome to URL Shortener API. Use POST /short?long_url= to create short URLs."
    }

@app.get("/short")
def create_short_url_get(long_url: str = Query(...)):
    # validation
    if not (long_url.startswith("http://") or long_url.startswith("https://")):
        raise HTTPException(
            status_code=400,
            detail="URL must start with http:// or https://"
        )

    return create_short_logic(long_url)


# ✅ OPTION 1: Request body
@app.post("/", status_code=status.HTTP_201_CREATED)
def create_short_url_body(request: URLRequest):
    return create_short_logic(str(request.long_url))


# ✅ OPTION 2: Path parameter
@app.post("/{long_url:path}", status_code=status.HTTP_201_CREATED)
def create_short_url_path(
    long_url: str = Path(..., description="Long URL")
):
    # ✅ Basic validation
    if not (long_url.startswith("http://") or long_url.startswith("https://")):
        raise HTTPException(
            status_code=400,
            detail="URL must start with http:// or https://"
        )

    return create_short_logic(long_url)

@app.post("/", status_code=status.HTTP_201_CREATED)
def create_short_url(request: URLRequest):
    # Generate unique short code
    short_code = generate_short_code(random_string_len)

    # Ensure uniqueness (avoid collision)
    while short_code in url_store:
        short_code = generate_short_code(random_string_len)

    # Store mapping
    url_store[short_code] = {
        "url": str(request.long_url),
        "visits": 0
    }
    short_url = f"{BASE_URL}/{short_code}"

    return {
        "short_url": short_url
    }


# Optional: GET endpoint to test redirect behavior
@app.get("/url/{short_code}")
def redirect_to_long_url(short_code: str):
    if short_code not in url_store:
        raise HTTPException(status_code=404, detail="URL not found")

    url_store[short_code]["visits"] += 1

    return {
        "long_url": url_store[short_code]["url"]
    }


@app.get("/info/{short_code}")
def get_url_info(short_code: str):
    if short_code not in url_store:
        raise HTTPException(status_code=404, detail="URL not found")

    return {
        "visits": url_store[short_code]["visits"]
    }
