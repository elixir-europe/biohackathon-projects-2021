from fastapi import FastAPI, APIRouter, Request, Response
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel, Field
from SPARQLWrapper import SPARQLWrapper, TURTLE, XML, JSON

from api import ranked_search, get_metadata


api_router = APIRouter()
api_router.include_router(ranked_search.router, tags=["Ranked Search"])
api_router.include_router(get_metadata.router, tags=["Get metadata"])


app = FastAPI(
    title='Ranking datasets',
    description="""API to rank datasets for the [BioHackathon 2021](https://github.com/elixir-europe/biohackathon-projects-2021/tree/main/projects/26).

[Source code](https://github.com/vemonet/biohackathon2021)    
""",
    license_info = {
        "name": "MIT license",
        "url": "https://opensource.org/licenses/MIT"
    },
    contact = {
        "name": "Vincent Emonet",
        "email": "vincent.emonet@gmail.com",
        "url": "https://github.com/vemonet",
    },
)

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

