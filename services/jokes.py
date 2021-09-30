import requests
import json
import models.joke as joke_model

jokes_categories = list("Programming,Miscellaneous,Dark,Pun,Spooky,Christmas".split(","))

def get_joke():
  """
  Programming,Miscellaneous,Dark,Pun,Spooky,Christmas
  """
  try:
    response = requests.get("https://v2.jokeapi.dev/joke/Any")
    joke = joke_model.joke_from_dict(json.loads(response.text))

    if (joke.error == "true"):
      return "There was an error while fetching joke, this is not a joke lol"


    if (joke.type == "single"):
      print("JOKE:" , joke.joke)
      return joke.joke
    else:
      print("SETUP:", joke.setup)
      print("DEL:", joke.delivery)

      return f"{joke.setup}\n\n{joke.delivery}"

  except Exception as e:
    print("[JOKE] ERROR:", e)
    return f"There was an error while fetching joke, this is not a joke, lol"