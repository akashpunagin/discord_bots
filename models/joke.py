# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = joke_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Flags:
    nsfw: bool
    religious: bool
    political: bool
    racist: bool
    sexist: bool
    explicit: bool

    def __init__(self, nsfw: bool, religious: bool, political: bool, racist: bool, sexist: bool, explicit: bool) -> None:
        self.nsfw = nsfw
        self.religious = religious
        self.political = political
        self.racist = racist
        self.sexist = sexist
        self.explicit = explicit

    @staticmethod
    def from_dict(obj: Any) -> 'Flags':
        assert isinstance(obj, dict)
        nsfw = from_bool(obj.get("nsfw"))
        religious = from_bool(obj.get("religious"))
        political = from_bool(obj.get("political"))
        racist = from_bool(obj.get("racist"))
        sexist = from_bool(obj.get("sexist"))
        explicit = from_bool(obj.get("explicit"))
        return Flags(nsfw, religious, political, racist, sexist, explicit)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nsfw"] = from_bool(self.nsfw)
        result["religious"] = from_bool(self.religious)
        result["political"] = from_bool(self.political)
        result["racist"] = from_bool(self.racist)
        result["sexist"] = from_bool(self.sexist)
        result["explicit"] = from_bool(self.explicit)
        return result


class Joke:
    error: bool
    category: str
    type: str
    setup: str
    delivery: str
    flags: Flags
    id: int
    safe: bool
    lang: str
    joke: str

    def __init__(self, error: bool, category: str, type: str, setup: str, delivery: str, flags: Flags, id: int, safe: bool, lang: str, joke: str) -> None:
        self.error = error
        self.category = category
        self.type = type
        self.setup = setup
        self.delivery = delivery
        self.flags = flags
        self.id = id
        self.safe = safe
        self.lang = lang
        self.joke = joke

    @staticmethod
    def from_dict(obj: Any) -> 'Joke':
        assert isinstance(obj, dict)
        error = from_bool(obj.get("error"))
        category = from_str(obj.get("category"))
        type = from_str(obj.get("type"))
        
        if obj.get("setup") is None:
          setup = ""
        else:
          setup = from_str(obj.get("setup"))
        
        if obj.get("delivery") is None:
          delivery = ""
        else:
          delivery = from_str(obj.get("delivery")) 

        if obj.get("joke") is None:
          joke = ""
        else:
          joke = from_str(obj.get("joke"))
        
        flags = Flags.from_dict(obj.get("flags"))
        id = from_int(obj.get("id"))
        safe = from_bool(obj.get("safe"))
        lang = from_str(obj.get("lang"))
        return Joke(error, category, type, setup, delivery, flags, id, safe, lang, joke)

    def to_dict(self) -> dict:
        result: dict = {}
        result["error"] = from_bool(self.error)
        result["category"] = from_str(self.category)
        result["type"] = from_str(self.type)
        result["setup"] = from_str(self.setup)
        result["delivery"] = from_str(self.delivery)
        result["flags"] = to_class(Flags, self.flags)
        result["id"] = from_int(self.id)
        result["safe"] = from_bool(self.safe)
        result["lang"] = from_str(self.lang)
        result["joke"] = from_str(self.joke)
        return result


def joke_from_dict(s: Any) -> Joke:
    return Joke.from_dict(s)


def joke_to_dict(x: Joke) -> Any:
    return to_class(Joke, x)
