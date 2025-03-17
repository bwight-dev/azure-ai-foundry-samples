# Azure AI Foundry Samples

This repository contains sample code for working with Azure AI Foundry, Microsoft's platform for building and deploying AI applications.

## Chat Completion Example

The `chat_example.py` script demonstrates how to use the Azure AI Foundry SDK to interact with deployed language models for chat completion tasks.

### Prerequisites

1. An Azure account with access to Azure AI Foundry
2. Python 3.8 or later
3. Required Python packages (see `requirements.txt`)

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/bwight-dev/azure-ai-foundry-samples.git
   cd azure-ai-foundry-samples
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Update the project details in `chat_example.py` with your Azure AI Foundry project information:
   - region
   - project_id
   - hub_name
   - project_name
   - model name

4. Run the example:
   ```bash
   python chat_example.py
   ```

## Authentication

The sample uses `DefaultAzureCredential` for authentication. Make sure you're logged in to Azure CLI (`az login`) or have appropriate credentials set up.

## Contributing

Feel free to submit issues and enhancement requests!