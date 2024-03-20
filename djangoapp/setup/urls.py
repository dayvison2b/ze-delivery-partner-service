from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from partners.views import PartnerViewSet, SearchPartnerView

router = DefaultRouter()
router.register(r"partners", PartnerViewSet)

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", include(router.urls), name="partners"),
    path("search/", SearchPartnerView.as_view(), name="search_partner"),
]
