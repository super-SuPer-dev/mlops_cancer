# clone
```cmd
git clone [<repository-url>](https://github.com/super-SuPer-dev/mlops_cancer.git)
cd mlops_cancer
```

# setup uv project
```cmd
uv sync
```

# ruff check
```cmd
ruff check scripts/ tests/
ruff check scripts/ tests/ --fix
rull check scripts/ tests/
```

# run ตามข้อ (ใช้ powershell นะ)
```cmd
ข้อที่ c1.1: uv run python -c "import mlflow, sklearn; print(mlflow.__version__, sklearn.__version__); print(mlflow.get_tracking_uri())"
ข้อที่ c1.2: uv run scripts/00_data_val.py

ข้อที่ c2.1: uv run scripts/01_data_validation.py
ข้อที่ c2.2: uv run scripts/01_data_validation_false.py; echo $LASTEXITCODE
ข้อที่ c2.3: uv run scripts/02_data_preprocessing.py

ข้อที่ c3.1: uv run scripts/03_train_evaluate_register.py <RUN_ID ชื่อ folder ใน mlruns ตัวอย่าง 2\b2341;klja... เอารหัสยาวๆมาว่าง> 10.0
ข้อที่ c3.2: uv run scripts/04_load_and_predict.py 
ข้อที่ c3.3: uv run python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001

ข้อที่ 4 ให้ run code จาก setup github ก่อน
ข้อที่ c4.1: ดูใน pdf เอา
ข้อที่ c4.2: ดูใน pdf เอา
```

# setup github
ตรงให้สร้าง github repo ขี้นมาเอง แค่ตั้งชื่อและกด "create repository" ได้เลย แล้วมันจะขึ้นอีกหน้า มี command ให้ copy แต่ให้ใช้รูปแบบตามด้านล่างแทน

```cmd
git add .
git commit -m "lab09 hands-on: mlflow pipeline + github actions"
git branch -M main
git remote add origin https://github.com/<your_github_name>/<your_repo_name>.git # เปลี่ยนตรงนี้
git push -u origin main
```