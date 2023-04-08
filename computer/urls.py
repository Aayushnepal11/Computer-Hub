from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "computer_hub"

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('product/<str:pk>', views.ProuctSpecification.as_view(), name="spec"),
    path('view_product_orders/<str:id>', views.ViewOrderPage.as_view(), name="view_orders"),
    path('update_product_orders/<str:pk>', views.OrderUpdateView.as_view(), name="update_orders"),
    path('create_orders/', views.DataCreateView.as_view(), name="create_spec"),
] 

if settings.DEBUG:
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

