from rest_framework import serializers
from ..models import User


#by serializing on certain fields per User role, only relevant fields will show up on the front end
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']