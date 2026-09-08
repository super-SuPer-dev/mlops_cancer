import mlflow
from sklearn.datasets import load_breast_cancer


def load_and_predict():
    """
    Simulates a production scenario by loading a model using an alias
    from the MLflow Model Registry and using it for prediction.
    """
    MODEL_NAME = "cancer-classifier-prod"
    MODEL_ALIAS = "staging"

    print(f"Loading model '{MODEL_NAME}' with alias '@{MODEL_ALIAS}'...")

    # Load the model from the Model Registry ด้วย Alias URI
    try:
        model = mlflow.pyfunc.load_model(model_uri=f"models:/{MODEL_NAME}@{MODEL_ALIAS}")
    except mlflow.exceptions.MlflowException as e:
        print(f"\nError loading model: {e}")
        print(f"Please make sure a model version has the alias '@{MODEL_ALIAS}' in the MLflow UI.")
        return

    # ✅ ข้อมูลชุดใหม่: Breast Cancer (binary)
    #    as_frame=True เพื่อให้ชื่อคอลัมน์ตรงกับ signature ของโมเดล
    X, y = load_breast_cancer(return_X_y=True, as_frame=True)

    # ✅ แผนที่เลขคลาสเป็นชื่อคำ (0 = benign, 1 = malignant)
    CLASS_NAMES = {0: "benign", 1: "malignant"}

    # ✅ หยิบรายแรกของแต่ละคลาส:
    #    idx_benign = ดัชนีแถวแรกที่ y == 0, idx_malignant = ดัชนีแถวแรกที่ y == 1
    idx_benign = y[y == 0].index[0]
    idx_malignant = y[y == 1].index[0]
    sample_indices = [idx_benign, idx_malignant]

    for idx in sample_indices:
        sample_data = X.iloc[[idx]]   # [[idx]] เพื่อให้เป็น DataFrame 1 แถว
        actual_label = int(y.iloc[idx])

        # ทำนายด้วย pipeline ทั้งก้อน (preprocessing อยู่ในโมเดลแล้ว)
        prediction = int(model.predict(sample_data)[0])

        print("-" * 30)
        print(f"Sample (row index {idx}):")
        print(f"  Actual Label:    {CLASS_NAMES[actual_label]} ({actual_label})")
        print(f"  Predicted Label: {CLASS_NAMES[prediction]} ({prediction})")
        print("-" * 30)


if __name__ == "__main__":
    load_and_predict()