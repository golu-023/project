# Simple Text Editor

A minimal desktop text editor built with Python and Tkinter. It lets you create a new document, open an existing `.txt` file, edit text, and save it back to disk, all from a small graphical window.

The whole application lives in a single file: `project.py`.

---

## Features

- **New**: clears the editor so you can start a fresh document
- **Open**: loads a `.txt` file from disk into the editor
- **Save**: writes the editor contents to a `.txt` file and shows a confirmation dialog
- **Exit**: closes the application
- Word-wrapped editing area (Helvetica, size 12, blue text)

---

## Requirements

| Requirement | Details |
|---|---|
| Python | 3.6 or newer (3.8+ recommended) |
| Tkinter | Included with Python on Windows and macOS; may need a separate install on Linux (see below) |
| Third-party packages | **None**. The project only uses the Python standard library (`tkinter`), so there is no `requirements.txt` and nothing to `pip install`. |
| Operating system | Windows, macOS, or Linux with a graphical desktop |

> A graphical display is required. The app will not run in a headless terminal or SSH session without a display.

---

## Step-by-Step Setup

### 1. Get the project files

Place `project.py` in a folder of your choice, for example `simple-text-editor/`. If the project is in a Git repository, clone it instead:

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Check that Python is installed

Open a terminal (macOS/Linux) or Command Prompt / PowerShell (Windows) and run:

```bash
python --version
```

If that fails, try:

```bash
python3 --version
```

You should see something like `Python 3.10.12`. If Python is not installed, download it from <https://www.python.org/downloads/>.

- **Windows:** during installation, tick **"Add Python to PATH"**.
- Use whichever command works (`python` or `python3`) for the rest of this guide.

### 3. Make sure Tkinter is available

Verify Tkinter with:

```bash
python -m tkinter
```

A small test window titled "tk" should appear. Close it and continue.

If you get `ModuleNotFoundError: No module named 'tkinter'`, install it for your OS:

| OS | Command |
|---|---|
| Debian / Ubuntu / Mint | `sudo apt update && sudo apt install python3-tk` |
| Fedora | `sudo dnf install python3-tkinter` |
| Arch | `sudo pacman -S tk` |
| macOS (Homebrew Python) | `brew install python-tk` |
| Windows / macOS (python.org installer) | Already included. Re-run the Python installer and make sure **"tcl/tk and IDLE"** is selected. |

### 4. (Optional) Create a virtual environment

Because there are no dependencies, this step is optional. It is still good practice for isolating your setup:

```bash
python -m venv venv
```

Activate it:

- **Windows (Command Prompt):** `venv\Scripts\activate`
- **Windows (PowerShell):** `venv\Scripts\Activate.ps1`
- **macOS / Linux:** `source venv/bin/activate`

### 5. Install dependencies

Nothing to install. The project uses only Python's built-in `tkinter` module.

### 6. Configuration

No configuration files, environment variables, or API keys are needed. If you want to change the look of the editor, edit these lines in `project.py`:

| Setting | Line in `project.py` | Default |
|---|---|---|
| Window title | `root.title("simple text Editor")` | `simple text Editor` |
| Window size | `root.geometry("800x600")` | `800x600` pixels |
| Font and text color | `tk.Text(..., font=("helvetica", 12), fg="blue")` | Helvetica 12, blue |

---

## Running the Application

From the folder containing `project.py`, run:

```bash
python project.py
```

(or `python3 project.py` on systems where `python` is not available).

An 800x600 window titled **"simple text Editor"** will open with an empty editing area and a **File** menu.

---

## How to Use

1. **Type** in the editing area to write text.
2. **File → New** clears the editor. Note: unsaved text is discarded without a prompt.
3. **File → Open** opens a file picker. Choose a `.txt` file and its contents replace the current editor text.
4. **File → Save** opens a "Save as" dialog. Choose a location and file name (`.txt` is added by default). A confirmation message appears when the file is saved.
5. **File → Exit** closes the program.

### Quick test to confirm everything works

1. Run `python project.py`.
2. Type `Hello, world!` into the window.
3. Choose **File → Save**, name the file `test`, and click Save. You should see a "file save successfully!" message.
4. Choose **File → New** (the text disappears).
5. Choose **File → Open**, select `test.txt`. `Hello, world!` should reappear.

---

## Troubleshooting

| Problem | Cause / Fix |
|---|---|
| `ModuleNotFoundError: No module named 'tkinter'` | Tkinter is not installed. See Step 3. |
| `'python' is not recognized` (Windows) | Python is not on PATH. Reinstall it with "Add Python to PATH" ticked, or use `py project.py`. |
| `python: command not found` (macOS/Linux) | Use `python3 project.py` instead. |
| `_tkinter.TclError: no display name and no $DISPLAY environment variable` | You are in an environment with no graphical display (e.g., plain SSH). Run on a desktop session. |
| Only `.txt` files appear in the Open dialog | By design: the file filter is limited to Text Files (`*.txt`). |

---

## Known Limitations

- Only plain-text `.txt` files are offered in the file dialogs.
- There is no "unsaved changes" warning when using New, Open, or Exit.
- Files are read and written using the system's default text encoding, so files with special characters in other encodings may not display correctly.
- Saving adds one trailing newline at the end of the file (a Tkinter `Text` widget behavior).

---

## Project Structure

```
.
├── project.py   # The entire application (UI + file logic)
└── README.md    # This file
```

## Code Overview

| Function / Section | Purpose |
|---|---|
| `new_file()` | Deletes all text in the editor |
| `open_file()` | Shows an open-file dialog and loads the chosen file into the editor |
| `save_file()` | Shows a save-file dialog, writes the editor contents to disk, and shows a success message |
| Main block | Creates the window, File menu (New / Open / Save / Exit), and the text area, then starts the Tkinter event loop with `root.mainloop()` |
