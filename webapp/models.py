from django.db import models

class course(models.Model):
    Chapter=models.CharField(max_length=20)
    Subject=models.CharField(max_length=20)
    Class=models.CharField(max_length=20)
    Logo=models.CharField(max_length=1000)
    Total=models.IntegerField()
    Serial_number=models.IntegerField()

    def __str__(self):
        return self.Subject + ' - ' + self.Chapter


    
    
    
    
