from django.test import TestCase
from django.urls import reverse, resolve
from ..views import PartnerViewSet, SearchPartnerView


class UrlsTest(TestCase):
    def test_partner_list_urls(self):
        """
        Ensure the partner list URL resolves to the correct view.
        """

        url = reverse("partner-list")
        self.assertEqual(resolve(url).func.view_class, PartnerViewSet)
