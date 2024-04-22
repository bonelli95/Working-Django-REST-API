from rest_framework import serializers
from school.models import Student, Course, Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'pin', 'tin', 'date_birth', 'photo']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        exclude = []

class ListEnrollmentStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()
    
class ListStudentsEnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Enrollment
        fields = ['student_name']

class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'cell', 'pin', 'tin', 'date_birth', 'photo']