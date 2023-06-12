def perform_monitoring():
         
    import streamlit as st

    st.header("Monitoring")
    st.write("Here is the reports of Dataset")
    # Path to your HTML file
    html_file_paths = [
        'Reports/DataQualityReport.html',
        'Reports/classification_performance_report.html',
        'Reports/data_drift.html',
        'Reports/data_quality.html',
        'Reports/num_target_drift_report.html'
    ]

    selected_file = st.selectbox("Select Monitoring HTML file", html_file_paths)
    return selected_file