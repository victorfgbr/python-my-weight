
# venv activation
python3 -m venv .venv
source .venv/Scripts/activate

# requirements
pip install pandas
pip install plotly
pip install streamlit

# run dash
streamlit run app.py