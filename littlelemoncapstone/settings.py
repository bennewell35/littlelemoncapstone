INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Restaurant',
    'rest_framework',
    'rest_framework.authtoken',
    'littlelemoncapstoneAPI',
    'djoser',  # Add 'djoser' app here
]

# Rest Framework settings for Token and Session authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # Add Session Authentication
    ],
    # ...
}

# ... (the rest of your settings)

# Djoser settings
DJOSER = {
    "USER_ID_FIELD": "username",  # Add USER_ID_FIELD as per your step 3
}

# Specific allowed hosts (production example)
ALLOWED_HOSTS = ['yourdomain.com', 'anotherdomain.com']

# Wildcard to allow all hosts (development/testing example)
# ALLOWED_HOSTS = ['*']

# Other settings...
MIDDLEWARE = [
    # ... other middleware ...
    'django.contrib.sessions.middleware.SessionMiddleware',  # Add this line
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Add this line
    'django.contrib.messages.middleware.MessageMiddleware',  # Add this line
    # ... other middleware ...
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Ensure this line is present
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MollyBen',
        'USER': 'ben_molly',
        'PASSWORD': 'MollyBen..12!!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
