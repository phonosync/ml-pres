#!/usr/bin/env python3
"""
Auto Quarto Render Script (Enhanced Version)
This script automatically triggers Quarto rendering at a specified interval
or when .qmd files are modified in the project directory.

Usage:
1. Save this script to your project directory
2. Run it with Python: python auto_quarto_render.py [project_path] [interval]
   - project_path: Path to the Quarto project (default: current directory)
   - interval: Seconds between renders (default: 60, 0 for file monitoring only)
3. Press Ctrl+C to stop the script.
"""
import os
import time
import subprocess
import datetime
import argparse
import sys
from pathlib import Path

def get_file_modification_times(directory):
    """Get modification times for all .qmd files in the directory and subdirectories"""
    mod_times = {}
    for path in Path(directory).rglob('*.qmd'):
        mod_times[path] = path.stat().st_mtime
    return mod_times

def check_for_changes(old_times, directory):
    """Check if any .qmd files have been modified since last check"""
    new_times = get_file_modification_times(directory)
    
    # Check for new or modified files
    for file_path, mod_time in new_times.items():
        if file_path not in old_times or mod_time > old_times[file_path]:
            return True, new_times
    
    # Check if any files were deleted
    if len(old_times) != len(new_times):
        return True, new_times
    
    return False, new_times

def render_quarto(project_path):
    """Render the Quarto project using simple command"""
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] Rendering Quarto project...")
    
    # Simple render command without any browser options
    cmd = ["quarto", "render", str(project_path)]
    
    # Windows needs shell=True to find commands properly
    use_shell = True if sys.platform == "win32" else False
    
    try:
        # Run the render command and capture output
        result = subprocess.run(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              text=True,
                              check=False,
                              shell=use_shell)
        
        # Check if command succeeded
        if result.returncode == 0:
            print(f"[{timestamp}] Render completed successfully")
            return True
        else:
            print(f"[{timestamp}] Error rendering project (exit code {result.returncode})")
            if result.stderr:
                print(f"Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"[{timestamp}] Exception while rendering: {e}")
        return False

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Auto Quarto Render Script")
    parser.add_argument("project_path", nargs="?", default="./", 
                        help="Path to the Quarto project (default: current directory)")
    parser.add_argument("interval", type=int, nargs="?", default=60, 
                        help="Seconds between renders (default: 60, 0 for file monitoring only)")
    
    return parser.parse_args()

def main():
    # Parse command line arguments
    args = parse_arguments()
    project_path = Path(args.project_path).resolve()
    interval = args.interval
    
    # Check if project path exists
    if not project_path.exists():
        print(f"Error: Project path does not exist: {project_path}")
        return
    
    print(f"Auto Quarto Render started")
    print(f"Project path: {project_path}")
    
    if interval > 0:
        print(f"Render interval: {interval} seconds")
    else:
        print("Mode: File monitoring (render on changes)")
    
    print(f"Press Ctrl+C to stop")
    print("-" * 50)
    
    # Get initial file modification times if in monitoring mode
    file_mod_times = get_file_modification_times(project_path) if interval == 0 else {}
    
    # Initial render
    render_quarto(project_path)
    last_render_time = time.time()
    
    try:
        # Main loop
        while True:
            if interval == 0:
                # File monitoring mode
                changes_detected, file_mod_times = check_for_changes(file_mod_times, project_path)
                if changes_detected:
                    render_quarto(project_path)
                    last_render_time = time.time()
                time.sleep(1)  # Check for changes every second
            else:
                # Time-based interval mode
                current_time = time.time()
                if current_time - last_render_time >= interval:
                    render_quarto(project_path)
                    last_render_time = current_time
                time.sleep(1)  # Sleep for a short time to avoid CPU overuse
                
    except KeyboardInterrupt:
        print("\nAuto Quarto Render stopped")

if __name__ == "__main__":
    main()