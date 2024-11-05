from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, cadastro, usuarios, cadastro_reparo, lista_reparos


urlpatterns = [
    # rota, view responsável, nome de referência
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('usuarios/', usuarios, name='listagem_usuarios'),
    path('cadastro-reparo/', cadastro_reparo, name='cadastro_reparo'),
    path('lista-reparos/', lista_reparos, name='lista_reparos'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)