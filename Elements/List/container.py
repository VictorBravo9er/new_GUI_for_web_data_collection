from typing import Callable
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from ..Field import EntryField


class Container:
    from ..data_entries import containers

    def __init__(self) -> None:
        self.entries: list[str | tuple[int, int]] | tuple[UploadedFile, Callable]
        self.content = st.container()
        with self.content:
            self.entries = [                 # type: ignore
                EntryField.make_container(**details)          # type: ignore
                for details in self.containers
            ]
        st.button(
            "submit", key="submit", on_click=self.upload_collected_data,
            # TODO:
            use_container_width=True
        )

    def upload_collected_data(self):
        ent = self.entries[1]
        print(ent)
      