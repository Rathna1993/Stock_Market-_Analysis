import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:\\Users\\Ashokmep\\Desktop\\Stock.csv")

# Print dataset
print(df)

# Create figure size
plt.figure(figsize=(10,5))

# Plot stock prices
plt.plot(
    df["Day"],
    df["Price"],
    marker='o',
    color='green',
    linewidth=3
)

# Add data labels
for i, value in enumerate(df["Price"]):

    plt.text(
        i,
        value,
        str(value),
        ha='center',
        fontsize=12
    )

# Title and labels
plt.title("Stock Market Analysis")

plt.xlabel("Days")
plt.ylabel("Stock Price")

# Grid
plt.grid(True)

# Show graph
plt.show()