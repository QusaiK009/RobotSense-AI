
import unittest
from unittest.mock import patch

from app import app


class TestDiagnosticsAPI(unittest.TestCase):

    def test_valid_diagnostics_request(self):

        client = app.test_client()

        readings = {"temperature_c": 82,"current_a": 3.5}

        with patch("app.explain_diagnostics",return_value="Simulated AI explanation"): #patch the explain_diagnostics function to bypass Google's AI servers just for the test of Flask. This returns the predefined string
            response = client.post("/diagnose",json=readings)

        result = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], "warning")
        self.assertEqual(result["ai_status"], "ok")
        self.assertEqual(result["ai_explanation"],"Simulated AI explanation")

    def test_llm_failure(self): # this tests if Google servers for example are down (like 503 or 404 error), it should in theory run the 'except' block in our app.py file and still handle this error well.

        client = app.test_client()

        readings = {"temperature_c": 82,"current_a": 3.5}

        with patch("app.explain_diagnostics",side_effect=RuntimeError("Simulated Gemini outage")): # just as with patch, this raises an exception
            response = client.post("/diagnose",json=readings)

        result = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], "warning")
        self.assertEqual(result["ai_status"], "unavailable")
        self.assertIsNone(result["ai_explanation"])

        self.assertIn("Motor temperature too high",result["warnings"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
