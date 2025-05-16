import conexion_firebase

def extractor(respuesta_json):

    print("Ésta es la respuesta del extractor: ")
    print(respuesta_json["proteinas"]["porcentaje"]) 

    

    print(f"Las respuestas de porcentajes son: {porcentaje_prots}, {porcentaje_carbs} y {porcentaje_lipids}...")
    print(f"Las respuestas de kcals son: {kcal_prots}, {kcal_carbs} y {kcal_lipids}...")
