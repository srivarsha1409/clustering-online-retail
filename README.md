
# 🛍️ Customer Segmentation

This project builds a **Customer Segmentation System** for an **Online Retail Dataset** using **Machine Learning Clustering Techniques**.

The goal is to group customers into **segments** (VIPs, Regulars, Occasional Buyers, etc.) to help businesses understand customer behavior and improve marketing strategies.

It also provides a **Streamlit Web App** for interactive exploration and prediction.

LIVE DEMO:https://clustering-online-retail-nmufdxe2xuzcbe6n6xeeka.streamlit.app/
---

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/srivarsha1409/clustering-online-retail.git
cd clustering-online-retail
```

### 2️⃣ Create Virtual Environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at **[http://localhost:8501](http://localhost:8501)** 🎉

---

## 📊 Dataset Description

The dataset contains customer transactions.

We derive **RFM Features**:

* **Recency (R):** How recently the customer made a purchase
* **Frequency (F):** How often the customer makes purchases
* **Monetary (M):** How much money the customer spends

These three features form the **RFM Matrix**, which is the basis for segmentation.

---

## 🔎 Methodology

### 1️⃣ Data Preprocessing

✔️ Removed missing values
✔️ Removed canceled orders / negative quantities
✔️ Converted dates to datetime format
✔️ Calculated **RFM features per customer**

---

### 2️⃣ Feature Engineering

* **Outlier Capping:** Prevent extreme values from dominating
* **Yeo-Johnson Transformation:** Reduced skewness of distributions
* **Standardization:** Using **StandardScaler** (mean=0, std=1) for clustering

---

### 3️⃣ Choosing the Clustering Algorithm

We used **KMeans Clustering** because:

* It’s efficient for large datasets
* Works well with numeric features like RFM
* Provides **clear customer segments**

---

### 4️⃣ Finding Optimal Number of Clusters

We experimented with different **k values (2–10)** and used:

#### 📐 Elbow Method

* Plotted **WCSS (Within-Cluster-Sum-of-Squares)** vs k
* Look for the “Elbow Point” → Best tradeoff between compactness & complexity

#### 📊 Silhouette Score

* Measures **how well customers fit inside their clusters**
* Range: -1 → 1 (higher = better clustering)
* Compared scores for different k

✅ From both methods, the best cluster number was **k = 3 (three customer groups)**

---

### 5️⃣ Building the Clusters

* Applied **KMeans with k=3**
* Assigned each customer to a **Cluster**
* Labeled clusters as:

  * **Cluster 0: VIP Customers (High Spend, High Frequency)**
  * **Cluster 1: Regular Customers (Moderate Spend & Frequency)**
  * **Cluster 2: Occasional Customers (Low Spend, Low Frequency)**

---

## 📈 Results & Insights

* Businesses can **target VIPs** with loyalty programs
* **Regulars** can be nurtured into VIPs
* **Occasional buyers** need promotions to re-engage

This segmentation helps **personalized marketing** and **customer retention** strategies.

---

## 🖥️ Streamlit Web App

Our **Streamlit Dashboard** provides:

### ✅ Dataset Preview

First 5 rows of customer data

### ✅ Cluster Profiling

Average Recency, Frequency, Monetary per cluster

* Customer count in each segment

### ✅ Customer Prediction

Enter **CustomerID** → Get **Cluster & Segment** instantly

---

## 📌 Example Usage

Run the app:

```bash
streamlit run app.py
```

1. Login with username & password
2. Explore dataset preview
3. View cluster profiling
4. Predict any customer’s segment

---

## 📊 Visualizations

* **Histograms** of R, F, M before & after transformation
 <img width="700" height="470" alt="image" src="https://github.com/user-attachments/assets/acea1ca9-b406-4946-8ae9-020455c85e65" />

* **Boxplots** to check outliers
  <img width="713" height="470" alt="image" src="https://github.com/user-attachments/assets/f4c2e1aa-a936-4655-86bf-2e365bcb19e1" />

* **Elbow Curve** (WCSS vs k)
 img width="713" height="470" alt="image" src="https://github.com/user-attachments/assets/9534c85e-eadd-4a84-82a3-c8a15a2e81ce" />
* **Silhouette Score Plot**
  <img width="700" height="470" alt="image" src="https://github.com/user-attachments/assets/da826991-46f6-4e17-aa3b-77a93a15fb77" />

* **Bar Charts** for cluster profiling
  <img width="549" height="393" alt="image" src="https://github.com/user-attachments/assets/6678d53c-f008-4b49-bc6f-6607ca4fcf4b" />


---
username:admin 
password:1234 
