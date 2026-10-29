import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# Sample reference data
reference_data = pd.DataFrame({
    "age": [20, 21, 22, 23, 24, 25],
    "score": [60, 65, 70, 75, 80, 85]
})

# Simulated new data with changed distributions
current_data = pd.DataFrame({
    "age": [30, 31, 32, 33, 34, 35],
    "score": [20, 25, 30, 35, 40, 45]
})

report = Report([
    DataDriftPreset()
])

snapshot = report.run(current_data, reference_data)
snapshot.save_html("drift_report.html")

print("Evidently data-drift report generated successfully.")