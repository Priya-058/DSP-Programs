import random

demo = ["alice@example.com","bob@evil.com","carol@example.org","team@bad.example"]

# Ask user once and reuse the response
s = input("Enter emails (comma separated) or press Enter for demo: ").strip()
mails = s.split(',') if s else demo

SUSP = {"evil.com","bad.example"}

for m in [x.strip() for x in mails]:
    risk = 0.3 + 0.5 * (any(d in m for d in SUSP)) + random.uniform(0, 0.2)
    status = "Compromised" if risk > 0.7 else "Safe"
    print("Email:", m, "| Risk:", round(risk, 2), "| Status:", status)

