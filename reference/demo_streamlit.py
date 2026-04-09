# To run this app, execute the following command in your terminal:
# streamlit run reference/demo_streamlit.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Starbucks Ordering Patterns Analytics",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# CACHING FOR EFFICIENCY (Feature 4)
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    """Load the dataset and perform basic pre-processing."""
    # Read the data
    df = pd.read_csv("data/starbucks_customer_ordering_patterns.csv")
    # Convert dates to datetime objects for any time-series formatting if needed
    df['order_date'] = pd.to_datetime(df['order_date']).dt.date
    return df

# Load the cached data
df_main = load_data()

# -----------------------------------------------------------------------------
# LAYOUTS AND ORGANIZATION: Sidebar (Feature 3)
# -----------------------------------------------------------------------------
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Starbucks_Corporation_Logo_2011.svg/1200px-Starbucks_Corporation_Logo_2011.svg.png", width=100)
st.sidebar.title("App Controls")
st.sidebar.markdown("Use the filters below to shape the analysis.")

# -----------------------------------------------------------------------------
# INTERACTIVE WIDGETS (Feature 2)
# -----------------------------------------------------------------------------
# Filter by Regions
all_regions = df_main['region'].unique().tolist()
selected_regions = st.sidebar.multiselect(
    "Select Regions", 
    options=all_regions, 
    default=all_regions
)

# Filter by Order Channel
all_channels = df_main['order_channel'].unique().tolist()
selected_channels = st.sidebar.multiselect(
    "Select Order Channels", 
    options=all_channels, 
    default=all_channels
)

# Slider for Total Spend
min_spend, max_spend = float(df_main['total_spend'].min()), float(df_main['total_spend'].max())
spend_range = st.sidebar.slider(
    "Filter by Total Spend Range ($)", 
    min_value=min_spend, 
    max_value=max_spend, 
    value=(min_spend, max_spend)
)

# Apply filters
df = df_main[
    (df_main['region'].isin(selected_regions)) & 
    (df_main['order_channel'].isin(selected_channels)) &
    (df_main['total_spend'] >= spend_range[0]) & 
    (df_main['total_spend'] <= spend_range[1])
]

# -----------------------------------------------------------------------------
# DISPLAYING DATA AND TEXT (Feature 1) & MAIN DASHBOARD
# -----------------------------------------------------------------------------
st.title("☕ Starbucks Customer Ordering Patterns")
st.markdown("""
**Welcome to the Starbucks Analytics Dashboard!** 
This app showcases Streamlit's awesome capabilities including data caching, 
dynamic layouts, interactive filtering, and comprehensive data visualizations.
""")

# Layouts: Columns for top-level metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Total Orders", value=f"{len(df):,}")
with col2:
    st.metric(label="Avg Total Spend", value=f"${df['total_spend'].mean():.2f}")
with col3:
    st.metric(label="Avg Satisfaction (1-5)", value=f"{df['customer_satisfaction'].mean():.2f}")
with col4:
    st.metric(label="Avg Fulfillment (mins)", value=f"{df['fulfillment_time_min'].mean():.1f}")

st.markdown("---")

# Layouts: Tabs to organize content cleanly
tab1, tab2 = st.tabs(["📊 Data Overview & EDA", "📈 Visualizations"])

with tab1:
    st.header("Dataset Overview")
    st.markdown("Here is the raw data matching your sidebar filters (note that pagination may be slow):")
    
    # Pagination
    page_size = 100
    total_pages = max(1, (len(df) - 1) // page_size + 1)
    page = st.number_input("Page", min_value=1, max_value=total_pages, value=1)
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    
    # Displaying the dataframe
    st.dataframe(df.iloc[start_idx:end_idx], width='stretch')
    
    st.subheader("Data Description")
    st.write("Summary statistics for continuous variables:")
    st.dataframe(df.describe())

with tab2:
    st.header("Data Explorations")
    # -----------------------------------------------------------------------------
    # VISUALIZATIONS (Feature 5) with Matplotlib
    # -----------------------------------------------------------------------------
    
    st.markdown("### Customer Segments & Popularity")
    viz_col1, viz_col2 = st.columns(2)
    
    with viz_col1:
        # Plot 1: How does Cart Size affect Total Spend?
        st.write("**1. How does Cart Size affect Total Spend?**")
        st.markdown("_Takeaway: Total spend scales linearly with cart size, as one would naturally expect._")
        
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        spend_cart = df.groupby('cart_size')['total_spend'].agg(['mean', 'std'])
        ax1.plot(spend_cart.index, spend_cart['mean'], color='#00704A', marker='o', linewidth=2)
        ax1.fill_between(spend_cart.index, spend_cart['mean'] - spend_cart['std'], spend_cart['mean'] + spend_cart['std'], alpha=0.2, color='#00704A')
        
        ax1.set_ylabel('Average Total Spend ($)')
        ax1.set_xlabel('Cart Size (Number of Items)')
        ax1.grid(axis='y', linestyle='--', alpha=0.7)
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        st.pyplot(fig1)

    with viz_col2:
        # Plot 2: Average Spend by Member Status
        st.write("**2. Do Rewards Members spend more?**")
        st.markdown("_Takeaway: Rewards members consistently output higher average carts than non-members._")
        
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        spend_member = df.groupby('is_rewards_member')['total_spend'].agg(['mean', 'std'])
        # Barplot mapping True/False to labels
        ax2.bar(['Non-Member', 'Rewards Member'], spend_member['mean'], yerr=spend_member['std'], capsize=5, color=['#1e3932', '#00704A'], edgecolor='black')
        ax2.set_ylabel('Average Total Spend ($)')
        ax2.grid(axis='y', linestyle='--', alpha=0.7)
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        st.pyplot(fig2)
        
    st.markdown("---")
    st.markdown("### Wait Times & Operational Efficiency")
    viz_col3, viz_col4 = st.columns(2)
    
    with viz_col3:
        # Plot 3: Impact of Customizations on Wait Times
        st.write("**3. How do customizations affect wait time?**")
        st.markdown("_Takeaway: Adding additional flavors or syrups does not penalize fulfillment time._")
        
        fig3, ax3 = plt.subplots(figsize=(6, 4))
        cust_time = df.groupby('num_customizations')['fulfillment_time_min'].agg(['mean', 'std'])
        ax3.plot(cust_time.index, cust_time['mean'], marker='o', color='#e03a3e', linewidth=2)
        ax3.fill_between(cust_time.index, cust_time['mean'] - cust_time['std'], cust_time['mean'] + cust_time['std'], alpha=0.2, color='#e03a3e')
        
        ax3.set_xlabel('Number of Customizations')
        ax3.set_ylabel('Average Wait Time (mins)')
        ax3.grid(axis='y', linestyle='--', alpha=0.7)
        ax3.set_xticks(cust_time.index)
        ax3.spines['top'].set_visible(False)
        ax3.spines['right'].set_visible(False)
        st.pyplot(fig3)

    with viz_col4:
        # Plot 4: Does food slow down orders?
        st.write("**4. Does adding food slow down the Drive-Thru?**")
        st.markdown("_Takeaway: Drive-thru lines spike dramatically when customers order food._")
        
        fig4, ax4 = plt.subplots(figsize=(6, 4))
        food_time_mean = df.pivot_table(index='order_channel', columns='has_food_item', values='fulfillment_time_min', aggfunc='mean')
        food_time_std = df.pivot_table(index='order_channel', columns='has_food_item', values='fulfillment_time_min', aggfunc='std')
        food_time_mean.plot(kind='bar', yerr=food_time_std, color=['#d4e9e2', '#00704A'], edgecolor='black', ax=ax4, capsize=4)
        ax4.set_ylabel('Avg Wait Time (mins)')
        ax4.set_xlabel('Order Channel')
        ax4.legend(title='Has Food Item?', labels=['No', 'Yes'], loc='upper left', bbox_to_anchor=(1, 1))
        ax4.grid(axis='y', linestyle='--', alpha=0.7)
        ax4.spines['top'].set_visible(False)
        ax4.spines['right'].set_visible(False)
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig4)

    st.markdown("---")
    st.markdown("### Customer Satisfaction & Trends")
    viz_col5, viz_col6 = st.columns(2)
        
    with viz_col5:
        # Plot 5: Satisfaction vs Average Wait Time
        st.write("**5. How long is too long to wait?**")
        st.markdown("_Takeaway: Customer satisfaction exhibits a slight, gradual decline as wait times increase, but remains relatively stable overall._")
        
        fig5, ax5 = plt.subplots(figsize=(6, 4))
        bucket_bins = [0, 2, 4, 6, 8, 15]
        # Copy to avoid setting with copy warning
        df_cut = df.copy()
        df_cut['wait_bucket'] = pd.cut(df_cut['fulfillment_time_min'], bins=bucket_bins, labels=['<2m', '2-4m', '4-6m', '6-8m', '>8m'])
        sat_wait = df_cut.groupby('wait_bucket', observed=False)['customer_satisfaction'].agg(['mean', 'std'])
        
        ax5.plot(sat_wait.index, sat_wait['mean'], color='#00704A', marker='s', linestyle='-', linewidth=2)
        ax5.fill_between(sat_wait.index, sat_wait['mean'] - sat_wait['std'], sat_wait['mean'] + sat_wait['std'], alpha=0.2, color='#00704A')
        ax5.set_ylim(1, 5)
        ax5.set_ylabel('Average Satisfaction (1-5)')
        ax5.set_xlabel('Wait Time Buckets')
        ax5.grid(axis='y', linestyle='--', alpha=0.7)
        ax5.spines['top'].set_visible(False)
        ax5.spines['right'].set_visible(False)
        st.pyplot(fig5)
        
    with viz_col6:
        # Plot 6: Orders by Hour
        st.write("**6. When do people order the most?**")
        st.markdown("_Takeaway: Order volumes spike during the early morning rush and see a significant secondary peak in the late afternoon._")
        
        fig6, ax6 = plt.subplots(figsize=(6, 4))
        
        # Get hours as integers properly
        df_cut['order_hour'] = pd.to_datetime(df_cut['order_time'], format='mixed').dt.hour
            
        hour_counts = df_cut['order_hour'].value_counts().sort_index()
        
        ax6.plot(hour_counts.index, hour_counts.values, color='#ffc519', marker='o')
        ax6.fill_between(hour_counts.index, hour_counts.values, alpha=0.4, color='#ffc519')
        ax6.set_xlabel('Hour of Day (24H)')
        ax6.set_ylabel('Total Number of Orders')
        ax6.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Format the x-axis to look like neat hours
        ax6.set_xticks(range(0, 24, 3))
        ax6.spines['top'].set_visible(False)
        ax6.spines['right'].set_visible(False)
        st.pyplot(fig6)