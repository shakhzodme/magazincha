from rest_framework import serializers

from core.models import Kategoriya, Tovar


class KategoriyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoriya
        fields = "__all__"

# KategoriyaSerializer.base_fields["ota_kategoriya"] = KategoriyaSerializer()

class TovarSerializer(serializers.ModelSerializer):
    kategoriya = KategoriyaSerializer(read_only=True)
    kategoriya_id = serializers.PrimaryKeyRelatedField(queryset = Kategoriya.objects.all(), source = 'kategoriya', write_only = True, allow_null = True)

    class Meta:
        model = Tovar
        fields = "__all__"