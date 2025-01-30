from promptflow.core import tool
import json
import requests

def submit_inspection(front_image: str, back_image: str, left_image: str, right_image: str, car_number: str) -> str:
    submit_api_url = "https://emc-b2b-api.azurewebsites.net/api/XAgents/SaveAIGenericData/submit_inspection"

    try:
        payload_data = json.dumps({
            "front_image": front_image,
            "back_image": back_image,
            "left_image": left_image,
            "right_image": right_image,
            "car_number": car_number
        })

        payload = {
            "data": payload_data
        }

        # payload_json = json.dumps(payload)
      
        submit_response = requests.post(submit_api_url, json=payload, headers={"Content-Type": "application/json"})
      
        if submit_response.status_code == 200:
            return "The inspection has been submitted successfully. An insurance representative will review it, and the policy will be issued based on the results. Thank you!"
        else:
            return "Something went wrong on our end."
    except Exception:
        return "Something went wrong on our end."

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