#!/usr/bin/env python3
"""
Encryption Concepts Demo - Educational Only
Demonstrates AES, hashing, and HMAC concepts used in payment systems.
Uses Python standard library (hashlib) + optional cryptography package.
"""

import hashlib
import hmac
import base64
import secrets

# Optional: use cryptography if available for AES demo
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    HAS_CRYPTO = True
except ImportError:
    HAS_CRYPTO = False


def demo_sha256_hash():
    """Demonstrate SHA-256 hashing (used for integrity, HMAC)."""
    print("\n" + "=" * 60)
    print("  1. SHA-256 HASHING (One-way, used for integrity)")
    print("=" * 60)
    data = b"UPI_TRANSACTION_1000_9876543210@paytm"
    digest = hashlib.sha256(data).hexdigest()
    print(f"  Input : {data.decode()}")
    print(f"  Hash  : {digest}")
    print("  Note  : Same input always gives same hash. Cannot reverse.")
    return digest


def demo_hmac():
    """Demonstrate HMAC (used for request signing)."""
    print("\n" + "=" * 60)
    print("  2. HMAC-SHA256 (Message authentication)")
    print("=" * 60)
    key = b"secret_api_key_do_not_share"
    message = b"POST /upi/collect amount=100 vpa=user@paytm"
    sig = hmac.new(key, message, hashlib.sha256).hexdigest()
    print(f"  Key     : (hidden, {len(key)} bytes)")
    print(f"  Message : {message.decode()}")
    print(f"  HMAC    : {sig[:32]}...")
    print("  Note    : Server verifies with same key. Tampering changes HMAC.")


def demo_aes_fernet():
    """Demonstrate symmetric encryption (AES-like via Fernet)."""
    if not HAS_CRYPTO:
        print("\n" + "=" * 60)
        print("  3. AES ENCRYPTION (Install: pip install cryptography)")
        print("=" * 60)
        print("  Skipped - run: pip install cryptography")
        return
    print("\n" + "=" * 60)
    print("  3. SYMMETRIC ENCRYPTION (Fernet = AES-128-CBC + HMAC)")
    print("=" * 60)
    key = Fernet.generate_key()
    f = Fernet(key)
    plain = b"sensitive_data:account_number_12345"
    encrypted = f.encrypt(plain)
    decrypted = f.decrypt(encrypted)
    print(f"  Plain     : {plain.decode()}")
    print(f"  Encrypted : {base64.urlsafe_b64encode(encrypted[:20]).decode()}...")
    print(f"  Decrypted : {decrypted.decode()}")
    print("  Note      : Same key encrypts and decrypts. Used for data at rest.")


def demo_secure_random():
    """Demonstrate secure random (for tokens, nonces)."""
    print("\n" + "=" * 60)
    print("  4. SECURE RANDOM (Tokens, nonces, UTR)")
    print("=" * 60)
    token = secrets.token_hex(16)
    nonce = secrets.token_urlsafe(8)
    print(f"  Token : {token}")
    print(f"  Nonce : {nonce}")
    print("  Note  : Used for UTR, session IDs. Cryptographically secure.")


def main():
    """Run all demos."""
    print("\n" + "#" * 60)
    print("#  UPI PAYMENT ENCRYPTION - EDUCATIONAL DEMO")
    print("#  These concepts are used in UPI, PhonePe, Google Pay, etc.")
    print("#" * 60)
    demo_sha256_hash()
    demo_hmac()
    demo_aes_fernet()
    demo_secure_random()
    print("\n" + "=" * 60)
    print("  Demos complete. See docs/SECURITY_AND_ENCRYPTION.md")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
