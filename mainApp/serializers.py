from rest_framework import serializers
from .models import mainDirectory,subDirectory,detailDirectory,Service,User,Expert,Review


#메인 카테고리-비즈니스,n잡커리어 등등
class mainDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = mainDirectory
        fields = ( '__all__')

#mainDirectory의 구성-비즈니스>디자인,IT프로그래밍 등등
class subDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = subDirectory
        fields = ( '__all__')

#subDirectory의 구성-디자인>로고브랜딩,상세이벤트 페이지 등등
class detailDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = detailDirectory
        fields = ( '__all__')
#Service
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ( 'service_id',' service_name','image_url','request_count')

#User
class UserSerializer(serializers.ModelSerializer):
    # choice = serializers.CharField(source='choice. interest_name')
    class Meta:
        model = User
        fields = ('email','user_name','password','phone_number')

#Expert
class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = '__all__'

#Review
class ReviewSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='writer.name')
    class Meta:
        model = Review
        fields = ['name','content','rating','created_at']
# #관심사 선택
# class InterestChoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InterestChoice
#         fields = ('__all__')


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Review
#         fields=('id','title','content','updated_at')