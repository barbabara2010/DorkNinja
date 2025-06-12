# utils/reporter.py
from datetime import datetime
import os

def generate_html_report(results_by_dork):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"reports/report_{timestamp}.html"
    os.makedirs("reports", exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("<html><head><title>DorkNinja Report</title></head><body>")
        f.write("<h1>DorkNinja Report</h1><hr>")
        for dork, results in results_by_dork.items():
            f.write(f"<h2>Dork: <code>{dork}</code></h2>")
            f.write(f"<p>Results found: {len(results)}</p><ul>")
            for r in results:
                f.write(f"<li><a href='{r['link']}'>{r['title']}</a></li>")
            f.write("</ul><hr>")
        f.write("</body></html>")
    return filepath
