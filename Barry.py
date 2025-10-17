import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# App Title and Description
st.set_page_config(page_title="Barry's Bar Chart App", layout="wide")
st.title("📊 Barry's Bar Chart App")
st.markdown("""
Welcome to **Barry's Bar Chart App**! 🎉  
This app allows you to create beautiful bar charts either by manually entering data or uploading a CSV file.  
Get started by selecting an input method from the sidebar! 🚀
""")

# Sidebar for Input Selection
st.sidebar.header("Input Options")
mode = st.sidebar.radio("Select input method:", ["Manual Input", "Upload CSV File"])

# Manual Input Mode
if mode == "Manual Input":
    st.subheader("Manual Input")
    st.markdown("Enter your data for the **x-axis** and **y-axis** below (comma-separated).")
    x_input = st.text_input("Enter x-axis values (e.g., 1, 2, 3):")
    y_input = st.text_input("Enter y-axis values (e.g., 10, 20, 30):")

    if st.button("Plot Bar Chart", key='bar_chart_manual'):
        try:
            x = [float(i) for i in x_input.split(",")]
            y = [float(i) for i in y_input.split(",")]

            if len(x) == len(y):
                fig, ax = plt.subplots(figsize=(8, 5))
                ax.bar(x, y, color='blue')
                ax.set_title("Bar Chart", fontsize=16, fontweight='bold')
                ax.set_xlabel("X-Axis", fontsize=12)
                ax.set_ylabel("Y-Axis", fontsize=12)
                ax.grid(axis='y', linestyle='--', alpha=0.5)
                st.pyplot(fig)
            else:
                st.error("❌ The number of x and y values must be the same.")
        except ValueError:
            st.error("❌ Please enter valid numeric values for both axes, separated by commas.")

# CSV Upload Mode
elif mode == "Upload CSV File":
    st.subheader("Upload CSV File")
    st.markdown("Upload a CSV file with **two columns**: one for the x-axis and one for the y-axis.")
    file_upload = st.file_uploader("Upload your CSV file", type=["csv"])

    if file_upload:
        try:
            df = pd.read_csv(file_upload)
            st.write("📄 **Preview of Uploaded File:**")
            st.dataframe(df)

            if df.shape[1] < 2:
                st.error("❌ The uploaded CSV file must have at least two columns.")
            else:
                if st.button("Plot Bar Chart", key='bar_chart_csv'):
                    try:
                        x = df.iloc[:, 0]
                        y = df.iloc[:, 1]

                        fig, ax = plt.subplots(figsize=(8, 5))
                        ax.bar(x, y, color='lightgreen')
                        ax.set_title("Bar Chart from CSV", fontsize=16, fontweight='bold')
                        ax.set_xlabel("X-Axis", fontsize=12)
                        ax.set_ylabel("Y-Axis", fontsize=12)
                        ax.grid(axis='y', linestyle='--', alpha=0.5)
                        st.pyplot(fig)
                    except Exception as e:
                        st.error(f"❌ An error occurred while plotting the chart: {e}")
        except Exception as e:
            st.error(f"❌ Failed to read the uploaded file: {e}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Barry")
