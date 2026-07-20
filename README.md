# 🧪 12-Point Web Audit Automation Framework

### Production-Grade SDET Framework — Automated Web Quality Diagnostics with Allure CI/CD Reporting

> Built to enterprise standards by **Atiqur Rahman** — an SDET & QA Automation Engineer who transforms manual web audits into fully automated, CI/CD-integrated, self-documenting test pipelines.

![Python Version](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-7.4+-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium_WebDriver-4.15+-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Allure](https://img.shields.io/badge/Allure_Report-2.27-FF6600?style=for-the-badge&logo=qameta&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Live_Dashboard-222222?style=for-the-badge&logo=github&logoColor=white)
![Chrome](https://img.shields.io/badge/Headless_Chrome-Automated-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-CI_Runner-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

---

## 🌐 Live Interactive Allure Dashboard

View the **live automated Allure execution report** with historical trends, pie charts, and detailed test step breakdowns:

### 👉 [**https://rahman-pro.github.io/web-audit-automation-framework/**](https://rahman-pro.github.io/web-audit-automation-framework/)

---

## 💡 Why This Framework?

| ❌ Without This Framework | ✅ With This Framework |
|:---|:---|
| Manual site audits take **2–4 hours per site** | Automated audit completes in **~60 seconds** |
| Results are scattered in spreadsheets | All results in **one interactive Allure dashboard** |
| No historical comparison between audits | **Historical trend charts** track quality over time |
| Easy to forget running periodic checks | **Automated weekly Sunday cron** via GitHub Actions |
| No evidence trail for client reporting | **Allure attachments** with screenshots & data snapshots |

---

## 📊 Key Metrics

| Metric | Value |
|:---|:---|
| **Total Test Cases** | 5 automated test methods |
| **Audit Diagnostic Points** | 12 technical checks |
| **Average Execution Time** | ~60 seconds (headless) |
| **CI/CD Frequency** | Weekly automated Sunday cron + every push |
| **Report History Retention** | Last 20 runs with trend comparison |
| **Browser Engine** | Google Chrome (Headless) via ChromeDriver |
| **CI Runner OS** | Ubuntu Latest (GitHub Actions) |
| **Deployment Target** | GitHub Pages (gh-pages branch) |

---

## 🏗️ Framework Architecture

```mermaid
flowchart TB
    subgraph TRIGGER["⚡ CI/CD Triggers"]
        A["Git Push / PR"] --> D
        B["Weekly Sunday Cron"] --> D
        C["Manual Dispatch"] --> D
    end

    subgraph CI["🔄 GitHub Actions Pipeline (Ubuntu)"]
        D["Checkout Source Code"] --> E["Setup Python 3.10"]
        E --> F["Install Dependencies<br/>pytest, selenium, allure-pytest,<br/>requests, beautifulsoup4"]
        F --> G["Execute Pytest Suite<br/>5 Test Methods × 12 Audit Points"]
        G --> H["Generate Allure Results<br/>JSON + Attachments"]
    end

    subgraph REPORT["📊 Allure Report Engine"]
        H --> I["Download Allure CLI 2.27"]
        I --> J["Copy Historical Data<br/>from gh-pages branch"]
        J --> K["Generate HTML Report<br/>with Trend Charts"]
    end

    subgraph DEPLOY["🚀 Deployment"]
        K --> L["Deploy to GitHub Pages<br/>gh-pages branch"]
        L --> M["Live Dashboard<br/>rahman-pro.github.io"]
    end

    style TRIGGER fill:#1a1a2e,stroke:#e94560,color:#fff
    style CI fill:#16213e,stroke:#0f3460,color:#fff
    style REPORT fill:#0f3460,stroke:#533483,color:#fff
    style DEPLOY fill:#533483,stroke:#e94560,color:#fff
```

---

## 🔬 Test Execution Flow

```mermaid
sequenceDiagram
    participant P as Pytest Runner
    participant C as Conftest.py
    participant W as WebAuditEngine
    participant B as Headless Chrome
    participant A as Allure Report

    P->>C: Initialize headless Chrome driver
    C->>B: Launch Chrome (--headless --no-sandbox)
    
    P->>W: Test 01 — HTTPS & Security Headers
    W-->>A: ✅ Attach security audit results

    P->>W: Test 02 — Page Load Performance
    W->>B: Navigate to target URL
    B-->>W: Return navigation timing data
    W-->>A: ✅ Attach load time metric

    P->>W: Test 03 — Meta Title & Description
    W->>B: Extract meta tags via Selenium
    B-->>W: Return meta content
    W-->>A: ✅ Attach SEO metadata audit

    P->>W: Test 04 — Headings & Image Alt Tags
    W->>B: Scan DOM elements
    B-->>W: Return H1 tags & image list
    W-->>A: ✅ Attach structure audit

    P->>W: Test 05 — Broken Links & Robots.txt
    W->>B: Extract anchor hrefs
    W-->>A: ✅ Attach link integrity scan

    C->>B: Quit Chrome driver
    P->>A: Generate final Allure JSON results
```

---

## 🎯 12-Point Technical Audit Coverage

```mermaid
pie title Audit Coverage by Category
    "Security (HTTPS + Headers)" : 2
    "Performance (Page Speed)" : 1
    "SEO (Title + Desc + OG + Canonical)" : 4
    "Content QA (Headings + Alt Tags)" : 2
    "Crawlability (Robots.txt)" : 1
    "Reliability (Broken Links + Console)" : 2
```

| # | Audit Check | Category | Tool / Method | Validation Logic |
|:---:|:---|:---|:---|:---|
| 1 | **HTTPS Protocol** | 🔒 Security | Python `urllib` | Asserts `https://` prefix on target URL |
| 2 | **Security Headers** | 🔒 Security | Python `Requests` | Checks HSTS, CSP, X-Frame-Options, X-Content-Type |
| 3 | **Page Load Speed** | ⚡ Performance | Selenium `performance.timing` | Navigation Timing API, asserts < 5.0s |
| 4 | **Meta Title** | 🔍 SEO | Selenium `driver.title` | Presence check + 30–65 character guideline |
| 5 | **Meta Description** | 🔍 SEO | Selenium XPath | SERP display limits (70–170 chars) |
| 6 | **H1 Heading Structure** | 📝 Content QA | Selenium `find_elements` | Single primary H1 tag validation |
| 7 | **Image Alt Attributes** | ♿ Accessibility | Selenium tag scan | Missing alt text detection |
| 8 | **Open Graph Tags** | 🔍 Social SEO | Selenium XPath | `og:title`, `og:description`, `og:image` |
| 9 | **Canonical Tag** | 🔍 SEO | Selenium XPath | Valid `<link rel="canonical">` check |
| 10 | **Robots.txt** | 🕷️ Crawlability | Python `Requests` | HTTP 200 response validation |
| 11 | **Broken Links** | 🔗 Reliability | Selenium + `Requests` | HTTP HEAD status code ≥ 400 detection |
| 12 | **Console JS Errors** | ⚠️ Stability | Selenium `get_log("browser")` | SEVERE-level JavaScript exception scan |

---

## 🛠️ Complete Tech Stack

| Layer | Technology | Purpose |
|:---|:---|:---|
| **Language** | Python 3.10+ | Core automation logic |
| **Test Framework** | Pytest 7.4+ | Test discovery, fixtures, markers, parametrize |
| **Browser Automation** | Selenium WebDriver 4.15+ | DOM interaction, navigation, element inspection |
| **Browser Engine** | Google Chrome (Headless) | Automated rendering via ChromeDriver |
| **HTTP Client** | Python Requests | REST API calls, header inspection, link validation |
| **HTML Parser** | BeautifulSoup4 | HTML content parsing and extraction |
| **Reporting** | Allure Framework 2.27 | Interactive HTML reports with steps, attachments, history |
| **CI/CD Platform** | GitHub Actions | Automated test execution on Ubuntu runners |
| **Deployment** | GitHub Pages | Static site hosting for Allure dashboard |
| **Version Control** | Git + GitHub | Source code management and collaboration |

---

## 📁 Repository Structure

```
web-audit-automation-framework/
├── .github/
│   └── workflows/
│       └── main.yml               # GitHub Actions CI/CD pipeline
├── test_web_audit.py              # Pytest suite + embedded WebAuditEngine
├── conftest.py                    # Headless Chrome fixture + Allure screenshot hook
├── requirements.txt               # Python package dependencies
├── .gitignore                     # Excludes cache, allure-results, __pycache__
└── README.md                      # This documentation
```

---

## 🚀 Quick Start Guide

### Prerequisites
- **Python 3.10+** installed ([python.org](https://www.python.org/downloads/))
- **Google Chrome** browser installed

### 1. Clone the Repository
```bash
git clone https://github.com/Rahman-Pro/web-audit-automation-framework.git
cd web-audit-automation-framework
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the 12-Point Audit Suite
```bash
python -m pytest test_web_audit.py -v --alluredir=allure-results
```

### 4. View Interactive Report (Optional — requires Allure CLI)
```bash
allure serve allure-results
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

This framework runs automatically via **GitHub Actions** on **Ubuntu Latest**:

| Trigger | When |
|:---|:---|
| `push` | Every commit to `main` / `master` branch |
| `pull_request` | Every PR targeting `main` / `master` |
| `schedule` | **Weekly Sunday at midnight UTC** (`cron: '0 0 * * 0'`) |
| `workflow_dispatch` | Manual trigger from GitHub Actions UI |

### Pipeline Steps:
1. ☑️ Checkout source code
2. ☑️ Setup Python 3.10 environment
3. ☑️ Install pip dependencies
4. ☑️ Execute Pytest suite with Allure output
5. ☑️ Install Allure CLI 2.27
6. ☑️ Merge historical test data from gh-pages
7. ☑️ Generate interactive HTML report
8. ☑️ Deploy to GitHub Pages (`gh-pages` branch)

---

## 👨‍💻 About the Author

### **Atiqur Rahman** — SDET & QA Automation Engineer

Specializing in designing and building **enterprise-grade test automation frameworks**, **CI/CD pipelines**, and **quality engineering solutions** for web applications.

| | |
|:---|:---|
| 🔗 **LinkedIn** | [**linkedin.com/in/atiqur-rahman-pro**](https://www.linkedin.com/in/atiqur-rahman-pro/) |
| 🐙 **GitHub** | [**github.com/Rahman-Pro**](https://github.com/Rahman-Pro) |

### Core Competencies
`Python` `Java` `Pytest` `Selenium WebDriver` `Playwright` `Rest Assured` `Allure Reports` `GitHub Actions` `CI/CD Pipelines` `API Testing` `Performance Testing` `Web Automation` `Cross-Browser Testing` `BDD/TDD` `Agile/Scrum`

---

<p align="center">
  <b>⭐ Star this repository if you found it useful! ⭐</b>
</p>
