# cloudinteractive-ai-insights / actions
# Copyright (C) 2023 CloudInteractive.
import argparse
import document
import azure_api


def QuestionTranscript(args: argparse.Namespace):
    print("Task: QuestionTranscript")
    if not args.pages:
        print("[ERROR]: pages option is required!")
        return

    streams = document.ConvertToImageStreams(list(map(int, args.pages)), args.filename[0])
    contents = azure_api.OCRFromImageStreams(streams, args.verbose)


def PageSummary(args: argparse.Namespace):
    pass

def CodeExtrect(args: argparse.Namespace):
    pass

global actions
actions = {"QuestionTranscript" : QuestionTranscript, "PageSummary" : PageSummary, "CodeExtract" : CodeExtrect}