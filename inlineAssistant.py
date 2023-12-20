# import requests
# 
# url = "https://raw.githubusercontent.com/MoisesJPG/genshin-inline-assistant/main/database.json"
# 
# try:
#     response = requests.get(url)
#     response.raise_for_status()  # Verificar si la solicitud fue exitosa
# 
#     # Obtener el contenido JSON
#     json_content = response.json()
# 
#     # Solicitar entrada de usuario para buscar información específica
#     search_key = input("Ingresa la clave para buscar en el JSON: ")
# 
#     # Verificar si la clave está presente en el JSON
#     if search_key in json_content:
#         # Mostrar el valor correspondiente a la clave ingresada
#         print(f"Valor para '{search_key}': {json_content[search_key]}")
#     else:
#         print(f"La clave '{search_key}' no se encontró en el JSON.")
# 
# except requests.exceptions.RequestException as e:
#     print(f"Error al obtener el contenido JSON: {e}")
# except ValueError as ve:
#     print(f"Error al decodificar JSON: {ve}")

screen = "main"
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
            else:
                print("El personajee '"+entrada_usuario.split(" ")[1]+"' no existe")

