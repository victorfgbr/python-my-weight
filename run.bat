@echo off

rem Step 1: Activate Python virtual environment
call .venv/Scripts/activate

rem Step 2: Run Streamlit app
streamlit run app.py

rem Deactivate the virtual environment when the script exits
deactivate