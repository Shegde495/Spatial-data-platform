from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import SpatialPoint


@admin.register(SpatialPoint)
class SpatialPointAdmin(OSMGeoAdmin):
    """Admin interface for SpatialPoint with PostGIS support."""
    list_display = ('name', 'category', 'latitude', 'longitude', 'elevation', 'created_at')
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'category')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'category')
        }),
        ('Location', {
            'fields': ('point', 'elevation'),
            'description': 'Use the map to set the point location'
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def latitude(self, obj):
        """Display latitude from Point geometry."""
        return f"{obj.point.y:.6f}" if obj.point else "N/A"
    latitude.short_description = 'Latitude'
    
    def longitude(self, obj):
        """Display longitude from Point geometry."""
        return f"{obj.point.x:.6f}" if obj.point else "N/A"
    longitude.short_description = 'Longitude'
