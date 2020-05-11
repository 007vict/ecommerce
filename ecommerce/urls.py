from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# from products.views import (
#     ProductListView,
#     product_list_view,
#     ProductDetailView,
#     ProductDetailSlugView,
#     product_detail_view,
#     ProductFeaturedListView,
#     ProductFeaturedDetailView,
#     )

from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('products/', include("products.urls", namespace='products')),
    path('search/', include("search.urls", namespace='search')),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<pk>/', ProductFeaturedDetailView.as_view()),
    # path('products/', ProductListView.as_view()),
    # path('products-fbv/', product_list_view),
    # # path('products/<pk>/', ProductDetailView.as_view()),
    # path('products/<slug>/', ProductDetailSlugView.as_view()),
    # path('products-fbv/<pk>/', product_detail_view),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
