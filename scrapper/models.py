from django.db import models

class Page_Data(models.Model):
    scraped_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


