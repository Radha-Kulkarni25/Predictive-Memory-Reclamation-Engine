from memory_simulation import PredictiveMemoryEngine, AppProcess

def main():
    print("\n--- Starting Memory Engine Trace Simulation ---")
    engine = PredictiveMemoryEngine()

    apps = [
        AppProcess("Calculator", 120, 150, False),
        AppProcess("MobileBanking", 320, 1800, True),
        AppProcess("Navigation", 520, 3200, False)
    ]

    for app in apps:
        engine.register_app(app)

    engine.record_app_launch("Calculator", 102.0)
    engine.record_app_launch("MobileBanking", 105.0)

    current_time = 135.0
    results = engine.execute_eviction_pipeline(current_time)

    print(f"\nSimulation Time: {current_time}s\n")
    print(f"{'Application':<15} | {'Priority Score':<15} | {'Decision Action'}")
    print("-" * 55)
    for name, info in results.items():
        print(f"{name:<15} | {info['priority_score']:<15.4f} | {info['action']}")

if __name__ == "__main__":
    main()
