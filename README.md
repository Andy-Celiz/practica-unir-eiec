# Repo for EIEC - DevOps - UNIR

This repository is intended to demonstrate the use of Git for the EIEC course and other related topics.

---

Makefile commands are designed for Linux and macOS. On Windows you may need to adapt them or run them inside a Linux virtual machine.

## Usage

Run the script with:

python3 main.py <filename> <dup>

- `filename`: path to a file containing a list of words, one per line.
- `dup`: `yes` or `no`. Use `yes` to remove duplicate words, `no` to keep duplicates.

## Example

Given a file `words.txt` with the following contents:

apple
banana
apple
cherry

Command (remove duplicates):

python3 main.py words.txt yes

Expected behaviour: the script will print or save the unique words from `words.txt` (order may depend on implementation).

Command (keep duplicates):

python3 main.py words.txt no

Expected behaviour: the script will process the file keeping duplicate entries.

## Additional functionality (suggested)

Here are a few suggested extra features you might want to add to the script:

- `--sort` : output the words sorted alphabetically.
- `--count` : output each word with its frequency/count.
- `--output <file>` : write the result to a specified file (e.g., CSV or TXT).

If you want, I can implement any of these features (or another one you prefer). Tell me which one you'd like me to add.
