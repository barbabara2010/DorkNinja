# utils/fetcher.py
import requests
from config import SERPAPI_KEY

def fetch_dork_results(dork, num_results=10):
    params = {
        "engine": "google",
        "q": dork,
        "api_key": SERPAPI_KEY,
        "num": num_results
    }
    try:
        res = requests.get("https://serpapi.com/search", params=params)
        data = res.json()
        results = []
        for item in data.get("organic_results", []):
            results.append({
                "title": item.get("title", "No Title"),
                "link": item.get("link", "#")
            })
        return results
    except Exception as e:
        print(f"[x] Failed to fetch for dork '{dork}': {e}")
        return []
