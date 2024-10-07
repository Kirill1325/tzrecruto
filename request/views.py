from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class View(APIView):
    def get(self, request):
        context = {
            "name": request.query_params.get("name"),
            "message": request.query_params.get("message"),
        }
        return render(request, "index.html", context)
    