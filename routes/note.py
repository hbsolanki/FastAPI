from fastapi import APIRouter,FastAPI,Request
from fastapi.responses import RedirectResponse
from models.note import Note
from config.db import conn
from schemas.note import noteEntity,notesEntity

note=APIRouter()

@note.get("/")
async def read_item(request:Request):
    docs=conn.notes.notes.find({}) 

    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc":doc["desc"],
            "important":doc["important "]
        })

    return newDocs

@note.post("/" ,response_class=RedirectResponse)
async def create_item(request : Request):
    form=await request.form()
    formDic=dict(form)
    formDic["important"]=True if formDic.get("important") == "on" else False # type: ignore
    note=conn.notes.notes.insert_one(formDic)
    # return {"Success":True}
    return RedirectResponse("http://localhost:5173" ,status_code=307, headers=None, background=None)