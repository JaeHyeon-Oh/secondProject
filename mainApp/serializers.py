from rest_framework import serializers
# from .models import mainDirectory,subDirectory,detailDirectory,Service,User,Expert,Review,StickyBanner

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser,mainDirectory,subDirectory

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        # token['fav_color'] = user.fav_color
        return token


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password','phonenumber')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
# class StickyBannerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StickyBanner
#         fields = ('id', 'linkUrl', 'imageUrl')
#메인 카테고리-비즈니스,n잡커리어 등등
class mainDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = mainDirectory
        fields = ( '__all__')

#mainDirectory의 구성-비즈니스>디자인,IT프로그래밍 등등
class subDirectorySerializer(serializers.ModelSerializer):
    parent_id = serializers.CharField(source='main_directory.main_directory_id')
    class Meta:
        model = subDirectory
        fields = ['sub_directory_id','sub_directory_name','banner_image','banner_text','parent_id']

# #subDirectory의 구성-디자인>로고브랜딩,상세이벤트 페이지 등등
# class detailDirectorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = detailDirectory
#         fields = ( '__all__')
# #Service
# class ServiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Service
#         fields = ( 'service_id',' service_name','image_url','request_count')
#
# #User
# class UserSerializer(serializers.ModelSerializer):
#     # choice = serializers.CharField(source='choice. interest_name')
#     class Meta:
#         model = User
#         fields = ('email','user_name','password','phone_number')
#
# #Expert
# class ExpertSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Expert
#         fields = '__all__'
#
# #Review
# class ReviewSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(source='writer.name')
#     class Meta:
#         model = Review
#         fields = ['name','content','rating','created_at']
# #관심사 선택
# class InterestChoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InterestChoice
#         fields = ('__all__')


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Review
#         fields=('id','title','content','updated_at')