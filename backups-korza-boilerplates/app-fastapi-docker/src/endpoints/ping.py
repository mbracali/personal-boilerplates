from fastapi import APIRouter

router = APIRouter()


@router.get("/ping", status_code=200)
def ping():
    """ Health check endpoint. Returns pong. """
    return {"message": "pong"}
