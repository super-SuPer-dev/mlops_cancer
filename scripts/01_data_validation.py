import mlflow
from sklearn.datasets import load_breast_cancer  # ✅ ชุดข้อมูลใหม่


def validate_data():
    """
    Loads the breast cancer dataset, performs basic validation checks,
    and logs the results to MLflow.
    """
    # ✅ ตั้งชื่อ experiment ให้สื่อถึงข้อมูลชุดใหม่
    mlflow.set_experiment("Breast Cancer - Data Validation")

    with mlflow.start_run():
        print("Starting data validation run...")
        mlflow.set_tag("ml.step", "data_validation")

        # 1. Load data as a Pandas DataFrame
        d = load_breast_cancer(as_frame=True)  # ✅
        df = d.frame
        print("Data loaded successfully.")

        # 2. Perform simple validation checks
        num_rows, num_cols = df.shape
        num_classes = df['target'].nunique()
        missing_values = df.isnull().sum().sum()

        # ✅ เพิ่มการตรวจ class balance:
        #    class_balance = สัดส่วนของคลาสที่น้อยที่สุด (0.0 - 1.0)
        class_counts = df['target'].value_counts()
        class_balance = class_counts.min() / num_rows

        print(f"Dataset shape: {num_rows} rows, {num_cols} columns")
        print(f"Number of classes: {num_classes}")
        print(f"Missing values: {missing_values}")
        print(f"Class distribution:\n{class_counts}")
        print(f"Class balance (minority class ratio): {class_balance:.4f}")

        # 3. Log validation results to MLflow
        mlflow.log_metric("num_rows", num_rows)
        mlflow.log_metric("num_cols", num_cols)
        mlflow.log_metric("missing_values", missing_values)
        mlflow.log_metric("class_balance", class_balance)  # ✅ log เป็น metric
        mlflow.log_param("num_classes", num_classes)

        # ✅ แก้เงื่อนไขจำนวนคลาสให้ถูกต้องกับชุดนี้:
        #    Breast Cancer มี 2 คลาส จึงต้อง == 2 (ไม่ใช่ < 3)
        # ✅ เพิ่มเงื่อนไข class balance: คลาสน้อยสุดต้อง >= 20%
        validation_status = "Success"
        if missing_values > 0 or num_classes != 2 or class_balance < 0.2: # 0.2
            validation_status = "Failed"

        mlflow.log_param("validation_status", validation_status)
        print(f"Validation status: {validation_status}")

        # 4. คืน exit code ที่ไม่ใช่ 0 เมื่อ Failed
        #    เพื่อให้ GitHub Actions จับความผิดปกติของข้อมูลได้
        if validation_status == "Failed":
            raise SystemExit("Data validation failed — หยุด pipeline ไม่ให้ไปขั้นถัดไป")

        print("Data validation run finished.")


if __name__ == "__main__":
    validate_data()