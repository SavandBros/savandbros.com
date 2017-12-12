from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.views import View
from typing import List


class GrantFormProcessor(View):
    """Grant Form Processor."""
    def post(self, request: HttpRequest, *args, **kwargs):
        lines: List[str] = []
        cio_email: str = request.POST.get('cio_email')

        for k, v in request.POST.items():
            lines.append(f'{k}: <b>{v}</b>')

        send_mail(
            'Grant Application',
            '\n'.join(lines),
            cio_email,
            ['alireza.savand@gmail.com', ]
        )

        return HttpResponse(status=201)
