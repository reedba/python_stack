from django.db import models



class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['title'])< 2:
            errors['title'] = 'Title must be atleast 2 characters'
        if len(postData['network'])< 3:
            errors['network'] = 'Network must be atleast 3 characters'
        if len(postData['description'])< 10 or len(postData['description']) == 0:
            errors['description'] = 'Description must be atleast 10 characters'
        if Shows.objects.filter(name=postData['title']):
            errors['title'] = 'Title already exists'
        
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()



