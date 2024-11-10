import pytest
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from src.visualizations import (
    plot_correlation_heatmap,
    plot_cgpa_vs_screen_time,
    plot_sleep_distribution
)

@pytest.fixture
def sample_data():
    """Create sample data for testing"""
    np.random.seed(42)
    data = {
        'Age': np.random.randint(18, 30, 100),
        'Screen Time': np.random.normal(6, 2, 100),
        'Social Media Usage': np.random.normal(4, 1.5, 100),
        'Sleep Duration': np.random.normal(7, 1, 100),
        'Stress index': np.random.randint(1, 6, 100),
        'Attendance': np.random.normal(85, 10, 100),
        'Happiness Index': np.random.randint(1, 6, 100),
        'CGPA': np.random.normal(3.5, 0.5, 100),
        'Gender': np.random.choice(['Male', 'Female'], 100)
    }
    return pd.DataFrame(data)

def test_correlation_heatmap(sample_data):
    """Test if correlation heatmap function runs without errors"""
    try:
        plot_correlation_heatmap(sample_data)
        plt.close()
        assert True
    except Exception as e:
        assert False, f"plot_correlation_heatmap raised an exception: {e}"

def test_cgpa_vs_screen_time(sample_data):
    """Test if CGPA vs Screen Time plot function runs without errors"""
    try:
        plot_cgpa_vs_screen_time(sample_data)
        plt.close()
        assert True
    except Exception as e:
        assert False, f"plot_cgpa_vs_screen_time raised an exception: {e}"

def test_sleep_distribution(sample_data):
    """Test if sleep distribution plot function runs without errors"""
    try:
        plot_sleep_distribution(sample_data)
        plt.close()
        assert True
    except Exception as e:
        assert False, f"plot_sleep_distribution raised an exception: {e}"
