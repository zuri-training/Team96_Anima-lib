from django.db import models
from django.contrib.auth.models import User
  
# class Profile (models.Model):
#     profile_pic = models.ImageField(default='default.jpg', upload_to='profile_img')
#     def __str__(self):
#         return str(self.profile_pic)

#         # To use this in the template you are going to use this in the <img src='{{ user.profile.image.url }}'

# class User (models.Model):
#     full_name = models.CharField(max_length = 300, null = True)
#     email = models.EmailField(max_length = 300, null = True)
#     bio = models.CharField(max_length = 500, null = True)
#     image = models.OneToOneField(Profile, on_delete=models.CASCADE)
    
#     date_added = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return self.full_name


# class Message (models.Model):
#     title = models.CharField(max_length=200, null=True)
#     content = models.TextField(max_length = 300, null = True)
#     image = models.OneToOneField(Profile, on_delete=models.CASCADE)

#     @property
#     def profile_pic(self):
#         return self.image.profile_pic

#     def __str__(self):
#         return str(self.title)

#     date_added = models.DateTimeField(auto_now_add=True, null=True)


# class My_Lib (models.Model):
#     mylib_name = models.CharField(max_length = 300, null = True)
#     date_added = models.DateTimeField(auto_now_add=True, null=True)
#     # anima_type = 
#     def __str__(self):
#         return str(self.mylib_name)


# class Lib (models.Model):
#     anima_name = models.CharField(max_length=300, primary_key=True)
#     anima_type = models.CharField(max_length=300, null = True)
#     anima_desc = models.TextField(max_length=500, null = True)
    
#     def __str__(self):
#         return str(self.anima_name)



# There is no need to create a new user model, we will use Django default user model to make things easy.

class Lib(models.Model):
    anima_name = models.CharField(max_length=300, primary_key=True)
    anima_type = models.CharField(max_length=300)
    anima_desc = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.anima_name


class MyLib(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animation = models.ForeignKey(Lib, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    liked = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)
    downloaded = models.BooleanField(default=False)

    def __str__(self):
        return (self.user, self.animation)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(max_length=500, null=True)   
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

   

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to = 'profile_pictures')
    bio = models.CharField(max_length = 200, null=True)
    
    def __str__(self):
        return self.user.username    
                     