from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Raj Techs Admin"
admin.site.site_title = "Raj Techs Admin Portal"
admin.site.index_title = "Welcome to Raj Techs Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("music.urls")),
]
