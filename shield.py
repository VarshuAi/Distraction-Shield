import os
import sys
import time
import ctypes
import datetime
from pathlib import Path

# Styled console printing using the rich library
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
    from rich.prompt import Prompt
    from rich.table import Table
    console = Console()
except ImportError:
    # Standard terminal fallback if rich is not installed yet
    class SimpleConsole:
        def print(self, text, *args, **kwargs):
            print(text)
        def rule(self, *args, **kwargs):
            print("-" * 60)
    console = SimpleConsole()
    class Panel:
        @staticmethod
        def fit(text, title=None, border_style=None):
            return f"=== {title} ===\n{text}\n================="

# Core Windows Paths and Host Settings
HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT_IP = "127.0.0.1"

# The standard list of distracting websites to block
WEBSITES_TO_BLOCK = [
    "www.youtube.com", "youtube.com",
    "www.instagram.com", "instagram.com",
    "www.facebook.com", "facebook.com",
    "www.reddit.com", "reddit.com",
    "www.twitter.com", "twitter.com",
    "www.x.com", "x.com",
    "www.netflix.com", "netflix.com",
    "www.discord.com", "discord.com",
    "www.twitch.tv", "twitch.tv"
]

# High-yield NEET motivational quotes for active study feedback (Physics, Chemistry, Biology)
NEET_QUOTES = [
    "🧬 Biology represents 50% of NEET. Master every single line of NCERT—your rank depends on it!",
    "⚡ Physics: Don't just memorize formulas. Understand the dimensional analysis and derivation!",
    "🧪 Chemistry: Organic mechanisms require repetition. Write them down step-by-step!",
    "⏳ NEET 2026 is on June 21st. Every focused Pomodoro session brings you closer to your dream medical college!",
    "🩺 Focus on the stethoscope, not the distraction. Keep your eyes on the goal!",
    "🌿 Fact check: Have you reviewed the Plant Kingdom classifications and morphology examples recently?",
    "🔋 Physics: Electrostatics and electromagnetism carry huge weightage. Solve 5 numerics after this!",
    "⚗️ Chemistry: Inorganic chemistry requires strict active recall. Revise coordination compounds tonight!",
    "🧬 Did you know? Replication proceeds in a 5' to 3' direction. Stay focused, like DNA polymerase!",
    "🌟 Consistent, small study blocks are infinitely more powerful than last-minute cramming. Keep pushing!"
]

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    # Automatically requests Windows UAC Administrator elevation
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )

def block_websites():
    console.print("[bold red]🔒 Activating Distraction Shield...[/bold red]")
    try:
        with open(HOSTS_PATH, "r", encoding="utf-8") as f:
            content = f.read()

        # Add websites that aren't already blocked
        new_lines = []
        for site in WEBSITES_TO_BLOCK:
            if site not in content:
                new_lines.append(f"{REDIRECT_IP} {site}\n")
        
        if new_lines:
            with open(HOSTS_PATH, "a", encoding="utf-8") as f:
                f.writelines(new_lines)
            console.print("[bold green]✅ Distracting websites successfully blocked![/bold green]")
        else:
            console.print("[yellow]Distraction shield was already active.[/yellow]")
            
    except Exception as e:
        console.print(f"[bold red]Failed to modify hosts file: {e}[/bold red]")
        sys.exit(1)

def restore_websites():
    console.print("\n[bold green]🔓 Deactivating Distraction Shield & Restoring Access...[/bold green]")
    try:
        with open(HOSTS_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Filter out the redirected websites
        clean_lines = []
        for line in lines:
            # Keep the line if none of the blocked sites are in it
            if not any(site in line for site in WEBSITES_TO_BLOCK):
                clean_lines.append(line)

        with open(HOSTS_PATH, "w", encoding="utf-8") as f:
            f.writelines(clean_lines)
        console.print("[bold green]✅ System access successfully restored! Enjoy your break.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Failed to restore hosts file: {e}[/bold red]")

def log_session(session_type, duration_mins, status):
    log_file = Path(__file__).parent / "focus_history.csv"
    
    # Create file and headers if it doesn't exist
    if not log_file.exists():
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("Date,Session Type,Duration (Mins),Status\n")
            
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{now},{session_type},{duration_mins},{status}\n")

def run_focus_timer(duration_mins, session_type):
    duration_secs = duration_mins * 60
    start_time = time.time()
    
    console.print(f"\n[bold cyan]🚀 Focus Session Engaged: {session_type} ({duration_mins} Minutes)[/bold cyan]")
    console.print("[dim]Press Ctrl+C at any time to abort and restore system access.[/dim]\n")
    
    # Load first random NEET quote
    quote_idx = 0
    console.print(Panel.fit(NEET_QUOTES[quote_idx], title="[bold violet]NEET Prep Pulse[/bold violet]", border_style="violet"))
    
    # Progress Bar Display loop
    try:
        with Progress(
            TextColumn("[bold cyan]{task.description}"),
            BarColumn(bar_width=40, complete_style="green", finished_style="bold green"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
            console=console
        ) as progress:
            task = progress.add_task("Concentrating...", total=duration_secs)
            
            last_quote_time = time.time()
            
            while not progress.finished:
                elapsed = time.time() - start_time
                progress.update(task, completed=elapsed)
                time.sleep(1)
                
                # Update motivational NEET quote every 5 minutes (300 seconds)
                if time.time() - last_quote_time > 300:
                    quote_idx = (quote_idx + 1) % len(NEET_QUOTES)
                    console.print("\n")
                    console.print(Panel.fit(NEET_QUOTES[quote_idx], title="[bold violet]NEET Prep Pulse[/bold violet]", border_style="violet"))
                    last_quote_time = time.time()

        # Session Completed Successfully
        log_session(session_type, duration_mins, "Completed")
        console.print("\n")
        console.print(Panel.fit(
            f"[bold green]🏆 Congratulations Varshan! You successfully completed your study block.[/bold green]\n"
            f"You have taken another massive step toward nailing NEET on [bold red]June 21st[/bold red]!",
            title="[bold gold]Session Finished[/bold gold]",
            border_style="yellow"
        ))
        
    except KeyboardInterrupt:
        # Session Aborted by User
        log_session(session_type, duration_mins, "Aborted")
        console.print("\n[bold red]⚠️ Session aborted by user![/bold red]")

def main():
    # 1. Require Admin rights
    if not is_admin():
        console.print("[bold yellow]🛡️ Distraction Shield requires Administrator permissions to modify your hosts file.[/bold yellow]")
        console.print("[cyan]Requesting UAC Elevation... Please click 'Yes' on the Windows pop-up.[/cyan]")
        time.sleep(1.5)
        run_as_admin()
        sys.exit()

    init_folders = Path(__file__).parent / "focus_history.csv"
    
    welcome_text = Text()
    welcome_text.append("🛡️ DISTRACTION-SHIELD FOR NEET 2026 PREPARATION 🛡️\n", style="bold red")
    welcome_text.append("Exam Date: June 21st, 2026 • Curate focus blocks, block apps, crush ranks", style="italic slate")
    
    console.print(Panel.fit(
        welcome_text,
        title="[bold red]Focus Engine Ready[/bold red]",
        border_style="red"
    ))

    # 2. Select Study Category
    console.print("\n[bold cyan]📚 Select focus category:[/bold cyan]")
    table = Table(show_header=True, header_style="bold red")
    table.add_column("No.", style="dim", width=6)
    table.add_column("Focus Category")
    
    table.add_row("1", "🧬 NCERT Biology Focus Block")
    table.add_row("2", "⚡ NCERT Physics Formulas & Numerics")
    table.add_row("3", "🧪 NCERT Chemistry Reaction Sprint")
    table.add_row("4", "💻 C++ Code & Algorithmic Practice")
    
    console.print(table)
    cat_choice = Prompt.ask("\nSelect focus block number", choices=["1", "2", "3", "4"])
    
    categories = {
        "1": "NCERT Biology Focus",
        "2": "NCERT Physics Formulas",
        "3": "NCERT Chemistry Sprint",
        "4": "C++ Coding Practice"
    }
    selected_category = categories[cat_choice]

    # 3. Get Timer Duration
    duration = Prompt.ask("\nEnter focus duration in minutes", default="45")
    try:
        duration_mins = int(duration)
    except ValueError:
        duration_mins = 45

    # 4. Activate Block & Run
    block_websites()
    
    try:
        run_focus_timer(duration_mins, selected_category)
    finally:
        # Crucial: Always restore system access when exiting (success or failure!)
        restore_websites()

if __name__ == "__main__":
    main()
