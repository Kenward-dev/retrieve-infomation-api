from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
import pytz

class RetrieveBasicInfo(APIView):
    def get(self, request):
        data = {
            "email": "codewithkenward@gmail.com",
            "current_datetime": datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "github_url": "https://github.com/Kenward-dev/retrieve-infomation-api"
        }
        return Response(data)
