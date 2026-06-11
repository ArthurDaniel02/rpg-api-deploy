from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

def api_root(request):
    return JsonResponse({"message": "Bem-vindo à API RPG!", "rotas": "/api/conta/, /api/aluno/, etc."})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root), # 
    path('api/', include('api.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]