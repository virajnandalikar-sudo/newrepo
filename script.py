def generate_data(n=10):
    print("Stage: Generate Data")
    data = []
    for i in range(n):
        val = (i * 37 + 11) % 100
        data.append(val)
    print("Data:", data)
    return data

def analyze_data(data):
    print("Stage: Analyze Data")
    total = 0
    for val in data:
        total += val
    mean_val = total / len(data)

    sorted_data = sorted(data)
    mid = len(sorted_data) // 2
    if len(sorted_data) % 2 == 0:
        median_val = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        median_val = sorted_data[mid]

    max_val = sorted_data[-1]
    min_val = sorted_data[0]

    print(f"Mean: {mean_val}, Median: {median_val}, Max: {max_val}, Min: {min_val}")
    return {"mean": mean_val, "median": median_val, "max": max_val, "min": min_val}

def run_tests(results):
    print("Stage: Run Tests")
    if results["mean"] < 0:
        print("Test failed: Mean is negative")
    elif results["max"] < results["min"]:
        print("Test failed: Max < Min")
    else:
        print("All tests passed!")

def deploy(results):
    print("Stage: Deploy")
    print("Deploying results...")
    print("Payload:", results)

def notify():
    print("Stage: Notify")
    print("Notification: Pipeline executed successfully!")

def main():
    print("=== Python Workflow Simulation (No Imports) ===")
    data = generate_data(15)
    results = analyze_data(data)
    run_tests(results)
    deploy(results)
    notify()
    print("=== Workflow Finished ===")

if __name__ == "__main__":
    main()
