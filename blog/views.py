from rest_framework import generics 
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by("-created")
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "slug"
    queryset = Post.objects.all()
    serializer_class = PostSerializer