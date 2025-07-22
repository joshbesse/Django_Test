from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Text
from .serializers import TextSerializer

# Create your views here.
@api_view(['GET'])
def default(request):
    return HttpResponse("Hello, Django!")

@api_view(['GET'])
def text_list(request):
    texts = Text.objects.all()
    serializer = TextSerializer(texts, many=True)
    return Response(serializer.data)

