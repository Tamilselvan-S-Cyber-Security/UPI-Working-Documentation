# UPI Educational Lab

Safe, educational lab for learning UPI architecture, payment flow, and security concepts.

## Lab Components

| Module | Purpose |
|--------|---------|
| `flowchart.py` | ASCII flowcharts: UPI pay flow, architecture, encryption flow |
| `encryption_demo.py` | Demonstrates SHA-256, HMAC, Fernet (AES), secure random |
| `simulated_payment_flow.py` | Simulates validation logic—no real payments |

## Usage

```bash
# Flowcharts
python lab/flowchart.py

# Encryption concepts (hashlib built-in; pip install cryptography for AES)
python lab/encryption_demo.py

# Simulated payment flow (interactive)
python lab/simulated_payment_flow.py

# Simulated payment flow (command-line)
python lab/simulated_payment_flow.py user@paytm merchant@ybl 500
```

## Documentation

- `docs/UPI_ARCHITECTURE.md` — UPI structure, entities, flow
- `docs/SECURITY_AND_ENCRYPTION.md` — Encryption used in payments
- `docs/THREAT_MODEL.md` — Threat categories and defenses

## Scope

- **Included:** Architecture, flowcharts, validation logic, encryption concepts, threat model
- **Excluded:** Real APIs, exploit code, attack tools, unauthorized access methods
