from django.urls import path
from .views import ProductAPIView, TaskListCreateAPIView
urlpatterns = [
    path("products/", ProductAPIView.as_view(), name="api_products"),
    path("tasks/", TaskListCreateAPIView.as_view(), name="task-list-create"),

]
