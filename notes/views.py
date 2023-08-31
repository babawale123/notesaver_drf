from django.shortcuts import render
from .serializer import NoteSerializer
from .models import Note

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework import permissions, authentication

class AddAndGetNote(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self,request):
        notes = Note.objects.filter(user=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

class DetailsView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_wale(self, pk):
        try:
            return Note.objects.get(pk=pk, user = self.request.user)
        except Note.DoesNotExist:
            return None
       
    
    def get(self, request, pk):
        note = self.get_wale(pk)
        if note:
            serializer = NoteSerializer(note)
            return Response(serializer.data)
        return Response({"error": "Note not found"}, status=404)
    
    

    def put(self,request,pk):
        note = self.get_wale(pk)
        if note:
            serializer = NoteSerializer(note,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({"error":"Can not update note as note could not be found"})

    def delete(self, request,pk):
        
        note = self.get_wale(pk)
        if note:
            note.delete()
            return Response({"Note has bee deleted successfully"})
        return Response({"error":"Can not delete note as note could not be found"})
