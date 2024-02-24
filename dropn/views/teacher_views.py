from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializers import TeacherSerializer

@api_view(['GET', 'POST'])
def teacher_list(request):
    """
    Retrieve a list of all teachers or create a new teacher.
    """
    if request.method == 'GET':
        teachers = User.objects.filter(is_teacher=True)
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        data['is_teacher'] = True
        if not data['is_student']:
            data['is_student'] = False
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def teacher_detail(request, pk):
    """
    Retrieve or delete a teacher by PK.
    """
    try:
        teacher = User.objects.filter(is_teacher=True).get(pk=pk)
    except User.objects.filter(is_teacher=True).DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
