from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from app.models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.serializers import *


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def empdata(request):
    LEO=Emp.objects.all()
    JEO=EmpModelSerializer(LEO,many=True)
    return Response(JEO.data)