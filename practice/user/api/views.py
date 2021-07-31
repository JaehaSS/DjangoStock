from rest_framework.response import Response
from rest_framework.views import APIView
from user.api.serializers import UserDisplaySerializer,UserlistSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from user.models import CustomUser

class CurrentUserAPIView(APIView):
    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)





class UserlistAPIView(APIView):
    def get(self, request):
        print(request.user)
        print(request)
        userlist = CustomUser.objects.all().filter(id=1)
        serializer = UserlistSerializer(userlist, many=True)
        return Response(serializer.data)
