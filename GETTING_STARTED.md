# ENGR315 - Getting Started Guide

> **Note:** This guide was generated with assistance from Claude (Anthropic AI) to ensure clear, comprehensive setup instructions for students.

Welcome to ENGR315: Computational Methods in Engineering! This guide will walk you through setting up your development environment for the course.

## Prerequisites

- A computer running Windows, macOS, or Linux
- Internet connection
- Administrator access to install software

## Step 1: Sign Up for GitHub

GitHub is a platform for hosting and collaborating on code. You'll use it to access course materials.

1. Go to [https://github.com](https://github.com)
2. Click **Sign up** in the top-right corner
3. Follow the prompts to create your account:
   - Enter your email address (use your school email if possible)
   - Create a password
   - Choose a username
   - Complete the verification
4. Verify your email address by clicking the link sent to your inbox

**Note:** If you already have a GitHub account, you can use it for this course.

## Step 2: Install GitHub Desktop

GitHub Desktop is a user-friendly application that makes it easy to manage your code and sync with GitHub.

1. Go to [https://desktop.github.com](https://desktop.github.com)
2. Click **Download for Windows** or **Download for macOS**
3. Install GitHub Desktop:
   - **Windows:** Run the downloaded `.exe` file and follow the installer
   - **macOS:** Open the downloaded `.dmg` file and drag GitHub Desktop to Applications
4. Launch GitHub Desktop
5. Sign in to GitHub:
   - Click **Sign in to GitHub.com**
   - Enter your GitHub username and password
   - Click **Authorize desktop** if prompted

**Note for Linux users:** GitHub Desktop is not officially supported on Linux. You can use Git command-line tools instead, or consider using a third-party client like GitKraken.

## Step 3: Install Python

**Important:** Install Python before VSCode so that VSCode can automatically detect it!

We'll use Python 3.12 for this course. Download Python 3.12 directly here: [https://www.python.org/downloads/release/python-31210/](https://www.python.org/downloads/release/python-31210/)

### Check if Python is Already Installed

1. Open a terminal:
   - **Windows:** Open Command Prompt or PowerShell
   - **macOS/Linux:** Open Terminal
2. Type `python3 --version` and press Enter
3. If you see `Python 3.12.x`, `Python 3.11.x`, or `Python 3.13.x`, you're good to go!

### If Python is Not Installed

**Windows:**
1. Go to [https://www.python.org/downloads/release/python-31210/](https://www.python.org/downloads/release/python-31210/)
2. Scroll down to the "Files" section and download **Windows installer (64-bit)**
3. Run the downloaded installer
4. **Important:** Check the box "Add Python to PATH" at the bottom
5. Click "Install Now"

**macOS:**
1. Go to [https://www.python.org/downloads/release/python-31210/](https://www.python.org/downloads/release/python-31210/)
2. Scroll down to the "Files" section and download **macOS 64-bit universal2 installer**
3. Open the downloaded `.pkg` file
4. Follow the installation wizard:
   - Click "Continue" through the introduction screens
   - Agree to the license
   - Click "Install" (you may need to enter your password)
5. Once complete, click "Close"
6. Python is now installed!

**Linux:**
```bash
sudo apt-get install python3 python3-pip  # Ubuntu/Debian
sudo yum install python3 python3-pip       # Fedora/CentOS
```

## Step 4: Install Visual Studio Code

Visual Studio Code (VSCode) is the code editor we'll use for this course.

1. Go to [https://code.visualstudio.com](https://code.visualstudio.com)
2. Click **Download** for your operating system
3. Install VSCode:
   - **Windows:** Run the downloaded `.exe` file and follow the installer
   - **macOS:** Open the downloaded `.dmg` file and drag VSCode to Applications
   - **Linux:** Follow the instructions for your distribution on the download page
4. Launch VSCode

### Install Python Extension

1. In VSCode, click the **Extensions** icon in the left sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X`)
2. Search for "Python"
3. Install the **Python** extension by Microsoft (it should be the first result)
4. VSCode should automatically detect the Python installation from Step 3

## Step 5: Fork and Clone the Course Repository

### Why Fork Instead of Just Clone?

In this step, you'll create your own personal copy of the course materials on GitHub (called a "fork"). Here's why this is important:

**What you get with a fork:**
- 💾 **Save your work**: Your code, notes, and modifications are saved to your GitHub account
- 🔄 **Get updates**: When your instructor adds new assignments or fixes, you can easily pull those into your copy
- 📝 **Track your progress**: You can commit your work as you go and see your history
- 🎒 **Portfolio piece**: Your fork serves as a portfolio showing your coursework

**The process:**
1. **Fork** on GitHub.com = Creates your personal copy on GitHub's servers
2. **Clone** to your computer = Downloads your fork so you can work on it locally

Think of it like getting your own textbook that you can write in, while the instructor can still give you updated pages!

### Part A: Fork the Repository on GitHub

1. Make sure you're signed into GitHub in your web browser
2. Go to the course repository: [https://github.com/JMU-Engineering/ENGR315-fa2026-student](https://github.com/JMU-Engineering/ENGR315-fa2026-student)
3. In the top-right corner of the page, click the **Fork** button
4. On the "Create a new fork" page:
   - Keep the default repository name: `ENGR315-fa2026-student`
   - You can add a description if you want (optional)
   - Make sure **"Copy the main branch only"** is checked
5. Click **Create fork**
6. GitHub will create your personal copy of the repository (this takes a few seconds)

You now have your own copy at `https://github.com/YOUR-USERNAME/ENGR315-fa2026-student`

### Part B: Clone Your Fork to Your Computer

1. Open **GitHub Desktop**
2. Click **File** → **Clone repository** (or press `Ctrl+Shift+O` / `Cmd+Shift+O`)
3. Look in the list of **Your repositories** - you should see `ENGR315-fa2026-student`
4. Select it and choose where to save it on your computer:
   - Click **Choose...** next to "Local path"
   - Select a location (e.g., `Documents/ENGR315`)
5. Click **Clone**
6. **Important:** GitHub Desktop will ask "How are you planning to use this fork?"
   - Select **"For my own purposes"**
   - This ensures you're working on your own copy, not trying to contribute back to the course repository
   - Click **Continue**
7. Wait for the repository to download (this may take a minute)
8. Once complete, click **Open in Visual Studio Code** (or go to Repository → Open in Visual Studio Code)

The course materials are now on your computer and opened in VSCode!

### Getting Updates from the Instructor

When your instructor updates the course materials, you can pull those changes into your fork:

1. Open **GitHub Desktop**
2. Make sure your repository is selected
3. Go to **Repository** → **Fetch** (or press `Ctrl+Shift+T` / `Cmd+Shift+T`)
4. Go to **Branch** → **Merge into current branch...** (or press `Ctrl+Shift+M` / `Cmd+Shift+M`)
5. Select branch **upstream/main** that to be merge into your branch **main**
6. The new changes will be downloaded to your computer

**Note:** If you've modified any files that the instructor also updated, you may need to resolve "merge conflicts." Ask for help if this happens!

**Note:** Frequent **commit** and **push** operations will help to track your changes, and sync Github (Cloud) with our local files.

## Step 6: Create a Virtual Environment and Install Python Packages

The course requires several Python packages for data analysis. We'll create a virtual environment (an isolated Python workspace) and install the packages there.

### Why Use a Virtual Environment?

A virtual environment keeps this course's packages separate from other Python projects on your computer. Think of it like having a separate toolbox just for this class!

### Create and Activate the Virtual Environment

1. In VSCode, open the repository folder (if not already open)
2. Go to **Terminal** → **New Terminal** (or press `` Ctrl+Shift+` ``)
   - A terminal panel will appear at the bottom of VSCode
3. Make sure you're in the repository folder. The terminal should show the path ending in `ENGR315-fa2026-student`
4. Create the virtual environment by typing this command and pressing Enter:
   
   **Windows:**
   ```bash
   python -m venv venv
   ```
   
   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   ```
   
5. Wait a few seconds while the virtual environment is created (a new `venv` folder will appear)

6. **Activate** the virtual environment:
   
   **Windows (Command Prompt or PowerShell):**
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

7. **You'll know it worked** when you see `(venv)` appear at the beginning of your terminal prompt, like:
   ```
   (venv) C:\Users\YourName\Documents\ENGR315\ENGR315-fa2026-student>
   ```
   or
   ```
   (venv) ~/Documents/ENGR315/ENGR315-fa2026-student %
   ```

### Install Required Packages

Now that your virtual environment is active, install the required packages:

1. With `(venv)` showing in your terminal prompt, type this command and press Enter:
   
   **Windows:**
   ```bash
   pip install -r requirements.txt
   ```
   
   **macOS/Linux:**
   ```bash
   pip3 install -r requirements.txt
   ```

2. Wait a few minutes while packages download and install (you'll see lots of text scrolling by)
3. When complete, you'll see "Successfully installed" followed by a list of packages

**What's being installed:**
- `numpy` - For numerical computations
- `pandas` - For data analysis
- `matplotlib` - For creating graphs
- `scipy` - For scientific computing
- And several other helpful packages!

### Tell VSCode to Use Your Virtual Environment

This is important! VSCode needs to know to use the virtual environment you just created:

1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS) to open the Command Palette
2. Type "Python: Select Interpreter" and select it from the list
3. You should see several Python options. Choose the one that says:
   - `Python 3.x.x ('venv': venv)` or
   - `./venv/bin/python` (macOS/Linux) or
   - `.\venv\Scripts\python.exe` (Windows)
4. Click on it to select it

Now VSCode will automatically use your virtual environment whenever you run Python code!

### Do You Need to Activate the Environment Every Time?

**Important: Always use your virtual environment for this course!** This ensures you have the correct packages and versions.

**Short answer:** Not usually! Once you've selected the interpreter in VSCode (step above), VSCode will automatically activate it for you when running Python files.

**However, if you ever open a new terminal manually** and see that `(venv)` is not showing, you **must** activate it again using the activation command from step 6 above before running `pip` commands or executing Python from the terminal.

**Quick check:** Look at your terminal prompt. If you see `(venv)` at the beginning, you're good! If not, activate it.

Once you see the success message, you're ready to code! 🎉

## Step 7: Run Your First Python Program

Let's verify everything is working by running a simple Python program!

### Open the File

1. Look at the **left sidebar** in VSCode - this is called the **Explorer**
2. You should see your repository folder with several folders inside
3. Click the folder icon next to `Module 0 - Getting Started` to expand it
4. Click on `Hello_World.py` - the file will open in the main editor area

You should now see Python code in the editor that looks something like:
```python
print("Hello, World!")
```

### Run the Program

There are several ways to run the program. Pick the easiest one:

**Method 1: Using the Play Button (Recommended)**
1. Look in the **top-right corner** of the editor window (where your code is)
2. You'll see a **▶️ (Play) button** with a small triangle
3. Click this button
4. The program will run immediately

**Method 2: Right-Click Menu**
1. **Right-click** anywhere in the code editor
2. Select **"Run Python File"** from the menu that appears
3. The program will execute

**Method 3: Keyboard Shortcut**
1. Make sure the `Hello_World.py` file is active (click in the editor)
2. Press `Ctrl+F5` (Windows/Linux) or `Cmd+F5` (macOS)

### Where to Look for the Output

After running the program, **look at the bottom half of VSCode**:

1. A **Terminal panel** should automatically appear at the bottom of your screen
2. You might see several tabs like "PROBLEMS", "OUTPUT", "DEBUG CONSOLE", and **"TERMINAL"**
3. Click on the **"TERMINAL"** tab if it's not already selected
4. In the terminal, you should see:
   ```
   Hello, World!
   ```
5. Above this output, you might see the command that ran, something like:
   ```
   /path/to/python /path/to/Hello_World.py
   ```

**Visual Guide:**
- **Top**: Menu bar and file tabs
- **Left sidebar**: Explorer (file tree)
- **Center**: Code editor (your Python file)
- **Right**: May have additional panels (can ignore for now)
- **Bottom**: Terminal/Output panel (this is where results appear!)

### Success!

If you see "Hello, World!" in the terminal at the bottom, **congratulations!** 🎉 

Your environment is set up correctly and you're ready to start coding!

### If You Don't See the Terminal

If the terminal doesn't appear at the bottom:
1. Go to the top menu: **View** → **Terminal**
2. Or press `` Ctrl+` `` (that's the backtick key, usually above Tab)
3. The terminal panel should now appear at the bottom

## Troubleshooting

### "python is not recognized" or "command not found"

**Solution:** Python is not in your PATH. 
- **Windows:** Reinstall Python and make sure to check "Add Python to PATH"
- **macOS/Linux:** Use `python3` instead of `python`

### "No module named 'numpy'" (or other package)

**Solution:** The required packages aren't installed.
- Run `pip3 install -r requirements.txt` in the terminal
- Make sure you're in the correct folder (the repository root)

### VSCode can't find Python

**Solution:** 
1. Press `Ctrl+Shift+P` / `Cmd+Shift+P`
2. Type "Python: Select Interpreter"
3. Choose the Python 3.x version you installed

### Git clone fails with authentication error

**Solution:**
- Make sure you're logged into GitHub in your browser
- Try cloning again
- If problems persist, download the repository as a ZIP file from GitHub and extract it

## Getting Help

If you encounter issues:

1. Ask during office hours
2. Email the instructor or TA
3. Search online (Stack Overflow is your friend!)

## Next Steps

Now that your environment is set up:

1. Explore the `Module 0 - Getting Started` folder
2. Review the course syllabus and schedule
3. Complete any assigned readings or exercises
4. Get familiar with VSCode's interface

Welcome to ENGR315! 🚀
