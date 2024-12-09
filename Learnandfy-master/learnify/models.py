from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    urldata = models.URLField(max_length=255,null=True,blank=True)
    title = models.CharField(max_length=100)

    @property
    def reply_count(self):
        return Comment.objects.filter(post_sno=self).count()

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post_sno = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.post_sno)

class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    post_sno = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.like_id)

class Events(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    description=models.TextField()
    lastdate=models.DateField(auto_now_add=False)
    url=models.URLField(max_length=255)
    image=models.URLField(null=True,blank=True)
    ENUM_CHOICES = (
        (1, 'Our Innitiative'),
        (2, 'Community Hackathons'),
    )
    tag = models.IntegerField(choices=ENUM_CHOICES)

    def __str__(self):
        return self.name

class Profile(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    sno=models.ForeignKey(User,on_delete=models.CASCADE)
    phoneno=models.BigIntegerField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    ENUM_CHOICES = (
        (1, 'Student'),
        (2, 'Professional'),
    )
    status = models.IntegerField(choices=ENUM_CHOICES,default=1)
    link=models.URLField(max_length=250)

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Student(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    institution=models.CharField(max_length=250)
    currentyear=models.IntegerField()
    fieldofinterest=models.CharField(max_length=250)
    degree=models.CharField(max_length=250)

    def __str__(self):
        return str(self.user)


class Professional(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    organization=models.CharField(max_length=250)
    experience_year=models.IntegerField()
    designation=models.CharField(max_length=250)

    def __str__(self):
        return self.user
    
class Project(models.Model):
    sno=models.AutoField(primary_key=True)
    projectname=models.CharField(max_length=150)
    description=models.TextField()
    leader=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.projectname} by {self.leader}"

class Folder(models.Model):
    projectno = models.ForeignKey(Project, on_delete=models.CASCADE)
    sno = models.IntegerField(primary_key=True)
    foldername = models.CharField(max_length=50, null=True)
    file = models.FileField(null=True)

    def __str__(self):
        return f"{self.projectno} {self.foldername}"

class Collaboration(models.Model):
    projectno = models.ForeignKey(Project,on_delete=models.CASCADE)
    friend = models.ForeignKey(User, on_delete=models.CASCADE)
    ENUM_CHOICES = (
        (True, 'Accept'),
        (False, 'Decline'),
    )
    status = models.BooleanField(choices=ENUM_CHOICES,default=False)

    def __str__(self):
        return f"{self.projectno} {self.friend}"


