from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, DatabaseError
from config import settings

class ExceptionHandler:
    def __init__(self, app: FastAPI):
        app.add_exception_handler(HTTPException, self.http_exception_handler)  
        app.add_exception_handler(Exception, self.global_exception_handler) 

    async def http_exception_handler(self, request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )

    async def global_exception_handler(self, request: Request, exc: Exception):
        if isinstance(exc, IntegrityError):
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"detail_integrity": settings.DUPLICATE_DATA_ERROR.format(error=str(exc))},
            )

        if isinstance(exc, DatabaseError):
            # print("Exception caught: ",DatabaseError.statement)
            # return JSONResponse(
            #     status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            #     content={"detail": DatabaseError.statement},
            # )
            # Now we access the statement and params from the actual exception instance
            print("Exception caught:", exc.statement, exc.params)

            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "detail": str(exc.statement),
                },
            )

        # Fallback for unexpected errors
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": settings.UNEXPECTED_ERROR.format(error=str(exc))},
        )
