
# Airflow Practices - Platzi Course

This repository contains Airflow DAGs and configurations created as part of my Airflow training from Platzi. The goal is to showcase my ability to build, manage, and monitor workflows using Apache Airflow. Each file represents a specific practice or feature of Airflow, including BashOperator, PythonOperator, task dependencies, sensors, and more.

## Project Structure

```
project-root/
├── dags/
│   ├── 0-primerdag.py
│   ├── 1-bashoperator.py
│   ├── 2-pythonoperator.py
│   ├── 3-dependencias.py
│   ├── 4-customoperator.py
│   ├── 5.1-orquestacion.py
│   ├── 5.2-Orquestacion.py
│   ├── 5.3-Orquestacion.py
│   ├── 6.1-monitoring.py
│   ├── 6.2-Monitoring.py
│   ├── 7.1-ExternalTaskSensor.py
│   ├── 7.2-ExternalTaskSensor.py
│   ├── 7.3-Filesensor.py
│   ├── 8-Templating.py
│   ├── 9-XCom.py
│   ├── 10-branchpythonoperator.py
│   └── hellooperator.py
└── docker-compose.yaml
```

### Not Included

Only the relevant DAG files and the `docker-compose.yaml` file are included to keep the repository clean and focused. Avoid uploading unnecessary folders created during the execution of Airflow Docker containers (e.g., `logs/`, `plugins/`, etc.).

---

## How to Initialize Airflow

To set up Airflow and run these examples, follow these steps:

1. **Install Docker** (if not already installed):
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)

2. **Start Airflow with Docker Compose**:
   - Navigate to the project root directory containing the `docker-compose.yaml` file.
   - Run the following command:
     ```bash
     docker-compose up -d
     ```

3. **Access the Airflow Web UI**:
   - Open your browser and navigate to `http://localhost:8080`.
   - Log in with the default credentials (username: `airflow`, password: `airflow`).

4. **Add the DAGs**:
   - Place the DAG files inside the `dags/` folder.
   - Restart the Airflow services if necessary:
     ```bash
     docker-compose restart
     ```

---

## Running the DAGs

1. Log in to the Airflow Web UI.
2. Enable the DAG you want to run.
3. Trigger the DAG manually or let it run on its schedule.

---

## License

This project is licensed under the MIT License. Feel free to use and adapt it for your own learning purposes.
