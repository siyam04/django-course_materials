from django.urls import path
# App importing
from blog.views import (
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
)


urlpatterns = [

    path('list/', post_list, name='list'),
    path('detail/<int:id>/', post_detail, name='detail'),
    path('create/', post_create, name='create'),
    path('update/<int:id>/', post_update, name='update'),
    path('delete/<int:id>', post_delete, name='delete'),

]