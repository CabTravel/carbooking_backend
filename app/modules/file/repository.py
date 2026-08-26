from fastapi import UploadFile,HTTPException,status
from pathlib import Path
from uuid import uuid4

from fastapi.responses import FileResponse

from app.modules.file.schema import FileUploadParam,FileLoadParam

class FileRepository:
    def __init__(self):
        self.upload_dir = Path("uploads")
            # Create folder if it doesn't exist
        self.upload_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    async def upload_file(self,param:FileUploadParam)-> str:
        if not param.file.filename:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="File name is missing"
            )
            # Get extension
        extension = Path(param.file.filename).suffix

            # Generate unique filename
        filename = f"{uuid4()}{extension}"

        file_path = self.upload_dir / filename

            # Save file
        with file_path.open("wb") as buffer:
            while chunk := await param.file.read(1024 * 1024):
                buffer.write(chunk)

        return str(file_path)

    async def load_file(self,param:FileLoadParam) -> FileResponse:
        file_path=Path(param.url)

        if not file_path.exists():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="File Not Found")
        if not file_path.is_file():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Path is not a file")

        return FileResponse(
            path=file_path,
            filename=file_path.name)
    
        

