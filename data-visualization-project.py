import matplotlib.pyplot as plt
import pandas as pd


months = ["Jan", "Feb", "Mar", "Apr"]
sales = [200, 250, 300, 280]
categories = ["A", "B", "C"]
cat_sales = [120, 180, 150]

plt.style.use("seaborn-v0_8-whitegrid")

fig, axs = plt.subplots(2, 2, figsize=(10, 6))


axs[0,0].plot(months, sales, linewidth=2.5)
axs[0,0].set_title("Monthly Sales")


axs[0,1].bar(categories, cat_sales)
axs[0,1].set_title("Category Sales")


axs[1,0].pie(cat_sales, labels=categories, autopct='%1.1f%%')
axs[1,0].set_title("Sales Distribution")


axs[1,1].axis("off")
axs[1,1].text(0.3, 0.5, "Total Sales\n₹1030", fontsize=14)

plt.tight_layout()
plt.show()
