"""
Mobile Computing – Assignment 1 (CO1)
Hexagonal cellular network planning and analysis.

Model inputs follow the uploaded assignment:
Area=12 km², channels=336, busy-hour traffic=0.025 Erlang/subscriber,
blocking target=2%, N=13, R=0.25 km, path-loss exponent n=2.5.
Install: pip install matplotlib numpy
Run: python mobile_computing_co1.py
The plots are analytical educational estimates, not field measurements.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

# -------------------- Assignment parameters --------------------
AREA_KM2 = 12.0
TOTAL_CHANNELS = 336
TRAFFIC_PER_SUBSCRIBER = 0.025
BLOCKING_TARGET = 0.02
CLUSTER_N = 13
CELL_RADIUS_KM = 0.25
PATH_LOSS_N = 2.5
INTERFERERS_OMNI = 6
INTERFERERS_SECTOR = 2
CELL_CAPACITY_ERLANGS = 17.50  # assignment's conservative value for 25 channels at 2%

def erlang_b(channels, traffic):
    """Erlang-B blocking probability using a stable recursive formula."""
    b = 1.0
    for m in range(1, channels + 1):
        b = traffic * b / (m + traffic * b)
    return b

def capacity_at_blocking(channels, target=BLOCKING_TARGET):
    """Find offered traffic at a specified Erlang-B blocking probability."""
    lo, hi = 0.0, 1000.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if erlang_b(channels, mid) > target:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

def hex_cell_area(radius):
    return (3 * math.sqrt(3) / 2) * radius**2

def reuse_distance(radius, cluster_size):
    return radius * math.sqrt(3 * cluster_size)

def sir_linear(cluster_size, path_loss_n=PATH_LOSS_N, interferers=INTERFERERS_OMNI):
    q = math.sqrt(3 * cluster_size)
    return q**path_loss_n / interferers

def sir_db(cluster_size, path_loss_n=PATH_LOSS_N, interferers=INTERFERERS_OMNI):
    return 10 * math.log10(sir_linear(cluster_size, path_loss_n, interferers))

def required_cells(subscribers):
    demand = subscribers * TRAFFIC_PER_SUBSCRIBER
    return math.ceil(demand / CELL_CAPACITY_ERLANGS)

def main():
    print("MOBILE COMPUTING – CO1 CELLULAR NETWORK ANALYSIS")
    print("-" * 55)
    area_cell = hex_cell_area(CELL_RADIUS_KM)
    coverage_cells = math.ceil(AREA_KM2 / area_cell)
    reuse = reuse_distance(CELL_RADIUS_KM, CLUSTER_N)
    channels_per_cell = TOTAL_CHANNELS // CLUSTER_N
    print(f"Hexagonal cell area       : {area_cell:.4f} km²")
    print(f"Coverage cells (ideal)    : {coverage_cells}")
    print(f"Reuse distance (N=13)     : {reuse:.3f} km")
    print(f"Channels per group        : {channels_per_cell} (integer floor)")
    print(f"SIR (N=13, n=2.5, I=6)   : {sir_db(CLUSTER_N):.2f} dB")
    print(f"Three-sector SIR estimate : {sir_db(CLUSTER_N, interferers=2):.2f} dB")
    print(f"Erlang-B for 25 ch, 17.5 E: {erlang_b(25, 17.5)*100:.2f}%")
    print("\nSubscriber forecast:")
    for users in [1000, 10000, 20000, 100000]:
        traffic = users * TRAFFIC_PER_SUBSCRIBER
        print(f"{users:>7,} users -> {traffic:>7.1f} Erlangs, "
              f"{required_cells(users):>3} capacity-driven cells")

    # Graph 1: busy-hour traffic growth
    subscribers = np.array([1000, 10000, 20000, 100000])
    traffic = subscribers * TRAFFIC_PER_SUBSCRIBER
    plt.figure(figsize=(8, 5))
    plt.plot(subscribers, traffic, marker="o")
    plt.xlabel("Number of subscribers")
    plt.ylabel("Offered busy-hour traffic (Erlangs)")
    plt.title("Traffic Growth with Subscriber Population")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graph1_traffic_growth.png", dpi=160)
    plt.close()

    # Graph 2: SIR against cluster size, for open/mixed/dense path-loss values
    n_values = [2.5, 3.0, 4.0]
    cluster_sizes = [1, 3, 4, 7, 9, 12, 13, 16, 19]
    plt.figure(figsize=(8, 5))
    for n in n_values:
        plt.plot(cluster_sizes,
                 [sir_db(N, n, INTERFERERS_OMNI) for N in cluster_sizes],
                 marker="o", label=f"path-loss exponent n={n}")
    plt.axhline(12, linestyle="--", label="12 dB SIR target")
    plt.xlabel("Frequency reuse cluster size (N)")
    plt.ylabel("Approximate SIR (dB)")
    plt.title("SIR versus Frequency Reuse Cluster Size")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graph2_sir_vs_cluster.png", dpi=160)
    plt.close()

    # Graph 3: blocking probability versus offered traffic for 25 channels
    loads = np.linspace(0.1, 35, 250)
    blocking = [erlang_b(25, a) * 100 for a in loads]
    plt.figure(figsize=(8, 5))
    plt.plot(loads, blocking)
    plt.axhline(BLOCKING_TARGET * 100, linestyle="--", label="2% blocking target")
    plt.axvline(17.5, linestyle=":", label="17.5 Erlangs (assignment estimate)")
    plt.yscale("log")
    plt.xlabel("Offered traffic per cell (Erlangs)")
    plt.ylabel("Call blocking probability (%) – logarithmic scale")
    plt.title("Erlang-B Blocking Probability (25 Traffic Channels)")
    plt.legend()
    plt.grid(True, which="both", alpha=0.3)
    plt.tight_layout()
    plt.savefig("graph3_blocking_probability.png", dpi=160)
    plt.close()

    # Graph 4: required capacity-driven sites against subscriber population
    pop = np.linspace(1000, 100000, 100)
    sites = [required_cells(int(x)) for x in pop]
    plt.figure(figsize=(8, 5))
    plt.plot(pop, sites, label="Capacity-driven cells")
    plt.axhline(coverage_cells, linestyle="--",
                label=f"Initial coverage layout ({coverage_cells} cells)")
    plt.scatter(subscribers, [required_cells(x) for x in subscribers], zorder=3)
    plt.xlabel("Number of subscribers")
    plt.ylabel("Required cells")
    plt.title("Required Cellular Sites versus Subscriber Population")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graph4_required_cells.png", dpi=160)
    plt.close()

    # Graph 5: uniform cell splitting recurrence
    rounds = np.arange(0, 4)
    cell_counts = 74 * (4 ** rounds)
    radius = CELL_RADIUS_KM / (2 ** rounds)
    capacity = 74 * CELL_CAPACITY_ERLANGS * (4 ** rounds)
    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(rounds, cell_counts, marker="o", label="Number of cells")
    ax1.set_xlabel("Uniform four-way split round")
    ax1.set_ylabel("Number of cells")
    ax1.set_xticks(rounds)
    ax2 = ax1.twinx()
    ax2.plot(rounds, capacity, marker="s", linestyle="--",
             label="Ideal aggregate capacity")
    ax2.set_ylabel("Aggregate capacity (Erlangs)")
    ax1.set_title("Uniform Cell-Splitting Growth")
    ax1.grid(True, alpha=0.3)
    lines = ax1.get_lines() + ax2.get_lines()
    ax1.legend(lines, [line.get_label() for line in lines], loc="upper left")
    fig.tight_layout()
    fig.savefig("graph5_cell_splitting.png", dpi=160)
    plt.close(fig)

    print("\nGraphs saved:")
    for filename in [
        "graph1_traffic_growth.png",
        "graph2_sir_vs_cluster.png",
        "graph3_blocking_probability.png",
        "graph4_required_cells.png",
        "graph5_cell_splitting.png",
    ]:
        print(" -", filename)

if __name__ == "__main__":
    main()
