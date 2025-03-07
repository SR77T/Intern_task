from rest_framework import serializers
from .models import  Article
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "username", "email", "password",]

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],

        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True, write_only = True)


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)
    class Meta:
        model = Article
        fields = ["id", "title", "content", "author", "created_at", "updated_at"]

        













        



# class ClassRoomSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(max_length=100)

# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     email = serializers.EmailField()
#     address = serializers.CharField(max_length=100)

# class ClassRoomModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClassRoom
#         fields = ["id", "name"]

# class StudentModelSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Student
#         fields = [ "id", "name", "age", "address", "email", "classroom"]

#     def get_fields(self):
#         fields = super().get_fields()
#         request = self.context.get("request")
#         if request and request.method == "GET":
#             fields["classroom"] = ClassRoomModelSerializer()
#         return fields