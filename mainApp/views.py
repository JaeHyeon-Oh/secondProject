
# Create your views here.
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from django.http import Http404

from .serializers import MyTokenObtainPairSerializer, CustomUserSerializer,mainDirectorySerializer,\
    subDirectorySerializer,detailDirectorySerializer,ServiceSerializer,StickyBannerSerializer, BannerSerializer,VideoSerializer,\
    ContentSerializer,IconSerializer,VideoReviewSerializer
from .models import mainDirectory,CustomUser,subDirectory,detailDirectory,Service,StickyBanner,Banner,Icon,Content,VideoReview,Video

# from .serializers import mainDirectorySerializer,subDirectorySerializer,detailDirectorySerializer,ServiceSerializer,UserSerializer,ExpertSerializer,ReviewSerializer,StickyBannerSerializer
# from .models import mainDirectory,subDirectory,detailDirectory,Service,User,Expert,Review,StickyBanner
# # Create your views here.

class StickyBannerList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        stickyBanners = StickyBanner.objects.all()

        serializer = StickyBannerSerializer(stickyBanners,many = True)
        return Response(serializer.data)

class ObtainTokenPairWithColorView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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

    # def get_object(self,pk):
    #     try:
    #         return mainDirectory.objects.get(pk=pk)
    #     except mainDirectory.DoesNotExist:
    #         raise Http404
    def get(self, request):
        directories = mainDirectory.objects.all()

        serializer = mainDirectorySerializer(directories, many=True)
        return Response(serializer.data)

        # 특정 게시물 조회
    # def get(self, request, pk, format=None):
    #     services = self.get_object(pk)
    #     serializer = mainDirectorySerializer(services)
    #     return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     firstcategories = self.get_object(pk)
    #     serializer = mainDirectorySerializer(firstcategories, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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

    # def get_object(self,pk):
    #     try:
    #         return mainDirectory.objects.get(pk=pk)
    #     except mainDirectory.DoesNotExist:
    #         raise Http404
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

class subDirectoryDetailList(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self,fk):
        try:
            return subDirectory.objects.get(fk=fk)
        except subDirectory.DoesNotExist:
            raise Http404
        # 특정 게시물 조회
    def get(self, request, fk, format=None):
        services = self.get_object(fk)
        serializer = subDirectorySerializer(services)
        return Response(serializer.data)

    def put(self, request, fk, format=None):
        subDirectories = self.get_object(fk)
        serializer = mainDirectorySerializer(subDirectories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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

class detailDirectoryList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        directories = detailDirectory.objects.all()

        serializer = detailDirectorySerializer(directories, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = detailDirectorySerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
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

#아이콘
class IconList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        services = Icon.objects.all()

        serializer = IconSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = IconSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

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

# #Pro
# class ExpertList(APIView):
#
#     def get(self, request):
#         Experts = Expert.objects.all()
#
#         serializer = ExpertSerializer(Experts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):  # 새 글 작성시
#         serializer = ExpertSerializer(
#             data = request.data)  # 사용자에게 받은 입력 데이터를
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
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