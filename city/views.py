from rest_framework.viewsets import ModelViewSet


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = serializers.CitySerializer
    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [permissions.AllowAny(),]
        else:
            return [permissions.IsAdminUser()]