name: Update GitHub Pages

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pandas mlxtend openpyxl

    - name: Run script to generate HTML
      run: analyse_transactions_to_html.py

    - name: Commit and push if changes
      run: |
        git config --global user.email "you@example.com"
        git config --global user.name "Your Name"
        git add -A
        git diff --staged --quiet || git commit -m "Update HTML report"
        git push
