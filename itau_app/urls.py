from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about_us/', views.about_us, name="about_us"),
    path('services/', views.our_services, name="services"),
   
    path('schedule/', views.schedule, name="schedule"),
    path('contact_us/', views.contact_us, name="contact_us"),

    path('blog/',views.blogPost, name="blog"),
    # path('single_blog/', views.single_blog, name="single_blog"),
    path('single_blog/<int:post_id>/', views.single_blog, name='single_blog'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    # path('search/', views.blog_search, name='blog_search'),

    path('auditAndAssurance/', views.auditAndAssurance, name="auditAndAssurance"),
    path('accountingAndFinance/', views.accountingAndFinance, name="accountingAndFinance"),
    path('taxAdvisory/', views.taxAdvisory, name="taxAdvisory"),
    path('financialAdvisory/', views.financialAdvisory, name="financialAdvisory"),
    path('training/', views.training, name="training"),
    path('managementConsulting/', views.managementConsulting, name="managementConsulting"),
    path('corporateSocialResponsibility/', views.corporateSocialResponsibility, name="corporateSocialResponsibility"),


    
    path('careers/', views.career_page, name="careers"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)