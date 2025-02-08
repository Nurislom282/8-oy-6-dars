# serializers.py
from rest_framework import serializers
from .models import Topic, Comment, Reply

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'created_at', 'user']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'topic', 'text', 'user', 'created_at', 'parent_comment']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'comment', 'text', 'user', 'created_at']