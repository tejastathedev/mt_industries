class Response:
    @staticmethod
    def success(data=None, message="Success", total_count=1, page_no=1, per_page=10):
        return {
            "status": True,
            "message": message,
            "data": data,
            "total_count": total_count,
            "page_no": page_no,
            "per_page": per_page,
        }

    @staticmethod
    def error(message="Something went wrong", data=None):
        return {"status": False, "message": message, "data": data}
