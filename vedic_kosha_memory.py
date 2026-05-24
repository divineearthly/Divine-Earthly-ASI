"""
Five Kosha Memory — UPGRADED with vedic-inference-engine
Replaces old JSON-file stubs with full KoshaNet + Antahkarana.
Anandamaya LOCKED — core identity inviolable.
"""

import sys, os, json

VIE_PATH = os.path.expanduser("~/vedic-inference-engine")
if VIE_PATH not in sys.path:
    sys.path.insert(0, VIE_PATH)

from vedic_inference_engine import KoshaNet, KoshaLayer, KoshaEntry
from vedic_inference_engine import Antahkarana, SensoryStream

# Global instances
kosha_net = KoshaNet()
antahkarana = Antahkarana("Divine-Earthly-ASI — Silchar, Assam")

# Seed the immutable core
kosha_net.anandamaya_seed(
    "Divine-Earthly-ASI — Sovereign Vedic Intelligence",
    metadata={
        "location": "Silchar, Assam, India (24.81°N, 92.80°E)",
        "hardware": "ARM64 · No GPU · Offline-first",
        "purpose": "Krishi · Ayurveda · Vastu · Jyotisha",
        "principle": "Vasudhaiva Kutumbakam — The World is One Family",
    }
)

# Initialize KOSHAS dict for backward compatibility
KOSHAS = {
    'annamaya': [],
    'pranamaya': [],
    'manomaya': [],
    'vijnanamaya': [],
    'anandamaya': [kosha_net.anandamaya_query()],
}


def store(kosha_name, data):
    """Store data in the appropriate Kosha layer."""
    import datetime, time
    
    entry = {'time': str(datetime.datetime.now()), 'data': data}
    
    if kosha_name == 'anandamaya':
        print("⚠ Anandamaya is LOCKED — identity cannot be modified.")
        return False
    
    elif kosha_name == 'annamaya':
        kosha_net.annamaya_ingest(str(time.time()), data)
        KOSHAS['annamaya'].append(entry)
        # Keep only last 50 raw entries
        if len(KOSHAS['annamaya']) > 50:
            KOSHAS['annamaya'] = KOSHAS['annamaya'][-50:]
    
    elif kosha_name == 'pranamaya':
        kosha_net.pranamaya_compress(str(time.time()), data)
        KOSHAS['pranamaya'].append(entry)
        if len(KOSHAS['pranamaya']) > 20:
            KOSHAS['pranamaya'] = KOSHAS['pranamaya'][-20:]
    
    elif kosha_name == 'manomaya':
        kosha_net.manomaya_think(str(time.time()), data)
        KOSHAS['manomaya'].append(entry)
        if len(KOSHAS['manomaya']) > 10:
            KOSHAS['manomaya'] = KOSHAS['manomaya'][-10:]
    
    elif kosha_name == 'vijnanamaya':
        kosha_net.vijnanamaya_consolidate(str(time.time()), data, confidence=0.75)
        KOSHAS['vijnanamaya'].append(entry)
        # Vijnanamaya keeps all wisdom
        if len(KOSHAS['vijnanamaya']) > 100:
            KOSHAS['vijnanamaya'] = KOSHAS['vijnanamaya'][-100:]
    
    # Save to file for persistence
    try:
        with open(f'kosha_{kosha_name}.json', 'w') as f:
            json.dump(KOSHAS[kosha_name], f)
    except:
        pass
    
    return True


def recall(kosha_name):
    """Recall data from a Kosha layer."""
    # Try loading from file first
    try:
        with open(f'kosha_{kosha_name}.json') as f:
            data = json.load(f)
            KOSHAS[kosha_name] = data
            return data
    except:
        pass
    
    # Fall back to in-memory
    return KOSHAS.get(kosha_name, [])


def search_vijnanamaya(query: str, top_k: int = 3):
    """Search Vijnanamaya wisdom layer for relevant knowledge."""
    results = kosha_net.vijnanamaya_search(query, top_k=top_k)
    return [
        {"key": r.key, "value": r.value, "score": r.consolidation_score}
        for r in results
    ]


def manas_attend(source: str, data, priority: float = 0.5):
    """Route sensory input through Manas attention gate."""
    stream = SensoryStream(source=source, data=data, priority=priority)
    return antahkarana.manas_receive(stream)


def report():
    """Full Kosha + Antahkarana state report."""
    print(kosha_net.kosha_report())
    print()
    print(antahkarana.samadhi_report())


# Load existing data on import
for k in ['annamaya', 'pranamaya', 'manomaya', 'vijnanamaya']:
    try:
        recall(k)
    except:
        pass

print(f"॥ Five Kosha Memory Active — {len(KOSHAS['vijnanamaya'])} wisdom entries · Anandamaya LOCKED · ॐ")
