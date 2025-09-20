import streamlit as st
import subprocess

def check_conda_available():
    """Проверяет, доступен ли conda в системе"""
    try:
        # Пробуем выполнить conda --version
        result = subprocess.run(["conda", "--version"],
                              capture_output=True, text=True, timeout=10)
        return result.returncode == 0
    except:
        return False

st.title("Check")

st.write(check_conda_available())