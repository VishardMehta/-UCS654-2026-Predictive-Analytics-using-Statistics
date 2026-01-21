📊 Sampling Techniques on Imbalanced Credit Card Dataset

📌 Objective

The objective of this assignment is to understand the importance of sampling techniques in handling imbalanced datasets and to analyze how different sampling strategies affect the performance of multiple machine learning models in credit card fraud detection.

⸻

📂 Dataset
	•	Dataset Name: Creditcard_data.csv
	•	Source:
https://github.com/AnjulaMehto/Sampling_Assignment/blob/main/Creditcard_data.csv
	•	Target Variable: Class
	•	0 → Legitimate Transaction
	•	1 → Fraudulent Transaction

The dataset is highly imbalanced, with fraudulent transactions being extremely rare.

⸻

⚙️ Methodology

1️⃣ Data Preparation
	•	The dataset was split into:
	•	Features (X): All columns except Class
	•	Target (y): Class
	•	A stratified 70:30 train–test split was used to preserve class distribution.
	•	Sampling techniques were applied only on the training data to prevent data leakage.

⸻

2️⃣ Sampling Techniques Applied

Five sampling strategies were evaluated:

Sampling ID	Technique
Sampling1	NoSampling
Sampling2	RandomOverSampler
Sampling3	RandomUnderSampler
Sampling4	SMOTE
Sampling5	SMOTETomek


⸻

3️⃣ Machine Learning Models

Five classifiers were trained with each sampling technique:

Model ID	Classifier
M1	Logistic Regression
M2	Decision Tree
M3	Random Forest
M4	Naive Bayes
M5	Support Vector Machine (SVM)


⸻

4️⃣ Evaluation Metrics

Each model was evaluated on unseen test data using:
	•	Accuracy
	•	Precision
	•	Recall
	•	F1-Score
	•	ROC-AUC

⚠️ Since fraud detection is a cost-sensitive problem, Recall was treated as the most important metric.

⸻

📊 Results & Graphical Analysis

⸻

🔹 Accuracy Heatmap

Accuracy values appear very high for most models, even without sampling.

Observation:
	•	Accuracy remains above 97% in most cases.
	•	High accuracy is misleading because the majority class dominates predictions.

⸻

🔹 Recall Heatmap

Recall represents the ability to detect fraudulent transactions.

Key Findings:
	•	NoSampling results in zero recall for most models.
	•	RandomUnderSampler achieved 100% recall for Random Forest.
	•	Sampling significantly improves fraud detection capability.

⸻

🔹 Precision Heatmap

Precision measures how many detected frauds are actually fraud.

Observation:
	•	Precision decreases when recall increases.
	•	This trade-off is expected in fraud detection systems.

⸻

🔹 F1-Score Heatmap

F1-score balances precision and recall.

Observation:
	•	Best F1-score observed for Decision Tree + RandomOverSampler.
	•	Many combinations show near-zero F1 due to poor recall.

⸻

🔹 ROC-AUC Heatmap

ROC-AUC evaluates the model’s ability to distinguish between classes.

Key Insight:
	•	RandomForest + RandomUnderSampler / SMOTETomek achieved the highest ROC-AUC.
	•	Random Forest shows the most stable performance across sampling techniques.

⸻

🔹 Average Recall per Sampling Method

This graph shows the effectiveness of each sampling method across all models.

Conclusion:
	•	RandomUnderSampler provides the highest average recall.
	•	RandomOverSampler also performs well.
	•	SMOTE-based techniques perform moderately.

⸻

🔹 Best Recall per Model

This graph highlights the best sampling method for each model based on recall.

Best Combinations:
	•	Logistic Regression → RandomOverSampler
	•	Decision Tree → RandomOverSampler
	•	Random Forest → RandomUnderSampler
	•	SVM → RandomOverSampler
	•	Naive Bayes → Poor performance overall

⸻

📋 Metrics Summary Table (Highlights)

Model	Best Sampling	Recall	ROC-AUC
Logistic Regression	RandomOverSampler	High	~0.71
Decision Tree	RandomOverSampler	High	~0.83
Random Forest	RandomUnderSampler	1.00	~0.86
SVM	RandomOverSampler	High	~0.77
Naive Bayes	None	0.00	Low

Full metrics are available in full_metrics.csv.

⸻

✅ Final Conclusion
	•	Sampling techniques are critical when working with imbalanced datasets.
	•	Accuracy alone is not reliable for fraud detection.
	•	RandomUnderSampler achieved the highest recall on average.
	•	RandomForest combined with RandomUnderSampler delivered the best overall performance in terms of recall and ROC-AUC.

