from rest_framework.response import Response
from rest_framework.views import APIView
from user.api.serializers import UserDisplaySerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)
