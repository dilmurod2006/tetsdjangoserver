from rest_framework.generics import ListAPIView, RetrieveAPIView
from Works.models import Works
from .serializers import WorksSerializer


class PostList(ListAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer
class Detailpost(RetrieveAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer
