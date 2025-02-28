from environs import Env

env = Env()
env.read_env()

# Google configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env.str('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')  # '<your app id goes here>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env.str('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')  # '<your app secret goes here>'

# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', 'profile']
SOCIAL_AUTH_USER_FIELDS = ['email', 'username', 'password', 'first_name', 'last_name']
# ['email', 'username', 'password', 'verified_email', 'name', 'given_name', 'id', 'picture']

# GOOGLE_API_KEY = env.str('GOOGLE_API_KEY', '')


# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [  # Must be on front-end side
#     'https://www.googleapis.com/auth/userinfo.email',
#     'https://www.googleapis.com/auth/userinfo.profile',
#     'https://www.googleapis.com/auth/openid',
#     'https://www.googleapis.com/auth/youtube.readonly',
#     'https://www.googleapis.com/auth/yt-analytics.readonly'
# ]
