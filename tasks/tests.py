from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskTest(TestCase): #setup genera la instancia que se usara para el test
    def setUp(self):
        Task.objects.create(title= 'Test task', description= 'This is the description use for test')

    def test_task_list_view(self):
        response = self.client.get(reverse('task-list'))
#client simula una peticion http, en este caso simula una peticion get
#en la funcion reverse debemos indicar en que url se ubica la view a testear
#en response se almacena la respuesta de la url  
        self.assertEqual(response.status_code, 200) 
#assert es el test. Equal tira test superado en caso de q coincidan las dos promesas indicadas
        self.assertContains(response, 'Test task')
