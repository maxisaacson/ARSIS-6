from fastapi import APIRouter
from pydantic import BaseModel

from .on_server_procedures.mock_procedure import MockProcedure

router = APIRouter(prefix="/procedures", tags=["procedures"])

mock_procedure = MockProcedure()

in_mem_procedures = {mock_procedure.get_name(): mock_procedure.get_task_list_encoded()}

class Procedure(BaseModel):
    data: str

@router.get("/")
async def procedures():
    return in_mem_procedures


@router.get("/{name}")
def procedure(name: str):
    res = in_mem_procedures.get(name, None)
    if res is not None:
        return {
            "name": name,
            "taskList": res,
        }
    return {"name": "Not found", "taskList": []}

@router.post("/")
def procedure(procedure: Procedure):
    print(procedure)
    return procedure
