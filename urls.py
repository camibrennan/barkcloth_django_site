from django.urls import path

import views

urlpatterns = [
    path('index.html', views.index),
    path('blog.html', views.blog),
    path('purchase.html', views.purchase),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

