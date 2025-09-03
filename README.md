# 🚗 Fuel Efficiency CI/CD Pipeline  

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)  
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/YOUR-USERNAME/fuel-efficiency-ci-cd/actions)  

A Python project that calculates **fuel efficiency and trip statistics** with a fully integrated **CI/CD pipeline** powered by GitHub Actions.  
This repo demonstrates **real-world software engineering practices**: automated testing, linting, packaging, and deployment-ready builds.  

---

## ✨ Features  
-  Calculate **fuel efficiency** (`distance / fuel`) in km per liter  
-  Compute **average efficiency** across multiple trips  
-  Identify the **best (most efficient) trip**  
-  Includes **unit tests** (Pytest) for reliability  
-  Automated **CI/CD pipeline**: Lint → Test → Build → Deploy  


---

## ⚙️ CI/CD Pipeline  
This project uses **GitHub Actions** for continuous integration & delivery:  

1. **Linting** → checks code quality with Flake8  
2. **Testing** → runs Pytest unit tests automatically  
3. **Building** → packages the project into distributable artifacts  
4. **Deployment** → stores artifacts (ready for publishing on PyPI or GitHub Releases)  

Every push to `main` triggers the pipeline automatically  

---

## 🚀 Quickstart  

### Clone the repo  
```bash
git clone https://github.com/ogetalha/fuel-efficiency-ci-cd.git
cd fuel-efficiency-ci-cd
``` 
### Install dependencies
``` bash
pip install -r requirements.txt
```

### Run tests
```bash
 pytest
 ```
Example Usage
```bash
from src.fuel_efficiency import calculate_fuel_efficiency, average_efficiency, best_trip

print(calculate_fuel_efficiency(500, 25))  # 20.0
trips = [(100, 5), (200, 10), (300, 20)]
print(average_efficiency(trips))  # 18.33
print(best_trip(trips))  # (100, 5, 20.0)
```

## What I Learned
How to set up a CI/CD pipeline with GitHub Actions

Writing scalable Python functions with type hints and docstrings

Using Pytest for test-driven development

Enforcing code quality with Flake8

Automating builds and preparing for deployment

📜 License
MIT License © 2025 Talha Khan