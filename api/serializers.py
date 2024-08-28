from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "phone", "first_name", "last_name", "password")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email", None)
        phone = data.get("phone", None)
        password = data.get("password", None)

        if not (email or phone):
            raise serializers.ValidationError(
                "Email or Phone number is required for login."
            )

        user = None
        if email:
            user = authenticate(username=email, password=password)
        elif phone:
            user = authenticate(username=phone, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials.")

        data["user"] = user
        return data
