
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User 
        fields = ['id',"_id",'username','name', 'email',"isAdmin"]

    def get_name(self,obj):
        name= obj.first_name
        if name == "":
            name = obj.email
        return name

    def get__id(self,obj):
        return obj.id
    
    def get_isAdmin(self,obj):
        return obj.is_staff

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username','email',"isAdmin",'name', 'token']

    def get_token(self, obj):
        token =RefreshToken.for_user(obj)
        return str(token.access_token)

#blog serializer
class BlogSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Blog
        fields ="__all__"

    def get_reviews(self,obj):
        reviews= obj.reviewblog_set.all()
        serializer = ReviewBlogSerializer(reviews, many=True)
        return serializer.data


class ReviewBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewBlog
        fields = "__all__"


class AgricProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= AgricProduct
        fields ="__all__"

    def get_reviews(self,obj):
        reviews= obj.review_set.all()
        serializer = ReviewAgricSerializer(reviews, many=True)
        return serializer.data

class ReviewAgricSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewAgric
        fields = "__all__"


class NaturalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= NaturalProduct
        fields ="__all__"
    def get_reviews(self,obj):
        reviews= obj.review_set.all()
        serializer = ReviewNaturalSerializer(reviews, many=True)
        return serializer.data

class ReviewNaturalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewNatural
        fields = "__all__"


class InformationTechProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= InformationTechProduct
        fields ="__all__"
    def get_reviews(self,obj):
        reviews= obj.review_set.all()
        serializer = ReviewInformationTechSerializer(reviews, many=True)
        return serializer.data

class ReviewInformationTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewIct
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = "__all__"

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta :
        model = ShippingAddress
        fields = '__all__'