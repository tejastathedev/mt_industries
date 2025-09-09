from extras.models import CompanyOTP
from datetime import timedelta, datetime
from sqlalchemy.orm import Session

filter_map = {
    'otp_companyid' : lambda value : CompanyOTP.company_id == int(value),
    'otp_otp' : lambda value : CompanyOTP.otp == str(value),
    'otp_hits_lt' : lambda value : CompanyOTP.hits <= int(3),
    'otp_genhits_lt' : lambda value : CompanyOTP.generationHits <= int(3),
    'otp_validgentime' : lambda value : CompanyOTP.creation_date+timedelta(minutes=30) < datetime.now()
}

def apply_filters(query, filters: dict):
    for key, value in filters.items():
        if key in filter_map:
            query = query.filter(filter_map[key](value))
    return query