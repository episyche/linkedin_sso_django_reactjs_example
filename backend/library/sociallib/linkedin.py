from django.conf import settings
import urllib.request as requests
import json
from urllib.parse import urlunparse


class Linkedin:
    """
    Github class to fetch the user info and return it
    """
    @staticmethod
    def validate(auth_token):
        """
        validate method Queries the linkedin url to fetch the user info
        """
        try:
            access_token_url = "https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&client_id=%s&client_secret=%s&code=%s&redirect_uri=%s" % (
                settings.LINKEDIN_CLIENT_ID, settings.LINKEDIN_CLIENT_SCERET, auth_token, settings.LINKEDIN_REDIRECT_URL)
            req = requests.urlopen(access_token_url)
            reply = req.read()
            access_token_json_decode = reply.decode('utf-8')
            access_token_json = json.loads(access_token_json_decode)
            access_token = access_token_json['access_token']

            url = 'https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))'
            headers = {
                "Authorization": f"Bearer {access_token}",
            }
            req = requests.Request(url, headers=headers)
            response = requests.urlopen(req)
            reply = response.read()
            data_response = reply.decode('utf-8')
            user_info = json.loads(data_response)
            return user_info['elements'][0]['handle~']

        except:
            return "The token is invalid or expired."