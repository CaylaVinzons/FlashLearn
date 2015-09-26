from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<card_id>[0-9]+)/$', views.view_card, name='view_card'),
    url(r'^(?P<card_id>[0-9]+)/edit/$', views.edit_card, name='edit_card'),
    url(r'^(?P<document_id>[0-9]+)/$', views.view_document, name='view_document'),
    url(r'^(?P<document_id>[0-9]+)/edit/$', views.edit_document, name='edit_document'),
]
