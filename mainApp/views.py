from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import mainDirectorySerializer,subDirectorySerializer,detailDirectorySerializer,ServiceSerializer,UserSerializer,ExpertSerializer,ReviewSerializer,StickyBannerSerializer
from .models import mainDirectory,subDirectory,detailDirectory,Service,User,Expert,Review,StickyBanner
# Create your views here.

class StickyBannerList(APIView):

    def get(self, request):
        stickyBanners = StickyBanner.objects.all()

        serializer = StickyBannerSerializer(stickyBanners, many=True)
        return Response(serializer.data)

class mainDirectoryList(APIView):

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

class mainDirectoryListDetail(APIView):

    def get_object(self,pk):
        try:
            return mainDirectory.objects.get(pk=pk)
        except mainDirectory.DoesNotExist:
            raise Http404


    #특정 게시물 조회
    def get(self,request,pk, format=None):
        services = self.get_object(pk)
        serializer = mainDirectorySerializer(services)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        mainDirectories = self.get_object(pk)
        serializer = mainDirectorySerializer(mainDirectories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class subDirectoryList(APIView):

    def get(self, request):
        directories = subDirectory.objects.all()

        serializer = subDirectorySerializer(directories, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = subDirectorySerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class detailDirectoryList(APIView):

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
#User
class UserList(APIView):

    def get(self, request):
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = UserSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#Pro
class ExpertList(APIView):

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
#Review
class ReviewList(APIView):


    def get(self, request):
        reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = ReviewSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


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