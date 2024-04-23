from rest_framework.test import APITestCase
from school.models import Course
from django.urls import reverse
from rest_framework import status

class CourseTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Courses-list')
        self.course_1 = Course.objects.create(
            code_course='CTT1', description='Course test1', level='B'
        )
        self.course_2 = Course.objects.create(
            code_course='CTT2', description='Course test2', level='A'
        )

    def test_request_get_to_list_courses(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_post_to_create_courses(self):
        data ={
            'code_course':'CTT3',
            'description':'Course test 3',
            'level':'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_to_delete_course(self):
        """test to verify that the DELETE request does NOT allow to delete a course"""
        response = self.client.delete('/Courses/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_request_put_to_update_course(self):
        data = {
            'code_course':'CTT1',
            'description':'New course test2',
            'level':'I'
        }
        response = self.client.put('/Courses/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)