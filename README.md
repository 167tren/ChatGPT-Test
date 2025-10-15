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

## Rogue-like cycles

The simulator now plays like a miniature rogue-lite run:

- Every run starts by choosing one of three **Resonances** (boons) that twist
  the physics—more particles, brighter glow, stronger cascades, and so on.
- Firing bursts and running the continuous emitter earns **quanta**. Fill the
  progress ring in the lower-left panel to advance the cycle.
- Advancing to a new cycle grants another resonance, while every third cycle
  forces you to endure a random **Entropy** curse that adds fresh constraints.
- Click the cards, press the matching number key (1–3), or hit <kbd>Esc</kbd>
  when skipping is allowed to make your selection.
- The “Restart Run” button lets you wipe your build and roll a fresh set of
  surprises at any time.

Experiment with different combinations—stack echoes for cascading bursts, lean
into shard generation for rapid leveling, or embrace curses that tame your
favorite color mode. Every run plays a little differently.
