
# Create your views here.
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics
from .serializers import MyTokenObtainPairSerializer, CustomUserSerializer,mainDirectorySerializer,\
    subDirectorySerializer,detailDirectorySerializer,ServiceSerializer, BannerSerializer,VideoSerializer,\
    ContentSerializer,VideoReviewSerializer,ServiceSerializer,ReviewSerializer,ExpertSerializer,SearchSerializer,ProductSerializer,ProductReviewSerializer
from .models import mainDirectory,CustomUser,subDirectory,detailDirectory,Service,Banner,Content,VideoReview,Video,Service,Expert,Product,Review
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
# from .serializers import mainDirectorySerializer,subDirectorySerializer,detailDirectorySerializer,ServiceSerializer,UserSerializer,ExpertSerializer,ReviewSerializer,StickyBannerSerializer
# from .models import mainDirectory,subDirectory,detailDirectory,Service,User,Expert,Review,StickyBanner
# # Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    # SearchFilter 기반으로 검색할 예정입니다
    filter_backends = [SearchFilter]
    # 어떤 칼럼을 기반으로 검색을 할 건지 search_fields에 *튜플* 형식으로 적어주세요
    search_fields = ('service_name')

# class StickyBannerList(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def get(self, request):
#         stickyBanners = StickyBanner.objects.all()
#
#         serializer = StickyBannerSerializer(stickyBanners,many = True)
#         return Response(serializer.data)

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

# class subDirectoryDetailList(APIView):
#     permission_classes = (permissions.AllowAny,)
#
#     def get_object(self):
#         username = self.kwargs.get('sub_directory_name')
#         slug = self.kwargs.get('category_id')
#
#         # find the user
#         user = subDirectory.objects.get(username=username)
#
#         try:
#             return subDirectory.objects.get()
#         except subDirectory.DoesNotExist:
#             raise Http404
#
#
#         # 특정 게시물 조회
#     def get(self, request, fk, format=None):
#         services = self.get_object(fk)
#         serializer = subDirectorySerializer(services)
#         return Response(serializer.data)
#
#     def put(self, request, fk, format=None):
#         subDirectories = self.get_object(fk)
#         serializer = mainDirectorySerializer(subDirectories, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
# class detailDirectoryList(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def get(self, request):
#         directories = detailDirectory.objects.all()
#
#         serializer = detailDirectorySerializer(directories, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):  # 새 글 작성시
#         serializer = detailDirectorySerializer(
#             data = request.data)  # 사용자에게 받은 입력 데이터를
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
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
# #아이콘
# class IconList(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def get(self, request):
#         services = Icon.objects.all()
#
#         serializer = IconSerializer(services, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):  # 새 글 작성시
#         serializer = IconSerializer(
#             data = request.data)  # 사용자에게 받은 입력 데이터를
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

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
#Pro
class ExpertList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        Experts = Expert.objects.all()

        serializer = ExpertSerializer(Experts, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = ExpertSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


#크몽에서 가장 인기있어요!
class ProductReviewList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        products = Product.objects.all()
        review_count =Review.objects.count()
        content = {'review_count': review_count}
        serializer = ProductReviewSerializer(products, many=True)

        # return Response(serializer.data)
        return Response(content)

    def post(self, request):  # 새 글 작성시
        serializer =ProductReviewSerializer(
            data = request.data)
        # 사용자에게 받은 입력 데이터를
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