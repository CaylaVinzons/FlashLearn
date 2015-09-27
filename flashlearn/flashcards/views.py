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
    if request.method == 'POST':
        form = DocumentEditForm(request.POST)
        if form.is_valid():
            try:
                document = Document.objects.get(pk=document_id)
            except Document.DoesNotExist:
                raise Http404("Document doesn't exist")
            d_name = request.POST['document_name']
            d_data = request.POST['document_data']
            edited_document = Document.objects.create(document_name=d_name, document_data=d_data)
            document = edited_document
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
