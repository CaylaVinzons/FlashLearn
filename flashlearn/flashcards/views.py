from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("You are at the flashcards page.")

def view_card(request, card_id):
    return HttpResponse("You are viewing card %s." % card_id)

def view_document(request, document_id):
    return HttpResponse("You are viewing document %s." % document_id)

def edit_card(request, card_id):
    return HttpResponse("You are editing card %s." % card_id)

def edit_document(request, document_id):
    return HttpResponse("You are editing document %s." % card_id)
