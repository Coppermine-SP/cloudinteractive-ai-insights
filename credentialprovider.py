# cloudinteractive-ai-insights / credentialprovider module.
# Copyright (C) 2023 CloudInteractive.
from abc import *
import requests
import json


class CredentialProvider(metaclass=ABCMeta):
    @abstractmethod
    def getCredential(self, key: str) -> str:
        pass

    def __init__(self, endpoint: str):
        self.endpoint = endpoint

class CloudinteractiveCredentialProvider(CredentialProvider):
    def __init__(self, endpoint: str):
        super().__init__(endpoint)

    def getCredential(self, key: str) -> str:
        response = requests.get(f"{self.endpoint}/{key}", verify=False)
        if response.status_code != 200:
            raise ConnectionError(f"{response} from server.")
        else:
            return response.text

class JsonCredentialProvider(CredentialProvider):
    def __init__(self, fileName:str, ObjectName: str):
        super().__init__(fileName)
        self.ObjectName = ObjectName
        with open(fileName, "r") as handle:
            self.json_data = json.load(handle)[self.ObjectName]

    def getCredential(self, key: str) -> str:
        value = self.json_data[key]
        if value is None:
            raise LookupError(f"key {key} does not exists.")
        else:
            return value