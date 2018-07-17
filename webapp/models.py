from django.db import models

class block(models.Model):
    block_id = models.CharField(max_length=20, primary_key=True)
    Type = models.CharField(max_length=15, null=True)
    ID = models.CharField(max_length=30, null=True)
    descendants = models.CharField(max_length=250, null=True)
    #Serial_number=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')

    
    def __str__(self):
        return self.ID
    
    
