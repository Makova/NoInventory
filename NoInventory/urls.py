from django.conf.urls import patterns, url
from NoInventory import views
from NoInventory.views import *

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^catalogos$', views.catalogos, name='catalogos'),
        url(r'^catalogo/(?P<id_catalogo>[\w\-]+)/$', views.catalogo, name='catalogo'),
        url(r'^addToCatalogo2/(?P<id_catalogo>[\w\-]+)/(?P<id_item>[\w\-]+)/$', views.addToCatalogo, name='addToCatalogo'),
        url(r'^addToCatalogo/$', views.addToCatalogo, name='addToCatalogo'),
        url(r'^addSearchToCatalogo/$', views.addSearchToCatalogo, name='addSearchToCatalogo'),
        url(r'^alertaCatalogo/$', views.alertaCatalogo, name='alertaCatalogo'),
        url(r'^catalogoToInforme/$', views.catalogoToInforme, name='catalogoToInforme'),
        url(r'^updateCatalogo/$', views.updateCatalogo, name='updateCatalogo'),
        url(r'^cleanCatalogo/$', views.cleanCatalogo, name='cleanCatalogo'),
        url(r'^borrarCatalogo/$', views.borrarCatalogo, name='borrarCatalogo'),
        url(r'^busquedaCatalogo/$', views.busquedaCatalogo, name='busquedaCatalogo'),
        url(r'^items$', views.items, name='items'),
        url(r'^item/(?P<id_item>[\w\-]+)/$', views.item, name='item'),
        url(r'^itemAndroid/(?P<id_item>[\w\-]+)/$', views.itemAndroid, name='itemAndroid'),
        url(r'^dataGraficos/$', views.dataGraficos, name='dataGraficos'),
        url(r'^datosTag1/$', views.datosTag1, name='datosTag1'),
        url(r'^datosTag2/$', views.datosTag2, name='datosTag2'),
        url(r'^datosTag3/$', views.datosTag3, name='datosTag3'),
        url(r'^graficos/$', views.graficos, name='graficos'),
        url(r'^informes/$', views.informes, name='informes'),
        url(r'^guardarInforme/$', views.guardarInforme, name='guardarInforme'),
        url(r'^visualizarInforme/$', views.visualizarInforme, name='visualizarInforme'),
        url(r'^borrarInforme/$', views.borrarInforme, name='borrarInforme'),
        url(r'^generaPDFCatalogoQRs/$', views.generaPDFCatalogoQRs, name='generaPDFCatalogoQRs'),
        url(r'^generaPDFCatalogoCodigosBarras/$', views.generaPDFCatalogoCodigosBarras, name='generaPDFCatalogoCodigosBarras'),
        url(r'^generaPDF/$', views.generaPDF, name='generaPDF'),
        url(r'^busqueda/$', views.busqueda, name='busqueda'),
        url(r'^prueba$', views.prueba, name='prueba'),
        #url(r'^nuevoItem/$', views.nuevoItem, name='nuevoItem'),
        #url(r'^nuevoCatalogo/$', views.nuevoCatalogo, name='nuevoCatalogo'),
        #url(r'^borrarItem/(?P<id_item>[\w\-]+)/$', views.borrarItem, name='borrarItem'),
        url(r'^borrarItem/$', views.borrarItem,name='borrarItem'),
        url(r'^borrarItems/$', views.borrarItems,name='borrarItems'),
        url(r'^borrarItemFromCatalogo/$', views.borrarItemFromCatalogo,name='borrarItemFromCatalogo'),
        (r'^nuevoItem/$', ItemCreator.as_view()),
        (r'^modificarItem/(?P<id_item>[\w\-]+)/$',ItemUpdater.as_view()),
        (r'^nuevoCatalogo/$', CatalogoCreator.as_view()),
        (r'^modificarCatalogo/(?P<id_catalogo>[\w\-]+)/$',CatalogoUpdater.as_view()),
        (r'^preferencias/$',Preferencias.as_view()),
        #url(r'^preferencias/$',views.preferencias,name='preferencias'),
        url(r'^catalogosJson/$',views.catalogosJson,name='catalogosJson'),
        url(r'^itemsJson/$',views.itemsJson,name='itemsJson'),
        url(r'^detectarItemJson/$',views.detectarItemJson,name='detectarItemJson'),
        url(r'^itemJson/$',views.itemJson,name='itemJson'),
        url(r'^deleteItems/$',views.deleteItems,name='deleteItems'),
        url(r'^deleteInventorys/$',views.deleteInventorys,name='deleteInventorys'),
        url(r'^deleteInformes/$',views.deleteInformes,name='deleteInformes'),
        url(r'^addItemFromQr/$',views.addItemFromQr,name='addItemFromQr'),
        url(r'^addItemFromNFC/$',views.addItemFromNFC,name='addItemFromNFC'),
        url(r'^borrarItemAndroid/$', views.borrarItemAndroid,name='borrarItemAndroid'),
        url(r'^addItemAndroid/$', views.addItemAndroid,name='addItemAndroid'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^androidLogin/$', views.androidLogin, name='androidLogin'),
        url(r'^androidRegister/$', views.androidRegister, name='androidRegister'),


        )
