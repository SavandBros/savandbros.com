from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.test import SimpleTestCase
from django.urls import reverse


class TestGrantFormProcessor(SimpleTestCase):
    """Unit testing Grant Form Processor."""
    allow_database_queries = True

    def test_send_application(self):
        view_path: str = reverse('planet:process_grant_application')

        resp: HttpResponse = self.client.post(view_path, data={
            'name': 'Alireza',
            'cio_email': 'my@email.com',
            'title': 'something'
        })

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(len(mail.outbox), 1)
        grant_mail: EmailMultiAlternatives = mail.outbox[0]

        self.assertEqual(grant_mail.subject, "Grant Application")
        self.assertEqual(
            grant_mail.body,
            'name: <b>Alireza</b>\ncio_email: <b>my@email.com</b>\n'
            'title: <b>something</b>'
        )
        self.assertEqual(grant_mail.from_email, 'my@email.com')
        self.assertEqual(grant_mail.to, ['alireza.savand@gmail.com', ])
