from rest_framework import viewsets, permissions
from . import serializers
from . import models


class smsonattenteViewSet(viewsets.ModelViewSet):
    """ViewSet for the smsonattente class"""

    queryset = models.smsonattente.objects.all()
    serializer_class = serializers.smsonattenteSerializer
    permission_classes = [permissions.IsAuthenticated]

class sys_paramtViewSet(viewsets.ModelViewSet):
    """ViewSet for the sys_paramt class"""

    queryset = models.sys_paramt.objects.all()
    serializer_class = serializers.sys_paramtSerializer
    # permission_classes = [permissions.IsAuthenticated]


class smstosendViewSet(viewsets.ModelViewSet):
    """ViewSet for the smstosend class"""

    queryset = models.smstosend.objects.all()
    serializer_class = serializers.smstosendSerializer
    # permission_classes = [permissions.IsAuthenticated]
