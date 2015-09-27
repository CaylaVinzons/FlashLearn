from django.db import models
from django.conf import settings

class Card(models.Model):
    front_data = models.TextField()
    back_data = models.TextField()
    def __str__(self):
        return self.front_data

class Document(models.Model):
    document_name = models.CharField(max_length = 100)
    document_data = models.TextField()
    def __str__(self):
        return self.document_name

class Scan(models.Model):
    scan_data = models.ImageField(upload_to="flashcards/static/scans/")

class UserDocument(models.Model):
    user_id = models.CharField(max_length = 10)
    document = models.ForeignKey(Document)
    def __str__(self):
        return "user_id: " + self.user_id + " document: " + str(self.document)

class DocumentCard(models.Model):
    document = models.ForeignKey(Document)
    card = models.ForeignKey(Card)
    def __str__(self):
        return "document: " + str(self.document) + " card: " + str(self.card)
