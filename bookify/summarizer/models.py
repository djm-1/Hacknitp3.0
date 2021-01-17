from django.db import models

# Create your models here.
class Bookify(models.Model):
    input_file=models.FileField(upload_to='pdf',null=True)
    output_file=models.FileField(upload_to='audio',null=True)
    def __str__(self):
        return str(self.id)