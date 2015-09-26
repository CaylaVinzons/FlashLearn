from django.db import models

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
