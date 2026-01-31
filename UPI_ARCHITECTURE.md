# UPI Architecture - Educational Reference

**Purpose:** Understanding how UPI (Unified Payments Interface) works for cybersecurity and payment system education.

---

## 1. Overview

UPI is India's real-time payment system operated by **NPCI (National Payments Corporation of India)**. It enables instant fund transfer between bank accounts using a single identifier (VPA/UPI ID or mobile number).

### Key Entities

| Entity | Role |
|--------|------|
| **NPCI** | Central switch; routes transactions between banks |
| **PSP (Payment Service Provider)** | Apps like PhonePe, Google Pay, Paytm |
| **Issuer Bank** | Bank of sender (debit) |
| **Acquirer Bank** | Bank of receiver (credit) |
| **VPA** | Virtual Payment Address (e.g., user@paytm) |

---

## 2. System Architecture (Simplified)

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Sender App    │     │   NPCI Switch   │     │  Receiver App   │
│ (PhonePe/GPay)  │────▶│   (Central)     │────▶│ (PhonePe/GPay)  │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Issuer Bank    │     │  Settlement     │     │ Acquirer Bank   │
│  (Sender's)     │     │  (RBI/NPCI)     │     │ (Receiver's)    │
└─────────────────┘     └─────────────────┘     ┌─────────────────┘
```

---

## 3. UPI Transaction Flow (Collect / Pay)

### Pay Flow (Sender initiates)

1. **Initiation:** User enters recipient VPA/number + amount in PSP app
2. **Validation:** PSP validates format, checks limits
3. **Request:** PSP sends collect/pay request to NPCI
4. **Routing:** NPCI routes to issuer (sender) and acquirer (receiver) banks
5. **Authorization:** Banks verify accounts, balance, fraud checks
6. **Settlement:** NPCI debits issuer, credits acquirer
7. **Confirmation:** Both parties receive UTR (Unique Transaction Reference)

### Collect Flow (Receiver requests)

1. Receiver generates collect request (amount + expiry)
2. Sender approves in their app
3. Same settlement flow as Pay

---

## 4. UPI ID / VPA Format

```
username@handle
     │      │
     │      └── PSP/Bank suffix (paytm, ybl, okicici, icici, etc.)
     └── User identifier (phone, custom name, or UPI number)
```

**Examples:**
- `9876543210@paytm` — Phone-based
- `john.doe@ybl` — Custom name (PhonePe)
- `merchant@okicici` — Business (Google Pay)

---

## 5. Security Layers (High-Level)

- **TLS/HTTPS** — All app-to-server traffic encrypted
- **Tokenization** — Sensitive data tokenized, not stored in plain text
- **OTP/MPIN** — Second factor for transaction auth
- **NPCI Certificates** — Mutual TLS between banks and NPCI
- **PCI-DSS** — Card/payment data handling standards

---

## 6. APIs (Non-Financial, for PSPs)

| API | Purpose |
|-----|---------|
| ReqListAccount | List accounts for a mobile number |
| ReqValAdd | Validate VPA before adding beneficiary |
| ReqChkTxn | Check transaction status |

*These are restricted to registered PSPs; not publicly available.*

---

*For encryption details and threat model, see SECURITY_AND_ENCRYPTION.md and THREAT_MODEL.md.*
