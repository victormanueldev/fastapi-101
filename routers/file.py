import shutil
from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    prefix='/files',
    tags=['file']
)


@router.post('/')
def get_file(file: bytes = File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return {'lines': lines}


@router.post('/uploadfile')
def get_upload_file(upload_file: UploadFile = File(...)):
    """
    UploadFile class provide more functionality and file properties
    :param upload_file:
    :return:
    """
    path = f'files/{upload_file.filename}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return {
        'filename': path,
        'type': upload_file.content_type
    }
