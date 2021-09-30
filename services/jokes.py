import requests
import json
import models.joke as joke_model

jokes_categories = list("Programming,Miscellaneous,Dark,Pun,Spooky,Christmas".split(","))

def get_joke(n_joke_category):
  """
  Programming,Miscellaneous,Dark,Pun,Spooky,Christmas
  """
  try:

    url = None
    if (n_joke_category < 0):
      url = "https://v2.jokeapi.dev/joke/Any"
    else:
      url = f"https://v2.jokeapi.dev/joke/{jokes_categories[n_joke_category - 1]}"

    print("[JOKE] URL>", url)

    response = requests.get(url)

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