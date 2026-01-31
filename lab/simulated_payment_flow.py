#!/usr/bin/env python3
"""
Simulated UPI Payment Flow - Educational Lab
Simulates validation and flow concepts. NO real payments. NO real APIs.
"""

import re
import hashlib
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional, Tuple


@dataclass
class SimulatedTransaction:
    """Simulated transaction record (for lab only)."""
    sender_vpa: str
    receiver_vpa: str
    amount: float
    utr: str
    status: str
    timestamp: str


def validate_amount(amount: float) -> Tuple[bool, str]:
    """Validate transaction amount (UPI limits: typically 1L default)."""
    if amount <= 0:
        return False, "Amount must be positive"
    if amount > 100_000:
        return False, "Amount exceeds default UPI limit (Rs 1,00,000)"
    return True, "OK"


def validate_vpa_format(vpa: str) -> Tuple[bool, str]:
    """Validate VPA format (username@handle)."""
    if not vpa or "@" not in vpa:
        return False, "Invalid format: need user@handle"
    parts = vpa.strip().split("@")
    if len(parts) != 2:
        return False, "Invalid format"
    user, handle = parts[0].strip().lower(), parts[1].strip().lower()
    if len(user) < 3:
        return False, "Username too short"
    if not re.match(r"^[a-z0-9._-]+$", user):
        return False, "Invalid characters in username"
    if not re.match(r"^[a-z0-9]+$", handle):
        return False, "Invalid handle"
    return True, "OK"


def generate_utr() -> str:
    """Generate simulated UTR (Unique Transaction Reference)."""
    import secrets
    return secrets.token_hex(8).upper()


def simulate_payment(sender_vpa: str, receiver_vpa: str, amount: float) -> SimulatedTransaction:
    """
    Simulate a UPI payment flow (validation + mock success).
    NO real money. NO real APIs. Educational only.
    """
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # Step 1: Validate sender VPA
    ok, msg = validate_vpa_format(sender_vpa)
    if not ok:
        return SimulatedTransaction(
            sender_vpa, receiver_vpa, amount,
            utr="N/A", status=f"FAILED: Sender VPA invalid - {msg}", timestamp=now
        )

    # Step 2: Validate receiver VPA
    ok, msg = validate_vpa_format(receiver_vpa)
    if not ok:
        return SimulatedTransaction(
            sender_vpa, receiver_vpa, amount,
            utr="N/A", status=f"FAILED: Receiver VPA invalid - {msg}", timestamp=now
        )

    # Step 3: Validate amount
    ok, msg = validate_amount(amount)
    if not ok:
        return SimulatedTransaction(
            sender_vpa, receiver_vpa, amount,
            utr="N/A", status=f"FAILED: {msg}", timestamp=now
        )

    # Step 4: Simulate MPIN check (would be local on real app)
    # Step 5: Simulate NPCI routing (would be real API)
    # Step 6: Generate UTR and success
    utr = generate_utr()
    return SimulatedTransaction(
        sender_vpa=sender_vpa,
        receiver_vpa=receiver_vpa,
        amount=amount,
        utr=utr,
        status="SUCCESS (SIMULATED)",
        timestamp=now
    )


def interactive_lab():
    """Run interactive simulated payment lab."""
    print("\n" + "=" * 60)
    print("  UPI PAYMENT FLOW - SIMULATED LAB (Educational)")
    print("  No real money. No real APIs. Validation only.")
    print("=" * 60)

    while True:
        print("\nEnter details (or 'quit' to exit):")
        try:
            sender = input("  Sender VPA   : ").strip()
            if sender.lower() in ("quit", "exit", "q"):
                print("  Lab ended.")
                break
            receiver = input("  Receiver VPA : ").strip()
            amount_str = input("  Amount (Rs)  : ").strip()
            try:
                amount = float(amount_str)
            except ValueError:
                amount = -1

            tx = simulate_payment(sender, receiver, amount)
            print("\n  --- Result ---")
            print(f"  Status  : {tx.status}")
            print(f"  UTR     : {tx.utr}")
            print(f"  Time    : {tx.timestamp}")
        except KeyboardInterrupt:
            print("\n  Lab ended.")
            break


def main():
    """Demo + interactive mode."""
    import sys
    if len(sys.argv) >= 4:
        sender, receiver, amount_str = sys.argv[1], sys.argv[2], sys.argv[3]
        try:
            amount = float(amount_str)
            tx = simulate_payment(sender, receiver, amount)
            print(f"Status: {tx.status}")
            print(f"UTR: {tx.utr}")
        except ValueError:
            print("Usage: python simulated_payment_flow.py sender@vpa receiver@vpa amount")
    else:
        interactive_lab()


if __name__ == "__main__":
    main()
