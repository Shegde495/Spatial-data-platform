from django.contrib import admin
from django.urls import path
from spatial_data.views import (
    CreateSpatialPointAPI, 
    GetSpatialPointsAPI, 
    GetSpatialPointsByCategoryAPI,
    UpdateSpatialPointAPI,
    DeleteSpatialPointAPI,
    CreateSpatialPolygonAPI,
    GetSpatialPolygonsAPI,
    GetSpatialPolygonsByCategoryAPI,
    UpdateSpatialPolygonAPI,
    DeleteSpatialPolygonAPI
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/spatial-points/', CreateSpatialPointAPI.as_view(), 
         name='create_spatial_point'),
    path('api/spatial-points/list/', GetSpatialPointsAPI.as_view(), 
         name='get_spatial_points'),
    path('api/spatial-points/category/<str:category>/', 
         GetSpatialPointsByCategoryAPI.as_view(), 
         name='get_spatial_points_by_category'),
    path('api/spatial-points/<int:point_id>/', UpdateSpatialPointAPI.as_view(), 
         name='update_spatial_point'),
    path('api/spatial-points/<int:point_id>/delete/', 
         DeleteSpatialPointAPI.as_view(), name='delete_spatial_point'),
    path('api/spatial-polygons/', CreateSpatialPolygonAPI.as_view(), 
         name='create_spatial_polygon'),
    path('api/spatial-polygons/list/', GetSpatialPolygonsAPI.as_view(), 
         name='get_spatial_polygons'),
    path('api/spatial-polygons/category/<str:category>/', 
         GetSpatialPolygonsByCategoryAPI.as_view(), 
         name='get_spatial_polygons_by_category'),
    path('api/spatial-polygons/<int:polygon_id>/', 
         UpdateSpatialPolygonAPI.as_view(), name='update_spatial_polygon'),
    path('api/spatial-polygons/<int:polygon_id>/delete/', 
         DeleteSpatialPolygonAPI.as_view(), name='delete_spatial_polygon'),
]
