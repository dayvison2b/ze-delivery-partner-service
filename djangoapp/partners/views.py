# djangoapp/partners/views.py

from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Partner
from .serializers import PartnerSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class SearchPartnerView(APIView):
    def get(self, request):
        longitude = request.query_params.get("long", None)
        latitude = request.query_params.get("lat", None)

        if longitude is None or latitude is None:
            return Response(
                {"error": "Missing longitude or latitude parameter."}, status=400
            )

        try:
            location = Point(
                float(longitude),
                float(latitude),
                srid=4326,  # srid=4326 - > sistema de referência de coordenadas WGS84 (padrão para GPS)
            )
            partners = Partner.objects.filter(coverageArea__contains=location)

            if not partners:
                return Response(
                    {"message": "No partner found for the given location."}, status=404
                )

            nearest_partner = (
                partners.annotate(distance=Distance("address", location))
                .order_by("distance")
                .first()
            )
            serializer = PartnerSerializer(nearest_partner)

            return Response(serializer.data)
        except ValueError:
            return Response(
                {"error": "Invalid longitude or latitude value."}, status=400
            )
