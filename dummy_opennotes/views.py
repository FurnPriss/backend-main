from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from dummy_opennotes.models import DummyOpenNotes
from dummy_opennotes.serializers import DummyOpenNotesSerializer

class DummyOpenNotesList(APIView):
    serializer_class = DummyOpenNotesSerializer
    """
    List all notes, or create a new notes
    """
    def get(self, request, format=None):
        notes = DummyOpenNotes.objects.all()
        serializer = DummyOpenNotesSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DummyOpenNotesSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DummyOpenNotesDetail(APIView):
    serializer_class = DummyOpenNotesSerializer
    """
    Retrieve, update, or delete a note.
    """
    def get_object(self, pk):
        try:
            return DummyOpenNotes.objects.get(pk=pk)
        except DummyOpenNotes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = DummyOpenNotesSerializer(note)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = DummyOpenNotesSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
