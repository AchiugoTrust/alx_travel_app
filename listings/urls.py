from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response

# Sample view for testing
class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})

urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello_world'),
]
