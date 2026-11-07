
# RobotSense AI

A Python-based robotics diagnostic prototype combining deterministic fault detection, REST APIs, and LLM-generated explanations.

## Overview

RobotSense AI demonstrates how conventional engineering logic can be integrated with generative AI to interpret simulated robotic actuator measurements.

The application evaluates motor temperature and current against configurable rules, produces structured diagnostic results, and uses Google's Gemini API to generate human-readable explanations.

All measurements and thresholds are simulated for demonstration purposes.

## Features

- Rule-based motor diagnostics
- Temperature and current monitoring
- REST API built with Flask
- JSON request and response handling
- Google Gemini LLM integration
- Graceful handling of LLM service failures
- Environment-based API key configuration

## Architecture

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

The deterministic diagnostic engine determines warning conditions independently. The LLM provides explanatory text and does not control the diagnostic rules.

## Technology Stack

- Python 3.13
- Flask
- Google Gemini API
- python-dotenv
- Git and GitHub

## Installation

1. Clone the repository.
2. Create a Python virtual environment.
3. Install dependencies:

   python -m pip install -r requirements.txt

4. Copy `.env.example` to `.env`.
5. Add your Gemini API key to `.env`.
6. Start the Flask application:

   python app.py

The server runs locally at:

http://127.0.0.1:5000

## API

### POST /diagnose

Example request:

{
  "temperature_c": 82,
  "current_a": 3.5
}

The endpoint returns the original measurements, diagnostic status, warnings, AI-generated explanation, and AI service status.

## Example Diagnostic Rules

- Temperature above 75°C triggers a warning.
- Current above 3.0 A triggers a warning.

These thresholds are illustrative and are not derived from validated motor specifications. You can alter the code to your liking/thresholds to test

## Limitations

- Uses simulated measurements only.
- Does not predict equipment failures.
- Does not train or deploy a machine learning model.
- LLM explanations may be inaccurate and require engineering review.
- Requires network connectivity and Gemini API access for AI explanations.
- Not validated for safety-critical or industrial operation.
- Uses Flask's local development server, not a production deployment.

## Future Improvements

- Additional sensor measurements
- Configurable threshold profiles
- Historical measurements and trend analysis
- Automated diagnostic testing
- Simple web dashboard

## Project Status

Functional learning prototype developed independently to explore Python backend development, REST APIs, and LLM integration.
