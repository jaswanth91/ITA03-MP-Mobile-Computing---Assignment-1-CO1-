# MOBILE COMPUTING – ASSIGNMENT 1 (CO1)
## Python-Based Cellular Network Analysis

### 1. Introduction

This project focuses on the analysis and optimization of a hexagonal cellular network for spectrum allocation, interference management, traffic capacity and scalable coverage planning.

The project uses Python programming to perform different cellular network analyses and generate graphs representing network performance.

### 2. Objectives

- To analyse hexagonal cellular network geometry.
- To study frequency reuse and interference.
- To calculate Signal-to-Interference Ratio (SIR).
- To analyse network capacity using the Erlang-B formula.
- To study subscriber growth and network scalability.
- To understand uniform and selective cell splitting.
- To compare different cellular network strategies.
- To analyse temporary network capacity for stadium events.

### 3. Software and Tools Required

- Python 3.x
- Visual Studio Code / PyCharm
- NumPy
- Matplotlib

### 4. Project Files and Descriptions

This project contains 8 separate Python programs.

| S.No | Python File | Description |
|---|---|---|
| 1 | 01_geometry_capacity.py | Hexagonal geometry and network capacity analysis |
| 2 | 02_frequency_reuse_strategies.py | Frequency reuse and SIR comparison |
| 3 | 03_best_average_worst_sir.py | Best, average and worst-case SIR analysis |
| 4 | 04_scaling_sensitivity.py | Subscriber scaling and sensitivity analysis |
| 5 | 05_cell_splitting_recurrences.py | Uniform and selective cell splitting |
| 6 | 06_strategy_simulation_experiment.py | Network strategy simulation and comparison |
| 7 | 07_recommendation_capacity_cost.py | Network capacity and cost comparison |
| 8 | 08_stadium_event_challenge.py | Stadium event traffic and microcell analysis |

### 5. Installation

Install Python and the required libraries.

Open Command Prompt and execute:

```bash
pip install numpy matplotlib
```

### 6. Execution Procedure

1. Download and extract the project ZIP file.
2. Open the project folder in Visual Studio Code or Command Prompt.
3. Install the required Python libraries.
4. Select the Python program you want to execute.
5. Run the program using the following command.

Example:

```bash
python 01_geometry_capacity.py
```

To execute other programs:

```bash
python 02_frequency_reuse_strategies.py
python 03_best_average_worst_sir.py
python 04_scaling_sensitivity.py
python 05_cell_splitting_recurrences.py
python 06_strategy_simulation_experiment.py
python 07_recommendation_capacity_cost.py
python 08_stadium_event_challenge.py
```

Each Python file works independently.

### 7. Graphs Generated

The programs generate the following graphs:

1. Erlang-B Blocking Probability Graph
2. Frequency Reuse versus SIR Graph
3. SIR Distribution Graph
4. Cell Radius Sensitivity Graph
5. SIR Sensitivity Graph
6. Uniform Cell Splitting Graph
7. Transmit Power and Handoff Graph
8. Network Capacity Comparison Graph
9. Network Cost Comparison Graph
10. Stadium Event Capacity Graph

### 8. Project Parameters

| Parameter | Value |
|---|---|
| Township Area | 12 km² |
| Available Traffic Channels | 336 |
| Busy-Hour Traffic | 0.025 Erlang/subscriber |
| Blocking Probability Target | 2% |
| Frequency Reuse Cluster Size | N = 13 |
| Initial Cell Radius | 0.25 km |
| Path Loss Exponent | 2.5 |
| SIR Target | 12 dB |
| Traffic Capacity per Cell | 17.50 Erlangs |

### 9. Expected Output

After executing the Python programs, the following outputs are obtained:

- Hexagonal cell area and number of cells.
- Frequency reuse distance.
- Traffic capacity and blocking probability.
- SIR values for different frequency reuse strategies.
- Subscriber traffic growth analysis.
- Cell splitting and network scalability results.
- Network strategy and cost comparisons.
- Stadium event traffic requirements.
- Graphical representations of network performance.

The simulation experiment also generates a CSV file containing illustrative results.

### 10. Applications

- Cellular network planning.
- Mobile communication systems.
- Frequency allocation.
- Interference management.
- Network capacity optimization.
- Microcell and macrocell deployment.
- Wireless communication research.

### 11. Conclusion

This project demonstrates the analysis and optimization of cellular networks using Python. The eight independent programs help understand cellular geometry, frequency reuse, interference, traffic capacity, cell splitting and network scalability.

The generated graphs provide a visual representation of cellular network performance and help compare different network planning strategies.

**Note:** The results are based on simplified analytical and educational models. They are not actual field measurements or a fully validated radio-network simulation.
