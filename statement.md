# Project Statement: Simple Text Editor

## 1. Problem Statement

Many people, especially students and beginners, need a quick way to write, view, and save plain-text notes without opening a large word processor or a full code editor. Heavy applications take time to launch, offer many features that are not needed for simple tasks, and can be confusing for first-time users.

This project solves that problem by providing a small, lightweight desktop text editor with a clean interface. It lets users create, open, edit, and save plain-text files in just a few clicks, with no installation of extra libraries and no learning curve.

## 2. Scope of the Project

### In scope

- A desktop application built with Python and Tkinter
- Creating a new blank document
- Opening and viewing existing `.txt` files
- Editing text in a word-wrapped editing area
- Saving text to a `.txt` file with a confirmation message
- A simple **File** menu with New, Open, Save, and Exit options
- Running on Windows, macOS, and Linux desktops that have Python 3 and Tkinter

### Out of scope

- Rich-text formatting (bold, italics, font changes, colors chosen by the user)
- Support for file formats other than plain text (`.docx`, `.pdf`, etc.)
- Find and replace, spell check, undo/redo menus, or syntax highlighting
- Multiple tabs or multiple documents open at once
- Cloud storage, sync, or collaboration features
- Warnings for unsaved changes

## 3. Target Users

| User group | How they benefit |
|---|---|
| **Students and beginners in Python** | A small, readable example of a GUI application built with Tkinter, useful for learning |
| **Everyday users** | A fast, distraction-free tool for jotting down quick notes and saving them as text files |
| **Educators and evaluators** | A compact project that demonstrates GUI programming, event handling, and file input/output |

No technical background is needed to use the editor itself.

## 4. High-Level Features

1. **New Document**: clears the editor so the user can start writing from scratch.
2. **Open File**: opens a file picker and loads the chosen `.txt` file into the editor.
3. **Save File**: opens a "Save as" dialog, writes the text to a `.txt` file, and shows a success message.
4. **Exit**: closes the application from the File menu.
5. **Comfortable Editing Area**: a large, word-wrapped text box (800x600 window) using Helvetica 12 in blue text.
6. **Zero Dependencies**: uses only Python's built-in `tkinter` module, so it runs with no `pip install` step.
