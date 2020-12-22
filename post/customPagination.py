

# rets_framework 
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class customPagination (LimitOffsetPagination):


    def get_paginated_response(self,data) -> dict:
        return Response({
            'data':{
                'next':self.get_next_link(),
                'preview':self.get_previous_link(),
                'size':self.count,
                'returl':data
            }
        })
