from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Diagnosis, Prediction
from .serializers import DiagnosisSerializer
import os

# Create your views here.

class DiagnosisViewSet(viewsets.ModelViewSet):
    serializer_class = DiagnosisSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        # Only return diagnoses for the current user
        return Diagnosis.objects.filter(patient=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Save the diagnosis
            diagnosis = serializer.save()
            
            # Here you would normally call your AI model
            # For now, we'll return dummy predictions
            sample_predictions = [
                {'condition': 'Eczema', 'probability': 0.8},
                {'condition': 'Psoriasis', 'probability': 0.15},
                {'condition': 'Dermatitis', 'probability': 0.05}
            ]
            
            # Save the predictions
            for pred in sample_predictions:
                Prediction.objects.create(
                    diagnosis=diagnosis,
                    condition=pred['condition'],
                    probability=pred['probability']
                )
            
            # Return the diagnosis with predictions
            return Response(
                self.get_serializer(diagnosis).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Delete the image file
        if instance.image:
            if os.path.isfile(instance.image.path):
                os.remove(instance.image.path)
        return super().destroy(request, *args, **kwargs)
