import hashlib, time

pw = input("Enter a password: ")
h = hashlib.sha256(pw.encode()).hexdigest()
print(f"\n🔐 Hashed password: {h}")

if len(pw) < 4: strength = "Weak ❌"
elif any(c.isdigit() for c in pw) and any(c.isupper() for c in pw): strength = "Strong 💪"
else: strength = "Medium ⚠️"
print("Password Strength:", strength)

dic = ["1234", "admin", "test", "password", "Secret", pw]
print("\n🚀 Starting dictionary attack...\n")
for w in dic:
    time.sleep(0.3)
    print("Trying:", w)
    if hashlib.sha256(w.encode()).hexdigest() == h:
        print(f"\n✅ Password cracked! → '{w}'")
        break
else:
    print("\n❌ Password not found in dictionary")

print("\n📊 Attack simulation complete.")
