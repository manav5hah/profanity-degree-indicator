# Profanity Degree Indication

[profanity-check](https://pypi.org/project/profanity-check/) module is being used to find the profanity degree.

## How It Works

`profanity-check` uses a linear SVM model trained on 200k human-labeled samples of clean and profane text strings. Its model is simple but surprisingly effective, meaning **`profanity-check` is both robust and extremely performant**.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install profanity-check.

```bash
pip install profanity-check
```

## Usage
After editing the demofile.txt run the following command to obtain the degree of profanity.
```python
python3 profanity-checker.py
```