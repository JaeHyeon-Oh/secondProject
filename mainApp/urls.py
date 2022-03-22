from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import mainDirectoryList,mainDirectoryListDetail,subDirectoryList,detailDirectoryList,ServiceList,UserList, ExpertList, ReviewList,StickyBannerList

urlpatterns = [
    # path('review/',ReviewList.as_view()),
    # path('review/<int:pk>/',ReviewDetail.as_view()),
    path('directories/', mainDirectoryList.as_view()),
    path('directories/<int:pk>/', mainDirectoryListDetail.as_view()),
    path('directories/directories', subDirectoryList.as_view()),
    path('directories/directories/directories', detailDirectoryList.as_view()),
    path('service/', ServiceList.as_view()),
    path('user/', UserList.as_view()),
    path('expert/', ExpertList.as_view()),
    path('review/', ReviewList.as_view()),
    path('banner/', StickyBannerList.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)