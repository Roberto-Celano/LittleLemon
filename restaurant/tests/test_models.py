from django.test import TestCase
from restaurant.models import Menu # Assicurati di importare il tuo modello

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")