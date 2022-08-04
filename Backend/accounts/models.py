from django.db import models
import uuid

# Create your models here.

# def user_directory_path(instance, filename):
  
#     # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)

# The reason for this function is that incase we have created a file_path in our settings.py file and we want to 
# store each image unique using filename into that file path we created. Then we are going to add the below line 
# of code to the user model. If it's something we want to use we can add. Though I've not done much research on it
# That's not a problem I can research more.

#     profile_pic = models.ImageField(upload_to = user_directory_path)
  


class User (models.Model):
    user_id = models.UUIDField(max_length=255, default = uuid.uuid4, primary_key=True)
    full_name = models.CharField(max_length = 300, null = True)
    email = models.EmailField(max_length = 300, null = True)
    bio = models.CharField(max_length = 500, null = True)
    profile_pic = models.ImageField(Blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name


class Message (models.Model):
    msg_id = models.UUIDField(max_length=255, default = uuid.uuid4, primary_key=True)
    content = models.CharField(max_length = 300, null = True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    
