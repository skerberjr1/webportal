from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from authentication.models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'username', 'email', 'created_date', 'updated_date',
                  'first_name', 'last_name',)
        read_only_fields = ('created_date', 'updated_date',)

        def create(self, validated_data):
            return Account.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.email = validated_data.get('email', instance.email)

            instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance
