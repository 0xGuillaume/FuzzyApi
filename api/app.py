from fastapi import FastAPI, HTTPException
from models import FooModel
from database import(
    fetch_foos,
    fetch_foo,
)


app = FastAPI()


@app.get("/foos")#, response_model=List[FooModel])
async def list_foos():
    """Get List of all foos"""

    response = await fetch_foos()

    return response


@app.get("/foo/{title}", response_model=FooModel)
async def get_foo_by_id(title):
    """Get a specific foo"""

    response = await fetch_foo(title)

    if response:
        return response
    raise HTTPException(404, f"[!] Title : {title} does not exist.")



