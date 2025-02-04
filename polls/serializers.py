# queryset to json

from rest_framework import serializers
from .models import  Questions

class QuestionsSerializer(serializers.ModelSerializer):
    # Meta class me bataya gaya hai ki Question model ka data serialize hoga.
    class Meta:
        model=Questions
        # fields me bataya gaya hai ki kaunse fields JSON response me dikhne chahiye.
        fields=['id','question_text','pub_date']