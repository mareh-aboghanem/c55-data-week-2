# AI Debug Report — Task 2

While building Task 1 (the Cleaner Pipeline), you will encounter at least one bug. (If not, introduce one intentionally — pick the most surprising thing about Python you noticed this week and break it.)

Use an LLM (ChatGPT, Claude, etc.) to help you debug it, then fill in the four sections below. The goal is not "the AI fixed it"; the goal is showing you understood what was broken, what the AI suggested, and whether you accepted or pushed back.

Aim for 100-200 words per section. Bullet points are fine.

## The Error

What went wrong? Paste the traceback or the wrong-output sample. Include the file and the line you were running when it broke.

```
python C:\Users\Beheerder\c55-data-week-2\task-1\src\pipeline.py
C:\Users\Beheerder\AppData\Local\Microsoft\WindowsApps\python.exe: can't open file 'C:\\Users\\Beheerder\\c55-data-week-2\\UsersBeheerderc55-data-week-2task-1srcpipeline.py': [Errno 2] No such file or directory

Beheerder@Marah MINGW64 ~/c55-data-week-2 (main)
$ python -m task-1.src.pipeline
dotenv works!
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Beheerder\c55-data-week-2\task-1\src\pipeline.py", line 77, in <module>
    run()
  File "C:\Users\Beheerder\c55-data-week-2\task-1\src\pipeline.py", line 51, in run
    raw = read_csv(INPUT_PATH)
          ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Beheerder\c55-data-week-2\task-1\src\pipeline.py", line 34, in read_csv
    with open(path, mode='r', encoding='utf-8') as file:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'data/messy_sales.csv'
```

## The Prompt

What did you ask the AI? Paste the actual prompt verbatim. (Include the code or stack trace you pasted alongside it; do NOT include any real `.env` values, API keys, or PII — replace those with `<REDACTED>`.)

```
python C:\Users\Beheerder\c55-data-week-2\task-1\src\pipeline.py
C:\Users\Beheerder\AppData\Local\Microsoft\WindowsApps\python.exe: can't open file 'C:\\Users\\Beheerder\\c55-data-week-2\\UsersBeheerderc55-data-week-2task-1srcpipeline.py': [Errno 2] No such file or directory

Beheerder@Marah MINGW64 ~/c55-data-week-2 (main)
$ python -m task-1.src.pipeline
dotenv works!
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Beheerder\c55-data-week-2\task-1\src\pipeline.py", line 77, in <module>
    run()
  File "C:\Users\Beheerder\c55-data-week-2\task-1\src\pipeline.py", line 51, in run
    raw = read_csv(INPUT_PATH)
          ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Beheerder\c55-data-week-2\task-1\src\pipeline.py", line 34, in read_csv
    with open(path, mode='r', encoding='utf-8') as file:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'data/messy_sales.csv'
Is this error because of the data file in a different folder?
```

## The Solution

What did the AI suggest? Did it work on the first try? Did you have to follow up? Paste the final code change (a small diff is best).

```
#LLM Response like that:
Yes, exactly! You hit the nail on the head.

The error happens because of **where you are standing** (your current directory) versus **where the computer is looking**.

### The Problem

You are standing in `~/c55-data-week-2`.
Your code is trying to find `data/messy_sales.csv`.
But looking at your file structure, the data is actually inside `task-1/data/messy_sales.csv`.

Because you are in the "Root" folder, Python looks for a folder named `data` right next to you, doesn't see it, and panics.

### The Fix

You have two ways to fix this. **Option 1 is usually what instructors want.**

#### Option 1: Fix the `INPUT_PATH` (Recommended)

Open your `config.py` (or wherever `INPUT_PATH` is defined) and change it to include the `task-1` folder:

```python
# Change this:
INPUT_PATH = "data/messy_sales.csv"

# To this:
INPUT_PATH = "task-1/data/messy_sales.csv"
OUTPUT_PATH = "task-1/output/cleaned_sales.csv"

```

#### Option 2: Run from inside the `task-1` folder

If you don't want to change the code, you have to move your terminal "closer" to the data:

1. **Move into the task folder:**
```bash
cd task-1

```


2. **Run the module from there:**
```bash
python -m src.pipeline

```


*(Note: Since you moved inside `task-1`, you drop the `task-1.` prefix from the command.)*

### Why "dotenv works!" is a good sign

The fact that you see `dotenv works!` means your Python environment is working and it successfully found your `pipeline.py`. You are 99% of the way there—you just need to point the "boss" (the script) to the right "filing cabinet" (the data folder).

**Try Option 1 first**, as it makes your project more stable when running from the main directory!
```

## Reflection

Did you understand *why* the original code was broken before the AI told you? If not, what was the gap in your mental model? If you understood it before asking, why did you still ask the AI — speed, second opinion, or something else?

(write here, ~100 words)
Actually, yes, I understand what the problem was, but I wanted to check if I understand the trace in the correct way, and also to add something in task-2 as well ^_^.