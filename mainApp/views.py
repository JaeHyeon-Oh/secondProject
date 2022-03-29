
# Create your views here.
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics
from django.db.models import Count,Sum,Avg
from .serializers import MyTokenObtainPairSerializer, CustomUserSerializer,mainDirectorySerializer,\
    subDirectorySerializer,detailDirectorySerializer,ServiceSerializer, BannerSerializer,VideoSerializer,\
    ContentSerializer,VideoReviewSerializer,ServiceSerializer,ExpertSerializer,SearchSerializer,ProductSerializer,ProductReviewSerializer,RatingSerializer,\
   PopularExpertSrializer,PopularSerializer,IconSerializer
from .models import mainDirectory,CustomUser,subDirectory,detailDirectory,Service,Banner,Content,VideoReview,Video,Service,Expert,Product
from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import filters
from mainApp import models, serializers
# from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from mainApp.models import Service
from mainApp.serializers import SearchSerializer
# StudentPagination
class StudentPagination(LimitOffsetPagination):
    default_limit =100000
# StudentViewSet
class SearchViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)

    queryset = Product.objects.annotate(review_count=Count('product', distinct=True),
                                        rating_avg=Avg('product__rating', distinct=True))
    serializer_class = SearchSerializer
    pagination_class = StudentPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]  # 👈 filters에 SearchFilter 지정
    search_fields = ['Service__service_name','expert__expert_description'] # 👈 search가 적용될 fields 지정
    ordering_fields = ['heart_count','review_count','rating_avg','created_at'] # ?ordering= -> 정렬을 허용할 필드의 화이트 리스트. 미지정 시에 serializer_class에 지정된 필드들.
    ordering = ['product_id'] # 디폴트 정렬을 지정

post_list = SearchViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

post_detail = SearchViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class ObtainTokenPairWithColorView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        users = CustomUser.objects.all()

        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class mainDirectoryList(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        directories = mainDirectory.objects.all()

        serializer = mainDirectorySerializer(directories, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = mainDirectorySerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class mainDirectoryDetailList(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self,pk):
        try:
            return mainDirectory.objects.get(pk=pk)
        except mainDirectory.DoesNotExist:
            raise Http404
        # 특정 게시물 조회
    def get(self, request, pk, format=None):
        services = self.get_object(pk)
        serializer = mainDirectorySerializer(services)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        firstcategories = self.get_object(pk)
        serializer = mainDirectorySerializer(firstcategories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class subDirectoryList(APIView):
    permission_classes = (permissions.AllowAny,)


    def get(self, request):
        directories = subDirectory.objects.all()

        serializer = subDirectorySerializer(directories,many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = subDirectorySerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#rating 평균
class ProductList(APIView):
    permission_classes = (permissions.AllowAny,)
    # queryset = Product.objects.annotate(rating_avg=Avg('product__rating'))
    # serializer = ProductSerializer(queryset, many=True)

    def get(self, request):
        # queryset = Product.objects.all().aggregate(rating_avg=Count('product'))
        # serializer = ProductSerializer(queryset, many=True)
        queryset = Product.objects.annotate(rating_avg=Avg('product__rating'))
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class subDirectoryDetailList(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = subDirectorySerializer
    lookup_url_kwarg='mainDirectory_id'
    lookup_field='mainDirectory_id'
    def get_queryset(self):
        mainDirectory_id = self.kwargs['mainDirectory_id']
        sub_directory_id = self.kwargs['sub_directory_id']

        return subDirectory.objects.filter(mainDirectory_id=mainDirectory_id, sub_directory_id=sub_directory_id)
#Banner
class BannerList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        banners = Banner.objects.all()

        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = BannerSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class detailDirectoryList(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = detailDirectorySerializer
    lookup_url_kwarg='subDirectory.mainDirectory_id'
    lookup_field='subDirectory.mainDirectory_id'
    def get_queryset(self):
        subDirectory.mainDirectory_id = self.kwargs['subDirectory.mainDirectory_id']
        subDirectory_id = self.kwargs['subDirectory_id']
        detail_directory_id= self.kwargs['detail_directory_id']

        return  detailDirectory.objects.filter(mainDirectory=subDirectory.mainDirectory_id, subDirectory_id=subDirectory_id,detail_directory_id=detail_directory_id)

#Service
class ServiceList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        services = Service.objects.all()

        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = ServiceSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#Search
class SearchList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        services = Service.objects.all()

        serializer = SearchSerializer(services, many=True)
        return Response(serializer.data)


#콘텐츠
class ContentList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        services = Content.objects.all()

        serializer = ContentSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = ContentSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#비디오
class VideoList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        video = Video.objects.all()

        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = VideoSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#비디오후기
class VideoReviewList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        video = VideoReview.objects.all()

        serializer = VideoReviewSerializer(video, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = VideoReviewSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#크몽에서 가장 인기 있어요!
class PopularList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        popular = detailDirectory.objects.annotate(
            service_count=Count('detailDirectory__Service__product')
        ).order_by('-service_count')
            # .order_by('service_count')
        serializer =PopularSerializer(popular, many=True)
        # popular = detailDirectory.objects.annotate(sub_name='subDirectory__sub_directory_name').order_by('-category_id')

        # serializer = PopularSerializer(popular, many=True)
        return Response(serializer.data)


#크몽에서 가장 인기 있어요!
class IconList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        icon = subDirectory.objects.all()
        serializer =IconSerializer(icon, many=True)
        return Response(serializer.data)

#Pro
class ExpertList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):

        queryset = Expert.objects.annotate(price_sum= Sum('expert__price')).order_by('-price_sum')
        serializer = ExpertProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer =ExpertProductSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



#전문가 순위
class PopularExpertList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        queryset = Expert.objects.annotate(price_sum=Sum('expert__price')).order_by('-price_sum')
        serializer = PopularExpertSrializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer =PopularExpertSrializer(
            data = request.data)
        # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# #전문가 순위
# class PopularExpertList(APIView):
#     permission_classes = (permissions.AllowAny,)
#
#     def grandparent_detail(request, child_id):
#         grandparent = Child.objects.get(id=child_id).parent.grandparent
#         return render(request, 'myapp/grandparent_detail.html', {'grandparent': grandparent})
#     def get(self, request):
#         queryset = Expert.objects.annotate(price_sum=Sum('expert__price')).order_by('-price_sum')
#         serializer = PopularExpertSrializer(queryset, many=True)
#         return Response(serializer.data)


#
# class IconList(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def get(self, request):
#         icons = Icon.objects.all()
#
#         serializer = IconSerializer(icons)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = IconSerializer( data =request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# class mainDirectoryListDetail(APIView):
#
#     def get_object(self,pk):
#         try:
#             return mainDirectory.objects.get(pk=pk)
#         except mainDirectory.DoesNotExist:
#             raise Http404
#
#
#     #특정 게시물 조회
#     def get(self,request,pk, format=None):
#         services = self.get_object(pk)
#         serializer = mainDirectorySerializer(services)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         mainDirectories = self.get_object(pk)
#         serializer = mainDirectorySerializer(mainDirectories, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# #Review
# class ReviewList(APIView):
#
#
#     def get(self, request):
#         reviews = Review.objects.all()
#
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):  # 새 글 작성시
#         serializer = ReviewSerializer(
#             data = request.data)  # 사용자에게 받은 입력 데이터를
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#

# class ReviewList(APIView):
#     def get(self,request):
#         reviews=Review.objects.all()
#
#         serializer=ReviewSerializer(reviews,many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer=ReviewSerializer(
#             data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class ReviewDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Review.objects.get(pk=pk)
#         except Review.DoesNotExist:
#             raise Http404
#
#     def get(self,request,pk,format=None):
#         review=self.get_object(pk)
#         serializer=ReviewSerializer(review)
#         return Response(serializer.data)
#
#     def put(self,request,pk,format=None):
#         review=self.get_object(pk)
#         serializer=ReviewSerializer(review,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk,format=None):
#         review=self.get_object(pk)
#         review.delete()
#         return Response(status=status.HTTP_201_CREATED)