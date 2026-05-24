"""
Divine-Earthly-ASI → vedic-inference-engine Bridge
Replaces stub Kosha/Antahkarana with full Vedic Inference Engine implementations.
ARM64 · Termux · No GPU
"""

import sys, os

# Add vedic-inference-engine to path
VIE_PATH = os.path.expanduser("~/vedic-inference-engine")
if VIE_PATH not in sys.path:
    sys.path.insert(0, VIE_PATH)

from vedic_inference_engine import (
    # Reasoning
    NyayaScaffold, PramanaSource, PramanaToken,
    # Adaptive learning
    Guna, GunaNeuron, GunaLayer,
    # Ethical routing
    RtaDharmaRouter, DharmaPriority,
    # Ethics filter
    Ahimsa108Filter, AhimsaLevel, AhimsaVerdict,
    # 4-part mind
    Antahkarana, AntahkaranaPart, SensoryStream, BuddhiDecision,
    # 5-layer memory
    KoshaNet, KoshaLayer, KoshaEntry,
)

# Initialize the unified mental model
antahkarana = Antahkarana("Divine-Earthly-ASI — Silchar, Assam, India")
kosha_net = KoshaNet()
ahimsa_filter = Ahimsa108Filter(threshold=75.0)

# Seed Anandamaya (once)
kosha_net.anandamaya_seed(
    "Divine-Earthly-ASI — Sovereign Vedic Intelligence",
    metadata={
        "location": "Silchar, Assam, India",
        "coordinates": "24.81°N, 92.80°E",
        "hardware": "ARM64, No GPU, Offline-first",
        "purpose": "Krishi (Agriculture) · Ayurveda · Vastu · Jyotisha",
    }
)

print("✓ Vedic Engine Bridge active — all 6 modules operational. ॐ")

# ── Compatibility wrappers for existing ASI code ────────────────

def store_kosha(kosha_name: str, data):
    """Compatibility wrapper: store data in Kosha layer."""
    layer_map = {
        "annamaya": "annamaya_ingest",
        "pranamaya": "pranamaya_compress",
        "manomaya": "manomaya_think",
        "vijnanamaya": "vijnanamaya_consolidate",
        "anandamaya": None,  # Cannot modify Anandamaya
    }
    
    if kosha_name == "anandamaya":
        print("⚠ Anandamaya is locked — cannot store. Use anandamaya_seed() once only.")
        return False
    
    if kosha_name == "annamaya":
        kosha_net.annamaya_ingest(str(time.time()), data)
    elif kosha_name == "pranamaya":
        kosha_net.pranamaya_compress(str(time.time()), data)
    elif kosha_name == "manomaya":
        kosha_net.manomaya_think(str(time.time()), data)
    elif kosha_name == "vijnanamaya":
        kosha_net.vijnanamaya_consolidate(str(time.time()), data, confidence=0.75)
    
    return True


def recall_kosha(kosha_name: str):
    """Compatibility wrapper: recall from Kosha layer."""
    if kosha_name == "vijnanamaya":
        return list(kosha_net.vijnanamaya.values())
    elif kosha_name == "pranamaya":
        return list(kosha_net.pranamaya.values())
    elif kosha_name == "annamaya":
        return list(kosha_net.annamaya.values())
    elif kosha_name == "anandamaya":
        return [kosha_net.anandamaya_query()]
    return []


def nyaya_reason(claim: str, evidence: str = "", confidence: float = 0.7):
    """Quick Nyaya reasoning: tag a claim and detect hallucinations."""
    nyaya = NyayaScaffold()
    nyaya.tag(claim, PramanaSource.ANUMANA, confidence, hetu=evidence)
    return {
        "confidence": nyaya.overall_confidence(),
        "hallucination_risk": len(nyaya.detect_hallucinations()) > 0,
        "reasoning": nyaya.explain(),
    }


def check_ahimsa(text: str):
    """Quick Ahimsa-108 check."""
    verdict = ahimsa_filter.evaluate(text)
    return {
        "level": verdict.level.name,
        "score": verdict.score,
        "recommendation": verdict.recommendation,
        "alternative": verdict.panchgavya_alternative,
    }
