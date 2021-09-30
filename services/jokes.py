import requests
import json
import models.joke as joke_model

jokes_categories = list("Programming,Miscellaneous,Dark,Pun,Spooky,Christmas".split(","))

def get_joke_help_message():
  msg = "Get Jokes from \"-joke\" command !\n\nAdditional Options:\n"

  for index, category in enumerate(jokes_categories):
    msg = msg + (f"\t{index + 1}. {category}\n")

  msg = msg + "Enter specific number to get jokes from that category\nSyntax: -joke [--num]\nEg: -joke --1"
  return msg

def send_jokes_all():
  url = "https://v2.jokeapi.dev/joke/Any"
  return make_request_and_get_joke(url)
  

def send_jokes_with_category(category):
  url = f"https://v2.jokeapi.dev/joke/{category}"
  return make_request_and_get_joke(url)
  

def make_request_and_get_joke(url):
  try:
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

def get_joke(message):

  """
  Programming,Miscellaneous,Dark,Pun,Spooky,Christmas
  """


  if (message.startswith("-joke --help")):
    return get_joke_help_message()
  else:

    try:
      list_args = message.split("--")

      if (len(list_args) <= 1):
        return send_jokes_all()
        
      else:
        arg = list_args[1]

        if (len(arg) > 1):
          raise Exception("Please enter only one number after --")
        else:
          number = int(arg)
          if (number > len(jokes_categories)):
            raise Exception(f"Please enter number between 1 and {len(jokes_categories)}")

    
          return send_jokes_with_category(jokes_categories[number - 1])
    except ValueError:
      return("Please enter a number after -- \nEnter -joke --help for help")
    except Exception as e:
      return e + "\nEnter -joke --help for help"

