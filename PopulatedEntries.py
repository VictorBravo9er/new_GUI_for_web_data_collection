from Elements.List import EntryData
from Elements.Field import EntryField
from entries import entries

# TODO need to re work this one. probably heavy refactoring


entries = EntryData(
    [
        EntryField(
            entry[0],*((True, entry[1]) if len(entry) == 2 else (False, "") )
        ) for entry in entries
    ]
)


