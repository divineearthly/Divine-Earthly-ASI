# Divine-Earthly-ASI

**Offline-first agricultural AI for rural Indian farmers**  
Built on Vedic knowledge systems. Runs on a phone. No internet required.

---

## The Problem

India has 100+ million smallholder farmers. They have smartphones. They do not have reliable internet, cloud access, or AI tools designed for them — in their language, for their crops, grounded in their knowledge systems.

Existing agricultural AI is cloud-dependent, English-first, and built for agribusiness.

This project is not that.

---

## What This Is

Divine-Earthly-ASI is a sovereign, offline-capable AI system that answers real farmer queries:

- *"When should I plant rice given this week's weather?"*
- *"My tomato leaves are turning yellow — what's wrong?"*
- *"How much water does my field need today?"*
- *"What price can I expect at the mandi this month?"*

It uses real data (NASA POWER API for soil/climate), runs a quantized LLM locally (Qwen2.5-0.5B via llama.cpp), and is orchestrated entirely from a single shell script on ARM64 Android.

**Everything runs on a phone. No GPU. No cloud. No subscription.**

---

## Architecture

```
run_asi.sh
├── vedic_bridge.py          # Vedic sutra routing layer
├── vedic_asi.py             # Core ASI orchestrator
│   ├── farmer_asi.py        # Farmer query interface
│   │   ├── krishi_calendar.py   # Planting calendar (NASA POWER + Jyotisha)
│   │   ├── krishi_disease.py    # Crop disease identification
│   │   ├── krishi_water.py      # Irrigation scheduling
│   │   └── krishi_market.py     # Market price guidance
│   └── vedic_pipeline/      # Six-sutra reasoning pipeline
└── llama.cpp (Qwen2.5-0.5B) # Local LLM, 4-bit quantized
```

**Data sources (offline-capable after sync):**
- NASA POWER API — soil temperature, humidity, solar radiation for Silchar (LAT 24.81, LON 92.80)
- SQLite local database — synced crop/market/disease data
- SuryaSiddhanta astronomical engine — Jyotisha-based planting calendar

---

## Performance (C++ Core)

The Vedic mathematics computation layer, benchmarked on ARM64:

| Module | Throughput | Status |
|---|---|---|
| Nikhilam (complement ops) | ~7 billion ops/sec | Production Ready |
| Ekadhikena (series gen) | ~900 million items/sec | Production Ready |
| ShunyamAnyat (normalize) | ~345 million items/sec | Production Ready |
| SuryaSiddhanta (solar calc) | < 1 nanosecond | Production Ready |
| BuddhiLogic (fuzzy inference) | ~135 million calls/sec | Production Ready |
| VedicMatrix (Urdhva matmul) | Beats Eigen 2.5× on ARM64 | Research Grade |

Full benchmark data: [vedic-kernels](https://github.com/divineearthly/vedic-kernels)

---

## Quick Start

```bash
# Clone
git clone https://github.com/divineearthly/Divine-Earthly-ASI
cd Divine-Earthly-ASI

# Install dependencies (Termux/ARM64)
pkg install python clang cmake
pip install requests sqlite3

# Run
bash run_asi.sh
```

**First run fetches NASA POWER data for your location. Subsequent runs are fully offline.**

---

## Vedic Architecture Principles

This is not decorative use of Vedic terminology. The system is genuinely structured around classical Indian epistemology:

| Vedic Framework | Technical Implementation |
|---|---|
| Pramana (valid knowledge sources) | Five-layer reasoning: observation → inference → analogy → testimony → absence |
| Kosha (memory layers) | Tiered context: immediate query → session → historical trends |
| Jyotisha (astronomical timing) | SuryaSiddhanta engine for planting calendar alignment |
| Ahimsa Protocol | Suppresses chemical fertilizer recommendations by architecture |
| Urdhva Tiryagbhyam | ARM64-optimized matrix multiply (2.5× faster than Eigen Default) |

---

## Supported Languages

Hindi, Bengali, Assamese, English

---

## Project Status

| Component | Status |
|---|---|
| llama.cpp compiled ARM64 | ✅ Working |
| Qwen2.5-0.5B running offline | ✅ Working |
| NASA POWER data integration | ✅ Working |
| Farmer query engines (4) | ✅ Working |
| Vedic reasoning pipeline | ✅ Working |
| Real farmer testing | 🔄 In progress |
| Multilingual interface | 🔄 In progress |

**Honest note:** The system answers queries correctly in testing. Real-world farmer validation — the most important metric — is the current priority.

---

## Why This Matters

- Built 100% on a phone (Android/Termux, ARM64) — no desktop, no server
- No formal CS background — independent researcher from Silchar, Assam
- Designed for farmers who have never been the target users of AI
- Grounded in Indian knowledge systems as genuine architecture, not branding

---

## Related Repositories

- [vedic-kernels](https://github.com/divineearthly/vedic-kernels) — C++ Vedic math benchmarks vs. Eigen
- [Krishi-Veda-Module](https://github.com/divineearthly/Krishi-Veda-Module) — Modular agricultural AI (FastAPI + PWA)
- [KAVACH](https://github.com/divineearthly/KAVACH) — Vedic-grounded cybersecurity framework

---

## Author

**Joydeep Das**  
Independent AI researcher, Silchar, Assam, India  
GitHub: [@divineearthly](https://github.com/divineearthly)

*All development done on Android phone via Termux. No desktop hardware. No institutional affiliation.*

---

## Contributing

If you are a farmer, agricultural extension worker, or rural community worker in India — your feedback on the query system is more valuable than any code contribution. Open an issue describing your crop, your question, and what answer you would need.

---

## License

MIT License

---

*"The earth does not ask for proof of rain. It simply opens."*
