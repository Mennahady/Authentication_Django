from rest_framework import serializers
from .models import Diagnosis, Prediction

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['condition', 'probability']

class DiagnosisSerializer(serializers.ModelSerializer):
    predictions = PredictionSerializer(many=True, read_only=True)
    image = serializers.ImageField(required=True)

    class Meta:
        model = Diagnosis
        fields = ['id', 'image', 'created_at', 'predictions']
        read_only_fields = ['created_at', 'predictions']

    def create(self, validated_data):
        # Get the current user from the context
        user = self.context['request'].user
        validated_data['patient'] = user
        return super().create(validated_data) 