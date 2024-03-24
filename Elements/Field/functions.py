from enum import Enum
from typing import Callable
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile


class EntryField:

    @staticmethod
    class FieldTypes(Enum):
        text = "str"
        age = "age"
        file = "file"

    @staticmethod
    def select_text(name: str):
        return st.text_input(
            name, key=name,
            help=f"Enter the {name}"
        )

    @staticmethod
    def select_age(name: str) -> tuple[int, int]: 
        years = range(0,101)
        months = range(0,12)
        col1,col2 = st.columns(2)
        with col1:
            selected_year = st.selectbox(
                label=name+" (years)", options=years, key=name+"years",
                help=f"Select age in years"
            )
        with col2:
            selected_months = (st.selectbox(
                label=name+" (months)", options=months, key=name+"months",
                help=f"Select age in months"
            ))
        return (selected_year, selected_months)       # type: ignore

    @staticmethod
    def get_data_from_file(name) -> UploadedFile | None:
        file = st.file_uploader(
            name, accept_multiple_files=False,
            key=name, help=f"Select the {name} file",
            # type=["csv"]
        )
        if file:
            file_details = file.read()
            st.text_area(f"What's in {name}", key=f"{name} {file_details}",value=file_details.decode("utf-8"), height=32)
            return file
        return 
        # return callback(file)  

    @staticmethod
    def make_container(name: str, type_: str, **_) -> str | tuple[int, int] | UploadedFile | None:
        match type_:
            case EntryField.FieldTypes.text:
                return EntryField.select_text(name)
            case EntryField.FieldTypes.age:
                return EntryField.select_age(name)
            case EntryField.FieldTypes.file:
                return EntryField.get_data_from_file(name)

        raise Exception(
            "something went wrong\n"
        )
