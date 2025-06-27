import os
from dotenv import load_dotenv
root_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

# 加载环境变量
if os.environ.get('ENVIRONMENT') == 'production':
    load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env.production'))
else:
    load_dotenv(root_path)

# 使用环境变量
APP_KEY = os.environ.get('APP_KEY')
APP_SECRET = os.environ.get('APP_SECRET')

DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

def main():
    print(f"APP_KEY: {APP_KEY}")
    print(f"APP_SECRET: {APP_SECRET}")
    print(f"Debug mode: {DEBUG}")

if __name__ == "__main__":
    main()
