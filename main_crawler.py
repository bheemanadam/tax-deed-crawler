import httpx
import json
from datetime import datetime

print("Initializing Robust Semi-Weekly Auction Scanner...")

# 1. Load your targeted county portal configuration map
try:
    with open("discovered_texas_auctions.json", "r") as f:
        portals = json.load(f)
except FileNotFoundError:
    print("Critical Error: discovered_texas_auctions.json is missing from this directory!")
    portals = []

upcoming_auctions = []
# Mimic a standard desktop browser to prevent being turned away by cloud security filters
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print(f"Target file loaded. Commencing verification on {len(portals)} county platforms...")

# 2. Iterate and scan the target array
with httpx.Client(timeout=15.0, headers=headers, follow_redirects=True) as client:
    for item in portals:
        county = item["county"].capitalize()
        url = item["url"]
        
        try:
            response = client.get(url)
            # If the site answers with a healthy 200 OK code, it is live
            if response.status_code == 200:
                page_text = response.text.lower()
                
                # Check for baseline vendor signatures that load instantly without heavy Javascript
                keywords = ["auction", "realauction", "sale", "foreclose", "sheriff", "register", "login"]
                matched_indicators = [word for word in keywords if word in page_text]
                
                if matched_indicators:
                    print(f"[LIVE] Verified active auction portal for {county} County.")
                    upcoming_auctions.append({
                        "county": county,
                        "url": url,
                        "status": "Online & Operational",
                        "detected_markers": matched_indicators,
                        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                else:
                    print(f"[INFO] Connected to {county} County, but page formatting was unrecognized.")
            else:
                print(f"[SYSTEM INFO] {county} County portal returned code: {response.status_code}")
        except httpx.RequestError:
            print(f"[TIMEOUT] {county} County portal is temporarily unresponsive.")
            continue

# 3. Commit records to data matrix
output_file = "upcoming_auctions.json"
with open(output_file, "w") as f:
    json.dump(upcoming_auctions, f, indent=2)

print(f"\nScan complete. Successfully populated {len(upcoming_auctions)} verified portals into {output_file}.")