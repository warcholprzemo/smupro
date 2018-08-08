from rest_framework import serializers

from multiplex.models import Cinema

"""
class Cinema(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    open_time = models.TimeField(null=True)
    close_time = models.TimeField(null=True)
    active = models.BooleanField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
"""

"""
//correct curl
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name": "Letnie", "address": "Mielno", "active": "true"}' \
http://localhost:8000/multiplex/cinemas/

//without name, response 400-Bad Request
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"address": "Konin", "active": "true"}' \
http://localhost:8000/multiplex/cinemas/

# For object of Cinema

// Test PUT
curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"name": "Zimowe", "address": "Leszno", "active": false, "open_time": "09:30:00"}' \
http://localhost:8000/multiplex/cinemas/4/

// Test DELETE. We don't need a data
curl --header "Content-Type: application/json" \
  --request DELETE \
http://localhost:8000/multiplex/cinemas/4/
"""

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('id', 'name', 'address', 'active', 'open_time', 'language')
