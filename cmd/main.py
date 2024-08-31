import sys
import os
import subprocess
import shutil
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scanner.code_scan import scan_code
from scanner.config_scan import check_config


def clone_repository(repo_url):
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    local_repo_path = os.path.join(os.getcwd(), repo_name)

    if os.path.exists(local_repo_path):
        shutil.rmtree(local_repo_path)

    subprocess.run(["git", "clone", repo_url, local_repo_path], check=True)
    return local_repo_path

#TODO: Add scanning dependencies Logic
def scan_dependencies(project_path):
    return []

def generate_report(dependencies, bandit_report_file, config_issues):
    report_data = {
        "dependencies": dependencies,
        "bandit_report_file": bandit_report_file,
        "config_issues": config_issues
    }
    
    report_file = "reports/security_report.json"
    with open(report_file, "w") as file:
        json.dump(report_data, file, indent=4)
    
    print(f"Security report written to {report_file}")
    return report_file

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <github_repo_url_or_local_directory>")
        sys.exit(1)

    input_path = sys.argv[1]

    if input_path.startswith("http"):
        repo_path = clone_repository(input_path)
    elif os.path.isdir(input_path):
        repo_path = input_path
    else:
        print("Invalid input. Please provide a valid GitHub URL or a local directory path.")
        sys.exit(1)

    dependencies_report = scan_dependencies(repo_path)
    bandit_report_file = scan_code(repo_path)
    config_report = check_config(repo_path)

    generate_report(dependencies_report, bandit_report_file, config_report)

if __name__ == "__main__":
    main()
