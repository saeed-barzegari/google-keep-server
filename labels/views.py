from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsOwner
from labels.models import Label
from labels.serializers import LabelSerializer

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        return Label.objects.filter(owner=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
