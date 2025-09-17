import os
import subprocess
import time
import requests
import json
import threading

# Configuration
MICROSERVICES_DIR = "./microservices_code"
API_CHECK_TIMEOUT = 10  # Seconds to wait for API to respond
START_PORT = 8000

def run_service(service_name, port):
    """Runs a microservice in a separate thread."""
    service_path = os.path.join(MICROSERVICES_DIR, service_name)
    try:
        # We use a subprocess to run the uvicorn command
        proc = subprocess.Popen(
            ["uvicorn", "app:app", "--port", str(port), "--reload"],
            cwd=service_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"🚀 Started {service_name} on port {port}. Waiting for it to become ready...")
        time.sleep(2) # Give it a moment to start
        return proc
    except FileNotFoundError:
        print(f"❌ Error: 'uvicorn' command not found. Please ensure it's installed.")
        return None

def check_api_ready(port):
    """Checks if the API is ready by making a GET request."""
    url = f"http://localhost:{port}/"
    try:
        response = requests.get(url, timeout=API_CHECK_TIMEOUT)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        return False

def main():
    if not os.path.exists(MICROSERVICES_DIR):
        print(f"Error: {MICROSERVICES_DIR} not found. Please generate microservices first.")
        return

    services = [d for d in os.listdir(MICROSERVICES_DIR) if os.path.isdir(os.path.join(MICROSERVICES_DIR, d))]
    total_services = len(services)
    successful_starts = 0
    processes = {}
    
    current_port = START_PORT

    for service_name in services:
        print(f"--- Testing {service_name} ---")
        proc = run_service(service_name, current_port)
        if proc:
            processes[service_name] = proc
            if check_api_ready(current_port):
                print(f"✅ {service_name} started successfully.")
                successful_starts += 1
            else:
                print(f"❌ {service_name} failed to start or respond on port {current_port}.")
        current_port += 1

    print("\n--- Evaluation Summary ---")
    print(f"Total services generated: {total_services}")
    print(f"Services started successfully: {successful_starts}")
    print(f"Code Generation Success Rate: {successful_starts/total_services * 100:.2f}%")

    # Clean up
    print("\n--- Cleaning up processes ---")
    for proc in processes.values():
        proc.terminate()
    print("Cleanup complete.")


if __name__ == "__main__":
    main()
