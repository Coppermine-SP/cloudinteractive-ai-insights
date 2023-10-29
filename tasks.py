# cloudinteractive-ai-insights / actions
# Copyright (C) 2023 CloudInteractive.
import argparse
import document
import azure_api
import openai_api


def QuestionTranscript(args: argparse.Namespace):
    print("Task: QuestionTranscript")

    role = "당신은 문제지 출제자입니다. 문서를 OCR한 문자열에서 각 문제를 띄워쓰기와 문법을 보정하고 요약하여 문제만 줄 단위로 정리하시오.문제에 번호는 붙이지 않는다."
    if args.filename[0].endswith(".pdf"):
        stream = document.ConvertToImageStreams(list(map(int, args.pages)), args.filename[0])
        if not args.pages:
            print("[ERROR]: pages option is required!")
            return
    elif args.filename[0].endswith(".png"):
        stream = document.LoadImagetoStream(args.filename[0])
    else:
        print("[ERROR]: Unsupported file type.")
        return

    text = azure_api.OCRFromImageStreams(stream, args.verbose)
    response = openai_api.ChatCompletion(text, role, openai_api.OpenAIModel.gpt_4, args.verbose)
    if response is None:
        return

    cells = []
    idx = 1
    if not args.out.endswith(".ipynb"): args.out += ".ipynb"
    with open(f"{args.out}", "w", encoding="utf-8") as notebook_file:
        print("Writing Jupyter Notebook file..")
        for x in response:
            for question in x.split("\n"):
                if not question.isspace() and question != "":
                    cells.append(("markdown", f"**{idx}. {__questionNormalization(question)}**"))
                    cells.append(("code", ""))
                    idx += 1
        notebook_file.write(document.create_notebook(cells))
    print("Complete!")


def PageSummary(args: argparse.Namespace):
    pass


def CodeExtrect(args: argparse.Namespace):
    pass


def __questionNormalization(string: str) -> str:
    quotes = ["'", '"', "`"]
    if string[:2] == "- ":
        return string[2:]
    elif string[0] in quotes and string[-1] in quotes:
        return string[1:len(string) - 1]
    elif string[0].isdigit() and string[1] == ".":
        return string[2:].lstrip()
    else:
        return string


global actions
actions = {"QuestionTranscript": QuestionTranscript, "PageSummary": PageSummary, "CodeExtract": CodeExtrect}
