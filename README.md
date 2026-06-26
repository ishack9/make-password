# make-password

A Python tool that generates all possible permutations of given keywords or characters — useful for wordlist creation and brute-force testing.

## Requirements

```
pip install tqdm
```

## Usage

Run the script and enter your characters separated by spaces:

```
python make\_password.py
```

**Example input:**

```
Enter characters (separated by spaces): admin 1234 test
```

All unique permutations will be saved to `password.txt`.

## Output

|Characters|Combinations|
|-|-|
|1|1|
|2|4|
|3|15|
|4|64|
|5|325|
|6|1,956|
|7|15,656|
|8|140,913|

> ⚠ Large inputs (9+) will generate very large wordlists and may take a long time and can seriously overload your computer.

