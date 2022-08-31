from django.conf import settings
from rest_framework import serializers
from library.sociallib import linkedin
from library.register.register import register_social_user
from rest_framework.exceptions import*


class LinkedinSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of Linkedin related data"""
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = linkedin.Linkedin.validate(auth_token)
        try:
            email = user_data['emailAddress']
            provider = 'linkedin'
        except:
            raise serializers.ValidationError(
                'The token  is invalid or expired. Please login again.'
            )
        return register_social_user(
            provider=provider, user_id=None, email=email, name=None)
