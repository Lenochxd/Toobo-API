# Toobo Weather API

Welcome to the Toobo Weather API! This API provides friendly and cheerful weather summaries for kids, inspired by Toobo from [La météo de Gulli](https://fr.wikipedia.org/wiki/La_M%C3%A9t%C3%A9o_de_Gulli).

## Features

- Summarizes weather data for multiple cities
- Provides kid-friendly weather descriptions
- Suggests appropriate clothing based on the weather

## API Endpoint

The API can be accessed at: https://toobo.bishokus.fr:8000

### Get Weather Resume

Endpoint: `/API/toobo`

Method: GET

Query Parameters:
- `date` (optional): The date for which you want the weather resume. Format: YYYY-MM-DD. If not provided, it defaults to tomorrow's date.

Example Request:
```
GET https://toobo.bishokus.fr:8000/API/toobo?date=2024-07-22
```


Response:

```
{
  "text": "Salut les enfants! C'est Toobo, votre champion météo! Préparez-vous pour une journée ensoleillée et joyeuse demain!

           À **Paris**, attendez-vous à un mélange de soleil et de nuages avec des températures agréables autour de 24°C. Parfait pour une journée chaude et agréable!

           **Marseille** bénéficiera d'un ciel dégagé avec des températures avoisinant les 29°C. Le vent sera léger, principalement du nord-ouest.

           À **Bordeaux**, le ciel sera partiellement nuageux, mais vous aurez des éclaircies. Prévoyez des températures autour de 26°C avec un léger vent d'ouest-nord-ouest.

           À **Toulouse**, attendez-vous à un ciel nuageux le matin avec des éclaircies l'après-midi. Les températures seront douces autour de 25°C.

           Pour **Saint-Brieuc**, la journée sera partiellement nuageuse, mais ne vous inquiétez pas, c'est toujours agréable. Prévoyez des températures douces autour de 21°C.

           À **Nice**, vous commencerez la journée avec un ciel dégagé, mais il pourrait y avoir quelques nuages plus tard. Les températures atteindront environ 30°C, parfait pour une journée sur la Côte d'Azur.

           À **Nancy**, le ciel sera nuageux avec quelques éclaircies. Les températures seront agréables autour de 22°C.

           En résumé, demain sera une journée ensoleillée et joyeuse dans la plupart des villes, avec des températures agréables! Assurez-vous d'apporter vos lunettes de soleil et de profiter de cette belle journée! 🌞🌸"
}
```


## Technical Details

- Built with FastAPI
- Uses OpenAI's GPT-3.5-turbo model for generating weather summaries
- Caches weather data for efficiency

Enjoy using the Toobo Weather API!
