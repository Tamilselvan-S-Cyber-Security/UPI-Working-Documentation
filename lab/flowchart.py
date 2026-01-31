#!/usr/bin/env python3
"""
UPI Payment Flow - Educational Flowchart Generator
Displays UPI transaction flow as ASCII flowchart for learning.
"""


def print_pay_flow():
    """Print UPI Pay transaction flow flowchart."""
    flow = """
+======================================================================+
|              UPI PAY TRANSACTION FLOW (Educational)                  |
+======================================================================+

  SENDER                    PSP APP                   NPCI SWITCH
  (User A)                (PhonePe/GPay)                (Central)
      |                         |                            |
      |  1. Enter VPA + Amount  |                            |
      |----------------------->|                            |
      |                         |                            |
      |  2. Enter MPIN          |  3. Validate & Sign        |
      |----------------------->|  (TLS + API Auth)          |
      |                         |--------------------------->|
      |                         |                            |
      |                         |  4. Route to Banks         |
      |                         |     (Issuer + Acquirer)    |
      |                         |<---------------------------|
      |                         |                            |
      |  5. UTR + Success       |  6. Debit/Credit           |
      |<-----------------------|     Settlement             |
      |                         |                            |
      v                         v                            v

  RECEIVER (User B) receives credit notification with same UTR.

  UTR = Unique Transaction Reference (tracking ID for the transaction)
  MPIN = Mobile PIN (never leaves device in plain form)
"""
    print(flow)


def print_architecture():
    """Print UPI system architecture."""
    arch = """
+======================================================================+
|                    UPI SYSTEM ARCHITECTURE                           |
+======================================================================+

    +---------------------------------------------------------------+
    |                     USER LAYER                                 |
    |  +----------+  +----------+  +----------+  +----------+        |
    |  | PhonePe  |  | Google   |  |  Paytm   |  |  BHIM    |  ...   |
    |  |   App    |  |   Pay    |  |   App    |  |   App    |        |
    |  +----+-----+  +----+-----+  +----+-----+  +----+-----+        |
    +------+-------------+-------------+-------------+---------------+
           |             |             |             |
           +-------------+------+------+-------------+
                                |
    +---------------------------+-------------------------------+
    |                    PSP LAYER (TLS/API)                     |
    |                           |                                |
    |              +------------v------------+                   |
    |              |    PSP Backend Servers   |                   |
    |              |  (Yes Bank, ICICI, etc)  |                   |
    |              +------------+------------+                   |
    +---------------------------+-------------------------------+
                                |
    +---------------------------+-------------------------------+
    |                    NPCI LAYER                              |
    |              +------------v------------+                   |
    |              |     UPI Switch (NPCI)    |                   |
    |              |  - Routing               |                   |
    |              |  - Settlement            |                   |
    |              |  - Certification         |                   |
    |              +------------+------------+                   |
    +---------------------------+-------------------------------+
                                |
    +---------------------------+-------------------------------+
    |                    BANK LAYER                              |
    |     +---------+  +---------+  +---------+  +---------+     |
    |     |  SBI    |  |  HDFC   |  |  ICICI  |  |  Axis   | ... |
    |     | (Issuer)|  |(Acquirer)|  |         |  |         |     |
    |     +---------+  +---------+  +---------+  +---------+     |
    +------------------------------------------------------------+
"""
    print(arch)


def print_encryption_flow():
    """Print encryption in payment flow."""
    enc = """
+======================================================================+
|              ENCRYPTION IN UPI PAYMENT FLOW                          |
+======================================================================+

  App                    Network                     Server
   |                         |                          |
   |  Plain: VPA, Amount     |                          |
   |  MPIN: Local only       |                          |
   |  (never sent)           |                          |
   |                         |                          |
   |  +-----------------+    |    +-----------------+   |
   |  | TLS Encrypt     |    |    | TLS Decrypt     |   |
   |  | (AES + RSA)     |--->|--->| (AES + RSA)     |   |
   |  +-----------------+    |    +-----------------+   |
   |                         |                          |
   |  Certificate validation |  Mutual TLS              |
   |  (RSA signatures)       |  (both sides verify)     |
   |                         |                          |
   |  Request signing        |  HMAC-SHA256             |
   |  (integrity check)      |  (tamper detection)      |
   |                         |                          |
"""
    print(enc)


def main():
    """Display all flowcharts."""
    print("\n" + "=" * 72)
    print("  UPI EDUCATIONAL FLOWCHARTS")
    print("=" * 72)
    print_pay_flow()
    print("\n")
    print_architecture()
    print("\n")
    print_encryption_flow()
    print("\n  See docs/ folder for detailed documentation.")


if __name__ == "__main__":
    main()
