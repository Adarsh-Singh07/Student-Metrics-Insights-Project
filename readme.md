# StudentMetrics Insight

A comprehensive data visualization project analyzing the relationships between academic performance, digital habits, and student well-being using Python.

## Overview

This project provides deep insights into student behavior patterns and their impact on academic performance by analyzing various metrics including:
- Screen time and social media usage
- Sleep patterns
- Stress levels
- Academic performance (CGPA)
- Attendance
- Happiness index
- Age and gender demographics

## Features

- 10 different types of visualizations including:
  - Correlation heatmaps
  - Multi-factor analysis
  - Age-based performance analysis
  - Screen time and stress pattern analysis
  - Social media usage patterns
  - Sleep duration distribution
  - Happiness and academic performance correlation

## Requirements

```
pandas
numpy
seaborn
matplotlib
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/studentmetrics-insight.git
cd studentmetrics-insight
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your data file (data1.csv) in the project directory
2. Run the main script:
```bash
python visualizations.py
```

## Data Format

The input CSV file should contain the following columns:
- Age
- Gender
- Screen Time
- Social Media Usage
- Sleep Duration
- Stress index
- Attendance
- Happiness Index
- CGPA
- Total

## Visualizations

1. **Correlation Heatmap**: Shows relationships between all numeric variables
2. **CGPA vs Screen Time**: Scatter plot with age groups and attendance
3. **Sleep Duration Analysis**: Distribution across age groups
4. **Happiness Index vs CGPA**: Box plot analysis by gender
5. **Screen Time vs Social Media**: Usage patterns by age
6. **Stress Analysis**: Impact on CGPA and sleep patterns
7. **Social Media Patterns**: Usage distribution by happiness and stress
8. **Age Performance Analysis**: CGPA distribution across age groups
9. **Screen Time Patterns**: Distribution and stress correlation
10. **Multi-factor Analysis**: Comprehensive view of multiple metrics

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

Your Name - Initial work

## Acknowledgments

- Dataset contributors
- Research partners
- Academic advisors
