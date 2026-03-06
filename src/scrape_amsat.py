import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.amsat.org/status/"
ACTIVE_COLOR = "#4169e1"  # royal blue
TIME_WINDOW_LOOKBACK = 24  # number of 2-hour windows in the last 24 hours (24h / 2h = 12)

# fetch page
resp = requests.get(URL)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

# find all tables - the satellite status table is the one with the most rows
# (typically table index 2, but find it by looking for the one with most rows)
tables = soup.find_all("table")
table = max(tables, key=lambda t: len(t.find_all("tr")))

rows = table.find_all("tr")

data = []

for row in rows[1:]:  # skip header row
    cols = row.find_all("td")

    if not cols:
        continue

    sat_name = cols[0].get_text(strip=True)
    
    # Extract the link text if available (cleaner format)
    sat_link = cols[0].find("a")
    if sat_link:
        sat_name = sat_link.get_text(strip=True)

    # Check each cell for blue background (bgcolor="#4169E1" = active)
    is_active = []
    for c in cols[1:]:
        # Check bgcolor attribute for blue (#4169E1 is royal blue = active)
        bgcolor = c.get("bgcolor", "").lower()
        has_blue = bgcolor == ACTIVE_COLOR
        
        is_active.append(1 if has_blue else 0)

    data.append((sat_name, is_active))

results = []

for sat, active_list in data:
    activity_sum = sum(active_list[:TIME_WINDOW_LOOKBACK])   # first 12 columns = 24 hours (12 × 2-hour windows)
    results.append((sat, activity_sum))

# sort by activity (most active first)
results.sort(key=lambda x: x[1], reverse=True)

df = pd.DataFrame(results, columns=["Satellite", "Activity"])
print(df.head(10))