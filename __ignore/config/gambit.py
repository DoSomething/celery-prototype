import os

gambit_config = {
    'api_key': os.getenv('GAMBIT_API_KEY', 'totallysecret'),
    'base_url': os.getenv('GAMBIT_BASE_URL', 'http://localhost')
}
