from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CoursesViewSet, EnrollmentsViewSet, ListEnrollmentStudent, ListStudentsEnrollment
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('Courses', CoursesViewSet, basename='Courses')
router.register('enrollment', EnrollmentsViewSet, basename='Enrollment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/enrollment/', ListEnrollmentStudent.as_view()),
    path('courses/<int:pk>/enrollment/', ListStudentsEnrollment.as_view()),
]
