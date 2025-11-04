# Sales_project

A small demo project that processes sales orders from a CSV and demonstrates a threaded order-processing simulation.

## Files

- `main.py` — main script. Contains data processing (CSV parsing) and a threaded simulation to process orders.
- `sales_data.csv` — sample sales data used by `main.py`.

## Branches & Commits created

- `main` — Initial commit with starter files.
- `feature/data-processing` — Implemented CSV parsing and data-processing helper.
- `feature/threading-simulation` — Added a simple threaded simulation that processes orders concurrently.

## How to run (Windows PowerShell)

1. Open PowerShell and change to the project folder:

```powershell
cd C:\Users\gayal\OneDrive\Desktop\sales_project
```

2. Run the script:

```powershell
python .\main.py
```

This will load `sales_data.csv`, print a short summary, and run a threaded simulation that prints per-order processing messages.


## Notes

- The project is intentionally minimal. Consider adding tests, logging, and more robust CSV validation.
- Branches have been pushed to the remote repository: `https://github.com/Gayal-C-Ashok/Sales_project.git`.

## Contact

If you need additional changes (README improvements, tests, CI), tell me what you'd like added and I will implement them.
