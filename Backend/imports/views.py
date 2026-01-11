# imports/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ExcelUploadSerializer
from .excel_import import import_scores_from_excel
from core.permissions import IsAdmin

class ExcelImportView(APIView):
    """
    Allows admin to import scores via Excel.
    """
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        serializer = ExcelUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = import_scores_from_excel(serializer.validated_data['file'])

        return Response({
            "message": "Import completed",
            "created_records": result["created"],
            "errors": result["errors"]
        })
