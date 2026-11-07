
from diagnostics import diagnose_motor


def diagnose_system(motors):
    results = []

    for motor in motors:
        readings = {
            "temperature_c": motor["temperature_c"],
            "current_a": motor["current_a"]
        }

        diagnosis = diagnose_motor(readings)

        results.append({
            "motor_id": motor["motor_id"],
            **diagnosis
        })

    warning_count = sum(
        motor["status"] == "warning"
        for motor in results
    )

    return {
        "system_status": "warning" if warning_count else "normal",
        "total_motors": len(results),
        "motors_with_warnings": warning_count,
        "motors": results
    }


if __name__ == "__main__":

    motors = [
        {"motor_id": "M1", "temperature_c": 54, "current_a": 1.8},
        {"motor_id": "M2", "temperature_c": 82, "current_a": 3.5},
        {"motor_id": "M3", "temperature_c": 64, "current_a": 2.1}
    ]

    result = diagnose_system(motors)

    print(result)
