from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("<h1>Welcome to the Shop API</h1><p>Use /api/v1/ for API endpoints.</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),
    path('', welcome),
]
