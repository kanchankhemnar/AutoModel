import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import io

def profile_data(dataset):
    if dataset is not None:
        st.subheader("📊 Automated Data Profiling")

        # Basic Info
        st.info("#### 🧾 Dataset Info Summary")

        st.markdown(f"""
        - **Number of rows:** `{dataset.shape[0]}`
        - **Number of columns:** `{dataset.shape[1]}`
        - **Column Names:** `{', '.join(dataset.columns)}`
        """)

        # Data types and nulls as a mini dataframe
        st.info("####  🧩 Column-wise Details")
        info_df = pd.DataFrame({
            "column name":dataset.columns,
            "Data Type": dataset.dtypes,
            "Missing Values": dataset.isnull().sum(),
            "Non-Null Count": dataset.notnull().sum()
        })
        st.dataframe(info_df,hide_index=True)

        # Data types pie chart
        st.markdown("### 🧬 Column Data Types")
        dtype_counts = dataset.dtypes.value_counts()
        fig2, ax2 = plt.subplots(figsize=(4.5, 1.5))
        ax2.pie(dtype_counts, labels=dtype_counts.index.astype(str), autopct='%1.1f%%', startangle=90, textprops={'fontsize': 4})
        ax2.axis("equal")
        st.pyplot(fig2)

        # Null value heatmap
        st.markdown("#### 🔍 Missing Values")
        null_counts = dataset.isnull().sum()
        if null_counts.sum() > 0:
            fig1, ax1 = plt.subplots(figsize=(4.5,2))
            null_counts[null_counts > 0].plot(kind='bar', color='salmon', ax=ax1)
            ax1.set_ylabel("Count", fontsize=8)
            ax1.set_title("Missing Values per Column", fontsize=10)
            ax1.tick_params(axis='x', labelrotation=0, labelsize=7)
            ax1.tick_params(axis='y', labelsize=7)
            st.pyplot(fig1)
        else:
            st.success("✅ No missing values found in the dataset!")




        st.info("#### 📐 Statistical Summary")
        st.write(dataset.describe())


        # Distribution plots
        st.markdown("#### 📈 Distribution of Numerical Features")
        num_cols = dataset.select_dtypes(include=['int64', 'float64']).columns
        for col in num_cols:
            fig3, ax3 = plt.subplots(figsize=(4.5, 1.8))
            sns.histplot(dataset[col].dropna(), kde=True, ax=ax3, color='skyblue')
            ax3.set_title(f"Distribution of {col}", fontsize=5)
            ax3.set_xlabel(col, fontsize=7)
            ax3.set_ylabel("Count", fontsize=7)
            ax3.tick_params(axis='x', labelsize=5)
            ax3.tick_params(axis='y', labelsize=5)
            st.pyplot(fig3)

        # Correlation heatmap
        st.markdown("#### 🧠 Correlation Heatmap")
        corr = dataset[num_cols].corr()
        fig4, ax4 = plt.subplots(figsize=(4.5, 2))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax4, annot_kws={"size": 6})
        ax4.set_title("Feature Correlation Matrix", fontsize=9)
        st.pyplot(fig4)

    else:
        st.warning("⬆️ Please upload a dataset in the Upload section first.")
