import matplotlib.pyplot as plt
import seaborn as sns

def set_visualization_style():
    """Set the default style for all visualizations"""
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10

def set_custom_palette(palette_name="husl"):
    """Set a custom color palette"""
    sns.set_palette(palette_name)

def set_figure_size(width=12, height=6):
    """Set custom figure size"""
    plt.rcParams['figure.figsize'] = (width, height)
