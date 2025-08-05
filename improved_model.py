import json
import google.generativeai as genai
from config import GEMINI_API_KEY
from json import JSONDecodeError

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def get_storage_report(crop_name):
    # Structured prompt for consistent JSON response
    structured_prompt = f"""
    Generate a comprehensive storage report for {crop_name} in JSON format with the following structure:
    {{
        "temperature": "optimal temperature range with units",
        "humidity": "ideal humidity percentage",
        "ventilation": "ventilation requirements description",
        "container": "recommended storage container type",
        "duration": "maximum storage duration with time units",
        "preservation_tips": ["list", "of", "preservation techniques"],
        "pests": ["list", "of", "common pests"],
        "disease_prevention": ["list", "of", "disease prevention methods"],
        "warning_signs": ["list", "of", "spoilage indicators"]
    }}
    
    Include detailed technical information suitable for agricultural professionals.
    Provide metric units for all measurements.
    List at least 3 items for array fields.
    """
    
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(structured_prompt)
        
        # Clean and parse the response
        response_text = response.text.strip()
        response_text = response_text.replace('```json', '').replace('```', '').strip()
        
        report_data = json.loads(response_text)
        
        # Ensure all required fields are present
        required_fields = ['temperature', 'humidity', 'ventilation', 'container',
                          'duration', 'preservation_tips', 'pests',
                          'disease_prevention', 'warning_signs']
        
        for field in required_fields:
            if field not in report_data:
                raise ValueError(f"Missing required field: {field}")
                
        return report_data
        
    except JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON response: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Error generating storage report: {str(e)}")