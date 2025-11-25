from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.permissions import IsOwner
from notes.models import Note
from notes.serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user).order_by('-created_at').all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        note = self.get_object()
        if note.is_deleted:
            self.perform_destroy(note)
            return Response(status=status.HTTP_204_NO_CONTENT)
        note.is_deleted = True
        note.save()
        return Response(status=status.HTTP_200_OK)

