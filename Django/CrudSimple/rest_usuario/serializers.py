from rest_framework import serializers
from Blog.models import Blog
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['BlogId','Title','Author_Name','Start_Date','End_Date']
        