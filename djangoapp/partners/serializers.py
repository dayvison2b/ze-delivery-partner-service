# djangoapp/partners/serializers.py

from django.contrib.gis.geos import MultiPolygon, Point, Polygon, LinearRing
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Partner


class PartnerSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Partner
        geo_field = "address"
        fields = "__all__"

    def to_internal_value(self, data):
        coverage_area_geojson = data["coverageArea"]["coordinates"]
        address_geojson = data["address"]["coordinates"]

        coverage_area = self.geojson_to_multipolygon(coverage_area_geojson)
        data["coverageArea"] = coverage_area

        address = self.geojson_to_point(address_geojson)
        data["address"] = address

        return super().to_internal_value(data)

    def geojson_to_multipolygon(self, coverage_area_geojson):
        # Assuming coverageArea GeoJSON is in the correct format
        polygons = []
        for polygon_coords in coverage_area_geojson:
            rings = []
            for ring_coords in polygon_coords:
                ring = LinearRing(ring_coords)
                rings.append(ring)
            polygon = Polygon(*rings)
            polygons.append(polygon)
        return MultiPolygon(polygons)

    def geojson_to_point(self, address_geojson):
        # Assuming address GeoJSON is in the correct format
        return Point(*address_geojson)
