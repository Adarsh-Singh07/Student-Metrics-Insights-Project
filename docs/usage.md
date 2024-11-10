# Usage Guide

## Basic Usage

### 1. Data Preparation
Place your CSV file in the `data/` directory with the following columns:
- Age
- Gender
- Screen Time
- Social Media Usage
- Sleep Duration
- Stress index
- Attendance
- Happiness Index
- CGPA

### 2. Running Visualizations

```python
from src.visualizations import generate_all_plots
import pandas as pd

# Read your data
df = pd.read_csv('data/your_data.csv')

# Generate all plots
generate_all_plots(df)
```

### 3. Individual Visualizations

```python
from src.visualizations import (
    plot_correlation_heatmap,
    plot_cgpa_vs_screen_time,
    plot_sleep_distribution
)

# Generate specific plots
plot_correlation_heatmap(df)
plot_cgpa_vs_screen_time(df)
plot_sleep_distribution(df)
```

## Customization

### Modifying Plot Styles
```python
from src.utils.style_config import (
    set_visualization_style,
    set_custom_palette,
    set_figure_size
)

# Set custom styles
set_visualization_style()
set_custom_palette("viridis")
set_figure_size(15, 8)
```

## Examples

### Basic Analysis
```python
# Example of basic analysis workflow
import pandas as pd
from src.visualizations import *

# Read data
df = pd.read_csv('data/student_data.csv')

# Generate correlation heatmap
plot_correlation_heatmap(df)

# Analyze CGPA vs Screen Time
plot_cgpa_vs_screen_time(df)
```

## Best Practices

1. Always check data quality before visualization
2. Use appropriate plot types for your data
3. Consider your audience when customizing visualizations
4. Save important figures for documentation
