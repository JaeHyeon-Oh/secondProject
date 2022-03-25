from django.urls import path , include
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView, CustomUserCreate, LogoutAndBlacklistRefreshTokenForUserView
from .views import mainDirectoryList,subDirectoryList,ObtainTokenPairWithColorView, CustomUserCreate,\
    detailDirectoryList,ServiceList,BannerList,mainDirectoryDetailList,\
    subDirectoryDetailList,ContentList, VideoList,VideoReviewList,ServiceViewSet,ExpertList,SearchList,ProductReviewList
# from rest_framework.routers import DefaultRouter
# from . import views

# router = DefaultRouter()
# router.register('viewset',views.ServiceViewSet)
#,UserList, ExpertList, ReviewList,StickyBannerList,
urlpatterns = [
    # path('review/',ReviewList.as_view()),
    # path('review/<int:pk>/',ReviewDetail.as_view()),
    # path('', include(router.urls)),
    path('directories/', mainDirectoryList.as_view()),
    path('directories/<int:pk>', mainDirectoryDetailList.as_view()),
    # path('directories/<int:mainDirectory_id>', subDirectoryList.as_view()),
    path('directories/<int:mainDirectory_id>/<int:sub_directory_id>', subDirectoryDetailList.as_view()),
    # path('directories/<int:subDirectory.mainDirectory_id>/<int:sub_directory_id>/<int:detail_directory_id>', detailDirectoryList.as_view()),
    # path('directories/<int:subDirectory_id>/<int:detail>', detailDirectoryList.as_view()),
    path('service/', ServiceList.as_view()),
    # path('user/', UserList.as_view()),
    # path('expert/', ExpertList.as_view()),
    # path('review/', ReviewList.as_view()),
    # path('banner/', StickyBannerList.as_view()),
    path('slider/', BannerList.as_view()),
    # path('icon/', IconList.as_view()),
    path('content/', ContentList.as_view()),
    path('search/', SearchList.as_view()),
    path('video/', VideoList.as_view()),
    path('videoReview/', VideoReviewList.as_view()),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('expert/',ExpertList.as_view()),
    path('review/',ProductReviewList.as_view()),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
]
# urlpatterns=format_suffix_patterns(urlpatterns)