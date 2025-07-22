import requests
import schedule
import time

# Configuration
REST_SERVICE_URL = 'http://localhost:8000/health'  # Example endpoint


def check_service_health():
    try:
        response = requests.get(REST_SERVICE_URL, timeout=5)
        print(f'Status: {response.status_code}, Response: {response.text}')
    except Exception as e:
        print(f'Error checking service health: {e}')


def main():
    schedule.every(30).seconds.do(check_service_health)
    print('Observability Agent started. Monitoring...')
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main() 