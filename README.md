# 🚀 Tech Stack Recommender

<p align="center">
  <b>A Machine Learning-based recommendation system that suggests suitable tech career paths based on a user's technical skills.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue?logo=python">
  <img src="https://img.shields.io/badge/Machine%20Learning-TF--IDF-orange">
  <img src="https://img.shields.io/badge/Framework-Streamlit-red">
  <img src="https://img.shields.io/badge/Recommendation%20System-Content%20Based-success">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen">
</p>



## 📌 Project Overview

Choosing the right technology career path can be challenging due to the wide range of available roles.

The **Tech Stack Recommender** is a content-based recommendation system that analyzes a user's technical skills and recommends the most relevant job roles. The system uses **TF-IDF Vectorization** and **Cosine Similarity** to measure the similarity between user skills and job profiles.

This project demonstrates the practical application of Machine Learning techniques in career recommendation systems.

---

## 🎯 Objectives

* Build a recommendation system using Content-Based Filtering.
* Apply TF-IDF Vectorization to transform textual skills into numerical vectors.
* Calculate similarity scores using Cosine Similarity.
* Understand the implementation of recommendation pipelines.
* Develop both CLI and Streamlit-based interfaces.

---

## ✨ Features

* Recommend relevant tech job roles based on user skills.
* Display similarity scores for each recommendation.
* Interactive Streamlit web interface.
* Command Line Interface (CLI) support.
* Easily expandable dataset for adding new roles and skills.
* Handles cold-start scenarios through user skill input.

---

## 🧠 Machine Learning Concepts Used

### 🔹 TF-IDF (Term Frequency – Inverse Document Frequency)

TF-IDF is used to convert textual skill data into numerical vectors by assigning importance to each skill based on its frequency and uniqueness.

### 🔹 Cosine Similarity

Cosine Similarity measures the similarity between the user's skill vector and job role vectors.

**Similarity = (A · B) / (||A|| × ||B||)**

The similarity score ranges from:

* **1** → Perfect Match
* **0** → No Similarity

---

## 🏗️ Project Structure

```bash
tech-stack-recommender/
│
├── app.py                # Streamlit Web Application
├── recommender.py        # Command Line Interface
├── raw_Skills.csv        # Dataset
├── requirements.txt      # Project Dependencies
└── README.md             # Documentation
```

---

## 📊 Dataset

The dataset contains various technology roles along with their required skills.

| Job Role              | Skills                                           |
| --------------------- | ------------------------------------------------ |
| Cloud Architect       | AWS, Cloud Computing, Automation, DevOps, Python |
| Data Scientist        | Python, Statistics, Machine Learning, SQL        |
| Frontend Developer    | JavaScript, React, CSS, HTML                     |
| Backend Developer     | Python, Java, APIs, Databases                    |
| DevOps Engineer       | Docker, Kubernetes, Jenkins, Linux               |
| AI Engineer           | TensorFlow, NLP, Deep Learning                   |
| Cybersecurity Analyst | SIEM, Cryptography, Risk Analysis                |
| Full Stack Developer  | React, Node.js, MongoDB                          |

---

## 📦 Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit

---

## ⚙️ Installation

### Prerequisites

* Python 3.7 or above

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

### Run Streamlit Web Application

```bash
streamlit run app.py
```

Enter your technical skills separated by commas and click **Recommend**.

Example:

```text
Python, Docker, Cloud Computing, Automation
```

### Run CLI Version

```bash
python recommender.py
```

---

## 🧪 Sample Output

### User Input

```text
Python, Cloud Computing, Automation, Docker
```

### Recommended Roles

| Rank | Job Role        | Similarity Score |
| ---- | --------------- | ---------------- |
| 🥇   | Cloud Architect | 87%              |
| 🥈   | DevOps Engineer | 76%              |
| 🥉   | AI Engineer     | 58%              |

---

## ❄️ Cold Start Handling

### User Cold Start

The system avoids user cold-start issues by collecting skills directly from users during input.

### Item Cold Start

New job roles can be added easily because recommendations rely on skill metadata rather than user interaction history.

---

## 🔮 Future Enhancements

* Expand the dataset with additional job roles.
* Integrate real-time job market data.
* Recommend learning resources for missing skills.
* Add visualization dashboards.
* Deploy the application on cloud platforms.

---

## 🎓 Internship Project

This project was developed as part of the **DecodeLabs Industrial Training Program (Batch 2026)**.

The project demonstrates the implementation of a **Content-Based Recommendation System** using Machine Learning techniques.

---

## 🏆 Key Learnings

* Content-Based Recommendation Systems
* TF-IDF Vectorization
* Cosine Similarity
* Text Processing Techniques
* Streamlit Application Development
* End-to-End ML Workflow
---

## 👩‍💻 Author

**Payal Priya**


---
