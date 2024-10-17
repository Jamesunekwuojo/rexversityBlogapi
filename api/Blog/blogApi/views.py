from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response  import Response
from .models import BlogPost
from .serializers import BlogPostSerializer

from rest_framework.decorators import api_view


#Blog post cretae function
@api_view(['POST'])
def createBlog(request):
    if request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)

        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Blog post get view
@api_view(['GET'])

def getBlog(request):
    if request.method == 'GET':
        blogposts = BlogPost.objects.all()

        serialiZer = BlogPostSerializer(blogposts, many=True)

        return Response(serialiZer.data)




















# Class based view using DRF generics
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all() # getting all of the blogpost models that exist
    serializer_class = BlogPostSerializer


# using custom functions to overide. That's to delete all of the different blog posts that exist
def delete(self, request, *args, **kwargs):
    BlogPost.objects.all()
    return Response(status=status.HTTP_204_NO_CONTENT)

# creating a new view which can be used to update and delete blog post by id

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk' # which is the primary key that's the id




