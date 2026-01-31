# Payment System Security & Encryption - Educational Guide

**Purpose:** Understanding encryption and security concepts used in UPI and payment systems.

---

## 1. Encryption Algorithms Used in Payments

### Symmetric Encryption (AES)

- **Role:** Encrypt bulk data (e.g., session data, payloads)
- **Common:** AES-256 (256-bit key)
- **How it works:** Same key encrypts and decrypts
- **In UPI context:** Securing data in transit and at rest

```
Plain Text ──[AES Encrypt + Key]──▶ Cipher Text ──[AES Decrypt + Key]──▶ Plain Text
```

### Asymmetric Encryption (RSA)

- **Role:** Key exchange, digital signatures, certificate validation
- **How it works:** Public key encrypts, private key decrypts (or vice versa for signatures)
- **In UPI context:** TLS handshake, API authentication, certificate chains

```
Sender: Encrypt with Recipient's Public Key
Recipient: Decrypt with Own Private Key
```

### Hashing (SHA-256)

- **Role:** Integrity checks, password storage, HMAC
- **One-way:** Cannot reverse hash to get original data
- **In UPI context:** Message authentication, request signing

```
Data ──[SHA-256]──▶ Fixed 64-char hash (irreversible)
```

---

## 2. TLS in Payment Flows

```
Client (App)                    Server (PSP/Bank)
     │                                │
     │──── Client Hello ─────────────▶│
     │◀─── Server Hello + Cert ───────│
     │──── Verify Certificate ────────│
     │──── Key Exchange ─────────────▶│
     │◀─── Encrypted Session ─────────│
     │                                │
     │═══ Encrypted Data Exchange ═══│
```

- All UPI app traffic uses **TLS 1.2+**
- Certificates signed by trusted CAs
- Prevents eavesdropping and tampering

---

## 3. Multi-Factor Authentication (MFA)

| Factor | Example in UPI |
|--------|----------------|
| Something you know | MPIN (Mobile PIN) |
| Something you have | Device (SIM, app) |
| Something you are | Biometric (fingerprint, face) |

**MPIN:** 4–6 digit PIN, never transmitted; used for local device auth + secure token to server.

---

## 4. Tokenization

- Sensitive data (card numbers, account details) replaced with tokens
- Tokens are useless outside the issuing system
- Reduces risk of data breach exposure

---

## 5. Secure Development Practices

- **Input validation** — Reject malformed UPI IDs, amounts
- **Output encoding** — Prevent injection in displays
- **Least privilege** — Apps request minimal permissions
- **Secure storage** — Keystore/Keychain for keys, encrypted DB for local data

---

*For threat types and defenses, see THREAT_MODEL.md.*
