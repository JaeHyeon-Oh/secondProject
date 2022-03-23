from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import mainDirectoryList,subDirectoryList,ObtainTokenPairWithColorView, CustomUserCreate,\
    detailDirectoryList,ServiceList,StickyBannerList,BannerList,IconList,mainDirectoryDetailList,\
    subDirectoryDetailList,ContentList, VideoList,VideoReviewList

#,UserList, ExpertList, ReviewList,StickyBannerList,
urlpatterns = [
    # path('review/',ReviewList.as_view()),
    # path('review/<int:pk>/',ReviewDetail.as_view()),
    path('directories/', mainDirectoryList.as_view()),
    path('directories/<int:pk>', mainDirectoryDetailList.as_view()),
    path('directories/directories', subDirectoryList.as_view()),
    path('directories/<int:fk>/directories', subDirectoryDetailList.as_view()),
    path('directories/directories/directories', detailDirectoryList.as_view()),
    path('service/', ServiceList.as_view()),
    # path('user/', UserList.as_view()),
    # path('expert/', ExpertList.as_view()),
    # path('review/', ReviewList.as_view()),
    path('banner/', StickyBannerList.as_view()),
    path('slider/', BannerList.as_view()),
    path('icon/', IconList.as_view()),
    path('content/', ContentList.as_view()),
    path('video/', VideoList.as_view()),
    path('videoReview/', VideoReviewList.as_view()),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
# urlpatterns=format_suffix_patterns(urlpatterns)