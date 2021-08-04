from django.http import response
from rest_framework.response import Response
from rest_framework.views import APIView
from user.api.serializers import UserDisplaySerializer,UserlistSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from user.models import CustomUser
import requests as httprequest
from bs4 import BeautifulSoup
from rest_framework.decorators import api_view


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


@api_view(['GET',])
def parse_blog(request):
    req = httprequest.get('https://finance.naver.com/news/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select(
        '.main_news > ul >li >a'
        )
    data = {}
    # (i.text)

    for i in titles:
      data[i.text] = i.get('href')

    return Response(data)
