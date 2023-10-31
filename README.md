# cloudinteractive-ai-insights
This project is a collection of AI tools designed to assist with your assignments and projects.

Use Microsoft Azure Cognitive Service and OpenAI's ChatGPT API to help you focus on what truly matters.




### Table of Contents
* [Responsible use of Generative AI](#responsible-use-of-generative-ai)
* [Features](#features)
* [Requirements](#requirements)
* [Configuration](#configuration)
* [How to Use](#how-to-use)
* [Showcase](#showcase)

## Responsible use of Generative AI

[책임감 있는 AI 사용이란 무엇입니까? (국문)](https://github.com/Coppermine-SP/Coppermine-SP/blob/main/ResponsibleUseOfAI_KR.md)

**WARNING:**
This project should only be used as an auxiliary tool. Generative AI is not a solution provider for your assignment. Relying on this tool to fully complete your assignments is a clear act of cheating. 

**Please agree to the responsible use of Generative AI before utilizing this tool.**

## Features
- **Question Transcription**:   Easily transfer questions from question papers directly into a Jupyter Notebook.
- **Page Summarization**:   Get concise summaries of specific page contents.
- **Code Extraction**:   Extract code from images containing sample code effortlessly.
- **Custom Prompt**:   Use ChatGPT to process content from images or document pages as you need.

This project can easily integrate into Visual Studio Code via task.json.
## Requirements
This project uses Microsoft Azure Cognitive Services and OpenAI ChatGPT. 

**Note:** Usage might incur charges.

You will need:
- **OpenAI API Key**
- **Microsoft Azure Cognitive Services API Endpoint**
- **Microsoft Azure Cognitive Services API Key**

## Configuration
**config.json file must be present in the below directory:**

Linux, macOS
```
home/{username}/.cloudinteractive/ai-insights/config.json
```
Windows
```
C:\Users\{username}\.cloudinteractive\ai-insights\config.json
```
This file contains your API keys and endpoints. Ensure this file is kept secure to prevent unauthorized access.
If the configuration file does not exist, the below default configuration file will be created.
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
    "Endpoint": "https://secure.icloudint.corp",
    "OpenAI_Key": "key/openai_api",
    "AzureCV_Key": "key/azure_cv_api",
    "AzureCV_Endpoint": "endpoint/azure_cv_api"
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
  If fetching credentials from CloudInteractive Credential API, use `CloudInteractive`.

- **CloudInteractiveCredentialProvider**:
  
  **Note:** Not for Public use, only works within CloudInteractive Corporate Intranet.
  
  Defines CloudInteractive Credential API endpoints and options.
  For more details, please refer to [https://docs.cloudint.corp/credential](https://docs.cloudint.corp/credential).
  
- **Credentials**:

  Enter your Microsoft Azure Cognitive Services API Endpoint and Key, OpenAI API Key. JsonCredentialProvider will fetch credentials from here.
  
## How to Use

**Install package via pip:**
```
pip install cloudinteractive_ai_insights
```
Alternatively, you can clone this repository and run main.py.

**How to run script:**
```
ai-insights {location of source file} {additional argument}
```
```
python3 main.py {location of source file} {additional argument}
```

**Additional Arguments**:
- `--task`, `-t` : Specifies the task.   Options: `QuestionTranscipt`, `CodeExtrect`, `PageSummary`, `CustomPrompt`
- `--page`, `-p` : Specifies pages to import from the source document.
- `--out`, `-o` : Specifies out file path.
- `--prompt` : Specifies custom prompt for the CustomPrompt task.
- `--verbose` : Enable verbose status messages.
- `--no-warnings` : Suppress any warnings.


Example:
```
ai-insights "F:\MyDocument\PythonBook.pdf" --task QuestionTranscript --page 217 218 --out "F:\Paper\Python_Chapter_4.ipynb" --no-warnings
```

## Showcase
**Page summarization from the scanned document:**

  <img src="sample/doc_1.png">
  <img src="sample/result_1.png">



**Question transcription from scanned document:**

  <img src="sample/doc_2.png">
  <img src="sample/result_2.png">
  <img src="sample/result_3.png">
