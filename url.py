from urllib.parse import urlparse
import ipaddress

url = input("Enter a URL: ")

result = urlparse(url)
domain = result.netloc

score = 0

print("\n--- URL ANALYSIS ---")
print("Protocol:", result.scheme)
print("Domain:", domain)
print("Path:", result.path)

# Check HTTPS
if result.scheme == "https":
    print("✓ HTTPS is used")
else:
    print("⚠ HTTP is used")
    score += 1

# Check IP address
try:
    ipaddress.ip_address(domain)
    print("⚠ IP address detected")
    score += 2
except ValueError:
    print("✓ Domain name detected")

print("\nRisk Score:", score)

if score == 0:
    print("Risk Level: LOW")
elif score <= 2:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: HIGH")
