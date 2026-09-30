# Python Hybrid Custom API Automation Framework

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![PyTest](https://img.shields.io/badge/PyTest-8.0+-0A9EDC?style=flat&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Requests](https://img.shields.io/badge/HTTP%20Client-Requests-2B5B84?style=flat)](https://requests.readthedocs.io/)
[![Allure Report](https://img.shields.io/badge/Reporting-Allure-FF7800?style=flat&logo=qameta&logoColor=white)](https://allurereport.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An enterprise-grade, modular, and scalable REST API test automation framework built using **Python 3.12** and **PyTest**. It supports full CRUD operations, JSON schema contract validation, multi-source data-driven testing, parallel execution, and rich reporting.

---

## 🚀 Key Highlights

- **Modular Design:** Strict separation of test logic, data models, payloads, and API interaction layers.
- **Full CRUD Testing:** End-to-end user lifecycle management (`POST`, `GET`, `PUT`, `PATCH`, `DELETE`).
- **Schema Validation:** Strict response contract validation powered by `jsonschema`.
- **Hybrid Test Data Management:** Ingestion from CSV, Excel (`.xlsx`), JSON templates, and dynamic generation via `Faker`.
- **Parallel Test Execution:** High-speed, multi-threaded test runs using `pytest-xdist`.
- **Rich Reporting:** Detailed visual dashboards via **Allure Report** and standalone **PyTest HTML** reports.
- **Frontend-Backend Sync:** Integration tests checking API data consistency against the web layer via Selenium.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Language** | Python 3.12 |
| **Test Runner** | PyTest |
| **HTTP Client** | Requests |
| **Contract Validation** | jsonschema |
| **Dynamic Data Generation** | Faker |
| **Tabular Data** | openpyxl (Excel), CSV |
| **Parallel Execution** | pytest-xdist |
| **UI Integration** | Selenium WebDriver |
| **Reporting** | Allure Report, pytest-html |

---

## 📁 Project Structure

```text
python-api-automation-framework/
│
├── config/                  # Environment endpoints and runtime configurations
│   ├── config.py            # Environment-aware configuration manager
│   └── environments.json    # Target environment mapping (QA, Dev)
│
├── data/                    # Test data storage (CSV, Excel, JSON)
│   ├── users_test_data.csv  # Parameterized inputs for data-driven tests
│   ├── test_data.xlsx       # Tabular multi-scenario test records
│   └── static_payloads.json # Baseline request templates and edge cases
│
├── helpers/                 # Framework utilities and wrappers
│   ├── api_client.py        # Centralized HTTP client with automatic Allure logging
│   ├── data_reader.py       # File parsers for CSV, Excel, and JSON
│   └── faker_utils.py       # Custom randomized data utilities
│
├── payloads/                # Request payload factories
│   └── user_payloads.py     # Dynamic payload builders using Faker
│
├── schemas/                 # JSON schema contracts
│   └── user_schema.py       # User entity JSON Schema specifications
│
├── tests/                   # Test suites
│   ├── conftest.py          # PyTest global fixtures and lifecycle hooks
│   ├── crud/                # CRUD endpoint and lifecycle tests
│   │   ├── test_create_user.py
│   │   └── test_user_e2e.py
│   └── integration/         # API-to-UI sync tests
│       └── test_api_ui_sync.py
│
├── reports/                 # Test run artifacts (HTML, Allure raw results)
├── .gitignore               # Files excluded from source control
├── pytest.ini               # PyTest global configuration
├── requirements.txt         # Pinned project dependencies
└── README.md
