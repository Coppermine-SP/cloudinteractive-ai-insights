from setuptools import setup, find_packages

setup(
    name="cloudinteractive-ai-insights",
    version="1.0.0",
    description="Collection of AI tools designed to assist with your assignments and projects.",
    author="CoppermineSP",
    author_email="copperminesp@cloudinteractive.net",
    url="https://github.com/Coppermine-SP/cloudinteractive-ai-insights",
    install_requires=["azure-cognitiveservices-vision-computervision","openai","pdf2image","tiktoken"],
    python_requires=">=3.9",
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    entry_points={
        'console_scripts': [
            'ai-insight = cloudinteractive-ai-insights.main:main',
        ],
    }
)