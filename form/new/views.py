from django.shortcuts import render

# views.py
from rest_framework import generics, permissions
from .models import Topic, Comment, Reply
from .serializers import TopicSerializer, CommentSerializer, ReplySerializer

class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated]

class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsOwnerOrReadOnly]

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsOwnerOrReadOnly]

class ReplyList(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticated]

class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsOwnerOrReadOnly]