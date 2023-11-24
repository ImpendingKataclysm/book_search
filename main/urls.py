from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'book_search'

urlpatterns = [
    path('', views.SearchPage.as_view(), name='search'),
    path('results/', views.ResultsPage.as_view(), name='results'),
    path('detail/<str:id>/', views.BookDetailPage.as_view(), name='detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
