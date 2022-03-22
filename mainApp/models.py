from django.db import models

# Create your models here.

class mainDirectory(models.Model):
    main_directory_id   =models.AutoField(primary_key=True)
    main_directory_name =models.CharField(max_length=10)

    class Meta:
        db_table="main_directories"

    def __str__(self):
        return self. main_directory_name


class subDirectory(models.Model):
    sub_directory_id    = models.AutoField(primary_key=True)
    main_directory      = models.ForeignKey(mainDirectory, on_delete=models.CASCADE)
    sub_directory_name  = models.CharField(max_length=10)
    # main_directory_url = models.URLField(null=True, blank=True)

    class Meta:
        db_table = "sub_directories"

    def __str__(self):
        return self.sub_directory_name

class detailDirectory(models.Model):
    detail_directory_id   = models.AutoField(primary_key=True)
    sub_directory         = models.ForeignKey(subDirectory, on_delete=models.CASCADE)
    detail_directory_name = models.CharField(max_length=10)

    class Meta:
        db_table = "detail_directories"

    def __str__(self):
        return self.detail_directory_name


class Service(models.Model):
    service_id       = models.AutoField(primary_key=True)
    detail_directory = models.ForeignKey(detailDirectory, on_delete=models.CASCADE)
    service_name     = models.CharField(max_length=20)
    image_url = models.URLField()
    request_count    = models.IntegerField()

    class Meta:
        db_table = "services"
        # ordering = ['-request_count']

# class Review(models.Model):
#     title=models.CharField(max_length=50)
#     content=models.TextField()
#     updated_at=models.DateTimeField(auto_now=True)

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    writer = models.ForeignKey('User', on_delete=models.CASCADE)
    expert = models.ForeignKey('Expert', on_delete=models.CASCADE, related_name='reviews')
    content = models.CharField(max_length=200,default="Good")
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reviews"
        ordering = ('-created_at',)


class User(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    # choice = models.ForeignKey('InterestChoice', null=True,on_delete=models.CASCADE)
    job_type= models.CharField(max_length=10,null=True)
    job_sector = models.CharField(max_length=20,null=True)
    user_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=100)
    profile_image = models.URLField(max_length=2000, null=True)
    phone_number=models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.user_name


class Expert(models.Model):
    pro_id = models.AutoField(primary_key=True, unique=True)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    # service        = models.ForeignKey('Service',on_delete=models.CASCADE)
    area= models.CharField(max_length=10)
    company_name = models.CharField(max_length=100, null=True)
    is_connect = models.BooleanField(default=False)
    expert_description = models.CharField(max_length=200)
    review_count = models.IntegerField(default=0)
    level=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "expert"

    def __str__(self):
        return self.company_name

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

