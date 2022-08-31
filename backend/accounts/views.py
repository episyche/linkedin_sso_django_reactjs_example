from rest_framework.generics import GenericAPIView
from .serializers import*
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


@permission_classes((AllowAny, ))
class LinkedInSocialAuthView(GenericAPIView):

    serializer_class = LinkedinSocialAuthSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an access token as from linkedin to get user information
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)
