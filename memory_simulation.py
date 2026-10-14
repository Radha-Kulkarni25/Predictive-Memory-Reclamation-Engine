import time

class AppProcess:
    def __init__(self, app_name, ram_mb, base_launch_penalty_ms, is_security_sensitive=False):
        self.app_name = app_name
        self.ram_mb = ram_mb
        self.base_launch_penalty_ms = base_launch_penalty_ms
        self.is_security_sensitive = is_security_sensitive  #session token flag
        self.access_history = []  #user launch timestamps
        self.page_fault_rate = 0.0

class PredictiveEngine:
    def __init__(self):
        self.running_apps = {}
        
    def register_app(self, app_name, ram_mb, penalty_ms, is_security_sensitive=False):
        self.running_apps[app_name] = AppProcess(app_name, ram_mb, penalty_ms, is_security_sensitive)

    def log_app_switch(self, app_name, current_time):
        if app_name in self.running_apps:
            self.running_apps[app_name].access_history.append(current_time)

    #mod 1: runtime behavior monitor (P_reuse,i)
    #evaluate temporal access gaps & usage habits
    def calculate_p_reuse(self, app_name, current_time):
        app = self.running_apps[app_name]
        if not app.access_history:
            return 0.1  #default baseline prob for cold apps
        
        last_accessed = app.access_history[-1]
        time_idle = current_time - last_accessed
        
        #temporal decay model
        decay_factor = 0.05
        p_reuse = 1.0 / (1.0 + decay_factor * time_idle)
        return round(p_reuse, 4)

    #mod2: app state analyzer (C_launch,i)
    #profiling of RAM footprint, relaunch latency, security sensitivity
    def calculate_c_launch(self, app_name):
        app = self.running_apps[app_name]
        max_penalty = 3000.0  #3s cold-start baseline cap
        
        #normalized score
        c_launch = app.base_launch_penalty_ms / max_penalty
        
        return round(c_launch, 4)

    #mod3: multi-factor scoring engine (S_i)
    #combining P_reuse, C_launch, RAM footprint, and security
    #high score = higher priority in ram; low score = evict
    def calculate_reclamation_priority_score(self, app_name, current_time):
        app = self.running_apps[app_name]
        p_reuse = self.calculate_p_reuse(app_name, current_time)
        c_launch = self.calculate_c_launch(app_name)
        
        #security multiplier (shields auth-heavy apps from sudden cleanup)
        sec_weight = 1.5 if app.is_security_sensitive else 1.0
        
        #system heuristic
        score = (p_reuse * 0.4) + (c_launch * 0.4) + (sec_weight * 0.2)
        return round(score, 4)
    #


if __name__ == "__main__":
    engine = PredictiveEngine()
    
    #test workload
    engine.register_app("Calculator", ram_mb=120, penalty_ms=150, is_security_sensitive=False)
    engine.register_app("MobileBanking", ram_mb=320, penalty_ms=1800, is_security_sensitive=True)
    engine.register_app("Navigation", ram_mb=520, penalty_ms=3200, is_security_sensitive=False)
    
    simulated_clock = 100.0
    
    #simulate user switching history
    engine.log_app_switch("Calculator", current_time=102.0)
    engine.log_app_switch("MobileBanking", current_time=105.0)
    
    simulated_clock = 135.0  #30s later
    
    print("--PREDICTIVE RECLAMATION ENGINE--\n")
    print(f"{'App Name':<16} | {'P_reuse':<8} | {'C_launch':<8} | {'Sec Flag':<8} | {'Priority Score (S_i)'}")
    
    for app_name in engine.running_apps:
        app = engine.running_apps[app_name]
        p_reuse = engine.calculate_p_reuse(app_name, simulated_clock)
        c_launch = engine.calculate_c_launch(app_name)
        score = engine.calculate_reclamation_priority_score(app_name, simulated_clock)
        
        print(f"{app_name:<16} | {p_reuse:<8} | {c_launch:<8} | {str(app.is_security_sensitive):<8} | {score}")
    
    print("\nPriority Score Interpretation:")
    print("Higher S_i -> Keep in physical RAM (high relaunch cost / sensitive security context)")
    print("Lower S_i  -> Prime candidate for memory reclamation during RAM pressure")
