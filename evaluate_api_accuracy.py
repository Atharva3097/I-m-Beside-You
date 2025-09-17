import requests
import json
import os

def load_microservices_plan(filepath="./microservices/microservices_plan.json"):
    """Loads the microservices plan from the JSON file."""
    if not os.path.exists(filepath):
        print(f"Error: Microservices plan not found at {filepath}.")
        return None
    with open(filepath, "r") as f:
        return json.load(f)

def evaluate_endpoints(plan):
    """Evaluates each endpoint defined in the plan."""
    results = {}
    total_endpoints = 0
    passed_endpoints = 0

    for service in plan.get("microservices", []):
        service_name = service["name"]
        endpoints = service.get("api_endpoints", [])
        
        # Assume services are running on ports 8000, 8001, etc.
        # You would need to map ports correctly if you run them.
        # For simplicity, this script just checks for the presence in the code.
        
        # A more advanced check would involve running the service and making a real API call.
        # This script performs a static check on the code content.
        
        results[service_name] = []
        for endpoint in endpoints:
            total_endpoints += 1
            
            # Simple check for endpoint string in the generated app.py file
            service_path = f"./microservices_code/{service_name}/app.py"
            if os.path.exists(service_path):
                with open(service_path, "r") as f:
                    code = f.read()
                    # Check for the endpoint string in the code
                    if f'app.get("{endpoint}")' in code or f'app.post("{endpoint}")' in code:
                        results[service_name].append({"endpoint": endpoint, "status": "PASS"})
                        passed_endpoints += 1
                    else:
                        results[service_name].append({"endpoint": endpoint, "status": "FAIL"})
            else:
                results[service_name].append({"endpoint": endpoint, "status": "FAIL (app.py not found)"})

    print("--- API Endpoint Accuracy Evaluation ---")
    for service, checks in results.items():
        print(f"\nService: {service}")
        for check in checks:
            print(f"  - Endpoint: {check['endpoint']} -> {check['status']}")

    print("\n--- Summary ---")
    print(f"Total Endpoints Checked: {total_endpoints}")
    print(f"Endpoints Found in Code: {passed_endpoints}")
    print(f"API Endpoint Accuracy: {passed_endpoints/total_endpoints * 100:.2f}%")


if __name__ == "__main__":
    plan = load_microservices_plan()
    if plan:
        evaluate_endpoints(plan)
