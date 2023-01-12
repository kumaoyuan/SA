from rest_framework import serializers
from .models import member

class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model=member
        fields=['id','memberAc','memberPw','memberName']