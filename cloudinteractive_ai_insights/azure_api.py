# cloudinteractive-ai-insights / Microsoft Azure ComputerVision API module
# Copyright (C) 2023 CloudInteractive.
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import io
import time

isInited = False

def Init(vision_key: str, vision_endpoint: str):
    global __vision_client
    __vision_client = ComputerVisionClient(vision_endpoint, CognitiveServicesCredentials(vision_key))
    isInited = True


def OCRFromImageStreams(streams: [io.BytesIO], verbose: bool = False) -> [str]:
    global __vision_client
    print(f"OCRFromImageStreams: {len(streams)} images.")
    count = 1;
    result_lst = []
    for buffer in streams:
        print(f"[{count}/{len(streams)}] - ", end="")
        result = ""
        response = __vision_client.read_in_stream(buffer, raw=True)
        operation_location = response.headers["Operation-Location"]
        operation_id = operation_location.split("/")[-1]
        while True:
            read_result = __vision_client.get_read_result(operation_id)
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
            if verbose: print(f"[verbose]:\n{result}\n")
        else:
            print("Failed!")
        count += 1
    print("OCRFromImageStreams: Complete!\n")
    return result_lst
