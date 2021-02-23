from django.db import models
from app.model.base import Base

class Assets(Base):
    file_name = models.FileField(upload_to='uploaded', null=True, blank=True)
    sizes = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'assets'
