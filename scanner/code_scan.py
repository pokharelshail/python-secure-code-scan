import subprocess
import os

def scan_code(project_path):
    report_file_name = "reports/vulnerability_scan_report.txt"
    with open(report_file_name, "w") as report_file:
        python_dirs = []

        for root, dirs, files in os.walk(project_path):
            if any(file.endswith(".py") for file in files):
                python_dirs.append(root)

        for py_dir in python_dirs:
            try:
                command = ["bandit", "-r", py_dir, "-ll", "-f", "txt"]
                result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
     
                report_file.write(f"Bandit scan for directory: {py_dir}\n")
                report_file.write(result.stdout)
                report_file.write(result.stderr)
                report_file.write("\n\n")
            except Exception as e:
                report_file.write(f"Error running Bandit on {py_dir}: {e}\n")

    print(f"Vulnerability scan report written to {report_file_name}")
    return report_file_name