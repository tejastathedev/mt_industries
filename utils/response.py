# class Response:
    # @staticmethod
    # def success(data=None, message="Success", total_count=1, page_no=1, per_page=10):
    #     return {
    #         "status": True,
    #         "message": message,
    #         "data": data,
    #         "total_count": total_count,
    #         "page_no": page_no,
    #         "per_page": per_page,
    #     }

    # @staticmethod
    # def error(message="Something went wrong", data=None):
    #     return {"status": False, "message": message, "data": data}


from .pagination_schema import PaginationSchema
from typing import Union,List,Dict
from enum import IntEnum
from fastapi import status
from fastapi.responses import JSONResponse
import warnings

class ApiResponseStatus(IntEnum):
    SUCCESS = 1
    ERROR = 0


class Response:
    @staticmethod
    def generic_response(
        data: Union[List, Dict] | None = None, 
        user_message: str | None = None, 
        status_code: int = status.HTTP_200_OK, 
        status: int = ApiResponseStatus.SUCCESS, 
        pagination: PaginationSchema = None):
        
        if pagination:
            warnings.warn(
            "The 'pagination' parameter is deprecated and will be removed in a future version. Pass request paramiter directly)",
            DeprecationWarning
            )
            # Calculate total pages
            total_pages = (pagination.total_records + pagination.per_page - 1) // pagination.per_page
            pagination.total_pages = total_pages
            # pagination = pagination.model_dump()
            def pagination_func():
                ...                
        
        return {
            "data" :data,
            "user_message" : user_message,
            "status_code" : status_code,
            "status" : status,
            "pagination" : pagination
   
        }




