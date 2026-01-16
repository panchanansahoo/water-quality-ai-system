"""Water Quality Classification Module."""

import json
from dataclasses import dataclass
from typing import Dict, List
from enum import Enum


class WaterQualityStatus(Enum):
    """Classification status."""
    SAFE = "SAFE"
    CAUTION = "CAUTION"
    UNSAFE = "UNSAFE"


@dataclass
class WaterQualityResult:
    """Classification result."""
    classification: WaterQualityStatus
    confidence: float
    reason: str
    recommended_actions: List[str]
    exceeded_parameters: List[str]


class WaterQualityClassifier:
    """Classifies water quality based on WHO standards."""

    WHO_STANDARDS = {
        'ph': {'min': 6.5, 'max': 8.5},
        'turbidity': {'max': 5},
        'bacterial_count': {'max': 0},
        'e_coli': {'max': 0},
        'chlorine_residue': {'min': 0.2, 'max': 1.0},
        'dissolved_oxygen': {'min': 5},
    }

    def classify(self, water_sample: Dict[str, float]) -> WaterQualityResult:
        """Classify water quality from sample parameters."""
        exceeded = self._check_parameters(water_sample)
        
        if len(exceeded) >= 3:
            classification = WaterQualityStatus.UNSAFE
            confidence = 95
        elif len(exceeded) == 1:
            classification = WaterQualityStatus.CAUTION
            confidence = 80
        elif len(exceeded) == 0:
            classification = WaterQualityStatus.SAFE
            confidence = 98
        else:
            classification = WaterQualityStatus.CAUTION
            confidence = 75
        
        reason = self._generate_reason(exceeded)
        actions = self._generate_actions(exceeded, water_sample)
        
        return WaterQualityResult(
            classification=classification,
            confidence=confidence,
            reason=reason,
            recommended_actions=actions,
            exceeded_parameters=exceeded
        )

    def _check_parameters(self, sample: Dict[str, float]) -> List[str]:
        """Check which parameters exceed WHO standards."""
        exceeded = []
        for param, value in sample.items():
            if param not in self.WHO_STANDARDS:
                continue
            standards = self.WHO_STANDARDS[param]
            if 'max' in standards and value > standards['max']:
                exceeded.append(param)
            if 'min' in standards and value < standards['min']:
                exceeded.append(param)
        return exceeded

    def _generate_reason(self, exceeded: List[str]) -> str:
        """Generate explanation."""
        if not exceeded:
            return "All parameters within WHO safe limits"
        reasons = [p.replace('_', ' ').title() for p in exceeded]
        return "Exceeded: " + ", ".join(reasons)

    def _generate_actions(self, exceeded: List[str], sample: Dict) -> List[str]:
        """Generate corrective actions."""
        actions = []
        if 'bacterial_count' in exceeded or 'e_coli' in exceeded:
            actions.append("IMMEDIATE: Issue boil water advisory")
            actions.append("Notify health authorities")
        if 'turbidity' in exceeded:
            actions.append("Increase water filtration")
        actions.append("Collect follow-up samples in 48 hours")
        return actions if actions else ["Continue monitoring"]

    def to_dict(self, result: WaterQualityResult) -> Dict:
        """Convert to dictionary."""
        return {
            'classification': result.classification.value,
            'confidence': result.confidence,
            'reason': result.reason,
            'recommended_actions': result.recommended_actions,
        }
