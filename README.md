ruff check scripts/ tests/

mlflow

python scripts/01_data_validation.py
python scripts/02_data_preprocessing.py # คัดลอก Run ID ที่พิมพ์ออกมา
python scripts/03_train_evaluate_register.py <RUN_ID> 10.0
python scripts/04_load_and_predict.py
python -m mlflow ui --backend-store-uri sqlite:///mlflow.db # เปิด http://localhost:5000
หรือ python -m mlflow ui # เปิด http://localhost:5000
# macOS: พอร์ต 5000 ถูก AirPlay Receiver ยึดไว้ ให้เติม --port 5001 แล้วเปิด http://localhost:5001


cd mlops_pipeline
git init
# สร้าง .gitignore ตามหัวข้อ 2 ให้เรียบร้อยก่อน ไม่งั้น mlflow.db และ mlruns/ จะติดขึ้นไปด้วย
git add .
git commit -m "lab09: mlflow pipeline + github actions"
git branch -M main
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main

# ps
uv run scripts/01_data_validation.py; echo $LASTEXITCODE