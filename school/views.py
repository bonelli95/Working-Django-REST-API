from rest_framework import viewsets, generics
from school.models import Student, Course, Enrollment
from school.serializer import StudentSerializer, StudentSerializerV2, CourseSerializer, EnrollmentSerializer, ListEnrollmentStudentSerializer, ListStudentsEnrollmentSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    """displaying all students"""
    queryset = Student.objects.all()
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        else:
            return StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    """displaying all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentsViewSet(viewsets.ModelViewSet):
    """displaying all enrollment"""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class ListEnrollmentStudent(generics.ListAPIView):
    """displaying all students enrollment"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListEnrollmentStudentSerializer

class ListStudentsEnrollment(generics.ListAPIView):
    """listing students enrolled in a course"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentsEnrollmentSerializer
