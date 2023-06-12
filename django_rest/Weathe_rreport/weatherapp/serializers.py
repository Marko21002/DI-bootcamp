from rest_framework import serializers
from .models import Report,Forecaster
from rest_framework.serializers import HyperlinkedRelatedField

class ReportSerializer(serializers.ModelSerializer):
    forecaster = HyperlinkedRelatedField(view_name='forecaster', read_only=True)

    class Meta:
        model = Report
        fields = '__all__'
        
class ForecasterSerializer(serializers.ModelSerializer):
     class Meta:
        model = Forecaster
        fields = '__all__'