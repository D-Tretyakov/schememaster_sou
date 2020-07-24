"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# from rest_framework import routers
from schemegen import views


# router = routers.DefaultRouter()
# router.register(r'trees', views.TreeViewSet)
# router.register(r'choices', views.ChoiceViewSet)
# router.register(r'variants', views.VariantViewSet)
# router.register(r'schema', views.SchemaViewSet)

urlpatterns = [
    path('', include('schemegen.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('schemegen/', include('schemegen.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)