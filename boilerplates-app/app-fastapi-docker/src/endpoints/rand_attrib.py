from fastapi import APIRouter

router = APIRouter()


@router.get("/rand_attrib", status_code=200)
def rand_attrib():
    """ Returns a random attribute. To be implemented. """
    return {"message": "Coming soon!"}
