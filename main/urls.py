from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'book_search'

urlpatterns = [
    path('', views.SearchPage.as_view(), name='search'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
