# cloudinteractive-ai-insights / Document module
# Copyright (C) 2023 CloudInteractive.

from pdf2image import convert_from_path
from typing import List
import io
import json
import PIL.Image


def ConvertToImageStreams(pages: List[int], path: str) -> List[io.BytesIO]:
    array = []
    print(f"ConvertToImageStreams : {path} / {len(pages)} pages.")
    for page in pages:
        print(f"Converting page {page} to image..")
        buffer = io.BytesIO()
        image = convert_from_path(path, first_page=page, last_page=page)
        image[0].save(buffer, format="PNG")
        buffer.seek(0)
        array.append(buffer)
    print("Complete!\n")
    return array

def LoadImagetoStream(path: str) -> List[io.BytesIO]:
    img = PIL.Image.open(path).convert("RGB")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return [buffer]


def create_notebook(cells):
    notebook_content = {
        "cells": [],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5
    }

    for cell_type, source in cells:
        cell = {
            "cell_type": cell_type,
            "metadata": {},
            "source": [source]
        }
        if cell_type == "code":
            cell["outputs"] = []
            cell["execution_count"] = None

        notebook_content["cells"].append(cell)

    return json.dumps(notebook_content, indent=4)