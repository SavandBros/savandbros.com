from cms.api import create_page
from cms.models import Page
from django.contrib.sites.models import Site
from django.test import TestCase

from menu_builder.models import Menu, NavigationLink


class TestNavigationLink(TestCase):
    """Unit testing Navigation Link model."""
    def test_link(self):
        site = Site.objects.all().first()
        menu: Menu = Menu.objects.create(name='Header')
        external_link: str = 'https://kloud51.com'
        page_slug = 'page-slug'
        page: Page = create_page(
            title='Yello',
            template='fullwidth.html',
            language='en',
            slug=page_slug,
            published=True,
            site=site,
        )
        page2: Page = create_page(
            "test page 2",
            'fullwidth.html', "en",
            parent=page,
            published=True
        )

        # Link should be None now
        nav_link: NavigationLink = NavigationLink.objects.create(
            menu=menu,
            label='Go Home!',
        )

        self.assertIsNone(nav_link.link)

        # The external URL should be returned
        nav_link.external_link = external_link
        self.assertEqual(nav_link.link, external_link)

        # The internal link (Page URL) should be returned
        nav_link.external_link = None
        nav_link.internal_link = page2
        nav_link.save()
        self.assertEqual(nav_link.link, page2.get_absolute_url())
        self.assertEqual(nav_link.link, '/en/test-page-2/')

    def test_magic_str(self):
        menu: Menu = Menu.objects.create(name='Header')
        nav_link: NavigationLink = NavigationLink.objects.create(
            menu=menu,
            label='Go Home!',
        )

        self.assertEqual(str(nav_link), nav_link.label)
