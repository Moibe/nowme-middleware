import firebase_admin
from firebase_admin import firestore
from firebase_admin import auth
from firebase_admin import credentials
import time

#obtenDato, creaDato y editaDato.


firebase_cred = credentials.Certificate('config.json')
firebase_admin.initialize_app(firebase_cred)

db = firestore.client()
#dato es el dato que traes  como el nombre del user. 
#info es la info de ese dato que estás buscando, como token.
def obtenDato(coleccion, documento, campo):
    #Future: Tentativamente ésta parte podría solo hacerse una vez y vivir en la app para ser reutilizado.
    
    #Primero debemos definir la referencia al documento, o sea a la hoja de usuario.
    doc_ref = db.collection(coleccion).document(documento)    
    #Éste es el documento que tiene los datos de ella.
    documento = doc_ref.get()    
    #Recuerda la conversión a diccionario.
    documento = doc_ref.get() 
    diccionario = documento.to_dict()
    return diccionario.get(campo)

def editaDato(coleccion, documento, campo, contenido):

    #Primero debemos definir la referencia al documento, o sea a la hoja de usuario.
    doc_ref = db.collection(coleccion).document(documento)
    
    doc_ref.update({
        # 'quote': quote,
        campo: contenido,
    })

def creaDato(coleccion, documento, campo, contenido):

    #Primero debemos definir la referencia al documento, o sea a la hoja de usuario.
    doc_ref = db.collection(coleccion).document(documento)
    
    doc_ref.set({
        # 'quote': quote,
        campo: contenido,
    })

def creaBlueprint_macros(plan_usuario, respuesta_json):

    print("Recibí parámetro plan_usuario:")
    print(plan_usuario)
    print("Recibí parámetro respuesta:")
    print(respuesta_json)

    print(plan_usuario["genero"])
    print(plan_usuario["tmb"])


    time.sleep(20)

    #Primero debemos definir la referencia al documento, o sea a la hoja de usuario.
    doc_ref = db.collection('blueprint_macros').document('usuario')    
    
    doc_ref.set({
        'porcentaje_prots' : respuesta_json["proteinas"]["porcentaje"],
        'porcentaje_carbs' : respuesta_json["carbohidratos"]["porcentaje"],
        'porcentaje_lipids' : respuesta_json["lipidos"]["porcentaje"],
        'kcal_prots' : respuesta_json["proteinas"]["kcal"],
        'kcal_carbs' : respuesta_json["carbohidratos"]["kcal"],
        'kcal_lipids' : respuesta_json["lipidos"]["kcal"],
    })

def verificar_token(id_token):
    """Verifica el token de ID de Firebase."""
    try:
        # Verifica el token y decodifica la información del usuario
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return uid  # Retorna el UID del usuario si el token es válido
    except auth.InvalidIdTokenError as e:
        print(f"Token inválido: {e}")
        return None  # Retorna None si el token es inválido