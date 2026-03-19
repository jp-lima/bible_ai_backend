from fastapi import APIRouter
from repositories.plans_repo import *

router = APIRouter(
 prefix="/plans", 
 tags=["plans"]
        )

@router.get("")
def get_plans():

    all_plans = get_all_plans()

    return all_plans 
    



