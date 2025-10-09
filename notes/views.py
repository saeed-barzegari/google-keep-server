from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from notes.models import Note
from notes.serializers import NoteSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user, is_deleted=False).all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

