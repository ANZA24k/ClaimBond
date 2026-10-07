# Fixture R-17 acceptance policy
This is a fictional technical fixture, not a real product certification.
Release R-17 is accepted only when every mandatory check has passed on build R-17.
Mandatory checks: C1 deterministic export; C2 backup roundtrip; C3 malformed-input rejection.
An optional performance benchmark may fail without blocking acceptance.
A result for another build cannot satisfy or refute an R-17 check.
Primary signed-off test records outrank a secondary digest when the digest omits build identifiers.
