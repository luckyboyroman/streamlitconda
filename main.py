import streamlit as st
import subprocess
import os


def find_conda():
    """Находит conda в системе"""
    try:
        # Для Windows
        if os.name == 'nt':
            result = subprocess.run(["where", "conda"],
                                    capture_output=True, text=True, timeout=10)
        # Для Linux/MacOS
        else:
            result = subprocess.run(["which", "conda"],
                                    capture_output=True, text=True, timeout=10)

        if result.returncode == 0:
            paths = result.stdout.strip().split('\n')
            return True, paths
        return False, []

    except Exception as e:
        return False, []


st.title("Поиск Conda")

found, paths = find_conda()
st.write(f"Conda найден: {found}")

if found:
    st.write("Найденные пути:")
    for path in paths:
        st.code(path)
else:
    st.warning("Conda не найден в системе")