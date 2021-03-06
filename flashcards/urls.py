from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^flashlearn/$', views.flashlearn, name='flashlearn'),
    url(r'^card/(?P<card_id>[0-9]+)/edit/$', views.edit_card, name='edit_card'),
    url(r'^card/add/$', views.add_card, name='add_card'),
    url(r'^card/(?P<card_id>[0-9]+)/delete/$', views.delete_card, name='delete_card'),
    url(r'^document/(?P<document_id>[0-9]+)/$', views.view_document, name='view_document'),
    url(r'^document/(?P<document_id>[0-9]+)/edit/$', views.edit_document, name='edit_document'),
    url(r'^scan/upload/$', views.upload_scan, name="upload_scan"),
    url(r'^library/$', views.view_library, name="view_library"),
    url(r'^login/$', views.login, name="login"),
]
