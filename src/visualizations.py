import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('data1.csv')

# Create a function to set common style elements
def set_style():
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 12
# Define the column mappings
column_mappings = {
    'Screen_Time': 'Screen Time',
    'Social_Media_Usage': 'Social Media Usage',
    'Sleep_Duration': 'Sleep Duration',
    'Stress_index': 'Stress index',
    'Attendance': 'Attendance',
    'Happiness_Index': 'Happiness Index',
    'CGPA': 'CGPA'
}

# Rename columns in the DataFrame
df.rename(columns=column_mappings, inplace=True)
# 1. Enhanced Correlation Heatmap
def plot_correlation_heatmap(df):
    plt.figure(figsize=(12, 10))
    numeric_cols = ['Age', 'Screen Time', 'Social Media Usage', 
                   'Sleep Duration', 'Stress index', 'Attendance', 
                   'Happiness Index', 'CGPA', 'Total']
    correlation = df[numeric_cols].corr()
    mask = np.triu(np.ones_like(correlation), k=1)
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, mask=mask)
    plt.title('Correlation Heatmap of Student Metrics')
    plt.tight_layout()
    plt.show()

# 2. CGPA vs Screen Time with Age Groups
def plot_cgpa_vs_screen_time(df):
    plt.figure(figsize=(12, 7))
    sns.scatterplot(data=df, x='Screen Time', y='CGPA', 
                   hue='Age', size='Attendance', 
                   sizes=(50, 200), palette='viridis')
    plt.title('CGPA vs Screen Time by Age (Size represents Attendance)')
    plt.tight_layout()
    plt.show()

# 3. Sleep Duration by Age Groups
def plot_sleep_distribution(df):
    plt.figure(figsize=(12, 6))
    df['Age_Group'] = pd.qcut(df['Age'], q=4, labels=['18-20', '21-22', '23-24', '25+'])
    sns.violinplot(data=df, x='Age_Group', y='Sleep Duration')
    plt.title('Sleep Duration Distribution by Age Groups')
    plt.tight_layout()
    plt.show()

# 4. Happiness Index vs CGPA with Gender
def plot_happiness_vs_cgpa(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Happiness Index', y='CGPA', hue='Gender')
    plt.title('CGPA Distribution by Happiness Index and Gender')
    plt.tight_layout()
    plt.show()

# 5. Screen Time vs Social Media Usage by Age
def plot_screen_vs_social(df):
    plt.figure(figsize=(12, 7))
    sns.scatterplot(data=df, x='Screen Time', y='Social Media Usage', 
                   hue='Age', size='CGPA',
                   sizes=(50, 200), palette='viridis')
    plt.title('Screen Time vs Social Media Usage by Age (Size represents CGPA)')
    plt.tight_layout()
    plt.show()

# 6. Stress and Performance Analysis
def plot_stress_analysis(df):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.scatterplot(data=df, x='Stress index', y='CGPA', hue='Gender', ax=ax1)
    ax1.set_title('Stress Index vs CGPA by Gender')
    
    sns.boxplot(data=df, x='Stress index', y='Sleep Duration', ax=ax2)
    ax2.set_title('Sleep Duration by Stress Index')
    
    plt.tight_layout()
    plt.show()

# 7. Social Media Usage Patterns
def plot_social_patterns(df):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.boxplot(data=df, y='Social Media Usage', x='Happiness Index', ax=ax1)
    ax1.set_title('Social Media Usage by Happiness Index')
    
    sns.violinplot(data=df, y='Social Media Usage', x='Gender', hue='Stress index', ax=ax2)
    ax2.set_title('Social Media Usage Distribution by Gender and Stress Level')
    
    plt.tight_layout()
    plt.show()

# 8. Age-based Performance Analysis
def plot_age_performance(df):
    plt.figure(figsize=(12, 6))
    df['Age_Group'] = pd.qcut(df['Age'], q=4, labels=['18-20', '21-22', '23-24', '25+'])
    
    sns.boxplot(data=df, x='Age_Group', y='CGPA', hue='Gender')
    plt.title('CGPA Distribution by Age Groups and Gender')
    plt.tight_layout()
    plt.show()

# 9. Screen Time and Stress Patterns
def plot_screen_patterns(df):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.histplot(data=df, x='Screen Time', hue='Gender', multiple="stack", ax=ax1)
    ax1.set_title('Screen Time Distribution by Gender')
    
    sns.scatterplot(data=df, x='Screen Time', y='Stress index', 
                    hue='Gender', size='CGPA', sizes=(50, 200), ax=ax2)
    ax2.set_title('Screen Time vs Stress Index')
    
    plt.tight_layout()
    plt.show()

# 10. Multi-factor Analysis
def plot_multi_factor(df):
    fig = plt.figure(figsize=(15, 10))
    gs = fig.add_gridspec(2, 2)
    
    # Attendance vs CGPA with Age
    ax1 = fig.add_subplot(gs[0, 0])
    sns.scatterplot(data=df, x='Attendance', y='CGPA', hue='Age', 
                   size='Screen Time', sizes=(50, 200), ax=ax1)
    ax1.set_title('Attendance vs CGPA by Age')
    
    # Sleep Duration vs Stress Index
    ax2 = fig.add_subplot(gs[0, 1])
    sns.scatterplot(data=df, x='Sleep Duration', y='Stress index', 
                   hue='Age', size='CGPA', sizes=(50, 200), ax=ax2)
    ax2.set_title('Sleep Duration vs Stress Index by Age')
    
    # Happiness Distribution
    ax3 = fig.add_subplot(gs[1, 0])
    df['Age_Group'] = pd.qcut(df['Age'], q=4, labels=['18-20', '21-22', '23-24', '25+'])
    sns.violinplot(data=df, x='Age_Group', y='Happiness Index', ax=ax3)
    ax3.set_title('Happiness Distribution by Age Groups')
    
    # Social Media Usage Patterns
    ax4 = fig.add_subplot(gs[1, 1])
    sns.boxplot(data=df, x='Age_Group', y='Social Media Usage', ax=ax4)
    ax4.set_title('Social Media Usage by Age Groups')
    
    plt.tight_layout()
    plt.show()

# Function to generate all plots
def generate_all_plots(df):
    set_style()
    plot_correlation_heatmap(df)
    plot_cgpa_vs_screen_time(df)
    plot_sleep_distribution(df)
    plot_happiness_vs_cgpa(df)
    plot_screen_vs_social(df)
    plot_stress_analysis(df)
    plot_social_patterns(df)
    plot_age_performance(df)
    plot_screen_patterns(df)
    plot_multi_factor(df)

# Generate all plots
if __name__ == "__main__":
    # Generate all visualizations
    generate_all_plots(df)