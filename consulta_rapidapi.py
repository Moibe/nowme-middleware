import requests

url = "https://nowme-ai.p.rapidapi.com/macronutrientes/"

querystring = {"prompt":"183 Haz una distribución de macronutrientes para un hombre que desea definición muscular, es muy activo, tiene 25 años y una tasa metabólica basal de 2100."}

payload = {}
headers = {
	"x-rapidapi-key": "e3218509f1msh9430768b9dfcd99p139f59jsn6bc4183c91be",
	"x-rapidapi-host": "nowme-ai.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.json())