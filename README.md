# Particle Bloom Simulator

This repository includes an interactive particle playground. The simulator lives in
[`particles.html`](particles.html) and can be launched directly in any modern
browser or by using the helper script described below.

## Quick start

1. Ensure you have Python 3.8 or newer installed.
2. From this repository's root folder, run:
   ```bash
   python3 run_particles.py
   ```
3. Your default browser will open the simulator automatically. If it does not,
   visit the printed local URL manually.
4. Press <kbd>Ctrl</kbd> + <kbd>C</kbd> in the terminal to stop the server when
you are done playing.

The script simply serves the HTML file from a local HTTP server so you can enjoy
the experience without manually configuring a server or editor.

## Direct launch

Alternatively, you can open `particles.html` directly in your browser by dragging
and dropping the file into a tab or using `File → Open`. The helper script is
provided for convenience if your environment blocks local `file://` access or if
you prefer a quick command-line launcher.
