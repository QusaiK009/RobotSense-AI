# RobotSense AI

A Python-based robotics diagnostics prototype integrating deterministic fault detection, Flask REST APIs, and Google Gemini AI to generate human-readable explanations of simulated motor measurements.

## Overview

RobotSense AI demonstrates how conventional engineering logic can be combined with generative AI within a backend application.

The system receives motor measurements through a REST API, evaluates them against predefined thresholds, and uses Google's Gemini API to explain the resulting diagnostic findings.

The deterministic rules operate independently of the language model, allowing diagnostic results to remain available even when the AI service fails.

**Project status:** Functional learning prototype.

**Data:** All measurements and thresholds are simulated for demonstration purposes.

## Features

- Rule-based motor diagnostics using Python
- Temperature and current threshold monitoring
- REST API using Flask
- JSON request validation and structured responses
- Google Gemini LLM integration
- Error handling for unavailable LLM services
- Environment-based API key management
- Automated unit testing using Python's `unittest`

## System Architecture

```text
Client (HTTP POST)
        |
        v
Flask REST API (app.py)
        |
        v
Diagnostic Engine (diagnostics.py)
        |
        v
Gemini Integration (llm_client.py)
        |
        v
Combined JSON Response
```

The diagnostic engine determines warning conditions using predefined engineering rules. The LLM provides explanatory text but does not determine warning status or override the diagnostic results.

## Technology Stack

- Python 3.13
- Flask
- Google Gemini API
- python-dotenv
- Python unittest
- Git and GitHub

## Installation

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Copy `.env.example` to `.env`.
5. Add your Gemini API key to `.env`.
6. Start the Flask application:

```bash
python app.py
```

The application runs locally at:

`http://127.0.0.1:5000`

## API Usage

### POST /diagnose

Example JSON request:

```json
{
  "temperature_c": 82,
  "current_a": 3.5
}
```

The endpoint returns:

- Original motor measurements
- Overall diagnostic status
- Detected warning messages
- AI-generated diagnostic explanation
- AI service availability status

## Diagnostic Rules

The current prototype uses these illustrative thresholds:

| Parameter | Warning condition |
|---|---|
| Motor temperature | Greater than 75°C |
| Motor current | Greater than 3.0 A |

These values are hardcoded for demonstration purposes and do not represent validated manufacturer operating limits.

## Multi-Actuator Diagnostics

RobotSense AI also supports evaluating multiple simulated robotic actuators through a reusable Python diagnostic module.

The `system_diagnostics.py` module processes a collection of motor measurements, evaluates each motor using the existing deterministic diagnostic rules, and generates a system-level summary.

**Current functionality:**
- Supports multiple motors identified by unique motor IDs.
- Evaluates temperature and current independently for each motor.
- Identifies motors exceeding illustrative warning thresholds.
- Counts the total number of motors and those reporting warnings.
- Reports an overall system status.

**Example:** A simulated system containing three motors, one of which exceeds both warning thresholds, produces an overall warning status with one affected motor.

The multi-actuator module currently runs as a standalone Python component. The Flask `/diagnose` endpoint supports individual motor readings; a dedicated multi-actuator API endpoint is a planned extension.

All readings and thresholds are simulated. The module is not validated for real-time industrial condition monitoring.

## Automated Testing

Automated tests are implemented using Python's built-in `unittest` framework.

The verified test cases include:

- Normal motor conditions
- Motor overheating detection

The tests verify that the diagnostic engine produces the expected status and warning messages.

To run the tests:

```bash
python -m unittest -v test_diagnostics
```

Tests can also be executed directly through VS Code using Code Runner when the test file includes a `unittest.main()` entry point.

## Limitations

- Uses simulated measurements rather than live sensors.
- Thresholds are illustrative and currently hardcoded.
- Does not train machine learning models or predict future failures.
- AI-generated explanations may contain inaccuracies.
- AI response times depend on external API availability.
- The application has not been validated for industrial or safety-critical operation.
- Uses Flask's local development server rather than production infrastructure.

## Future Improvements

- Integration with real sensor hardware
- Configurable motor-specific diagnostic thresholds
- Historical sensor measurements and trend analysis
- Expanded automated testing and API failure simulation
- Interactive web dashboard
- Additional actuator and sensor diagnostics
- Improved timeout and retry handling for LLM requests

## Project Purpose

RobotSense AI is an independently developed learning project exploring the intersection of robotics engineering, Python backend development, REST APIs, and generative AI.

The project demonstrates how deterministic engineering logic and language-model-based explanations can be integrated while keeping safety-related decisions outside the LLM.