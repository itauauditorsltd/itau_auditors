from django.shortcuts import render
from .models import CompanyInfo, BlogPost, Tag, AboutUs, Feature, Testimony, Partner, OurTeam, Career
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count 
from calendar import month_name
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.db.models import Q


# Create your views here.

def home(request):
    topHeader = CompanyInfo.objects.first()
    posts = BlogPost.objects.order_by('-date')[:3]
    about_us = AboutUs.objects.first()
    features = Feature.objects.all()[:3]
    testimonials = Testimony.objects.all()
    partners = Partner.objects.all()  # Add this line
    return render(request, 'ITAU_Auditors_Ltd/index.html', {
        'topHeader': topHeader,
        'posts': posts,
        'about_us': about_us,
        'features': features,
        'testimonials': testimonials,
        'partners': partners,  # Add this line
    })


def about_us(request):
    about_us = AboutUs.objects.first()
    features = Feature.objects.all()[:3]
    team_members = OurTeam.objects.all()
    topHeader = CompanyInfo.objects.first()
    return render(request, 'ITAU_Auditors_Ltd/about.html', {'topHeader': topHeader,'about_us': about_us, 'features': features, 'team_members': team_members})

def about_itau_auditors (request):
    about_us = AboutUs.objects.first()
    features = Feature.objects.all()[:3]
    team_members = OurTeam.objects.all()
    topHeader = CompanyInfo.objects.first()
    return render(request, 'ITAU_Auditors_Ltd/about_itau_auditors.html', {'topHeader': topHeader,'about_us': about_us, 'features': features, 'team_members': team_members})

def our_services(request):
    topHeader = CompanyInfo.objects.first()
    return render(request,'ITAU_Auditors_Ltd/services.html', {'topHeader': topHeader})

def auditAndAssurance(request):
    topHeader = CompanyInfo.objects.first()
    return render(request,'ITAU_Auditors_Ltd/AuditAndAssurance.html', {'topHeader': topHeader})

def training(request):
    topHeader = CompanyInfo.objects.first()
    return render(request, 'ITAU_Auditors_Ltd/training.html', {'topHeader': topHeader})

def audit(request):
    topHeader = CompanyInfo.objects.first()
    return render(request, 'ITAU_Auditors_Ltd/audit.html', {'topHeader': topHeader})

def accountingAndFinance(request):
    topHeader = CompanyInfo.objects.first()
    return render(request, 'ITAU_Auditors_Ltd/AccountingAndFinance.html', {'topHeader': topHeader})

def taxAdvisory(request):
    topHeader = CompanyInfo.objects.first()
    return render(request, 'ITAU_Auditors_Ltd/TaxAdvisory.html', {'topHeader': topHeader})

def financialAdvisory(request):
    topHeader = CompanyInfo.objects.first()
    return render(request, 'ITAU_Auditors_Ltd/FinancialAdvisory.html', {'topHeader': topHeader})

def managementConsulting(request):
    topHeader = CompanyInfo.objects.first()

    return render(request,'ITAU_Auditors_Ltd/ManagementConsulting.html', {'topHeader': topHeader}) 

def corporateSocialResponsibility(request):
    topHeader = CompanyInfo.objects.first()

    return render(request,'ITAU_Auditors_Ltd/CorporateSocialResponsibility.html', {'topHeader': topHeader}) 


def dataAnalysis(request):
    topHeader = CompanyInfo.objects.first()

    return render(request,'ITAU_Auditors_Ltd/dataanalysis.html', {'topHeader': topHeader}) 


def cyberSecurityReview(request):
    topHeader = CompanyInfo.objects.first()

    return render(request,'ITAU_Auditors_Ltd/cyberSecurityReview.html', {'topHeader': topHeader})

def reviewsofISOStandards(request):
    topHeader = CompanyInfo.objects.first()

    return render(request,'ITAU_Auditors_Ltd/reviewsofISOStandards.html', {'topHeader': topHeader})



def schedule(request):
    topHeader = CompanyInfo.objects.first()

    return render(request,'ITAU_Auditors_Ltd/schedule.html', {'topHeader': topHeader})

def contact_us(request):
    topHeader = CompanyInfo.objects.first()
    
    return render(request,'ITAU_Auditors_Ltd/contact.html', {'topHeader': topHeader})

def blogPost(request):
    posts = BlogPost.objects.order_by('-date')
    postrecent = BlogPost.objects.order_by('-date')[:6]
    categories = BlogPost.objects.values('category').annotate(count=Count('category'))

    # Fetching archive data and grouping by year and month
    archive_dates = BlogPost.objects.dates('date', 'month', order='DESC')
    archive_with_month_names = []
    for date in archive_dates:
        count = BlogPost.objects.filter(date__year=date.year, date__month=date.month).count()
        archive_with_month_names.append({
            'year': date.year,
            'month': date.month,
            'month_name': month_name[date.month],
            'count': count
        })

    all_tags = Tag.objects.all()
    topHeader = CompanyInfo.objects.first()

    # Pagination
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'ITAU_Auditors_Ltd/blog-right-sidebar.html', {
        'topHeader': topHeader,
        'posts': posts,
        'postrecent': postrecent,
        'categories': categories,
        'archive_dates': archive_with_month_names,
        'all_tags': all_tags
    })



# search blog




def single_blog(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    posts = BlogPost.objects.order_by('-date')[:4]
    topHeader = CompanyInfo.objects.first()
    return render(request, 'ITAU_Auditors_Ltd/blog-details.html', {'post': post, 'posts': posts, 'topHeader': topHeader})

def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    post.likes += 1
    post.save()
    # Redirect to the single blog page of the liked post
    return redirect('single_blog', post_id=post_id)

def career_page(request):
    topHeader = CompanyInfo.objects.first() 
    careers = Career.objects.all()
    return render(request, 'ITAU_Auditors_Ltd/careers.html', {'topHeader': topHeader, 'careers': careers})

