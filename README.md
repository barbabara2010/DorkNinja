# DorkNinja 🥷🔍
A powerful CLI-based Google Dorking tool using SerpAPI. Designed for bug bounty hunters and OSINT ninjas.

---

## 🚀 Features

- Run custom Google dorks on any domain
- HTML report generation with results
- Discord webhook alert support (optional)
- Supports domain lists for subdomain recon
- Uses SerpAPI for real-time Google search scraping

---

## 📦 Requirements

- Python 3.8+
- SerpAPI account + key

Install dependencies:

```bash
pip3 install -r requirements.txt
```

## 🔐 Setup .env
Create a .env file in the root directory:
```
SERPAPI_KEY=your_serpapi_key
DISCORD_WEBHOOK=https://discord.com/api/webhooks/your_webhook_here
```
You can leave DISCORD_WEBHOOK blank if you don't want notifications.

## 🛠 Usage
🔹 Run on a single domain:
```
python dorkninja.py -d example.com
```
🔹 Run on multiple domains from a list:
```
python dorkninja.py -l subdomains.txt
```

📄 Output
```dorkninja_report.html``` - a simple report with:
Dork used
Number of results found
Top links

## 📬 Discord Notifications (Optional)
If DISCORD_WEBHOOK is set in .env, result summaries will be sent there.

## 💡 Tip
Use dorks.txt to add your own dork patterns. One per line, example:
```
inurl:admin
intitle:"login"
ext:log
```

## 🧠 Inspired by
Bug bounty automation, recon tools, and the hunger to find those juicy endpoints. 🔥


