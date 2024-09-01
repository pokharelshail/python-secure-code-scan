# Open Source Python Security Scanner

## Overview

This project is a Python-based security scanner that works with both GitHub repositories and local directories. Currently, it scans only Python files for vulnerabilities, using Bandit for code analysis and checking for exposed secrets in configuration files.

## Features

- **Clone GitHub Repositories**: Automatically clone a GitHub repository to scan it.
- **Code Scanning**: Uses Bandit to find security issues in Python code.
- **Configuration Scanning**: Detects exposed secrets in `.env` files.
- **Reports**: Generates detailed reports in the `reports/` directory.

## Usage

### Cloning and Scanning a GitHub Repository

```bash
python3 cmd/main.py https://github.com/user/repo.git
```

### Scanning a Local Directory

```bash
python3 cmd/main.py /path/to/local/directory
```

## Example with a Vulnerable Flask Project

To see the scanner in action, you can use a deliberately vulnerable Flask project. From the project root, run the scanner with the following command:

```bash
python3 cmd/main.py https://github.com/we45/Vulnerable-Flask-App.git
```

This example uses [Vulnerable-Flask-App](https://github.com/we45/Vulnerable-Flask-App) which is an intentionally vulnerable Flask application. Running the command will scan the project for vulnerabilities and generate reports in the reports/ directory.

## Requirements

Install the required Python packages with:

```bash
pip install -r requirements.txt
```

## Output

- **Vulnerability Scan Report**: `vulnerability_scan_report.txt`
- **Final Security Report**: `security_report.json`

## Contributing

Feel free to fork this repository and submit pull requests to improve the scanner.
