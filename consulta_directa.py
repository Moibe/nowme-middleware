import json
import requests
import extractor
import conexion_firebase

usuario = "A9yynA0GPNfLkzu8HUDp"
plan_usuario = {
            'id': 'A9yynA0GPNfLkzu8HUDp', 
            'username': 'moibe', 
            'genero': 'masculino',
            'objetivo': 'bajar de peso',
            'nivel_actividad': 'activo',
            'edad': '25',
            'tmb': '2100',
            'fecha': ''
            }
url = "https://moibe-nowme.hf.space/macronutrientes/"

# La consulta que quieres enviar a la API.
consulta = "Haz una distribución de macronutrientes para un hombre que desea definición muscular, es muy activo, tiene 25 años y una tasa metabólica basal de 2100."

# Construir la URL con el parámetro 'prompt' en la cadena de consulta.
url_completa = f"{url}?prompt={consulta}"

try:
    response = requests.post(url_completa)
    response.raise_for_status()

    respuesta = response.json()
    respuesta_json = json.loads(respuesta)
    conexion_firebase.creaBlueprint_macros(plan_usuario, respuesta_json)

except requests.exceptions.RequestException as e:
    print(f"Error al consumir la API: {e}")
    if hasattr(response, 'text'):
        print("Respuesta del servidor:", response.text)
except json.JSONDecodeError:
    print("Error: No se pudo decodificar la respuesta JSON.")
    if hasattr(response, 'text'):
        print("Respuesta del servidor:", response.text)