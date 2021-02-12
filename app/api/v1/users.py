from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def read_user():
    ...


@router.post("/")
async def create_user():
    ...


@router.get("/me")
async def read_user_me():
    ...


@router.put("/me")
async def update_user_me():
    ...


@router.get("/{user_id}")
async def read_user_by_id(user_id: int):
    ...


@router.put("/{user_id}")
async def update_user(user_id: int):
    ...
