from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    path('', BoardList.as_view()),
    path('<int:pk>/', BoardDetail.as_view()),
    path('<int:pk>/update/', BoardUpdate.as_view()),
    path('<int:pk>/destroy/', BoardDestroy.as_view()),
    path('<int:post>/comments/', CommentDetail.as_view()),
]