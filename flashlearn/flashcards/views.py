from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect

from .models import *
from .forms import *

from django.http import HttpResponse

def loggedin(request):
    return request.user and (not request.user.is_anonymous or request.user.pk is not None)

def index(request):
    if loggedin(request):
        return redirect("flashcards:flashlearn")
    else:
        return render(request, "flashcards/index.html")

def flashlearn(request):
    form = ScanUploadForm()
    return render(request, "flashcards/flashlearn.html", {'form': form, 'request': request, 'user': request.user})

def login(request):
    return render(request, "flashcards/login.html")

def view_document(request, document_id):
    form = DocumentEditForm()
    try:
        document = Document.objects.get(pk=document_id)
    except Document.DoesNotExist:
        raise Http404("Document doesn't exist")
    document_cards = DocumentCard.objects.all().filter(document=document)
    return render(request, "flashcards/document.html", {'document': document, 'card_deck': document_cards, 'form': form})

def add_card(request):
    if request.method == 'POST':
        form = CardEditForm(request.POST)
        if form.is_valid():
            c_document = request.POST['card_document']
            c_front = request.POST['front_data']
            c_back = request.POST['back_data']
            card = Card(front_data=c_front, back_data=c_back)
            card.save()
            card_document = DocumentCard(card=card, document=Document.objects.get(pk=c_document))
            card_document.save()
            return redirect("flashcards:view_document", document_id=card_document.document.pk)

def edit_card(request, card_id):
    if request.method == 'POST':
        form = CardEditForm(request.POST)
        if form.is_valid():
            try:
                card = Card.objects.get(pk=card_id)
            except Card.DoesNotExist:
                raise Http404("Card doesn't exist")
            c_front = request.POST['front_data']
            c_back = request.POST['back_data']
            card.front_data = c_front
            card.back_data = c_back
            card.save()
            card_document = DocumentCard.objects.get(card=card)
            return redirect("flashcards:view_document", document_id=card_document.document.pk)

def delete_card(request, card_id):
    card = Card.objects.get(pk=card_id)
    DocumentCard.objects.filter(card=card).delete()
    card.delete()
    if request.method == 'POST':
        card_document_id = request.POST['document_id']
        return redirect("flashcards:view_document", document_id=card_document_id)
    else:
        return redirect("flashcards:view_library")

def edit_document(request, document_id):
    if request.method == 'POST':
        try:
            document = Document.objects.get(pk=document_id)
        except Document.DoesNotExist:
            raise Http404("Document doesn't exist")
        d_name = request.POST['document_name']
        d_data = request.POST['document_data']
        document.document_name = d_name
        document.document_data = d_data
        document.save()
        return redirect("flashcards:view_document", document_id=document_id)

def view_library(request):
    if loggedin(request):
        user_docs = UserDocument.objects.all().filter(user_id=request.user.pk)
        return render(request, "flashcards/library.html", {'userlibrary': user_docs})
    else:
        return redirect("flashcards:index")

def upload_scan(request):
    if request.method == 'POST':
        form = ScanUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_scan = form.save(commit=False)
            new_scan.scan_data = request.FILES['scan_data']
            new_scan.save()

        return redirect("flashcards:view_library")
