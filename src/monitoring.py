import streamlit as st

def perform_monitoring():
    st.header("Monitoring")
    st.write("Here are the reports of the Dataset")

    # Dictionary to store the file names and their corresponding paths
    html_files = {
        "Data Quality Report": "reports/dataqualityreport.html",
        "Classification Performance Report": "reports/classification_performance_report.html",
        "Data Drift Report": "reports/data_drift.html",
        "Data Quality Report 2": "reports/data_quality.html",
        "Num Target Drift Report": "reports/num_target_drift_report.html"
    }

    # Get the list of file names
    html_file_names = list(html_files.keys())

    # Use the file names as options in the selectbox
    selected_file_name = st.selectbox("Select Monitoring Report", html_file_names)

    # Get the selected file path based on the selected file name
    selected_file_path = html_files[selected_file_name]

    return selected_file_path
