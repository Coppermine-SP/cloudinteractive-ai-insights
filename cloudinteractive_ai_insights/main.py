#!/usr/bin/env python3

# cloudinteractive-ai-insights
# Copyright (C) 2023 CloudInteractive.

import json
import argparse
import os.path
from pathlib import Path
import cloudinteractive_ai_insights.tasks as tasks
import cloudinteractive_ai_insights.openai_api as openai_api
import cloudinteractive_ai_insights.azure_api as azure_api
from cloudinteractive_ai_insights.credentialprovider import *

__CONFIG_FILE_NAME = f"config.json"
__CONFIG_PATH = f"{Path.home()}{os.sep}.cloudinteractive{os.sep}ai-insights{os.sep}"
__CONFIG_FILE_PATH = f"{__CONFIG_PATH}{__CONFIG_FILE_NAME}"
__DEFAULT_CONFIG_FILE_CONTENT = '''{
  "CredentialProvider" : "Json",
  "JsonCredentialProvider" : {
    "ObjectName": "Credentials",
    "OpenAI_Key" : "OpenAI_API_Key",
    "AzureCV_Key": "AzureCV_Key",
    "AzureCV_Endpoint" : "AzureCV_Endpoint"
  },
  "CloudInteractiveCredentialProvider": {
    "Endpoint": "https://secure.icloudint.corp",
    "OpenAI_Key": "key/openai_api",
    "AzureCV_Key": "key/azure_cv_api",
    "AzureCV_Endpoint": "endpoint/azure_cv_api"
  },
  "Credentials" : {
    "OpenAI_API_Key": "YOUR_OPENAI_API_KEY",
    "AzureCV_Key": "YOUR_AZURECV_KEY",
    "AzureCV_Endpoint": "YOUR_AZURECV_ENDPOINT"
  }
}
'''

global credentials


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs='+', help='Example) example.pdf', dest='filename')
    parser.add_argument('--pages', '-p', nargs='*', help='Example) 11 12 13', default=[], dest='pages')
    parser.add_argument('--task', '-t', nargs="*", help="Example) CodeExteraction", default="None", dest='task')
    parser.add_argument('--out', '-o', nargs='*', help='Example) Chapter_5', default="", dest='out')
    parser.add_argument('--prompt', default="", dest="prompt")
    parser.add_argument('--verbose', action="store_true", dest="verbose")
    parser.add_argument('--no-warnings', action="store_true", dest="no_warnings")
    args = parser.parse_args()

    print("CloudInteractive ai-insights 1.0.0")
    print("Copyright(C) 2023 CloudInteractive.\n")

    if not __check_config_file(): return
    if not __get_credentials(): return
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


def __check_config_file() -> bool:
    if not os.path.exists(__CONFIG_FILE_PATH):
        print(
            f"[ERROR] There is no configuration file!\nPlease see the repository readme to configure.\nfile location: {__CONFIG_FILE_PATH}")
        try:
            os.makedirs(__CONFIG_PATH, exist_ok=True)
            with open(__CONFIG_FILE_PATH, "w") as handle:
                handle.write(__DEFAULT_CONFIG_FILE_CONTENT)
        except Exception as e:
            print(f"[ERROR] Exception while creating default config file:\n{e}")
        return False
    else:
        return True


def __get_credentials() -> bool:
    global credentials
    credentials = {"OpenAI_Key": None, "AzureCV_Endpoint": None, "AzureCV_Key": None}

    print("Loading credentials...")
    try:
        with open(__CONFIG_FILE_PATH, "r") as handle:
            config = json.load(handle)
        providerName = config["CredentialProvider"]

        if providerName not in ["Json", "CloudInteractive"]:
            print(f"[ERROR] {providerName} is not vaild CredentialProvider. Please check config.json file!")
            return False
        providerConfig = config[providerName + "CredentialProvider"]
        print(f"Provider: {providerName}CredentialProvider\n")
        providerObject = JsonCredentialProvider(__CONFIG_FILE_NAME, providerConfig["ObjectName"]) \
            if providerName == "Json" else CloudinteractiveCredentialProvider(providerConfig["Endpoint"])
    except Exception as e:
        print(f"[ERROR] Exception in CredentialProvider : {e}")
        return False

    for key in credentials.keys():
        credentials[key] = providerObject.getCredential(providerConfig[key])
    return True

if __name__ == '__main__':
    main()
