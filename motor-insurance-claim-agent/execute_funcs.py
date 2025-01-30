from promptflow.core import tool
import requests
import json

def validate_policy_number(policy_number: str) -> str:
    api_url = f"https://emc-b2b-api.azurewebsites.net/api/XAgents/ClaimAgentValidatePolicy/{policy_number}"
    
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            
            if data.get("exists"):
                return "The policy number exists in DB. Proceed next."
            else:
                return "The policy number not found. Ask the user to provide correct policy number."
        else:
            return f"Failed to validate policy number. API returned status code {response.status_code}."
    except Exception as e:
        return f"An error occurred while validating the policy number: {str(e)}"

@tool
# Function to handle execution of other functions based on a response message
# This allows dynamic function calls with arguments passed in a structured format
def run_functions(response_message: dict) -> str:
    # Check if there is a function call in the response message
    function_call = response_message.get("function_call", None)
    if function_call and "name" in function_call and "arguments" in function_call:
        # Extract the function name and arguments from the response message
        function_name = function_call["name"]
        function_args = json.loads(function_call["arguments"])
        print(function_args) # Debug: Print the arguments for the function call

        # Dynamically call the function by name using globals() and pass the arguments
        result = globals()[function_name](**function_args)
    else:
        print("No function call") # Debug: Indicate no function call was found

        result = response_message.get("content", None)

    # Return the result of the function call or the response message content
    return result