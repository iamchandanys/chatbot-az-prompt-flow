from promptflow.core import tool
from promptflow.contracts.multimedia import Image as PFImage
from PIL import Image as Image
import io

def process_questions(questions):
    updated_questions = questions.copy()
   
    for question in questions:
        if isinstance(questions, list):
            for item in questions:
                if "image" in str(type(item)).lower():
                    return updated_questions
                
    return "DO NOT DETECT"

@tool
def my_python_tool(questions: list) -> str:
   result = process_questions(questions)
   return result