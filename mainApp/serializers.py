from rest_framework import serializers
# from .models import mainDirectory,subDirectory,detailDirectory,Service,User,Expert,Review,StickyBanner

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser,mainDirectory,subDirectory,detailDirectory,Service,Banner,Content,\
    VideoReview,Video,Product,Expert,Review

#토큰 받기 위한 클래스
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        # token['fav_color'] = user.fav_color
        return token

#회원가입 유저
class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    # email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    class Meta:
        model = CustomUser
        fields = ('username', 'password','phonenumber','first_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance






#Expert
class ExpertProductSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='user.username')
    # profile_image = serializers.URLField(source='user.profile_image')
    # product = ProductSerializer(many=True,read_only=True)
    class Meta:
        model = Expert
        fields = ['expert_id','company_name','is_connect','expert_description']

#Service의 구성-디자인>로고브랜딩>로고디자인>상품
class ProductSerializer(serializers.ModelSerializer):
    expert = ExpertProductSerializer(read_only=True)
    # expert_name = serializers.CharField(source='expert.company_name')
    # expert_area = serializers.CharField(source='expert.area')
    class Meta:
        model = Product
        fields = ['product_id','product_name','price','expert']
#Expert
class ExpertSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='user.username')
    # profile_image = serializers.URLField(source='user.profile_image')
    product = ProductSerializer(many=True,read_only=True)
    class Meta:
        model = Expert
        fields = ['expert_id','company_name','is_connect','product']
#detailDirectory의 구성-디자인>로고브랜딩>로고디자인, 브랜딩
class ServiceSerializer(serializers.ModelSerializer):
    Service= ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Service
        fields = ['service_id','service_name','category_id','Service']

#subDirectory의 구성-디자인>로고브랜딩,상세이벤트 페이지 등등
class detailDirectorySerializer(serializers.ModelSerializer):
    detailDirectory = ServiceSerializer(many=True, read_only=True)
    class Meta:
        model = detailDirectory
        fields = [ 'detail_directory_id','detail_directory_name','detailDirectory']
#mainDirectory의 구성-비즈니스>디자인,IT프로그래밍 등등
class subDirectorySerializer(serializers.ModelSerializer):
    subDirectory=detailDirectorySerializer(many=True,read_only=True)
    class Meta:
        model = subDirectory
        fields = ['sub_directory_id','sub_directory_name','banner_image','banner_text','subDirectory']
#메인 카테고리-비즈니스,n잡커리어 등등
class mainDirectorySerializer(serializers.ModelSerializer):
    mainDirectory=subDirectorySerializer(many=True,read_only=True)
    class Meta:
        model = mainDirectory
        fields = ['main_directory_id','main_directory_name','mainDirectory']


#고정된 큰 배너
class StickyBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('__all__')

#슬라이더 배너
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ( '__all__')
# #상세분야
# class DetailFieldSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=DetailField
#         fields = ['detail_field_name']
# #전문가 분야
# class ExpertFieldSerializer(serializers.ModelSerializer):
#     detail_field=DetailFieldSerializer(many=True, read_only=True)
#     class Meta:
#         model=ExpertField
#         fields = ['expert_field_name','detail_field']
#search
class SearchSerializer(serializers.ModelSerializer):
    expert=ExpertProductSerializer(many=True,read_only=True)
    class Meta:
        model=Service
        fields = ['service_name','expert']
# #서브 디렉토리 아이콘
# class IconSerializer(serializers.ModelSerializer):
#     sub_directory_name= serializers.CharField(source='sub_directory.sub_directory_id')
#     class Meta:
#         model = Icon
#         fields = ( '__all__')

#'크몽을 200%활용하는 법'콘텐츠
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ( '__all__')

#'박명수 있는 유투브 비디오'
class  VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ( '__all__')

#'유투브 후기'
class  VideoReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoReview
        fields = ( '__all__')

#리뷰
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['review_id','review_content','rating','updated_at']

# #상품리뷰
# class ProductReviewSerializer(serializers.ModelSerializer):
#     review=ReviewSerializer(many=True,read_only=True)
#     review_count=serializers.IntegerField()
#     count = Review.objects.count()
#     def update(self, instance, validated_data):
#         instance.review_count = validated_data.get('title', instance.count)
#         instance.save()
#         return instance
#     class Meta:
#         model=Product
#         fields=['product_id','product_description','review_count','review']



# class ExpertServiceSerializer(serializers.ModelSerializer):
#     expert_name = serializers.CharField(source='expert.company_name')
#     description = serializers.CharField(source='expert. expert_description')
#     service_name=serializers.CharField(source='service .service _name')
#
#     class Meta:
#         model = ExpertService
#         fields = ('expert_name','description','service_name')
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


