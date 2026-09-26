import tkinter as tk
from tkinter import filedialog, messagebox
import os


# ============================================================
# TERMINAL TEXT EDITOR
# ============================================================

def terminal_editor():

    while True:

        print("\n" + "=" * 50)
        print("           TERMINAL TEXT EDITOR")
        print("=" * 50)

        print("1. New File")
        print("2. Open File")
        print("3. Save File")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        # ----------------------------------------------------
        # NEW FILE
        # ----------------------------------------------------

        if choice == "1":

            print("\n--- New File ---")
            print("Enter your text.")
            print("Type '::END::' on a new line to finish.\n")

            lines = []

            while True:
                line = input()

                if line == "::END::":
                    break
                lines.append(line)

            text_content = "\n".join(lines)

            print("\nYour text:")
            print("-" * 50)
            print(text_content)
            print("-" * 50)

            save_choice = input(
                "\nDo you want to save this file? (y/n): ").lower()

            if save_choice == "y":
                save_terminal_file(text_content)

        # ----------------------------------------------------
        # OPEN FILE
        # ----------------------------------------------------

        elif choice == "2":
            file_path = input(
                "\nEnter the path of the file to open: "
            ).strip()

            if os.path.exists(file_path):
                try:
                    with open(
                        file_path,
                        "r",
                        encoding="utf-8"
                    ) as file:

                        content = file.read()

                    print("\n" + "-" * 50)
                    print("FILE CONTENT")
                    print("-" * 50)

                    print(content)

                    print("-" * 50)

                    edit_choice = input(
                        "\nDo you want to edit this file? (y/n): "
                    ).lower()

                    if edit_choice == "y":
                        print(
                            "\nEnter new content.")

                        print(
                            "Type '::END::' on a new line "
                            "to finish.\n")

                        lines = []

                        while True:
                            line = input()

                            if line == "::END::":
                                break
                            lines.append(line)

                        new_content = "\n".join(lines)

                        save_choice = input(
                            "\nDo you want to save changes? (y/n): ").lower()

                        if save_choice == "y":
                            save_terminal_file(
                                new_content,
                                file_path
                            )

                except Exception as error:

                    print(
                        "\nError opening file:",
                        error
                    )

            else:
                print("\nFile not found.")

        # ----------------------------------------------------
        # SAVE FILE
        # ----------------------------------------------------

        elif choice == "3":
            print(
                "\nTo save a new file, "
                "enter your text below.")

            print(
                "Type '::END::' on a new line "
                "to finish.\n")

            lines = []

            while True:
                line = input()

                if line == "::END::":
                    break
                lines.append(line)

            content = "\n".join(lines)
            save_terminal_file(content)

        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        elif choice == "4":
            print(
                "\nExiting Terminal Editor...")
            break

        else:
            print(
                "\nInvalid choice. "
                "Please select 1-4.")


def save_terminal_file(content, existing_path=None):
    if existing_path:
        file_path = existing_path

    else:
        file_path = input(
            "\nEnter filename to save "
            "(example: notes.txt): "
        ).strip()

    if not file_path:
        print("Invalid filename.")
        return

    # Automatically add .txt
    if not file_path.lower().endswith(".txt"):
        file_path += ".txt"

    try:
        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(content)

        print(
            f"\nFile saved successfully!")

        print(
            "Location:",
            os.path.abspath(file_path))

    except Exception as error:

        print(
            "\nError saving file:",
            error)


# ============================================================
# GUI TEXT EDITOR
# ============================================================

def gui_editor():

    root = tk.Tk()

    root.title("Simple Text Editor")

    root.geometry("800x600")

    # --------------------------------------------------------
    # NEW FILE
    # --------------------------------------------------------

    def new_file():

        text.delete(
            "1.0",
            tk.END)

        root.title("Simple Text Editor - New File")

    # --------------------------------------------------------
    # OPEN FILE
    # --------------------------------------------------------

    def open_file():

        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")])

        if file_path:
            try:
                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as file:
                    content = file.read()

                text.delete(
                    "1.0",
                    tk.END)

                text.insert(
                    tk.END,
                    content)

                root.title(
                    f"Simple Text Editor - "
                    f"{os.path.basename(file_path)}")

            except Exception as error:

                messagebox.showerror(
                    "Error",
                    f"Unable to open file:\n{error}")

    # --------------------------------------------------------
    # SAVE FILE
    # --------------------------------------------------------

    def save_file():

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")])

        if file_path:

            try:
                content = text.get(
                    "1.0",
                    tk.END)

                with open(
                    file_path,
                    "w",
                    encoding="utf-8"
                ) as file:

                    file.write(content)

                messagebox.showinfo(
                    "Success",
                    "File saved successfully!")

                root.title(
                    f"Simple Text Editor - "
                    f"{os.path.basename(file_path)}")

            except Exception as error:

                messagebox.showerror(
                    "Error",
                    f"Unable to save file:\n{error}")

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    def exit_editor():

        root.destroy()

    # --------------------------------------------------------
    # MENU
    # --------------------------------------------------------

    menu = tk.Menu(root)

    root.config(
        menu=menu)

    # File menu
    file_menu = tk.Menu(
        menu,
        tearoff=0)

    menu.add_cascade(
        label="File",
        menu=file_menu)

    file_menu.add_command(
        label="New",
        command=new_file)

    file_menu.add_command(
        label="Open",
        command=open_file)

    file_menu.add_command(
        label="Save",
        command=save_file)

    file_menu.add_separator()

    file_menu.add_command(
        label="Exit",
        command=exit_editor)

    # --------------------------------------------------------
    # TEXT AREA
    # --------------------------------------------------------

    text = tk.Text(
        root,
        wrap=tk.WORD,
        font=("Helvetica", 12),
        fg="blue")

    text.pack(
        expand=True,
        fill=tk.BOTH)

    # --------------------------------------------------------
    # SCROLLBAR
    # --------------------------------------------------------

    scrollbar = tk.Scrollbar(
        root,
        command=text.yview)

    scrollbar.pack(
        side=tk.RIGHT,
        fill=tk.Y)

    text.config(
        yscrollcommand=scrollbar.set)

    # --------------------------------------------------------
    # KEYBOARD SHORTCUTS
    # --------------------------------------------------------

    root.bind(
        "<Control-n>",
        lambda event: new_file())

    root.bind(
        "<Control-o>",
        lambda event: open_file())

    root.bind(
        "<Control-s>",
        lambda event: save_file())

    root.bind(
        "<Control-q>",
        lambda event: exit_editor())

    # --------------------------------------------------------
    # START GUI
    # --------------------------------------------------------

    root.mainloop()


# ============================================================
# START PROGRAM
# ============================================================

def main():

    print("\n" + "=" * 60)
    print("             SIMPLE TEXT EDITOR")
    print("=" * 60)

    print("\nHow would you like to run the editor?")

    print("\n1. Terminal")
    print("2. GUI Editor")
    print("3. Exit")

    while True:

        choice = input(
            "\nEnter your choice (1/2/3): "
        ).strip()

        if choice == "1":
            terminal_editor()
            break

        elif choice == "2":
            gui_editor()
            break

        elif choice == "3":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. "
                "Please enter 1, 2, or 3.")


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":

    main()
