from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    job_type = models.CharField(max_length=10, null=True)
    job_sector = models.CharField(max_length=20, null=True)
    profile_image = models.URLField(max_length=2000, null=True)
    phonenumber = models.CharField(max_length=11)

class Expert(models.Model):
    expert_id = models.AutoField(primary_key=True, unique=True)
    user = models.OneToOneField(CustomUser,related_name='user', on_delete=models.CASCADE)
    area= models.CharField(max_length=10)
    company_name = models.CharField(max_length=100, null=True)
    is_connect = models.BooleanField(default=False)
    expert_description = models.CharField(max_length=200)
    level=models.CharField(max_length=200)
    price_sum=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "expert"

    def __str__(self):
        return self.company_name

# class ExpertField(models.Model):
#     expert_field=models.AutoField(primary_key=True)
#     Expert = models.ForeignKey(Expert, related_name='Expert', on_delete=models.CASCADE)
#     expert_field_name=models.CharField(max_length=10)
#
# class DetailField(models.Model):
#     detail_field=models.AutoField(primary_key=True)
#     ExpertField=models.ForeignKey(ExpertField, related_name='ExpertField',on_delete=models.CASCADE)
#     detail_field_name = models.CharField(max_length=10)

class mainDirectory(models.Model):
    main_directory_id   =models.AutoField(primary_key=True)
    main_directory_name =models.CharField(max_length=10)
    linkUrl = models.URLField(max_length=2000, null=True)
    category_id=models.IntegerField(blank=False)


    class Meta:
        indexes = [
            models.Index(fields=['category_id'])
        ]

class subDirectory(models.Model):
    sub_directory_id    = models.AutoField(primary_key=True)
    mainDirectory      = models.ForeignKey(mainDirectory, related_name='mainDirectory',on_delete=models.CASCADE)
    sub_directory_name  = models.CharField(max_length=10)
    banner_image = models.URLField(null=True, blank=True)
    banner_text=models.CharField(max_length=20)
    image_url = models.URLField(max_length=2000,null=True)
    linkUrl = models.URLField(max_length=2000, null=True)
    category_id=models.IntegerField(blank=False)
    # parent_id=mainDirectory_id

    class Meta:
        indexes = [
            models.Index(fields=['category_id'])
        ]

    def __str__(self):
        return self.sub_directory_name

class detailDirectory(models.Model):
    detail_directory_id   = models.AutoField(primary_key=True)
    subDirectory         = models.ForeignKey(subDirectory, related_name='subDirectory', on_delete=models.CASCADE)
    detail_directory_name = models.CharField(max_length=10)
    linkUrl = models.URLField(max_length=2000, null=True)
    category_id=models.IntegerField(blank=False)
    # parent_id=subDirectory.sub_directory_id

    class Meta:
        indexes = [
            models.Index(fields=['category_id'])
        ]

    def __str__(self):
        return self.detail_directory_name


class Service(models.Model):
    service_id       = models.AutoField(primary_key=True)
    detailDirectory = models.ForeignKey( detailDirectory,related_name='detailDirectory', on_delete=models.CASCADE)
    expert=models.ManyToManyField(Expert)
    service_name     = models.CharField(max_length=20)
    linkUrl = models.URLField(max_length=2000, null=True)
    category_id=models.IntegerField(blank=False)

    class Meta:
        indexes = [
            models.Index(fields=['category_id'])
        ]
#상품
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    Service = models.ForeignKey(Service, related_name='Service', on_delete=models.CASCADE)
    expert= models.ForeignKey(Expert, related_name='expert', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    product_description = models.CharField(max_length=200)
    price = models.IntegerField(default=10000, null=True)
    image_url = models.URLField(max_length=200)
    review_count = models.IntegerField(default=0)
    heart_count=models.IntegerField(default=0)
    linkUrl = models.URLField(max_length=2000, null=True)
    index_id = models.IntegerField(blank=False)
    class Meta:
        indexes = [
            models.Index(fields=['index_id'])
        ]






# #여러 서비스 제공하는 고수 서비스 중 각각에 대한 정보
# class ExpertService(models.Model):
#     Expertservice_id  = models.AutoField(primary_key=True)
#     expert            = models.ForeignKey('Expert', on_delete=models.CASCADE)
#     service        = models.ForeignKey('Service', on_delete=models.CASCADE)
#     price          = models.IntegerField(default=10000, null=True)
#     item_img       = models.URLField(null=True)
#     item_name      = models.CharField(max_length=100, null=True)
#     class Meta:
#         unique_together = ('expert','service')

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



#고정 배너,슬라이더 배너
class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    image_url = models.URLField(max_length=2000)
    linkUrl = models.URLField(max_length=2000, null=True)
    type=models.CharField(max_length=10)
    class Meta:
        db_table = "banners"




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

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    writer = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    # detailDirectory = models.ManyToManyField(detailDirectory)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product')
    # expert = models.ForeignKey('Expert', on_delete=models.CASCADE, related_name='reviews')
    review_content = models.CharField(max_length=200,default="Good")
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reviews"
        ordering = ('-created_at',)

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

#
#

