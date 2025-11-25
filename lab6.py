from cryptography.fernet import Fernet
alice_key = Fernet.generate_key()
bob_key = Fernet.generate_key()
alice_cipher = Fernet(alice_key)
bob_cipher   = Fernet(bob_key)
shared_key = Fernet.generate_key()
alice = Fernet(shared_key)
bob   = Fernet(shared_key)
plain_text = "Hi Bob! This is Alice (secret message 🔒)"
cipher_text = alice.encrypt(plain_text.encode())  # E2E encryption
print("\n📤 Alice sends (encrypted):", cipher_text)
server_relay = cipher_text  # server sees only ciphertext, not plaintext
decrypted = bob.decrypt(server_relay).decode()
print("📥 Bob decrypts and reads:", decrypted)
print("\n✅ Transport Layer Security (TLS): connection is encrypted during transit.")
print("✅ End-to-End Encryption (E2EE): only Alice & Bob can see the real message.\n")
