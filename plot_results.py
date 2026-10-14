import matplotlib.pyplot as plt
import numpy as np


def generate_priority_score_chart():
    apps = ['Calculator', 'MobileBanking', 'Navigation']
    p_reuse = [0.1667, 0.4000, 0.1000]
    c_launch = [0.0500, 0.6000, 1.0000]
    final_scores = [0.3867, 0.8400, 0.6400]

    x = np.arange(len(apps))
    width = 0.2

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(x - width, p_reuse, width, label='P_reuse (Temporal Decay)', color='#3498db')
    ax.bar(x, c_launch, width, label='C_launch (Relaunch Penalty)', color='#f39c12')
    ax.bar(x + width, final_scores, width, label='Final Priority Score (S_i)', color='#2ecc71')

    ax.axhline(y=0.7, color='g', linestyle='--', linewidth=1.5, label='Preserve Threshold (>= 0.7)')
    ax.axhline(y=0.4, color='r', linestyle='--', linewidth=1.5, label='Terminate Threshold (< 0.4)')

    ax.set_ylabel('Score Metric')
    ax.set_title('4-Module Predictive Memory Engine: Process Evaluation')
    ax.set_xticks(x)
    ax.set_xticklabels(apps)
    ax.set_ylim(0, 1.1)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(axis='y', linestyle=':', alpha=0.6)

    plt.tight_layout()
    plt.savefig('priority_score_breakdown.png', dpi=300)
    plt.show()
    print("Saved: priority_score_breakdown.png")


def generate_latency_comparison_chart():
    apps = ['Calculator', 'MobileBanking', 'Navigation']
    lmkd_relaunch_delay = [150, 1800, 3200]
    predictive_relaunch_delay = [150, 0, 80]

    x = np.arange(len(apps))
    width = 0.35

    fig, ax = plt.subplots(figsize=(7, 4.5))

    ax.bar(x - width/2, lmkd_relaunch_delay, width, label='Standard LMKD (Full Relaunch Delay)', color='#e74c3c')
    ax.bar(x + width/2, predictive_relaunch_delay, width, label='Predictive Engine (zRAM/RAM Preservation)', color='#27ae60')

    ax.set_ylabel('App Relaunch Delay (ms)')
    ax.set_title('Relaunch Latency Comparison: Standard LMKD vs. Predictive Engine')
    ax.set_xticks(x)
    ax.set_xticklabels(apps)
    ax.legend()
    plt.grid(axis='y', linestyle=':', alpha=0.6)

    plt.tight_layout()
    plt.savefig('latency_comparison.png', dpi=300)
    plt.show()
    print("Saved: latency_comparison.png")


if __name__ == "__main__":
    generate_priority_score_chart()
    generate_latency_comparison_chart()
