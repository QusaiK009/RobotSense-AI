
import unittest

from diagnostics import diagnose_motor


class TestMotorDiagnostics(unittest.TestCase):

    def test_normal_motor(self):

        # define case test

        readings = {"temperature_c": 60,"current_a": 1.5}

        result = diagnose_motor(readings)

        # check results

        self.assertEqual(result["status"], "normal")
        self.assertEqual(result["warnings"], [])

    def test_overheating(self):
        readings = {"temperature_c": 82,"current_a": 1.5}

        result = diagnose_motor(readings)

        self.assertEqual(result["status"], "warning")
        self.assertIn("Motor temperature too high",result["warnings"]
        )

    def test_overcurrent(self):
        readings = {"temperature_c": 60,"current_a": 3.5}

        result = diagnose_motor(readings)

        self.assertEqual(result["status"], "warning")
        self.assertIn("Motor current too high",result["warnings"])

if __name__ == "__main__":
    unittest.main(verbosity=2) #0 minimal out, 1 default output, 2 detailed out
