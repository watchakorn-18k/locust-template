# Locust Load Testing Framework

# Set Env

```
python -m venv _env
_env\Scripts\activate
```

# Start

```
pip install locust
locust -f locust.py --headless --users 100 --spawn-rate 10 -t 1m -H http://127.0.0.1:6161
```
