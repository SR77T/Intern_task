from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    def __str__(self):
        return self.name

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'role')


class Article(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'articles')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title



# class ClassRoom(models.Model):
#     name = models.CharField(max_length=20)


#     def __str__(self):
#         return self.name

# class Student(models.Model): 
#     classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, null=True, blank=True, related_name="students")
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()
#     email = models.EmailField(max_length = 20)
#     address = models.CharField(max_length = 50)

#     def __str__(self):
#         return f"Student {self.name}"