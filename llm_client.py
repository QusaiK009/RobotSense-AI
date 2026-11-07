
import json
import os

from dotenv import load_dotenv
from google import genai

from diagnostics import diagnose_motor

load_dotenv()


def explain_diagnostics(diagnostic_result):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = (
        "You are assisting with a prototype robotics diagnostic application. The warning thresholds are illustrative, not validated safety limits. "
        "Explain the provided diagnostic findings in 2-3 sentences. Do not invent causes or claim that the thresholds are official. Explain the results like the user is 5. Preserve technical Accuracy \n\n"
        f"Diagnostic data:\n{json.dumps(diagnostic_result)}"
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    motor_data = {"temperature_c": 55,"current_a": 1.2}

    result = diagnose_motor(motor_data)

    explanation = explain_diagnostics(result)

    print("Rule-based diagnostics:")
    print(result)

    print("\nAI explanation:")
    print(explanation)
