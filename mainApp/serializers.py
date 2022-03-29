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





class ProductExpertSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='user.username')
    # profile_image = serializers.URLField(source='user.profile_image')
    # product = ProductSerializer(many=True,read_only=True)

    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'price']

#리뷰
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['review_id','review_content','rating','updated_at']
#Expert
class ExpertSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='user.username')
    # profile_image = serializers.URLField(source='user.profile_image')
    # expert = ExpertProductSerializer(read_only=True)

    # price_sum = serializers.IntegerField(read_only=True)
    class Meta:
        model = Expert
        fields = ['expert_id','company_name','is_connect','level','expert_description']

# class RatingSerializer(serializers.ModelSerializer):
#     product = ReviewSerializer(many=True, read_only=True)
#     rating_avg = serializers.IntegerField(read_only=True)
#
#     class Meta:
#         model = Product
#         fields = ['rating_avg','product']
#Service의 구성-디자인>로고브랜딩>로고디자인>상품, rating 평균
class ProductSerializer(serializers.ModelSerializer):
    # expert = ExpertSerializer(read_only=True)

    # rating_avg = serializers.IntegerField(source='product.rating')
    # expert_area = serializers.CharField(source='expert.area')
    product = ReviewSerializer(many=True, read_only=True)
    # rating_avg = serializers.IntegerField(read_only=True)
    # rating = RatingSerializer(many=True,read_only=True)

    class Meta:
        model = Product
        fields = ['product_id','product_name','image_url','price','product']

#크몽에서 인기있는 디테일 디렉토리
class PopularSerializer(serializers.ModelSerializer):
    service_count = serializers.IntegerField(read_only=True)
    # service_count = serializers.CharField(read_only=True)
    sub_name = serializers.CharField(source='subDirectory.sub_directory_name')
    class Meta:
        model = detailDirectory
        fields = [ 'detail_directory_id','sub_name','detail_directory_name','linkUrl','service_count']
#detailDirectory의 구성-디자인>로고브랜딩>로고디자인, 브랜딩
class ServiceSerializer(serializers.ModelSerializer):
    # Service= ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Service
        fields = ['service_id','service_name','category_id']


#subDirectory의 구성-디자인>로고브랜딩,상세이벤트 페이지 등등
class detailDirectorySerializer(serializers.ModelSerializer):
    detailDirectory = ServiceSerializer(many=True, read_only=True)
    class Meta:
        model = detailDirectory
        fields = [ 'detail_directory_id','detail_directory_name','detailDirectory']
        # fields = ('__all__')
        # depth=2
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

#category Icon
class IconSerializer(serializers.ModelSerializer):
    main_name = serializers.CharField(source='mainDirectory.main_directory_name')
    class Meta:
        model = subDirectory
        fields = ['sub_directory_id','sub_directory_name','image_url','main_name']
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
#Expert
class PopularExpertSrializer(serializers.ModelSerializer):
    detail_name= serializers.CharField(read_only=True)
    profile_image = serializers.URLField(source='user.profile_image')
    expert = ProductExpertSerializer(many=True,read_only=True)
    price_sum = serializers.IntegerField(read_only=True)
    service=ServiceSerializer(many=True,read_only=True)
    class Meta:
        model = Expert
        fields = ['expert_id', 'company_name','detail_name', 'is_connect', 'expert_description','price_sum','profile_image','expert','service']
        # depth=2
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


#상품리뷰
class ProductReviewSerializer(serializers.ModelSerializer):
    product=ReviewSerializer(many=True,read_only=True)
    review_count=serializers.IntegerField(read_only=True)
    rating_avg=serializers.DecimalField(max_digits=11, decimal_places=1)
    class Meta:
        model=Product
        fields=['product_id','product_description','review_count','rating_avg','product','created_at']


#search
class SearchSerializer(serializers.ModelSerializer):
    expert=ExpertSerializer(read_only=True)
    # Service=serializers.CharField(source='Service.service_name')
    Service = ServiceSerializer(read_only=True)
    # product = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(read_only=True)
    rating_avg = serializers.DecimalField(max_digits=11, decimal_places=1)
    category=serializers.CharField(read_only=True)
    # product=ProductReviewSerializer(many=True,read_only=True)
    class Meta:
        model=Product
        # fields = ['Service','expert']
        fields = ['product_id','product_name','heart_count','rating_avg','review_count','created_at', 'image_url','category','Service','expert']
        # fields= ( '__all__')
        # depth=3

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







