from django.contrib.gis.db import models


class SpatialPoint(models.Model):
    """Model for storing spatial point data with PostGIS."""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    point = models.PointField(
        geography=True, 
        spatial_index=True, 
        null=True, 
        blank=True
    )
    category = models.CharField(
        max_length=50,
        default='other'
    )
    elevation = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['created_at'])
        ]
    
    def __str__(self):
        return f"{self.name} ({self.point.x}, {self.point.y})"


class SpatialPolygon(models.Model):
    """Model for storing spatial polygon data with PostGIS."""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    polygon = models.PolygonField(
        geography=True, 
        spatial_index=True, 
        null=True, 
        blank=True
    )
    category = models.CharField(
        max_length=50,
        default='other'
    )
    area_sqm = models.FloatField(null=True, blank=True)
    perimeter_m = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['created_at'])
        ]
    
    def __str__(self):
        return f"{self.name} (Polygon)"
    
    def save(self, *args, **kwargs):
        if self.polygon:
            self.area_sqm = self.polygon.area
            self.perimeter_m = self.polygon.length
        super().save(*args, **kwargs)
