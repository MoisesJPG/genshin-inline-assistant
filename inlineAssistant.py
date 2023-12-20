import requests

url = "https://raw.githubusercontent.com/MoisesJPG/genshin-inline-assistant/main/database.json"

try:
    response = requests.get(url)
    response.raise_for_status()  # Verificar si la solicitud fue exitosa

    # Obtener el contenido JSON
    json_content = response.json()

    # Mostrar el contenido
    print(json_content)

except requests.exceptions.RequestException as e:
    print(f"Error al obtener el contenido JSON: {e}")
