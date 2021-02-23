from django.db import models
from app.model.base import Base

class Contact(Base):
    name = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField()
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'contact'
        
    def __str__(self):
        return str(self.name)