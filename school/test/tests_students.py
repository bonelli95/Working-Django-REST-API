from rest_framework.test import APITestCase
from school.models import Student
from django.urls import reverse
from rest_framework import status

class StudentTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Students-list')
        self.student_1 = Student.objects.create(
            name='student test 1', pin='123456789', tin='987654321', date_birth='2000-10-21', photo=''
        )
        self.student_2 = Student.objects.create(
            name='student test 2', pin='0123456789', tin='0987654321', date_birth='2003-08-15', photo=''
        )

    def test_request_get_to_list_students(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_post_to_create_students(self):
        data = {
            'name':'student test 3',
            'pin':'126324789',
            'tin':'598754321',
            'date_birth':'2000-04-04',
            'photo':''
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_request_delete_to_delete_student(self):
        response = self.client.delete('/students/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_request_put_to_update_student(self):
        data = {
            'name':'student test 1',
            'pin':'165498789',
            'tin':'593215921',
            'date_birth':'1999-02-21',
            'photo':''
        }

        response = self.client.put('/students/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        