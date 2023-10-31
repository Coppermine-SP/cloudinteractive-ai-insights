# cloudinteractive-ai-insights / OpenAI ChatGPT API module
# Copyright (C) 2023 CloudInteractive.

import openai
import tiktoken
from typing import List
from typing import Final
from typing import Optional
from enum import Enum


def Init(api_key: str, no_warn: bool):
    openai.api_key = api_key
    global no_warning
    no_warning = no_warn

class OpenAIModel(Enum):
    gpt_4 = "gpt-4"
    gpt_35 = "gpt-3.5-turbo"


# first: request_price, second: response_price
OpenAIModelChargeTable: Final = {OpenAIModel.gpt_4: (0.00003, 0.00006), OpenAIModel.gpt_35: (0.0000015, 0.000002)}


def ChatCompletion(messages: List[str], role: str, model: OpenAIModel, verbose: bool = False) -> Optional[List[str]]:
    global no_warning
    result = []
    encoding = tiktoken.encoding_for_model(model.value)
    get_tokenlen = lambda x: len(encoding.encode(x))
    tokens = get_tokenlen(role) * len(messages)
    for content in messages:
        tokens += get_tokenlen(content)

    print(f"OpenAIChatCompletion: {len(messages)} messages.")
    print("WARNING: This Action uses the OpenAI API and you will be charged accordingly!")
    print("requests and responses are billed separately.")
    print(
        f"Estimated charge for this request{'s' if len(messages) > 1 else ''}: {OpenAIModelChargeTable[model][0] * tokens}$ ({tokens} tokens.)")

    user_input = ""
    count =1
    while user_input not in ['y', 'n']:
        if no_warning:
            user_input = 'y'
            print("")
        else:
            user_input = input("\nDo you want to continue? (y/n): ")
        if user_input == 'y':
            for message in messages:
                print(f"[{count}/{len(messages)}] - ", end="")
                try:
                    response = openai.ChatCompletion.create(
                        model=model.value,
                        messages=[
                            {"role": "system", "content": role},
                            {"role": "user", "content": message}
                        ],
                        temperature=0)
                except:
                    print("Failed!")
                    continue
                print("Completed.")
                print(
                    f"Estimated charge for this response: {OpenAIModelChargeTable[model][1] * response['usage']['completion_tokens']}$ ({response['usage']['completion_tokens']} tokens.)")
                result.append(response['choices'][0]['message']['content'])
                count += 1
                if verbose: print(f"[verbose]:\n{response['choices'][0]['message']['content']}\n")
        elif user_input == 'n':
            print("Task was cancelled by user.")
            return None
    return result
