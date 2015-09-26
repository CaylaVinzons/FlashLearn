from django.http import Http404
from django.shortcuts import render

from .models import *

from django.http import HttpResponse

def index(request):
    return HttpResponse("You are at the flashcards page.")

def view_card(request, card_id):
    try:
        card = Card.objects.get(pk=card_id)
    except Card.DoesNotExist:
        raise Http404("Card doesn't exist")
    return render(request, "flashcards/card.html", {'card': card})

def view_document(request, document_id):
    try:
        document = Document.objects.get(pk=document_id)
    except Document.DoesNotExist:
        raise Http404("Document doesn't exist")
    return render(request, "flashcards/document.html", {'document': document})

def edit_card(request, card_id):
    return HttpResponse("You are editing card %s." % card_id)

def edit_document(request, document_id):
    return HttpResponse("You are editing document %s." % card_id)
