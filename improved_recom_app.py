import streamlit as st
from improved_model import get_storage_report
import time

# Configure page settings
st.set_page_config(
    page_title="FarmConnect Analytics",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
    <style>
    .main {background-color: #FFF0D1;}
    h1 {color: #FFF0D1;}
    .stButton>button {background-color: #664343; color: white;}
    .stTextInput>div>div>input {border: 2px solid #664343;}
    .report-header {color: #FFF0D1;}
    .highlight {background-color: #FFF0D1; padding: 15px; border-radius: 10px;}
    body {color: #FFF0D1;}
    </style>
    """, unsafe_allow_html=True)

# App header
st.markdown("# 🌱 Crop Storage Intelligence System")
st.markdown("### Optimized Preservation Strategies for Agricultural Products")

# Sidebar with information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This system provides comprehensive storage recommendations for agricultural products based on:
    - Optimal temperature ranges
    - Humidity requirements
    - Pest control measures
    - Preservation best practices
    """)
    st.markdown("---")
    st.markdown("**Supported crops:**\n- Grains (wheat, rice, corn)\n- Legumes\n- Tubers\n- Commercial crops")
    st.markdown("---")
    st.markdown("📧 Contact: info@farmconnect.com")

# Main content area
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        crop_name = st.text_input(
            "Enter Crop Name:",
            placeholder="e.g., Wheat, Rice, Potatoes...",
            help="Enter the name of the crop you need storage information for"
        )
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        generate_btn = st.button("Generate Report 🚀")

# Report generation section
if generate_btn:
    if not crop_name:
        st.toast("⚠️ Please enter a crop name", icon="⚠️")
        st.warning("Please enter a crop name to generate the report")
    else:
        with st.spinner(f"Analyzing storage requirements for {crop_name}..."):
            try:
                start_time = time.time()
                report = get_storage_report(crop_name)
                processing_time = time.time() - start_time
                
                st.success(f"Report generated in {processing_time:.2f} seconds!")
                st.toast("Report ready!", icon="✅")
                
                # Display report with enhanced formatting
                with st.expander(f"📑 Full Storage Report for {crop_name.capitalize()}", expanded=True):
                    st.markdown(f"## 📊 {crop_name.capitalize()} Storage Analysis")
                    st.markdown("---")
                    
                    # Assuming the report is a dictionary with structured data
                    st.subheader("🌡️ Optimal Storage Conditions")
                    st.markdown(f"""
                    - **Temperature Range:** {report['temperature']}
                    - **Humidity Level:** {report['humidity']}
                    - **Ventilation Requirements:** {report['ventilation']}
                    """)
                    
                    st.subheader("🛡️ Preservation Guidelines")
                    st.markdown(f"""
                    - **Container Type:** {report['container']}
                    - **Max Storage Duration:** {report['duration']}
                    - **Quality Preservation Tips:**  
                      {report['preservation_tips']}
                    """)
                    
                    st.subheader("⚠️ Risk Factors")
                    st.markdown(f"""
                    - **Common Pests:** {report['pests']}
                    - **Disease Prevention:** {report['disease_prevention']}
                    - **Critical Warning Signs:**  
                      {report['warning_signs']}
                    """)
                    
                    # Add download button
                    report_text = f"Storage Report for {crop_name}\n\n" + "\n".join(
                        [f"{k}: {v}" for k, v in report.items()])
                    
                    st.download_button(
                        label="Download Report 📥",
                        data=report_text,
                        file_name=f"{crop_name}_storage_report.txt",
                        mime="text/plain"
                    )
                
                # Additional recommendations
                st.markdown("---")
                with st.container():
                    st.subheader("📌 Expert Recommendations")
                    st.markdown("""
                    - Regular quality inspections (bi-weekly recommended)
                    - Implement FIFO (First-In First-Out) inventory management
                    - Maintain detailed storage logs
                    - Conduct staff training on proper handling procedures
                    """)
                    
            except Exception as e:
                st.error(f"Error generating report: {str(e)}")
                st.toast("❌ Report generation failed", icon="❌")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #666;'>"
            "👨‍🌾 FarmConnect AI by Ali Umar"
            "</div>", unsafe_allow_html=True)