from typing import List
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from starlette.responses import RedirectResponse


class NewsItemSerializer(BaseModel):
    title: str
    subtitle: str
    body: str


mock_items: List[NewsItemSerializer] = [NewsItemSerializer(title='fdsdfs',
                                                           subtitle='fdsdfs',
                                                           body='fdsdfs', ), NewsItemSerializer(title='orajupe',
                                                                                                subtitle='orajupe',
                                                                                                body='orajupe', ), ]
app = FastAPI(title='Small api')

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


@app.get("/item", response_model=List[NewsItemSerializer])
async def get_items(limit: int = 100, skip: int = 0):
    return mock_items[skip:limit+skip]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
