from rest_framework import serializers

from users.models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('login', 'screen_name', 'password',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = CustomUser(
            login=self.validated_data['login'],
            screen_name=self.validated_data['screen_name'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'firstname', 'lastname', 'date_joined')
        read_only_fields = ('email', 'firstname', 'lastname', 'date_joined')


class TgTokenSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('user_token', )
