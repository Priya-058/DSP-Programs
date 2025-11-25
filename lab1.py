import hashlib, time, random
data = input("Enter data to protect: ")
key = int(input("Enter a secret key: "))

enc = ''.join(chr(ord(c) ^ key) for c in data)
dec = ''.join(chr(ord(c) ^ key) for c in enc)
print("\nConfidentiality ->", enc, "→", dec)

h1 = hashlib.sha256(data.encode()).hexdigest()
tampered = data + "!"  
h2 = hashlib.sha256(tampered.encode()).hexdigest()
print("Integrity ->", "Safe" if h1 == h2 else "Tampered ")

print("Availability -> System under load...")
time.sleep(random.uniform(0.5, 1.5))
print("System recovered and data accessible!")
                              