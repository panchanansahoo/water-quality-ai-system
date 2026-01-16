"""Water Quality AI System API."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from ai_modules.water_classifier import WaterQualityClassifier

app = FastAPI(
    title="Water Quality AI System",
    description="AI-powered water quality monitoring for SDG 6",
    version="0.1.0"
)

# Initialize classifier
classifier = WaterQualityClassifier()


class WaterSample(BaseModel):
    """Water sample parameters."""
    ph: float
    turbidity: float
    bacterial_count: float = 0
    e_coli: float = 0
    chlorine_residue: float = 0.5
    dissolved_oxygen: float = 7.0


class ClassificationResponse(BaseModel):
    """Classification response."""
    classification: str
    confidence: float
    reason: str
    recommended_actions: List[str]


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Water Quality AI System API",
        "version": "0.1.0",
        "endpoints": {
            "classify": "/api/classify",
            "health": "/health"
        }
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.post("/api/classify", response_model=ClassificationResponse)
async def classify_water(sample: WaterSample):
    """Classify water quality from sample parameters.
    
    Example:
    {
        "ph": 6.1,
        "turbidity": 5.2,
        "bacterial_count": 420,
        "e_coli": 1,
        "chlorine_residue": 0.3,
        "dissolved_oxygen": 7.5
    }
    """
    try:
        sample_dict = sample.dict()
        result = classifier.classify(sample_dict)
        return ClassificationResponse(
            classification=result.classification.value,
            confidence=result.confidence,
            reason=result.reason,
            recommended_actions=result.recommended_actions
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
