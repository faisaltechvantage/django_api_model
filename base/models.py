from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True, null=False, blank= False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email
    
class Claim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length= 256)
    claim_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateField(auto_now= True)

    class Meta:
        db_table = 'claim_data'

    def __str__(self):
        return f"Claim for {self.user.name}"