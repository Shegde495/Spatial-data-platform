from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.gis.geos import Point, Polygon
from .models import SpatialPoint, SpatialPolygon


class CreateSpatialPointAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            
            name = data.get('name')
            description = data.get('description', '')
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            category = data.get('category', 'other')
            elevation = data.get('elevation')
            
            if not name or latitude is None or longitude is None:
                return Response({
                    'success': False,
                    'errors': ['Name, latitude, and longitude are required']
                }, status=status.HTTP_400_BAD_REQUEST)
            
            point = Point(longitude, latitude, srid=4326)
            
            spatial_point = SpatialPoint.objects.create(
                name=name,
                description=description,
                point=point,
                category=category,
                elevation=elevation
            )
            
            return Response({
                'success': True,
                'spatial_point': {
                    'id': spatial_point.id,
                    'name': spatial_point.name,
                    'description': spatial_point.description,
                    'coordinates': [spatial_point.point.y, spatial_point.point.x],
                    'point_coordinates': [spatial_point.point.x, spatial_point.point.y],
                    'category': spatial_point.category,
                    'elevation': spatial_point.elevation,
                    'created_at': spatial_point.created_at.isoformat()
                }
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({
                'success': False,
                'errors': [str(e)]
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetSpatialPointsAPI(APIView):
    def get(self, request):
        try:
            points = SpatialPoint.objects.all()
            data = []
            
            for point in points:
                data.append({
                    'id': point.id,
                    'name': point.name,
                    'description': point.description,
                    'coordinates': ([point.point.y, point.point.x] 
                                  if point.point else None),
                    'point_coordinates': ([point.point.x, point.point.y] 
                                        if point.point else None),
                    'category': point.category,
                    'elevation': point.elevation,
                    'created_at': point.created_at.isoformat()
                })
            
            return Response({
                'success': True,
                'spatial_points': data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'success': False,
                'errors': [str(e)]
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetSpatialPointsByCategoryAPI(APIView):
    def get(self, request, category):
        try:
            points = SpatialPoint.objects.filter(category=category)
            data = []
            
            for point in points:
                data.append({
                    'id': point.id,
                    'name': point.name,
                    'description': point.description,
                    'coordinates': ([point.point.y, point.point.x] 
                                  if point.point else None),
                    'point_coordinates': ([point.point.x, point.point.y] 
                                        if point.point else None),
                    'category': point.category,
                    'elevation': point.elevation,
                    'created_at': point.created_at.isoformat()
                })
            
            return Response({
                'success': True,
                'spatial_points': data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'success': False,
                'errors': [str(e)]
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateSpatialPointAPI(APIView):
    def put(self, request, point_id):
        try:
            data = request.data
            
            try:
                spatial_point = SpatialPoint.objects.get(id=point_id)
            except SpatialPoint.DoesNotExist:
                return Response({
                    'success': False,
                    'errors': ['Spatial point not found']
                }, status=status.HTTP_404_NOT_FOUND)
            
            if 'name' in data:
                spatial_point.name = data['name']
            if 'description' in data:
                spatial_point.description = data['description']
            if 'category' in data:
                spatial_point.category = data['category']
            if 'elevation' in data:
                spatial_point.elevation = data['elevation']
            
            if 'latitude' in data and 'longitude' in data:
                point = Point(data['longitude'], data['latitude'], srid=4326)
                spatial_point.point = point
            
            spatial_point.save()
            
            return Response({
                'success': True,
                'spatial_point': {
                    'id': spatial_point.id,
                    'name': spatial_point.name,
                    'description': spatial_point.description,
                    'coordinates': [spatial_point.point.y, spatial_point.point.x],
                    'point_coordinates': [spatial_point.point.x, spatial_point.point.y],
                    'category': spatial_point.category,
                    'elevation': spatial_point.elevation,
                    'created_at': spatial_point.created_at.isoformat(),
                    'updated_at': spatial_point.updated_at.isoformat()
                }
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'success': False,
                'errors': [str(e)]
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteSpatialPointAPI(APIView):
    def delete(self, request, point_id):
        try:
            try:
                spatial_point = SpatialPoint.objects.get(id=point_id)
            except SpatialPoint.DoesNotExist:
                return Response({
                    'success': False,
                    'errors': ['Spatial point not found']
                }, status=status.HTTP_404_NOT_FOUND)
            
            spatial_point.delete()
            
            return Response({
                'success': True,
                'message': 'Spatial point deleted successfully'
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'success': False,
                'errors': [str(e)]
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateSpatialPolygonAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            
            name = data.get('name')
            description = data.get('description', '')
            coordinates = data.get('coordinates')
            category = data.get('category', 'other')
            
            if not name or not coordinates:
                return Response({
                    'success': False,
                    'errors': ['Name and coordinates are required']
                }, status=status.HTTP_400_BAD_REQUEST)
            
            polygon = Polygon(coordinates, srid=4326)
            
            spatial_polygon = SpatialPolygon.objects.create(
                name=name,
                description=description,
                polygon=polygon,
                category=category
            )
            
            return Response({
                'success': True,
                'spatial_polygon': {
                    'id': spatial_polygon.id,
                    'name': spatial_polygon.name,
                    'description': spatial_polygon.description,
                    'coordinates': list(spatial_polygon.polygon.coords[0]),
                    'category': spatial_polygon.category,
                    'area_sqm': spatial_polygon.area_sqm,
                    'perimeter_m': spatial_polygon.perimeter_m,
                    'created_at': spatial_polygon.created_at.isoformat()
                }
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({
                'success': False,
                'errors': [str(e)]
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetSpatialPolygonsAPI(APIView):
    def get(self, request):
        try:
            polygons = SpatialPolygon.objects.all()
            data = []
            
            for polygon in polygons:
                data.append({
                    'id': polygon.id,
                    'name': polygon.name,
                    'description': polygon.description,
                    'coordinates': (list(polygon.polygon.coords[0]) 
                                  if polygon.polygon else None),
                    'category': polygon.category,
                    'area_sqm': polygon.area_sqm,
                    'perimeter_m': polygon.perimeter_m,
                    'created_at': polygon.created_at.isoformat()
                })
            
            return Response({
                'success': True,
                'spatial_polygons': data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'success': False,
                'errors': [str(e)]
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetSpatialPolygonsByCategoryAPI(APIView):
    def get(self, request, category):
        try:
            polygons = SpatialPolygon.objects.filter(category=category)
            data = []
            
            for polygon in polygons:
                data.append({
                    'id': polygon.id,
                    'name': polygon.name,
                    'description': polygon.description,
                    'coordinates': (list(polygon.polygon.coords[0]) 
                                  if polygon.polygon else None),
                    'category': polygon.category,
                    'area_sqm': polygon.area_sqm,
                    'perimeter_m': polygon.perimeter_m,
                    'created_at': polygon.created_at.isoformat()
                })
            
            return Response({
                'success': True,
                'spatial_polygons': data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'success': False,
                'errors': [str(e)]
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateSpatialPolygonAPI(APIView):
    def put(self, request, polygon_id):
        try:
            data = request.data
            
            try:
                spatial_polygon = SpatialPolygon.objects.get(id=polygon_id)
            except SpatialPolygon.DoesNotExist:
                return Response({
                    'success': False,
                    'errors': ['Spatial polygon not found']
                }, status=status.HTTP_404_NOT_FOUND)
            
            if 'name' in data:
                spatial_polygon.name = data['name']
            if 'description' in data:
                spatial_polygon.description = data['description']
            if 'category' in data:
                spatial_polygon.category = data['category']
            
            if 'coordinates' in data:
                polygon = Polygon(data['coordinates'], srid=4326)
                spatial_polygon.polygon = polygon
            
            spatial_polygon.save()
            
            return Response({
                'success': True,
                'spatial_polygon': {
                    'id': spatial_polygon.id,
                    'name': spatial_polygon.name,
                    'description': spatial_polygon.description,
                    'coordinates': list(spatial_polygon.polygon.coords[0]),
                    'category': spatial_polygon.category,
                    'area_sqm': spatial_polygon.area_sqm,
                    'perimeter_m': spatial_polygon.perimeter_m,
                    'created_at': spatial_polygon.created_at.isoformat(),
                    'updated_at': spatial_polygon.updated_at.isoformat()
                }
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'success': False,
                'errors': [str(e)]
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteSpatialPolygonAPI(APIView):
    def delete(self, request, polygon_id):
        try:
            try:
                spatial_polygon = SpatialPolygon.objects.get(id=polygon_id)
            except SpatialPolygon.DoesNotExist:
                return Response({
                    'success': False,
                    'errors': ['Spatial polygon not found']
                }, status=status.HTTP_404_NOT_FOUND)
            
            spatial_polygon.delete()
            
            return Response({
                'success': True,
                'message': 'Spatial polygon deleted successfully'
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'success': False,
                'errors': [str(e)]
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 