from rest_framework import viewsets, generics
from school.models import Student, Course, Enrollment
from school.serializer import StudentSerializer, StudentSerializerV2, CourseSerializer, EnrollmentSerializer, ListEnrollmentStudentSerializer, ListStudentsEnrollmentSerializer
from rest_framework import status
from rest_framework.response import Response

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
    
    def create(self, request):
        """self-documenting protocol"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response

class EnrollmentsViewSet(viewsets.ModelViewSet):
    """displaying all enrollment"""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    #http_method_names =['get', 'post', 'put', 'path', 'delete']

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
