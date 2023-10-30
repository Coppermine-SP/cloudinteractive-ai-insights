#!/usr/bin/env python3

# cloudinteractive-ai-insights
# Copyright (C) 2023 CloudInteractive.

import azure_api as azure
import openai_api as openai
from credentialprovider import *
import document
import json
import azure_api
import argparse
import os.path
import tasks
import openai_api

CONFIG_FILE_NAME = "config.json"
global credentials


def main(args):
    print("CloudInteractive ai-insights 1.0.0")
    print("Copyright(C) 2023 CloudInteractive.\n")
    if not os.path.exists(f"{os.getcwd()}\\{CONFIG_FILE_NAME}"):
        print(f"[ERROR] There is no {CONFIG_FILE_NAME} file!\nPlease see the repository readme to configure.")
        return

    if not get_credentials(): return
    azure_api.Init(credentials["AzureCV_Key"], credentials["AzureCV_Endpoint"])
    openai_api.Init(credentials["OpenAI_Key"], args.no_warnings)
    if args.task[0] not in tasks.actions:
        print(f"[ERROR] Task '{args.task[0]}' is not valid task.")
        return

    if args.out == "":
        print("WARNING: Outfile name is not configured!\nUsing default outfile name.\n")
        args.out = args.filename[0].split('.')[0]
    else:
        args.out = args.out[0]

    tasks.actions[args.task[0]](args)


def get_credentials() -> bool:
    global credentials
    credentials = {"OpenAI_Key": None, "AzureCV_Endpoint": None, "AzureCV_Key": None}

    print("Loading credentials...")
    try:
        with open(CONFIG_FILE_NAME, "r") as handle:
            config = json.load(handle)
        providerName = config["CredentialProvider"]

        if providerName not in ["Json", "CloudInteractive"]:
            print(f"[ERROR] {providerName} is not vaild CredentialProvider. Please check config.json file!")
            return False
        providerConfig = config[providerName + "CredentialProvider"]
        print(f"Provider: {providerName}CredentialProvider\n")
        providerObject = JsonCredentialProvider(CONFIG_FILE_NAME, providerConfig["ObjectName"]) \
            if providerName == "Json" else CloudinteractiveCredentialProvider(providerConfig["Endpoint"])
    except Exception as e:
        print(f"[ERROR] Exception in CredentialProvider : {e}")
        return False

    for key in credentials.keys():
        credentials[key] = providerObject.getCredential(providerConfig[key])
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs='+', help='Example) example.pdf', dest='filename')
    parser.add_argument('--pages', '-p', nargs='*', help='Example) 11 12 13', default=[], dest='pages')
    parser.add_argument('--task', '-t', nargs="*", help="Example) CodeExteraction", default="None", dest='task')
    parser.add_argument('--out', '-o', nargs='*', help='Example) Chapter_5', default="", dest='out')
    parser.add_argument('--prompt', default="", dest="prompt")
    parser.add_argument('--verbose', action="store_true", dest="verbose")
    parser.add_argument('--no-warnings', action="store_true", dest="no_warnings")
    main(parser.parse_args())
