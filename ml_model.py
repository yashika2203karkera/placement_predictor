import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib
import os

# 1. Load dataset
df = pd.read_csv("data/placement.csv")

# 2. Drop unnecessary columns if present
if 'sl_no' in df.columns:
    df = df.drop('sl_no', axis=1)

if 'salary' in df.columns:
    df = df.drop('salary', axis=1)

# 3. Convert ALL text columns (including 'Commerce', 'Science', etc.) to numbers
categorical_cols = [
    'gender', 'ssc_b', 'hsc_b', 'hsc_s', 
    'degree_t', 'workex', 'specialisation', 'status'
]

for col in categorical_cols:
    if col in df.columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))

# 4. Separate Features (X) and Target (y)
X = df.drop('status', axis=1)
y = df['status']

# 5. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 7. Save trained model
os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/placement_model.joblib')

print("SUCCESS: Model trained and saved to model/placement_model.joblib!")