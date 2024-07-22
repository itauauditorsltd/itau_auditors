from django.db import models
from django.utils import timezone
from storages.backends.s3boto3 import S3Boto3Storage

class CompanyInfo(models.Model):
    logo = models.ImageField(upload_to='logos/', storage=S3Boto3Storage())
    logo_two = models.ImageField(upload_to='logostwo/', storage=S3Boto3Storage())
    street_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    working_hours = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    brochure = models.FileField(upload_to='brochures/', null=True, blank=True, storage=S3Boto3Storage())
    
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    pinterest = models.URLField(max_length=200, blank=True, null=True)
    rss = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.street_address} - {self.phone}"

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_us_images/', null=True, blank=True, storage=S3Boto3Storage())

    def __str__(self):
        return self.title

class Feature(models.Model):
    icon_class = models.CharField(max_length=50,  null=True, blank=True)
    title = models.CharField(max_length=80,  null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Testimony(models.Model):
    description = models.TextField(null=True, blank=True)
    client_name = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    job_title = models.CharField(max_length=25, null=True, blank=True)
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True, storage=S3Boto3Storage())

    def __str__(self):
        return self.client_name

class Partner(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='partners/', null=True, blank=True, storage=S3Boto3Storage())

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True, storage=S3Boto3Storage())
    author = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    category = models.CharField(max_length=100)
    subImage = models.ImageField(upload_to='blog_images/', null=True, blank=True, storage=S3Boto3Storage())
    subImage2 = models.ImageField(upload_to='blog_images/', null=True, blank=True, storage=S3Boto3Storage())
    subTitle = models.CharField(max_length=200, blank=True, null=True)
    subDescription = models.TextField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def formatted_date(self):
        return self.date.strftime('%d %b, %Y')

class OurTeam(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='ourTeam_images/', null=True, blank=True, storage=S3Boto3Storage())
    position = models.CharField(max_length=100)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Career(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    application_link = models.URLField()

    def __str__(self):
        return self.title