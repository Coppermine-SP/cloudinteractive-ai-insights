# cloudinteractive-ai-insights / Microsoft Azure ComputerVision API module
# Copyright (C) 2023 CloudInteractive.
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import io
import time

_isInited = False
_vision_client = None


def Init(vision_key: str, vision_endpoint: str):
    _vision_endpoint = vision_endpoint
    _vision_key = vision_key
    _vision_client = ComputerVisionClient(vision_endpoint, CognitiveServicesCredentials(vision_key))
    _isInited = True


def OCRFromImageStreams(streams: [io.BytesIO]) -> [str]:
    print("Waiting for Microsoft Azure Congitive Service API...")
    count = 1;
    result_lst = []
    for buffer in streams:
        print(f"[{count}/{len(streams)}] - ", end="")
        result = ""
        response = _vision_client.read_in_stream(buffer, raw=True)
        operation_location = response.headers["Operation-Location"]
        operation_id = operation_location.split("/")[-1]
        while True:
            read_result = _vision_client.get_read_result(operation_id)
            if read_result.status not in ['notStarted', 'running']:
                break
            time.sleep(1)

        # Print the detected text, line by line
        if read_result.status == OperationStatusCodes.succeeded:
            for text_result in read_result.analyze_result.read_results:
                for line in text_result.lines:
                    result += line.text
            result_lst.append(result)
            print("Completed.")
        else:
            print("Failed!")
        count += 1
    print("All tasks are completed!")
    return result_lst
