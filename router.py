from typing import Annotated
from shemas import STaskAdd
from fastapi import Depends, APIRouter
from repository import TaskRepository
router = APIRouter(prefix='/tasks', tags=['Таски'])


@router.post('')
async def add_task(task: Annotated[STaskAdd, Depends()]):
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}


@router.get('')
async def get_home():
    tasks = await TaskRepository.find_all()
    return {'data': tasks}
