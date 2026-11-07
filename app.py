
from flask import Flask, jsonify, request

from diagnostics import diagnose_motor
from llm_client import explain_diagnostics

app = Flask(__name__)

@app.route("/diagnose", methods=["POST"])
def diagnose():
    readings = request.get_json(silent=True)

    if not isinstance(readings, dict):
        return jsonify({"error": "Expected a JSON object"}), 400

    for key in ("temperature_c", "current_a"):
        if type(readings.get(key)) not in (int, float):
            return jsonify({"error": f"{key} must be a number"}), 400

    
    result = diagnose_motor(readings)

    try:
        explanation = explain_diagnostics(result)
        result["ai_explanation"] = explanation
        result["ai_status"] = "ok" if explanation else "empty_response"

    except Exception: #This is to protect us if google's specific model server experiences an 'unavailable' error which causes Flask to throw a server error. This makes the AI service for us an OPTION rather than a requirement
        app.logger.exception("LLM explanation failed")
        result["ai_explanation"] = None
        result["ai_status"] = "unavailable"

    return jsonify(result) #This will sort dictionary headings in alphabetical order, so measurements -> status -> warnings

if __name__ == "__main__":
    app.json.sort_keys = False #this preserves the order of the JSON keys (this is for me to see the display in powershell terminal. Future apps will just request the specific JSON key, e.g "status")
    app.run(debug=True)
    
