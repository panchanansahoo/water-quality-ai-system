# Water Quality AI System

[![SDG 6](https://img.shields.io/badge/SDG-6%20Clean%20Water-blue)](https://www.un.org/sustainabledevelopment/clean-water-sanitation/)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![1M1B Project](https://img.shields.io/badge/1M1B-IBM%20SkillsBuild%20AI%2BSustainability-brightgreen)](https://www.1m1b.ai/)

AI-powered water quality monitoring and contamination prediction system for SDG 6 (Clean Water & Sanitation). This project uses IBM Granite LLM, Retrieval-Augmented Generation (RAG), time-series prediction, and conversational AI to provide timely, accurate water quality assessments for urban and rural water management.

## Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Solution Architecture](#solution-architecture)
- [Key Features](#key-features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Responsible AI](#responsible-ai)
- [Contributing](#contributing)
- [License](#license)

## Overview

Water contamination affects over 150 million people in India annually, with waterborne diseases causing significant morbidity and mortality. Traditional water testing is slow (5-7 days per sample) and expensive (₹2,000-5,000 per test), making early contamination detection difficult.

This system addresses these challenges by providing:

- **Real-time Classification**: AI-powered classification of water safety (Safe/Caution/Unsafe)
- **Predictive Alerts**: 3-7 day advance warnings of contamination events
- **Knowledge-Driven Responses**: RAG system retrieving WHO standards and local regulations
- **Natural Language Interface**: Accessible guidance in local languages (Bengali, Hindi)

## Problem Statement

**How might we use AI to predict and classify water contamination patterns so that municipal authorities and rural water committees can become more proactive in preventing waterborne disease outbreaks?**

### Key Challenges
- Time lag in traditional lab testing (5-7 days)
- High cost barriers (₹2,000-5,000 per test)
- Lack of real-time monitoring in rural areas
- Reactive disease management (responding AFTER outbreaks)
- Technical reports not accessible to lay users

## Solution Architecture

```
┌─────────────────────────────┐
│   Water Quality Data Input  │
│  (Lab results, IoT sensors)  │
└──────────────┬──────────────┘
               ↓
┌──────────────────────────────┐
│   AI Processing Pipeline     │
├──────────────────────────────┤
│ 1. Classification Engine     │
│    (IBM Granite LLM)         │
├──────────────────────────────┤
│ 2. Prediction Module         │
│    (Time-series analysis)    │
├──────────────────────────────┤
│ 3. RAG System                │
│    (Knowledge retrieval)     │
├──────────────────────────────┤
│ 4. Conversational Agent      │
│    (Natural language Q&A)    │
└──────────────┬──────────────┘
               ↓
┌──────────────────────────────┐
│     Output & Alerts          │
│  - Risk Classifications      │
│  - Predictions & Alerts      │
│  - Recommended Actions       │
│  - Web Dashboard             │
│  - SMS/Email Notifications   │
└──────────────────────────────┘
```

## Key Features

### 1. Water Quality Classification
- AI-powered analysis of water samples
- Inputs: pH, turbidity, bacterial count, chemical pollutants, temperature, dissolved oxygen
- Outputs: Safe/Caution/Unsafe classification with confidence scores
- Based on WHO and Indian Standards Bureau guidelines

### 2. Contamination Prediction
- Analyzes 12+ months of historical water quality data
- Identifies seasonal patterns and weather correlations
- Predicts contamination peaks 3-7 days in advance
- Enables proactive treatment plant operations

### 3. Retrieval-Augmented Generation (RAG)
- Knowledge base: WHO water quality standards, Indian regulations, municipal guidelines
- Context-aware responses to stakeholder queries
- Examples: "What contaminants detected?" → Retrieves relevant protocols

### 4. Conversational AI Assistant
- Natural language interface for water committee members and municipal staff
- Explains test results in accessible language
- Provides guidance on corrective actions
- Real-time Q&A on water safety concerns

## Installation

### Prerequisites
- Python 3.9 or higher
- pip or conda
- Git

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/water-quality-ai-system.git
cd water-quality-ai-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

### Example 1: Water Quality Classification

```python
from src.ai_modules.water_classifier import WaterQualityClassifier

classifier = WaterQualityClassifier()

sample_data = {
    'ph': 6.1,
    'turbidity': 5.2,
    'bacterial_count': 420,
    'e_coli': 'Present',
    'chlorine_residue': 0.3,
    'temperature': 28
}

result = classifier.classify(sample_data)
print(f"Classification: {result['classification']}")
print(f"Confidence: {result['confidence']}%")
print(f"Recommended Actions: {result['actions']}")
```

### Example 2: Contamination Prediction

```python
from src.prediction_engine.predictor import ContaminationPredictor

predictor = ContaminationPredictor()
historical_data = load_historical_data('path/to/data.csv')

prediction = predictor.predict_next_7_days(historical_data)
print(f"Alert Level: {prediction['alert_level']}")
print(f"Predicted Peak: {prediction['peak_date']}")
print(f"Reasoning: {prediction['explanation']}")
```

## Project Structure

```
water-quality-ai-system/
├── src/
│   ├── ai_modules/
│   │   ├── water_classifier.py          # Classification logic
│   │   └── prompt_templates.py          # LLM prompt engineering
│   ├── prediction_engine/
│   │   ├── predictor.py                 # Time-series prediction
│   │   └── models.py                    # ML models
│   ├── rag_system/
│   │   ├── knowledge_base.py            # Knowledge base management
│   │   └── retriever.py                 # RAG retrieval logic
│   ├── chatbot/
│   │   └── conversational_ai.py         # Chatbot interface
│   └── api/
│       ├── main.py                      # FastAPI application
│       └── routes.py                    # API endpoints
├── data/
│   ├── sample_data/                     # Sample water quality datasets
│   ├── rag_knowledge/                   # RAG knowledge base files
│   └── models/                          # Trained models
├── tests/
│   ├── test_classifier.py
│   ├── test_predictor.py
│   └── test_api.py
├── notebooks/
│   └── demo.ipynb                       # Jupyter notebook demo
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## API Documentation

### POST /api/classify
Classify water quality from lab test data.

**Request:**
```json
{
  "ph": 6.1,
  "turbidity": 5.2,
  "bacterial_count": 420,
  "e_coli": "Present"
}
```

**Response:**
```json
{
  "classification": "UNSAFE",
  "confidence": 89,
  "reason": "Coliform bacteria exceeds WHO safe limit",
  "actions": ["Notify authorities", "Issue boil water advisory"]
}
```

### GET /api/predict
Get 7-day contamination prediction.

**Response:**
```json
{
  "alert_level": "HIGH",
  "predicted_peak": "2026-01-18",
  "probability": 0.82,
  "explanation": "Based on seasonal patterns and weather correlation"
}
```

## Responsible AI

### Fairness
- Dataset balanced across urban (60%) and rural (40%) areas
- Regular accuracy audits across geographic regions
- No discrimination by location or population

### Transparency
- All decisions explained with confidence scores
- <70% confidence triggers manual verification
- Open documentation of prompt engineering

### Ethics
- Zero false negatives prioritized for safety
- Non-discriminatory treatment of all water sources
- Informed community consent for data use

### Privacy
- No personal health data stored
- GDPR & India DPA compliant
- Data anonymization: sources identified by code, not address
- 12-month data retention policy

## Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### Areas for Contribution
- Improving model accuracy with more training data
- Expanding RAG knowledge base with additional standards
- Multilingual support (Tamil, Marathi, Gujarati)
- Mobile app development
- Real-time IoT sensor integration

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- 1M1B IBM SkillsBuild AI + Sustainability Virtual Internship
- WHO Water Quality Guidelines
- Indian Standards Bureau (ISB)
- NIT Kolkata Computer Science Department

## Contact

For questions or support, please open an issue on [GitHub Issues](https://github.com/yourusername/water-quality-ai-system/issues).

---

**SDG 6 - Ensure availability and sustainable management of water and sanitation for all**
