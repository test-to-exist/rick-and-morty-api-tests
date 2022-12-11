import requests

def test_character_endpoint(name):

    # TRY using this one:
    # https: // realpython.com / python - testing /  # testing-for-web-frameworks-like-django-and-flask

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    baseUrl = 'rickandmortyapi.com/api';
    character_endpoint = f'https://{baseUrl}/character'
    response = requests.get(character_endpoint)
    print(response.json())

if __name__ == '__main__':
    test_character_endpoint('PyCharm')