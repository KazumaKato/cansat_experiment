from django.db import models
import uuid

class CapturedImage(models.Model):
    image = models.ImageField(upload_to='images')
    distance = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.created_at)
