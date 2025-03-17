from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

def main():
    try:
        # Azure AI Foundry project details
        region = "eastus2"
        project_id = "78b0f7fe-2d0e-4ae5-9d5c-fc31e6cf75de"
        hub_name = "rg-wightbrad-7033_ai"
        project_name = "wightbrad-2624"

        # Construct the connection string
        project_connection_string = f"{region}.api.azureml.ms;{project_id};{hub_name};{project_name}"
        
        print("Initializing Azure AI Foundry client...")
        project_client = AIProjectClient.from_connection_string(
            credential=DefaultAzureCredential(),
            conn_str=project_connection_string,
        )

        print("Getting chat completions client...")
        chat = project_client.inference.get_chat_completions_client()

        # Get a chat completion based on a user-provided prompt
        user_prompt = input("\nEnter your question: ")
        print("\nGenerating response...")

        response = chat.complete(
            model="Phi-4",  # Replace with your deployed model name
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that answers questions."},
                {"role": "user", "content": user_prompt},
            ],
        )
        
        print("\nResponse:")
        print(response.choices[0].message.content)

    except Exception as ex:
        print(f"\nError occurred: {str(ex)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure you have the correct Azure AI Foundry project details")
        print("2. Verify you have proper authentication set up (DefaultAzureCredential)")
        print("3. Check if you have access to the specified project and model")
        print("4. Ensure you're using the correct region")

if __name__ == "__main__":
    main()