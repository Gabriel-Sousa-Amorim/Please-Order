# [Please-Order](https://github.com/Gabriel-Sousa-Amorim/Please-Order/)

A Python Project, that can order a directory and their children. That can order or by Modification Date or by Extension Type.

### Requirements

- Python 3.4+ (recommended Python 3.4 or later)
- Pip (required if using Python below 3.4)
- Git (optional for cloning the repository)

## Installation

1. Clone the repository or download the source code:

```sh
git clone https://github.com/Gabriel-Sousa-Amorim/Please-Order.git
```

2. Navigate to the project directory:

```sh
cd Please-Order/
```

3. Install requirements:

```
pip install -r requirements.txt
```

## Usage

To generate ASCII art from an image, run the following command:

```sh
python3 order.py <option-of-order> <path-to-order>
```

- Replace `<option-to-order>`, with one of the two options:
  - `-d` Sort by Date.
  - `-t` Sort by Type.

- Replace `<path-to-order>` to a relative or absolute path to be ordered. 

> [!WARNING]  
> It Does not copy the files, it moves the files. And can remove files with the same name, so before running the script, it is reccomended to BACKUP the files.

## Running Tests

Check the [tests/](https://gabriel-sousa-amorim.github.io/Please-Order/tests/) folder for example outputs.
