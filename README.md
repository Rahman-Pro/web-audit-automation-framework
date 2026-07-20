# 🧪 12-Point Web Audit Automation Framework & Allure CI/CD Pipeline (Python & Pytest)

An enterprise-grade, full-stack **Technical Web Audit & Automated Quality Suite** built with **Python, Pytest, Selenium WebDriver, Allure Reporting, and GitHub Actions CI/CD**.

This framework automates 12 critical technical diagnostics (SEO, HTTPS Security Headers, Page Load Speeds, Broken Links, Heading Hierarchy, and Accessibility) and publishes interactive **Allure Reports with Historical Trends** to GitHub Pages on an automated weekly Sunday cron schedule.

![Python Version](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Pytest Version](https://img.shields.io/badge/Pytest-7.4+-green?logo=pytest&logoColor=white)
![Selenium Version](https://img.shields.io/badge/Selenium-4.15+-green?logo=selenium&logoColor=white)
![Allure Report](https://img.shields.io/badge/Allure-Reports%20%2B%20History-orange?logo=qameta&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-Automated%20Sunday%20Run-blue?logo=githubactions&logoColor=white)

---

## 🌐 Live Interactive Allure Dashboard (GitHub Pages)
View the live automated Allure execution report with historical trends:

👉 **[https://rahman-pro.github.io/web-audit-automation-framework/](https://rahman-pro.github.io/web-audit-automation-framework/)**

---

## 🎯 12-Point Technical Audit Coverage

| Audit Check | Category | Diagnostic & Validation Logic |
| :--- | :--- | :--- |
| **1. HTTPS Protocol Enforcement** | Security | Asserts SSL certificate encryption on all target URLs. |
| **2. Security Headers (HSTS, CSP)** | Security | Audits `Strict-Transport-Security` and `Content-Security-Policy`. |
| **3. Navigation Page Speed** | Performance | Calculates browser navigation timing signals (`performance.timing`). |
| **4. Meta Title Validation** | SEO | Validates presence and 30–60 character guidelines. |
| **5. Meta Description Audit** | SEO | Ensures meta descriptions fit Google's SERP display limits (110–160 chars). |
| **6. Heading Structure (`H1`)** | Content QA | Validates presence of a single, non-duplicate primary `H1` tag. |
| **7. Image Alt Attributes** | Accessibility | Scans page images for missing alternative text tags. |
| **8. Open Graph (OG) Tags** | Social SEO | Checks `og:title`, `og:description`, and `og:image` social cards. |
| **9. Canonical Tag Hygiene** | SEO | Verifies valid canonical link tags to prevent duplicate content flags. |
| **10. Robots.txt Accessibility** | Crawlability | Validates HTTP 200 accessibility for site crawler instructions. |
| **11. Asynchronous Broken Links** | Reliability | Audits anchor links for HTTP 404/500 connection failures. |
| **12. Browser Console JS Errors** | Stability | Scans browser console logs for severe JavaScript exceptions. |

---

## 📁 Repository Architecture
```
web-audit-automation-framework/
├── .github/
│   └── workflows/
│       └── audit.yml          # GitHub Actions CI/CD with Sunday Cron & gh-pages
├── tests/
│   └── test_web_audit.py      # Pytest suite with Allure epics/features/stories
├── utils/
│   └── audit_engine.py        # 12-Point Web Diagnostic Engine
├── conftest.py                # Headless Chrome setup & Allure failure screenshot hook
├── requirements.txt           # Python dependencies
├── .gitignore                 # Excludes allure-results & cache
└── README.md                  # Enterprise SDET documentation
```

---

## 🚀 Setup & Local Execution Guide

### 1. Requirements
*   **Python 3.10+** and **Google Chrome** installed.

### 2. Installation
Navigate to the repository folder and install dependencies:
```bash
cd c:\Users\rahma\Desktop\web-audit-automation-framework
pip install -r requirements.txt
```

### 3. Execute Pytest Suite with Allure Output
Run the 12-point audit suite and output results for Allure:
```bash
pytest --alluredir=allure-results
```

### 4. Serve & View Interactive Allure Report Locally
If you have Allure CLI installed:
```bash
allure serve allure-results
```

---

## 🔄 Automated CI/CD & GitHub Pages Deployment
This framework features a fully automated **GitHub Actions Workflow** (`.github/workflows/audit.yml`):
*   **Triggers:** Automatically runs on every `push`, `pull_request`, manual trigger (`workflow_dispatch`), and a **weekly Sunday cron schedule (`0 0 * * 0`)**.
*   **Environment:** Runs headless Chrome on `ubuntu-latest`.
*   **Allure History:** Deploys generated HTML reports to the `gh-pages` branch, persisting test execution history over time.

---

## 👨‍💻 Hire Atiqur Rahman (SDET & QA Automation Engineer)
Specializing in Web Automation Frameworks, API Testing, Performance Auditing, and CI/CD Integrations.

*   **LinkedIn Profile:** **[Atiqur Rahman on LinkedIn](https://www.linkedin.com/in/atiqur-rahman-pro/)**
*   **Tech Stack:** Python, Pytest, Selenium, Playwright, Allure Reports, Java, Rest Assured, GitHub Actions CI/CD.
