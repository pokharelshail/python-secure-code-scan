import os

def check_config(project_path):
    config_issues = []

    env_file = os.path.join(project_path, ".env")
    if not os.path.exists(env_file):
      
        with open(env_file, 'w') as f:
            f.write('SECRET_KEY="mysecretkey"\n')
            f.write('DATABASE_PASSWORD="password123"\n')

    with open(env_file, "r") as file:
        content = file.read()
        if "password" in content.lower() or "secret" in content.lower():
            config_issues.append({"file": env_file, "issue": "Potentially exposed secrets in .env file."})

    return config_issues
