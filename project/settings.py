import os
from core.settings import *
from django.utils.translation import gettext_lazy as _

SITE_NAME = META_SITE_NAME = 'World Heat Flow Database'
EMAIL_DOMAIN = "@heatflow.world"
ADMINS = MANAGERS = [('Sam', 'jennings@gfz-potsdam.de')]

# UNCOMMENT TO COLLECTSTATIC TO AWS S3
# STATICFILES_STORAGE = 'project.storage_backends.StaticStorage'
# STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/"

# enter additional domains or ip addresses of allowed hosts here. 127.0.0.1 and localhost are already included
ALLOWED_HOSTS += []

INSTALLED_APPS = [

    'core',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'grappelli.dashboard',
    'grappelli',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django_cleanup.apps.CleanupConfig',
    'authentication',
    'user',
    'django.contrib.gis',
    'django.contrib.humanize',
    'django.contrib.admindocs',
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.orcid",
    "invitations",
    'organizations',
    'cms',
    'menus',
    'sekizai',
    'treebeard',

    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_file',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_bootstrap5',
    'djangocms_bootstrap5.contrib.bootstrap5_alerts',
    'djangocms_bootstrap5.contrib.bootstrap5_badge',
    'djangocms_bootstrap5.contrib.bootstrap5_card',
    'djangocms_bootstrap5.contrib.bootstrap5_carousel',
    'djangocms_bootstrap5.contrib.bootstrap5_collapse',
    'djangocms_bootstrap5.contrib.bootstrap5_content',
    'djangocms_bootstrap5.contrib.bootstrap5_grid',
    'djangocms_bootstrap5.contrib.bootstrap5_jumbotron',
    'djangocms_bootstrap5.contrib.bootstrap5_link',
    'djangocms_bootstrap5.contrib.bootstrap5_listgroup',
    'djangocms_bootstrap5.contrib.bootstrap5_media',
    'djangocms_bootstrap5.contrib.bootstrap5_picture',
    'djangocms_bootstrap5.contrib.bootstrap5_tabs',
    'djangocms_bootstrap5.contrib.bootstrap5_utilities',
    'djangocms_video',

    'rest_framework',
    'rest_framework_gis',
    "drf_spectacular",
    'rest_framework_datatables_editor',

    'solo',
    'import_export',
    'simple_history',
    'django_extensions',
    'djgeojson',
    'widget_tweaks',
    'taggit',
    'taggit_autosuggest',
    'django_filters',
    'storages',
    'crispy_forms',
    'crispy_bootstrap5',
    'fluent_comments',
    'threadedcomments',
    'django_comments',

    'django_social_share',
    'meta',
    "sortedm2m",
    'ordered_model',
    "rosetta",
    'bootstrap_datepicker_plus',
    "django_gravatar",
    "django_ckeditor_5",
    "django_jsonforms",
    "treewidget",
    'django_htmx',
    'formtools',


    # Custom Standalone Apps
    'kepler',
    "well_logs",
    'crossref',
    'crossref.cms',
    'datacite',
    "global_tectonics",
    'earth_science',


    # GHFDB Apps
    'main',
    'database',
    'thermal_data',
    'publications',
    'mapping',
    'theme',
    # 'review',
    "research_organizations",

    # "debug_toolbar",
]

EARTH_MATERIALS_INCLUDE = [
    'Igneous rock and sediment',
    'Metamorphic rock',
    'Sediment and sedimentary rock'
]

GRAPPELLI_INDEX_DASHBOARD = 'main.admin_dashboard.AdminDashboard'
GRAPPELLI_AUTOCOMPLETE_LIMIT = None
GRAPPELLI_ADMIN_TITLE = f'{SITE_NAME} Administration'

TREEWIDGET_SETTINGS = {
    'search': True,
    # 'show_buttons': True
    "can_add_related": False,
}

TREEWIDGET_TREEOPTIONS = {
    "core": {
        "themes": {
            "variant": "large",
            "icons": False,
        },
    },
    'search': {
        # 'fuzzy':True,
        'show_only_matches': True,
    },
    'checkbox': {
        'three_state': False,
    },
    "plugins": ["checkbox"]
}

DEFAULT_FROM_EMAIL = f'info{EMAIL_DOMAIN}'


SOCIALACCOUNT_PROVIDERS = {
    'orcid': {
        # Base domain of the API. Default value: 'orcid.org', for the production API
        'BASE_DOMAIN': 'sandbox.orcid.org',  # for the sandbox API
        # Member API or Public API? Default: False (for the public API)
        'MEMBER_API': False,
    }
}


# ADAPTER FOR DJANGO-INVITATION TO USE DJANGO-ALLAUTH
ACCOUNT_ADAPTER = 'invitations.models.InvitationsAdapter'


# DJANGO-ORGANISATIONS SETTINGS
INVITATION_BACKEND = 'organizations.backends.defaults.InvitationBackend'
REGISTRATION_BACKEND = 'organizations.backends.defaults.RegistrationBackend'


CROSSREF_UA_STRING = f"{SITE_NAME} (https://thermoglobe.app)"
CROSSREF_MAILTO = ';'.join([v[1] for v in ADMINS])

MIDDLEWARE += [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
]
# MIDDLEWARE.append('lockdown.middleware.LockdownMiddleware')

# THUMBNAIL_DEFAULT_STORAGE = 'project.storage_backends.PublicMediaStorage'
# PRIVATE_FILE_STORAGE = DEFAULT_FILE_STORAGE = 'project.storage_backends.PrivateMediaStorage'

REST_FRAMEWORK = {
    "HTML_SELECT_CUTOFF": 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'api.v1.throttling.AnonBurstRate',
        'api.v1.throttling.AnonSustainedRate',
        'api.v1.throttling.UserBurstRate'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon_burst': '4/second',
        'anon_sustained': '30/minute',
        'user_burst': '25/second'
    },
    'DEFAULT_PERMISSION_CLASSES': [
        "api.access_policies.SiteAccessPolicy",
    ],
    'DEFAULT_RENDERER_CLASSES': [
        "drf_orjson_renderer.renderers.ORJSONRenderer",
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_csv.renderers.PaginatedCSVRenderer',
        'drf_excel.renderers.XLSXRenderer',
        'rest_framework_datatables_editor.renderers.DatatablesRenderer',
        'api.v1.renderers.GeoJsonRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_datatables_editor.filters.DatatablesFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_datatables_editor.pagination.DatatablesPageNumberPagination',

    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,

    'DEFAULT_PARSER_CLASSES': [
        'drf_orjson_renderer.parsers.ORJSONParser',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

GRAPH_MODELS = {
    'app_labels': ["database", "thermal_data", "publications", "well_logs", "crossref"],
    "exclude_models": ['PublicationAbstract', 'UUIDTaggedItem', 'SiteAbstract', 'IntervalAbstract', 'HistoricalSite', 'HistoricalInterval', 'AbstractLog', 'ChoiceAbstract', 'AuthorAbstract', 'MP_Node'],
    'all_applications': False,
    'group_models': True,
    # 'hide_edge_labels': True,
    # "hide_relations_from_fields":True,
    # 'skip_check':True,
}