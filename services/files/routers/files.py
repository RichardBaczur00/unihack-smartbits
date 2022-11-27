import json

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import FileResponse

from models import files as file_models

router = APIRouter()


@router.get('/')
async def get_file(query: str):
    lookup_table = json.load(open('lookup.json', 'r'))

    if query not in lookup_table:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'detail': 'The file you are looking for was not found.'}
        )

    return FileResponse(lookup_table[query])
