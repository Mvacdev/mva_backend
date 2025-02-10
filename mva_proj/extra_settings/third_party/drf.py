# *** Django REST Framework settings ***

from django.conf import settings


REST_FRAMEWORK_PROD = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'drf_social_oauth2.authentication.SocialAuthentication',

        'rest_framework.authentication.SessionAuthentication',
        # 'dj_rest_auth.jwt_auth.JWTCookieAuthentication',

        # 'rest_framework_simplejwt.authentication.JWTAuthentication',  # before
        # 'apps.accounts.authenticate.CustomAuthentication'  # after (overridden)
        # 'apps.accounts.backends.JWTAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    #     # 'rest_framework.renderers.TemplateHTMLRenderer',
    # ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    # 'USER_DETAILS_SERIALIZER': 'apps.accounts.api.serializers.UserSerializer', TODO

    # 'EXCEPTION_HANDLER': 'crm_proj.exceptions.core_exception_handler',
    # 'NON_FIELD_ERRORS_KEY': 'error',
}

if not settings.IS_PRODUCTION_ENV:
    REST_FRAMEWORK_PROD.update({
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10
    })

REST_FRAMEWORK = REST_FRAMEWORK_PROD


# simplejwt settings
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
#     'REFRESH_TOKEN_LIFETIME': timedelta(hours=1),
#     'ROTATE_REFRESH_TOKENS': True,
#     'BLACKLIST_AFTER_ROTATION': True,
#     'UPDATE_LAST_LOGIN': True,
#
#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': settings.SECRET_KEY,
#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,
#     'JWK_URL': None,
#     'LEEWAY': 0,
#
#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',
#     'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
#
#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',
#     'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
#
#     'JTI_CLAIM': 'jti',
#
#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
#
#     # custom
#     'AUTH_COOKIE': 'access_token',  # Cookie name. Enables cookies if value is set.
#     'AUTH_REFRESH_COOKIE': 'refresh_token',  # Refresh cookie name. (for dj-rest-auth)
#     'AUTH_COOKIE_DOMAIN': None,     # A string like "example.com", or None for standard domain cookie.
#     'AUTH_COOKIE_SECURE': False,    # Whether the auth cookies should be secure (https:// only).
#     'AUTH_COOKIE_HTTP_ONLY': True,  # Http only cookie flag.It's not fetch by javascript.
#     'AUTH_COOKIE_PATH': '/',        # The path of the auth cookie.
#     'AUTH_COOKIE_SAMESITE': 'Strict',  # Whether to set the flag restricting cookie leaks on cross-site requests.
#     # This can be 'Lax', 'Strict', or None to disable the flag.
# }


# # dj-rest-auth settings
# REST_USE_JWT = True
# JWT_AUTH_COOKIE = SIMPLE_JWT.get('AUTH_COOKIE')
# JWT_AUTH_REFRESH_COOKIE = SIMPLE_JWT.get('AUTH_REFRESH_COOKIE')
# REST_SESSION_LOGIN = False
# # if settings.IS_PRODUCTION_ENV:
# #     JWT_AUTH_SECURE = True
# # else:
# JWT_AUTH_SECURE = False  # must enable security
# # CORS_ALLOW_CREDENTIALS = True                  # for local frontend :3000
# # CORS_ALLOWED_ORIGINS = ['https://example.com'] # for local frontend :3000
# REST_AUTH_SERIALIZERS = {
#     'LOGIN_SERIALIZER': 'apps.accounts.api.serializers.LoginSerializer',
#     'JWT_TOKEN_CLAIMS_SERIALIZER': 'apps.accounts.api.serializers.MyTokenObtainPairSerializer',
#     'PASSWORD_RESET_SERIALIZER': 'apps.accounts.api.serializers.MyPasswordResetSerializer'
# }
# REST_AUTH_REGISTER_SERIALIZERS = {
#     "REGISTER_SERIALIZER": 'apps.accounts.api.serializers.RegisterSerializer'
# }


# DEFAULTS = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
#     'ROTATE_REFRESH_TOKENS': True,
#     'BLACKLIST_AFTER_ROTATION': True,
#
#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': settings.SECRET_KEY,
#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,
#
#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',
#
#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',
#
#     'JTI_CLAIM': 'jti',
#
#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
# }

# R_F_SAME = {
#     'DEFAULT_FILTER_BACKENDS': [
#         'django_filters.rest_framework.DjangoFilterBackend'
#     ],
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.SessionAuthentication',
#         # 'rest_framework_simplejwt.authentication.JWTAuthentication',  # before
#         # 'apps.accounts.authenticate.CustomAuthentication'  # after (overridden)
#         'dj_rest_auth.jwt_auth.JWTCookieAuthentication',  # LAST
#         # 'apps.accounts.backends.JWTAuthentication',
#         # 'rest_framework.authentication.TokenAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ],
#     'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
#     # 'DEFAULT_RENDERER_CLASSES': (
#     #     'rest_framework.renderers.JSONRenderer',
#     #     # 'rest_framework.renderers.TemplateHTMLRenderer',
#     # ),
#     'TEST_REQUEST_DEFAULT_FORMAT': 'json',
#     'USER_DETAILS_SERIALIZER': 'apps.accounts.api.serializers.UserSerializer',
#
#     'EXCEPTION_HANDLER': 'ugoda_proj.exceptions.core_exception_handler',
#     'NON_FIELD_ERRORS_KEY': 'error',
# }
#
# if not IS_PRODUCTION_ENV:
#     R_F_SAME.update({
#         'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#         'PAGE_SIZE': 10
#     })
#     REST_FRAMEWORK = R_F_SAME
#
# else:
#     REST_FRAMEWORK = R_F_SAME

