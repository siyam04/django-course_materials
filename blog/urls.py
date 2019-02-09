from django.urls import path
# App importing
from blog.views import post_list, post_detail

urlpatterns = [

    path('list/', post_list, name='list'),
    path('detail/<int:id>/', post_detail, name='detail')

]