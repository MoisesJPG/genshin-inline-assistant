import requests

# Obtener el contenido JSON
url = "https://raw.githubusercontent.com/MoisesJPG/genshin-inline-assistant/main/database.json"

try:
    response = requests.get(url)
    # Verificar si la solicitud fue exitosa
    response.raise_for_status()
    # Guarda los datos en la variable mainDatabase
    mainDatabase = response.json()

except requests.exceptions.RequestException as e:
    print(f"Error al obtener el contenido JSON: {e}")
except ValueError as ve:
    print(f"Error al decodificar JSON: {ve}")

screen = "builds"
def obtener_entrada():
    if screen == "main":
        return input("/")
    if screen == "builds":
        return input("/builds ")

while True:
    entrada_usuario = obtener_entrada()
    # Comandos globales
    if entrada_usuario.lower() == "window":
        print(screen)

    # Comandos por "ventana"
    ## main
    if screen == "main":
        if entrada_usuario.lower() == 'exit':
            break
        if entrada_usuario.lower() == 'builds':
            print("Accediendo a las builds...")
            screen = "builds"
    ## builds
    if screen == "builds":
        if entrada_usuario.lower() == 'exit':
            screen = "main"
            print("Volviendo al menu principal...")
        if entrada_usuario.lower().split(" ")[0] == 'character':
            if entrada_usuario.lower().split(" ")[1] == 'amber':
                print("Mostrando builds de 'Amber':")
                print(mainDatabase["character"])
            else:
                print("El personajee '"+entrada_usuario.split(" ")[1]+"' no existe")

