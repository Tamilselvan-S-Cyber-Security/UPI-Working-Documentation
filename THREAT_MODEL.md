# UPI Threat Model - Educational Reference

**Purpose:** Understanding common threats to payment systems and how to defend against them. **This document is for learning only—not for exploitation.**

---

## 1. Threat Categories

### A. Social Engineering

| Threat | Description | Defense |
|--------|-------------|---------|
| **Phishing** | Fake UPI links, fake customer care, fake QR codes | Verify URLs, use official apps only |
| **Vishing** | Calls pretending to be bank/PSP support | Never share OTP, MPIN, or UPI collect approval blindly |
| **Fake UPI IDs** | Similar-looking IDs to trick senders | Double-check VPA before sending |

### B. Technical Attacks (Conceptual)

| Threat | Description | Defense |
|--------|-------------|---------|
| **Man-in-the-Middle** | Intercept traffic if TLS is broken or user on malicious network | TLS, certificate pinning, avoid public Wi‑Fi for payments |
| **Malware** | Keyloggers, screen capture to steal MPIN | Use official app stores, avoid sideloading, keep OS updated |
| **Session Hijacking** | Stealing session tokens | Short-lived tokens, secure storage, re-auth for high-value ops |
| **Replay Attacks** | Reusing captured valid requests | Nonces, timestamps, transaction IDs (UTR) |

### C. Fraud Patterns

| Threat | Description | Defense |
|--------|-------------|---------|
| **Collect Abuse** | Sending collect requests to unsuspecting users | Verify amount and sender before approving |
| **Wrong Recipient** | Sending to similar VPA by mistake | Always verify UPI ID and name before confirming |
| **SIM Swap** | Attacker takes over phone number to receive OTP | Use UPI PIN/MPIN, link with email, report suspicious activity |

---

## 2. Why Certain Attacks Don't Work

### No Direct UPI "Hacking"

- UPI apps don’t expose public APIs for payment initiation
- Banks and NPCI use mutual TLS and strong authentication
- No public endpoints to brute-force or exploit
- Financial APIs require bank/PSP registration and KYC

### Why Phone Number Lookup Fails

- Banks/PSPs hold mapping of VPA ↔ phone
- This data is not exposed via public APIs
- Privacy regulations restrict disclosure

### Why Encryption Can't Be "Bypassed"

- AES-256 and RSA are industry standards
- Breaking them would require impractical computational power
- Real breaches come from social engineering, weak passwords, or server misconfig—not algorithm weakness

---

## 3. Security Best Practices (User)

1. **Verify before pay** — Check VPA, name, amount
2. **Use official apps** — Download only from Play Store / App Store
3. **Don’t share** — OTP, MPIN, UPI collect approvals
4. **Enable 2FA** — Use device lock, biometrics
5. **Monitor transactions** — Check history, set alerts

---

## 4. Security Best Practices (Developer)

1. **Never store** — MPIN, passwords in plain text
2. **Validate input** — UPI format, amounts, limits
3. **Use TLS** — For all API and web traffic
4. **Follow standards** — PCI-DSS, OWASP guidelines
5. **Audit and test** — Regular security reviews, penetration tests (with authorization)

---

*This is educational material only. Unauthorized access to systems or misuse of payment infrastructure is illegal.*
