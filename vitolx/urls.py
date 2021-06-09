from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from vitolx.health import HealthView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HealthView.as_view()),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/product/', include('product.urls')),
    path('api/v1/chat/', include('chat.urls')),
    path('api/v1/exchange/', include('exchange.urls')),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
