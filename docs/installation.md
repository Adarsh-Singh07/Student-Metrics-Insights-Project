# Installation Guide

## Prerequisites
- Python 3.8 or higher
- pip package manager

## Step-by-Step Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/studentmetrics-insight.git
cd studentmetrics-insight
```

2. **Create a Virtual Environment** (Optional but recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Install the Package in Development Mode**
```bash
pip install -e .
```

## Verification
To verify the installation:
```bash
python -c "import studentmetrics_insight; print('Installation successful!')"
```

## Common Issues and Solutions

### Missing Dependencies
If you encounter missing dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Matplotlib Backend Issues
If you encounter Matplotlib backend issues:
- For Jupyter notebooks: use %matplotlib inline
- For scripts: ensure you have a proper backend configured

### Version Conflicts
If you encounter version conflicts:
1. Create a new virtual environment
2. Install dependencies in the new environment
3. If problems persist, check the specific package versions in requirements.txt
