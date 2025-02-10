from environs import Env

env = Env()
env.read_env()

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = env.str('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = env.str('SOCIAL_AUTH_FACEBOOK_SECRET')

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from Facebook.
# Email is not sent by default, to get it, you must request the email permission.

# We need to set at least the following scopes, to ensure that we can read
# basic profile details and email addresses.
# NB: These scopes are never actually used on the backend; things will work
# just fine if you omit these settings from the backend. However, the
# _frontend_ needs to be sure to send at least these scopes in order for the
# tokens to have enough permissions to get the user model updates / matching
# working properly.
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

# another source
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
]


