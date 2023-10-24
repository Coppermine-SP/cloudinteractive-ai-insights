# cloudinteractive-ai-insights
This project is a collection of AI tools designed to assist with your assignments and projects.

Use Microsoft Azure Cognitive Service and OpenAI's ChatGPT API to help you focus on what matters.




### Table of Contents
* [Responsible use of Generative AI](#responsible-use-of-generative-ai)
* [Features](#features)
* [Requirements](#requirements)
* [Configuration](#configuration)
* [Installation](#installation)
* [How to use](#how-to-use)
* [Showcase](#showcase)

## Responsible use of Generative AI
**WARNING:**
This project should only be used as an auxiliary tool. Generative AI is not a solution provider for your assignment. Relying on this tool to fully complete your assignments is a clear act of cheating. 

**Please agree to the responsible use of Generative AI before utilizing this tool.**

## Features
- **Problem Transcription**:   Easily transfer problems from question papers directly into a Jupyter Notebook.
- **Page Summarization**:   Get concise summaries of specific page contents.
- **Code Extraction**:   Extract code from images containing sample code effortlessly.
- **Custom Prompt**:   Use ChatGPT to process content from images or document pages as you need.

This project can easily integrate into Visual Studio Code via task.json.
## Requirements
This project uses Microsoft Azure Cognitive Services and OpenAI ChatGPT. 
Please note: Usage might incur charges.

You will need:
- **OpenAI API Key**
- **Microsoft Azure Cognitive Services API Endpoint**
- **Microsoft Azure Cognitive Services API Key**

## Configuration
config.json file must be present in the program directory.
This file contains your API keys and endpoints. Ensure this file is kept secure to prevent unauthorized access.

```
{
  "CredentialProvider" : "Json",
  "JsonCredentialProvider" : {
    "ObjectName": "Credentials",
    "OpenAI_Key" : "OpenAI_API_Key",
    "AzureCV_Key": "AzureCV_Key",
    "AzureCV_Endpoint" : "AzureCV_Endpoint"
  },
  "CloudInteractiveCredentialProvider": {
    "Endpoint": "https://secure.cloudint.corp",
    "OpenAI_Key": "key/openai",
    "AzureCV_Key": "key/azure_cv",
    "AzureCV_Endpoint": "endpoint/azure_cv"
  },
  "Credentials" : {
    "OpenAI_API_Key": "YOUR_OPENAI_KEY",
    "AzureCV_Key": "YOUR_AZURECV_KEY",
    "AzureCV_Endpoint": "YOUR_AZURECV_ENDPOINT"
  }
}
```

- **CredentialProvider**: `Json` or `CloudInteractive`.
  
  Use `Json` if fetching credentials directly from this configuration file.
  or fetching credentials from CloudInteractive Credential API, use `CloudInteractive`.

- **CloudInteractiveCredentialProvider**:

  Defines CloudInteractive Credential API endpoints and options.
  For more details, please refer to [https://docs.cloudint.corp/credential](https://docs.cloudint.corp/credential).

- **Credentials**:

  Enter your Microsoft Azure Cognitive Services API Endpoint and Key, OpenAI API Key. JsonCredentialProvider will fetch credentials from here.
