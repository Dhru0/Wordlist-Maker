import itertools
import pyfiglet
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from time import sleep

def generate_wordlist(characters, length, filename):
    """Generates all possible combinations of given characters with the specified length."""
    with open(filename, "w") as file:
        for combination in itertools.product(characters, repeat=length):
            file.write("".join(combination) + "\n")
    console.print(Panel.fit(f"[bold green]Wordlist saved to {filename}[/bold green]", style="red"))

if __name__ == "__main__":
    console = Console()
    
    # Large pixelated Zero2Null skull banner
    zero2null_banner = """
        ██████████████████████████████████████████████
        █─▄─▄─█─▄▄▄─█─▄▄─█▄─▄█─█─█─▄▄▄▄█─▄▄▄─█─▄▄─█▄─▄█
        ███─███─███▀█─██─██─██─▄─█─██▄─█─███▀█─██─██─██
        █▄▄▄█▄▄▄▄▄█▄▄▄▄█▄▄▄█▄█▄█▄▄▄▄▄█▄▄▄▄▄█▄▄▄▄█▄▄▄█
    """
    zero2null_text = """
    ███████╗███████╗██████╗  ██████╗  ██████╗ ██╗   ██╗██╗     
    ██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██║   ██║██║     
    █████╗  █████╗  ██████╔╝██║   ██║██║   ██║██║   ██║██║     
    ██╔══╝  ██╔══╝  ██╔═══╝ ██║   ██║██║   ██║██║   ██║██║     
    ██║     ███████╗██║     ╚██████╔╝╚██████╔╝╚██████╔╝███████╗
    ╚═╝     ╚══════╝╚═╝      ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝  
    """
    
    banner = pyfiglet.figlet_format("ZERO2NULL")
    console.print(f"[bold red]{zero2null_banner}[/bold red]")
    console.print(f"[bold green]{zero2null_text}[/bold green]")
    console.print(f"[bold cyan]{banner}[/bold cyan]")
    console.print(Panel.fit("[bold yellow]WARNING: This tool generates massive wordlists! Use responsibly.[/bold yellow]", style="red"))
    
    sleep(1)  # Dramatic effect
    console.print("[bold green]Initializing brute-force wordlist generator...[/bold green]")
    sleep(1)
    
    characters = Prompt.ask("[bold cyan]Enter characters to use (e.g., abc123!@#)[/bold cyan]")
    length = int(Prompt.ask("[bold cyan]Enter word length[/bold cyan]", default="3"))
    filename = Prompt.ask("[bold cyan]Enter filename (e.g., wordlist.txt)[/bold cyan]", default="wordlist.txt")
    
    console.print("\n[bold magenta]Generating combinations... This might take some time...[/bold magenta]\n")
    sleep(1)
    generate_wordlist(characters, length, filename)
    console.print("[bold red]Process completed! Exiting...[/bold red]")
