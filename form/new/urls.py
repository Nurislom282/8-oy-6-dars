from django.urls import path
from . import views

urlpatterns = [
    path('topics/', views.TopicList.as_view(), name='topic_list'),
    path('topics/<int:pk>/', views.TopicDetail.as_view(), name='topic_detail'),
    path('topics/<int:pk>/comments/', views.CommentList.as_view(), name='comment_list'),
    path('topics/<int:pk>/comments/<int:comment_pk>/', views.CommentDetail.as_view(), name='comment_detail'),
    path('topics/<int:pk>/comments/<int:comment_pk>/replies/', views.ReplyList.as_view(), name='reply_list'),
    path('topics/<int:pk>/comments/<int:comment_pk>/replies/<int:reply_pk>/', views.ReplyDetail.as_view(), name='reply_detail'),
]