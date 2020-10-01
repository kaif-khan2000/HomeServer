from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
# Create your models here.
class Directory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("Directory",on_delete=models.CASCADE,null=True)
    path = models.CharField(max_length=500,default='/')

    def __str__(self):
        return self.name

class File(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    typeOfFile = models.CharField(max_length = 5)
    parent = models.ForeignKey(Directory,on_delete=models.CASCADE)
    size = models.CharField(max_length = 20)
    actual_file = models.FileField(upload_to='static/content')
    uploaded_on = models.DateField(auto_now=True)
    def __str__(self):
        return self.name + str(self.id)


@receiver(pre_delete, sender=File)
def File_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.actual_file.delete(False)
