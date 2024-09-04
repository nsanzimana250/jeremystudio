from django.contrib import admin
from .models import Image
from .models import Video
from .models import Customer, CustomerProduct
import datetime
from .models import Contact
from .models import customer_videos

# contact form 
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'phone_number', 'message')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('subject',)
    fields = ('name', 'email', 'subject', 'phone_number', 'message')
    readonly_fields = ('email',)
    actions = ['mark_as_read']
    def mark_as_read(self, request, queryset):
        queryset.update(subject='Read')
    mark_as_read.short_description = 'Mark selected contacts as read'
admin.site.register(Contact, ContactAdmin)

# image 

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'imagefile', 'description', 'date')
    search_fields = ('name', 'description')
    list_filter = ('date',)
    fields = ('name', 'imagefile', 'description', 'date')
    readonly_fields = ()
    actions = ['make_recent']
    def make_recent(self, request, queryset):
        queryset.update(date=datetime.date.today())
    make_recent.short_description = 'Mark selected images as recent'
admin.site.register(Image, ImageAdmin)

# video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'videofile', 'description', 'date')
    search_fields = ('name', 'description')
    list_filter = ('date',)
    fields = ('name', 'videofile', 'description', 'date')
    readonly_fields = ()
    actions = ['make_recent']

    def make_recent(self, request, queryset):
        queryset.update(date=datetime.date.today())
    
    make_recent.short_description = 'Mark selected videos as recent'

admin.site.register(Video, VideoAdmin)

# customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'created_at')
    search_fields = ('full_name',)
    readonly_fields = ('created_at',)

admin.site.register(Customer, CustomerAdmin)

# CustomerProduct

class CustomerProductAdmin(admin.ModelAdmin):
    list_display = ('customer', 'image_file', 'description', 'created_date')
    search_fields = ('description',)
    list_filter = ('created_date',)
    readonly_fields = ('created_date',)
    autocomplete_fields = ('customer',)

    def __str__(self):
        return f'{self.customer} - {self.description}'

admin.site.register(CustomerProduct, CustomerProductAdmin)

# CustomerVideos

class CustomerVideosAdmin(admin.ModelAdmin):
    list_display = ('customer', 'name', 'videofile', 'description', 'created_date')
    search_fields = ('name', 'description')
    list_filter = ('created_date',)
    readonly_fields = ('created_date',)
    autocomplete_fields = ('customer',)

    def __str__(self):
        return f'{self.customer.full_name} - {self.name}'

admin.site.register(customer_videos, CustomerVideosAdmin)
