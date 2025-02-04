
from fastapi import FastAPI, APIRouter
app = FastAPI()
router = APIRouter()

"""
add user 
"""
@router.post('/add')
def add():
    return {'msg':'new data added successfully'}
"""
fetch user
"""
@router.get('/fetch')
def fetch():
    return {'msg':'data fetched successfully'}

"""update user"""
@router.put('/update')
def update(): 
    return {'msg':'data updated successfully'}

"""
delete user
"""
@router.delete('/delete')
def delete():
    return  {'msg':'data deleted successfully'}