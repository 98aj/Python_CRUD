from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # Creting an Instance of FastAPI

class Todo(BaseModel):
    id:int
    title:str

todoList = []

@app.get('/todo')
async def root():
    return {"message": todoList}

@app.get('/todo/{todoId}')
async def get_todo_by_id(todoId:int):
    for t in todoList:
        if t.id == todoId:
            return {"message": t}
        else:
            return {"message" : 'Invalid todo id.'}

@app.post('/todo')
async def create_new_todo(todo:Todo):
    todoList.append(todo)
    return {'message': 'Todo added successfully'}

@app.delete('/deleteTodo/{todoId}')
async def delete_tood(todoId:int):
    for t in todoList:
        if t.id == todoId:
            todoList.remove(t)
            return {'message': 'Todo deleted successfully'}
        else:
            return {'message' : 'Todo id invalid.'}
