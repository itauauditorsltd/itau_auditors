from django.contrib import admin
from .models import CompanyInfo, AboutUs, Feature, Testimony, Partner, BlogPost, Tag, OurTeam, Career

class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('street_address', 'phone', 'working_hours')
    search_fields = ('street_address', 'phone')

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class')
    search_fields = ('title', 'icon_class')

class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'job_title')
    search_fields = ('client_name', 'job_title')

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'formatted_date', 'category')
    search_fields = ('title', 'author', 'category')
    list_filter = ('date', 'category')
    readonly_fields = ('formatted_date',)

    def formatted_date(self, obj):
        return obj.date.strftime('%b %d, %Y')

    formatted_date.short_description = 'Date'

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('name', 'position')

class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'application_link')
    search_fields = ('job_title', 'description')

admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Testimony, TestimonyAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(Career, CareerAdmin)
