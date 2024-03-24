from typing import Callable
from .Field import FieldTypes

containers: list[dict[(str, str|None|Callable)]] = [
    {
        "name": "Website Name",
        "type_": FieldTypes.text,
        "callback": str
    },
    {
        "name":"Age",
        "type_": FieldTypes.age,
        "callback": lambda x: {
            "years":x[0],
            "months": x[1]}
    },
    {
        "name":"Niche", 
        "type_": FieldTypes.text,
        "callback": str
    },
    {
        "name":"DA/PA", 
        "type_": FieldTypes.file,
        "callback": None
    },
    {
        "name":"Performance Data", 
        "type_": FieldTypes.file,
        "callback": None
    },
    {
        "name":"AHREFS", 
        "type_": FieldTypes.file,
        "callback": None
    },
    {
        "name":"Monetization", 
        "type_": FieldTypes.file,
        "callback": None
    },
    {
        "name":"Revenue Data", 
        "type_": FieldTypes.file,
        "callback": None
    },
]

