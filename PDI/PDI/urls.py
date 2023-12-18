
from django.contrib import admin
from django.urls import path
from app_PDI import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),

    # rota, view responsável, nomde de rederència

    path("",views.home,name='home'), #local main
    
    path("vendas/",views.vendas,name='vendas_produtos'), #local vendas


    path("estoque/",views.estoque,name='estoque'), #ver estoque

    path("estoque/cadrasto/",views.push_estoque,name='cadrasto_estoque'), #cadrastar produto no estoque

    path("estoque/home",views.estoque_home,name="estoque_home"),

    path("rh/cadrasto",  views.codrasto_funcionarios, name='cadrasto_funcionarios'),

    path('finalizar_compra/', views.finalizar_compra, name='finalizar_compra'),



    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)