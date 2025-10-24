# 🕸️ GitHub Crawler

## 📌 Overview
This project is a **GitHub Crawler** that uses **GitHub’s GraphQL API** to collect repository data — specifically repository names and their star counts.  
The data is stored in a database and exported to a `.csv` file.  
The workflow is fully automated using **GitHub Actions**.

---

## ⚙️ Features
- Uses **GitHub GraphQL API** to fetch repositories
- Stores results in a database (`repos.db`)
- Exports output to a CSV file (`repos.csv`)
- Runs automatically through **GitHub Actions**
- Uses the **default GitHub Token** (no private secrets required)

---

## 🗂️ Project Structure
github-crawler/
│
├── crawler/
│ ├── main.py # Main script to run the crawler
│ ├── db.py # Database schema and data insertion logic
│ └── github_api.py # GitHub GraphQL API request handler
│
├── repos.db # Database storing repository data
├── repos.csv # Exported repository data
└── .github/


---

## 🚀 How It Works
1. The GitHub Action sets up Python and installs dependencies.  
2. It runs `crawler/main.py` which:
   - Fetches repositories and their star counts
   - Stores data in `repos.db`
   - Exports results to `repos.csv`
3. The workflow completes automatically and uploads the output as an artifact.

---

## ✅ Workflow Status
The workflow runs successfully in GitHub Actions.  
Latest run: **Succeeded ✅**

---

## 👩‍💻 Author
**Marium Zehra**  
GitHub: [@marium17](https://github.com/marium17)

└── workflows/
└── main.yml # GitHub Actions workflow file
