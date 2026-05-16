import httpx
import json
from datetime import datetime

print("Initializing Semi-Weekly Auction Scanner...")

# 1. Load the active portals list
try:
    with open("discovered_texas_auctions.json", "r") as f:
        portals = json.load(f)
except FileNotFoundError:
    print("Error: discovered_texas_auctions.json not found in the repository folder!")
    portals = []

upcoming_auctions = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

print(f"Loaded {len(portals)} active auction targets. Commencing scans...")

# 2. Scan each portal for keyword modifications
with httpx.Client(timeout=10.0, headers=headers) as client:
    for item in portals:
        county = item["county"].capitalize()
        url = item["url"]
        
        try:
            # Fetch the landing page text of the auction site
            response = client.get(url, follow_redirects=True)
            if response.status_code == 200:
                page_text = response.text.lower()
                
                # Check for indicators of active/upcoming schedules
                has_active_auction = any(keyword in page_text for keyword in [
                    "upcoming auctions", "current sales", "auction schedule", "bidding open"
                ])
                
                if has_active_auction:
                    print(f"[ALERT] Active auction detected in {county} County!")
                    upcoming_auctions.append({
                        "county": county,
                        "url": url,
                        "status": "Active/Upcoming Auctions Listed",
                        "last_checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
        except httpx.RequestError:
            print(f"Skipping {county} County (Temporary connection timeout)")
            continue

# 3. Save the results back to the repo
output_file = "upcoming_auctions.json"
with open(output_file, "w") as f:
    json.dump(upcoming_auctions, f, indent=2)

print(f"Scan finalized. Detected {len(upcoming_auctions)} active markets. Data updated in {output_file}.")