from promptflow.core import tool
import requests
import json

def submit_claim(policy_number: str, reason_for_claim: str, date_of_incident: str) -> str:
    api_url = "https://emc-b2b-api.azurewebsites.net/api/XAgents/SaveAIGenericData/submit_claim"

    try:
        payload_data = json.dumps({
            "policyNumber": policy_number,
            "reasonForClaim": reason_for_claim,
            "dateOfIncident": date_of_incident
        })

        payload = {
            "data": payload_data
        }

        response = requests.post(api_url, json=payload, headers={"Content-Type": "application/json"})

        if response.status_code == 200:
            return "Thank you! Your motor insurance claim has been successfully submitted. Let us know if you need any further assistance."
        else:
            return f"Failed to submit claim. Status code: {response.status_code}, Response: {response.text}"
    except Exception as e:
        return f"An error occurred while submitting the claim: {str(e)}"

@tool
def run_functions(response_message: dict) -> str:
    function_call = response_message.get("function_call", None)

    if function_call and "name" in function_call and "arguments" in function_call:
        function_name = function_call["name"]
        function_args = json.loads(function_call["arguments"])
        result = globals()[function_name](**function_args)
    else:
        result = response_message.get("content", None)

    return result
