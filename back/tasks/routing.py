from django.urls import path, re_path
from .consumers import TasksConsumer

# ws_urpatterns = [
#     # path('ws/tasks_info/', TasksConsumer.as_asgi()),
#     re_path(r'ws/tasks_info/$',TasksConsumer.as_asgi()),
# ]

websocket_urlpatterns = [
    re_path(r'^ws/tasks_info/$', TasksConsumer.as_asgi()),
]

