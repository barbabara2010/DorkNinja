# dorkninja.py
import argparse
from utils.fetcher import fetch_dork_results
from utils.reporter import generate_html_report
from config import RESULTS_PER_DORK
from rich.console import Console
from rich.progress import track

console = Console()

def load_dorks(file_path="dorks.txt"):
    with open(file_path, "r") as f:
        return [line.strip("- ").strip() for line in f if line.strip()]

def main():
    parser = argparse.ArgumentParser(description="DorkNinja - Google Dorking Tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g. example.com or *.example.com)")
    args = parser.parse_args()

    target = args.domain
    dorks = load_dorks()
    console.print(f"[bold green]Loaded {len(dorks)} dorks for site: {target}[/bold green]")

    results_by_dork = {}
    for dork in track(dorks, description="[blue]Running Dorks..."):
        full_dork = f'site:{target} {dork}'
        results = fetch_dork_results(full_dork, RESULTS_PER_DORK)
        results_by_dork[full_dork] = results

    path = generate_html_report(results_by_dork)
    console.print(f"[bold yellow]Report saved at:[/bold yellow] {path}")

if __name__ == "__main__":
    main()
