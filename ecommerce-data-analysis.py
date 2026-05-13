# Ecommerce Dataset Summary & Professional Dashboard in Python

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# ==========================================
# LOAD DATA
# ==========================================
file_path = r"C:/Users/user/Downloads/ecommerce_powerbi_dataset.xlsx"

# Read Excel Sheet
Data = pd.read_excel(file_path, sheet_name='EcommerceData')

# ==========================================
# DISPLAY BASIC INFORMATION
# ==========================================
print("\n========== DATASET OVERVIEW ==========")
print(Data.head())

print("\n========== DATASET SHAPE ==========")
print(Data.shape)

print("\n========== COLUMN NAMES ==========")
print(Data.columns)

print("\n========== MISSING VALUES ==========")
print(Data.isnull().sum())

print("\n========== DATA TYPES ==========")
print(Data.dtypes)

print("\n========== STATISTICAL SUMMARY ==========")
print(Data.describe())

# ==========================================
# CONVERT DATE COLUMN
# ==========================================
Data['Order Date'] = pd.to_datetime(Data['Order Date'])

# ==========================================
# KPI VALUES
# ==========================================
Total_Sales = Data['Total_Amount'].sum()
Total_Orders = len(Data)
Total_Customers = Data['Customer_Name'].nunique()
Top_Category = Data.groupby('Category')['Total_Amount'].sum().idxmax()

print("\n========== BUSINESS SUMMARY ==========")
print(f"Total Sales      : ₹{Total_Sales:,.2f}")
print(f"Total Orders     : {Total_Orders}")
print(f"Total Customers  : {Total_Customers}")
print(f"Top Category     : {Top_Category}")

# ==========================================
# POWER BI STYLE THEME
# ==========================================
plt.style.use('dark_background')

mpl.rcParams['font.size'] = 11
mpl.rcParams['figure.facecolor'] = '#121212'
mpl.rcParams['axes.facecolor'] = '#1f1f2e'
mpl.rcParams['axes.edgecolor'] = 'white'
mpl.rcParams['axes.labelcolor'] = 'white'
mpl.rcParams['xtick.color'] = 'white'
mpl.rcParams['ytick.color'] = 'white'

# ==========================================
# CREATE FIGURE
# ==========================================
fig = plt.figure(figsize=(18, 10), constrained_layout=True)

# GRID LAYOUT
Grid = fig.add_gridspec(3, 4)

# KPI CARDS
ax_kpi1 = fig.add_subplot(Grid[0, 0])
ax_kpi2 = fig.add_subplot(Grid[0, 1])
ax_kpi3 = fig.add_subplot(Grid[0, 2])
ax_kpi4 = fig.add_subplot(Grid[0, 3])

# CHARTS
ax1 = fig.add_subplot(Grid[1, 0:2])
ax2 = fig.add_subplot(Grid[1, 2:4])
ax3 = fig.add_subplot(Grid[2, :])

# ==========================================
# KPI CARD FUNCTION
# ==========================================
def KPI_CARD(ax, title, value, color):

    ax.set_facecolor('#242444')

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xticks([])
    ax.set_yticks([])

    ax.text(
        0.05,
        0.65,
        title,
        fontsize=14,
        color='lightgray',
        transform=ax.transAxes
    )

    ax.text(
        0.05,
        0.25,
        value,
        fontsize=22,
        fontweight='bold',
        color=color,
        transform=ax.transAxes
    )

# ==========================================
# DISPLAY KPI CARDS
# ==========================================
KPI_CARD(ax_kpi1, "Total Sales", f"₹ {Total_Sales:,.0f}", '#00FFB3')
KPI_CARD(ax_kpi2, "Total Orders", f"{Total_Orders}", '#4DA6FF')
KPI_CARD(ax_kpi3, "Customers", f"{Total_Customers}", '#FFD700')
KPI_CARD(ax_kpi4, "Top Category", f"{Top_Category}", '#FF6B6B')

# ==========================================
# CHART 1 : CATEGORY SALES
# ==========================================
Category_Sales = (
    Data.groupby('Category')['Total_Amount']
    .sum()
    .sort_values(ascending=False)
)

bars = ax1.bar(
    Category_Sales.index,
    Category_Sales.values,
    edgecolor='white',
    linewidth=1.5
)

ax1.set_title(
    'Category Wise Sales',
    fontsize=16,
    fontweight='bold'
)

ax1.tick_params(axis='x', rotation=20)

# VALUE LABELS
for bar in bars:

    value = bar.get_height()

    ax1.text(
        bar.get_x() + bar.get_width()/2,
        value,
        f'{value:,.0f}',
        ha='center',
        va='bottom',
        fontsize=9
    )

# ==========================================
# CHART 2 : PAYMENT METHOD SHARE
# ==========================================
Payment_Data = Data['Payment Method'].value_counts()

ax2.pie(
    Payment_Data.values,
    labels=Payment_Data.index,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={
        'edgecolor':'white',
        'linewidth':1
    }
)

ax2.set_title(
    'Payment Method Distribution',
    fontsize=16,
    fontweight='bold'
)

# ==========================================
# CHART 3 : MONTHLY SALES TREND
# ==========================================
Data['Month'] = Data['Order Date'].dt.strftime('%b')

Monthly_Sales = (
    Data.groupby('Month')['Total_Amount']
    .sum()
)

Month_Order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

Monthly_Sales = Monthly_Sales.reindex(Month_Order)

ax3.plot(
    Monthly_Sales.index,
    Monthly_Sales.values,
    marker='o',
    linewidth=3,
    markersize=8
)

ax3.fill_between(
    Monthly_Sales.index,
    Monthly_Sales.values,
    alpha=0.2
)

ax3.set_title(
    'Monthly Sales Trend',
    fontsize=16,
    fontweight='bold'
)

ax3.set_xlabel('Month')
ax3.set_ylabel('Sales Amount')

ax3.grid(True, linestyle='--', alpha=0.3)

# ==========================================
# MAIN TITLE
# ==========================================
fig.suptitle(
    'ECOMMERCE SALES DASHBOARD',
    fontsize=24,
    fontweight='bold',
    color='white'
)

# ==========================================
# SHOW DASHBOARD
# ==========================================
plt.show()


