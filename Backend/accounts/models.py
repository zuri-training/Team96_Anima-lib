from django.db import models
  
class Profile (models.Model):
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_img')
    def __str__(self):
        return str(self.profile_pic)

        # To use this in the template you are going to use this in the <img src='{{ user.profile.image.url }}'

class User (models.Model):
    full_name = models.CharField(max_length = 300, null = True)
    email = models.EmailField(max_length = 300, null = True)
    bio = models.CharField(max_length = 500, null = True)
    image = models.OneToOneField(Profile, on_delete=models.CASCADE)
    
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name


class Message (models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(max_length = 300, null = True)
    image = models.OneToOneField(Profile, on_delete=models.CASCADE)

    @property
    def profile_pic(self):
        return self.image.profile_pic

    def __str__(self):
        return str(self.title)

    date_added = models.DateTimeField(auto_now_add=True, null=True)


class My_Lib (models.Model):
    mylib_name = models.CharField(max_length = 300, null = True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    # anima_type = 
    def __str__(self):
        return str(self.mylib_name)


class Lib (models.Model):
    anima_name = models.CharField(max_length=300, primary_key=True)
    anima_type = models.CharField(max_length=300, null = True)
    anima_desc = models.TextField(max_length=500, null = True)
    
    def __str__(self):
        return str(self.anima_name)