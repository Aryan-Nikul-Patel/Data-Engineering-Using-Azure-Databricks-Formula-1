# Data Engineering Using Azure Databricks: Formula 1

![Formula 1](https://images2.alphacoders.com/121/thumb-1920-1214054.png)

## 🚀 Project Overview
This project aims to provide a data analysis solution for Formula 1 race results using **Azure Databricks**. The ETL pipeline ingests Formula 1 motor racing data, transforms it, and loads it into a data warehouse for reporting and analysis. The data is sourced from **ergast.com** and stored in **Azure Data Lake Gen2**. Data transformation and analysis are performed using **Azure Databricks**, and the process is orchestrated using **Azure Data Factory**.

---

## 🏎️ Formula 1 Overview
Formula 1 (F1) is the premier international racing series governed by the **FIA**. It consists of **10 teams**, each with **two drivers**, competing in **20-23 races (Grands Prix)** per season. The driver with the highest points at the end of the season is crowned the **Drivers' Champion**, while the best-performing team wins the **Constructors' Championship**.

### Key Features of F1:
- **Hybrid-engine, high-tech cars** 🏎️
- **50-70 lap races** across various countries 🌍
- **Pit stops** for tire changes and adjustments 🔧
- **Grid positions** determined by qualifying rounds ⚡

---

## 📊 Architecture Diagram
![Solution Architecture](https://github.com/Aryan-Nikul-Patel/Data-Engineering-Using-Azure-Databricks-Formula-1/blob/main/resource/ETL_Architecture.png)

---

## 📜 ER Diagram
Database structure based on the **Ergast Developer API**:

![ER Diagram](https://github.com/Aryan-Nikul-Patel/Data-Engineering-Using-Azure-Databricks-Formula-1/blob/main/resource/formula1_db_data_model.png)

For detailed documentation, visit the [Database User Guide](http://ergast.com/docs/f1db_user_guide.txt).

---

## ⚙️ How It Works
### 📂 Source Data Files
Data is sourced from **Ergast Developer API**, covering race results from **1950 to 2022**.

| File Name   | File Type               |
|------------|-------------------------|
| Circuits   | CSV                     |
| Races      | CSV                     |
| Constructors | JSON (Single Line)     |
| Drivers    | JSON (Nested)           |
| Results    | JSON (Single Line)      |
| PitStops   | JSON (Multi Line)       |
| LapTimes   | CSV (Split Files)       |
| Qualifying | JSON (Multi Line Split) |

### 🔄 Execution Overview
- **Bronze Zone**: Raw data ingestion using **Azure Data Factory (ADF)**.
- **Silver Zone**: Data transformation into **Delta Tables** using **Azure Databricks**.
- **Gold Zone**: Aggregated data for **reporting and analytics**.
- **ETL Pipelines** handle:
  - **Ingestion** (Bronze → Silver)
  - **Transformation** (Silver → Gold)

---

## 🏗️ Azure Resources Used
- **Azure Data Lake Storage** 📁
- **Azure Data Factory** 🔄
- **Azure Databricks** 🔥
- **Azure Key Vault** 🔑

---

## 📌 Project Requirements
### 1️⃣ Data Ingestion
✅ Ingest all 8 files into **Azure Data Lake**  
✅ Apply **schema** and **audit columns**  
✅ Store data in **Delta format**  
✅ Enable **incremental loading**  

### 2️⃣ Data Transformation
✅ Join tables for **reporting** & **analysis**  
✅ Apply **audit columns**  
✅ Store data in **Delta format**  
✅ Handle **incremental loads**  

### 3️⃣ Data Reporting
✅ **Driver Standings** 📊  
✅ **Constructor Standings** 🏎️  

### 4️⃣ Data Analysis
✅ Identify **dominant drivers & teams** 🏆  
✅ Visualize **outputs in Databricks and PowerBI Dashboards** 📈  

### 5️⃣ Scheduling
✅ **Automated pipeline execution** every **Sunday at 10 PM** ⏳  
✅ **Monitoring & alerts** for failures 🔔  
✅ **Rerun failed pipelines** ♻️  

### 6️⃣ Non-Functional Requirements
✅ Ability to **delete individual records**  
✅ Ability to **see history and time travel** ⏪  
✅ Ability to **roll back to a previous version** 🔄  

---

## 📉 Analysis Results
![Result1](https://github.com/Aryan-Nikul-Patel/Data-Engineering-Using-Azure-Databricks-Formula-1/blob/main/PowerBI/F1_Dashboard.png)

---

## Setup Using Service Principal  
📌 *Follow the setup guide in the [Setup Folder](set-up/Mount ADLS.py)*  

![Service Principal Setup](https://github.com/Aryan-Nikul-Patel/Data-Engineering-Using-Azure-Databricks-Formula-1/blob/main/resource/Set_up.png)  

---

## Incremental Load Process  
🔹 **Day 1 (Cutover Date)**  
![Incremental Load - Day 1](https://github.com/Aryan-Nikul-Patel/Data-Engineering-Using-Azure-Databricks-Formula-1/blob/main/resource/IL_d1.png)  

🔹 **Day 2**  
![Incremental Load - Day 2](https://github.com/Aryan-Nikul-Patel/Data-Engineering-Using-Azure-Databricks-Formula-1/blob/main/resource/IL_d2.png)  

🔹 **Day 3**  
![Incremental Load - Day 3](https://github.com/Aryan-Nikul-Patel/Data-Engineering-Using-Azure-Databricks-Formula-1/blob/main/resource/IL_d3.png)  

---

## Azure Data Factory (ADF) Pipelines  
📌 **ADF Components Overview**  
![ADF Components](https://github.com/Aryan-Nikul-Patel/Data-Engineering-Using-Azure-Databricks-Formula-1/blob/main/ADF_Pipeline_Automation/ADF%20components.png)  

📌 **Formula 1 Data Pipeline**  
![F1 Pipeline](https://github.com/Aryan-Nikul-Patel/Data-Engineering-Using-Azure-Databricks-Formula-1/blob/main/ADF_Pipeline_Automation/End_To_End_Automation.png)  

📌 **F1 Pipeline Run Execution**  
![F1 Pipeline Run](https://github.com/Aryan-Nikul-Patel/Data-Engineering-Using-Azure-Databricks-Formula-1/blob/main/ADF_Pipeline_Automation/Pipeline%20Runs.png)  

---

## Technologies/Tools Used  
- Pyspark  
- Spark SQL  
- Delta Lake  
- Azure Databricks  
- Azure Data Factory  
- Azure Data Lake Storage Gen2  
- Azure Key Vault  
- Power BI  

---

## 📌 Getting Started
### Prerequisites
- Azure subscription  
- Databricks workspace  
- Azure Data Factory  

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Aryan-Nikul-Patel/Data-Engineering-Using-Azure-Databricks-Formula-1.git
   ```
2. Configure **Azure Databricks** and **ADF**.
3. Set up **Azure Key Vault** for security.
4. Run the **ETL pipeline** and start analyzing!

---

## 📜 Conclusion
This project leverages **Azure Databricks** to process **Formula 1 race data** efficiently. By implementing an optimized **ETL pipeline**, it enables **data-driven insights**, analytics, and reporting for F1 statistics.

🚀 If you found this project useful, **give it a ⭐ on GitHub!** 🎉

---

## 🤝 Connect with Me
🔗 [LinkedIn](https://www.linkedin.com/in/aryan-nikul-patel/)  
📧 Email: **anpnhp2002@gmail.com**