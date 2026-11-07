
def diagnose_motor(readings):
    warnings = []

    if readings["temperature_c"] > 75:
        warnings.append("Motor temperature too high")

    if readings["current_a"] > 3.0:
        warnings.append("Motor current too high")

    return {
        "status": "warning" if warnings else "normal",
        "warnings": warnings,
        "measurements": readings
    }


if __name__ == "__main__":
    motor_data = {"temperature_c": 82,"current_a": 3.5}

    result = diagnose_motor(motor_data)
    print(result)
