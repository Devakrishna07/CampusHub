# imports/serializers.py
from rest_framework import serializers

class ExcelUploadSerializer(serializers.Serializer):
    """
    Serializer for validating Excel file uploads.
    """
    file = serializers.FileField()

    def validate_file(self, file):
        if not file.name.endswith('.xlsx'):
            raise serializers.ValidationError("Only .xlsx files are supported.")
        return file
