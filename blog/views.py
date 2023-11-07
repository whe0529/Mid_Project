from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import *

def post_list(request):
        posts = Post.objects.filter(published_date = timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})


class CaptureImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



    