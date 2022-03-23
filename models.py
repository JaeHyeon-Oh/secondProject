from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    job_type = models.CharField(max_length=10, null=True)
    job_sector = models.CharField(max_length=20, null=True)
    profile_image = models.URLField(max_length=2000, null=True)
    phonenumber = models.CharField(max_length=11)

class Expert(models.Model):
    expert_id = models.AutoField(primary_key=True, unique=True)
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    # service        = models.ForeignKey('Service',on_delete=models.CASCADE)
    area= models.CharField(max_length=10)
    company_name = models.CharField(max_length=100, null=True)
    is_connect = models.BooleanField(default=False)
    expert_description = models.CharField(max_length=200)
    level=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "expert"

    def __str__(self):
        return self.company_name

class mainDirectory(models.Model):
    main_directory_id   =models.AutoField(primary_key=True)
    main_directory_name =models.CharField(max_length=10)

    class Meta:
        db_table="main_directories"

    def __str__(self):
        return self. main_directory_name


class subDirectory(models.Model):
    sub_directory_id    = models.AutoField(primary_key=True)
    main_directory      = models.ForeignKey('mainDirectory', on_delete=models.CASCADE)
    sub_directory_name  = models.CharField(max_length=10)
    banner_image = models.URLField(null=True, blank=True)
    banner_text=models.CharField(max_length=20)

    class Meta:
        db_table = "sub_directories"

    def __str__(self):
        return self.sub_directory_name

class detailDirectory(models.Model):
    detail_directory_id   = models.AutoField(primary_key=True)
    sub_directory         = models.ForeignKey('subDirectory', on_delete=models.CASCADE)
    detail_directory_name = models.CharField(max_length=10)

    class Meta:
        db_table = "detail_directories"

    def __str__(self):
        return self.detail_directory_name


class Service(models.Model):
    service_id       = models.AutoField(primary_key=True)
    detail_directory = models.ForeignKey('detailDirectory', on_delete=models.CASCADE)
    service_name     = models.CharField(max_length=20)
    service_description =models.CharField(max_length=200)
    image_url = models.URLField(max_length=200)
    review_count    = models.IntegerField(default=0)
    class Meta:
        db_table = "services"
        # ordering = ['-request_count']

#여러 서비스 제공하는 고수 서비스 중 각각에 대한 정보
class ExpertService(models.Model):
    Expertservice_id  = models.AutoField(primary_key=True)
    expert            = models.ForeignKey('Expert', on_delete=models.CASCADE)
    service        = models.ForeignKey('Service', on_delete=models.CASCADE)
    price          = models.IntegerField(default=10000, null=True)
    item_img       = models.URLField(null=True)
    item_name      = models.CharField(max_length=100, null=True)
    class Meta:
        unique_together = ('expert','service')

    #rating        = models.FloatField(default=0)
    #review_count
#밑 콘텐츠
class Content(models.Model):
    id=models.AutoField(primary_key=True)
    imageUrl=models.URLField(max_length=2000)
    linkUrl=models.URLField(max_length=2000, null=True)
    title = models.CharField(max_length=50,null=True)
    description= models.CharField(max_length=200,null=True)

    class Meta:
        db_table = "contents"

#배너 들어간 곳 위 중간 2곳 아래 총 4곳 모두 활용
class StickyBanner(models.Model):
    id=models.AutoField(primary_key=True)
    imageUrl=models.URLField(max_length=2000)
    linkUrl=models.URLField(max_length=2000, null=True)

    class Meta:
        db_table = "stickyBanners"

#중간 움직이는 슬라이더 배너
class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    image_url = models.URLField(max_length=2000)
    title = models.CharField(max_length=50)
    class Meta:
        db_table = "banners"
#아이콘
class Icon(models.Model):
    icon_id=models.AutoField(primary_key=True)
    sub_directory=models.ForeignKey('subDirectory', on_delete=models.CASCADE)
    image_url=models.URLField()

    class Meta:
        db_table="icons"


class Video(models.Model):
    video_id = models.AutoField(primary_key=True)
    video_url = models.URLField(max_length=2000)

    class Meta:
        db_table="videos"

#크몽을 이용한 고객들의 생생한 후기
class VideoReview(models.Model):
    videoReview_id = models.AutoField(primary_key=True)
    expert=models.ForeignKey('Expert', on_delete=models.CASCADE)
    videoReview_url = models.URLField()

    class Meta:
        db_table="videoReviews"


#관심사 선택-디자인,it프로그래밍,영상 사진 음향 등등
# class InterestChoice(models.Model):
#     interest_name=models.CharField(max_length=10)
#
#     class Meta:
#         db_table = "interest_choice"
#
#     def __str__(self):
#         return self.interest_name


    # rating        = models.FloatField(default=0)
    # review_count

#
# # class Review(models.Model):
# #     title=models.CharField(max_length=50)
# #     content=models.TextField()
# #     updated_at=models.DateTimeField(auto_now=True)
#
# class Review(models.Model):
#     review_id = models.AutoField(primary_key=True)
#     writer = models.ForeignKey('User', on_delete=models.CASCADE)
#     expert = models.ForeignKey('Expert', on_delete=models.CASCADE, related_name='reviews')
#     content = models.CharField(max_length=200,default="Good")
#     rating = models.DecimalField(max_digits=2, decimal_places=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         db_table = "reviews"
#         ordering = ('-created_at',)
#
#

