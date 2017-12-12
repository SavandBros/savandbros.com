from django.db.models import QuerySet
from django.test import TestCase

from menu_builder.models import Menu, NavigationLink


class TestMenu(TestCase):
    """Unit testing Menu model."""
    def test_magic_str(self):
        menu: Menu = Menu.objects.create(name='Footer')

        self.assertEqual(str(menu), 'Footer')

    def test_ancestors(self):
        menu: Menu = Menu.objects.create(name='Footer')

        nav_link1: NavigationLink = NavigationLink.objects.create(
            menu=menu,
            label='Go Home!',
        )
        nav_link2: NavigationLink = NavigationLink.objects.create(
            menu=menu,
            label='Go My Home!',
        )
        nav_link1_child: NavigationLink = NavigationLink.objects.create(
            menu=menu,
            label='Go My Home!',
            parent=nav_link1,
        )
        nav_link2_child: NavigationLink = NavigationLink.objects.create(
            menu=menu,
            label='Go My Home!',
            parent=nav_link2,
        )

        ancestors: QuerySet = menu.ancestors

        self.assertEqual(ancestors.count(), 2)
        self.assertIn(nav_link1, ancestors)
        self.assertIn(nav_link2, ancestors)
        self.assertNotIn(nav_link1_child, ancestors)
        self.assertNotIn(nav_link2_child, ancestors)
