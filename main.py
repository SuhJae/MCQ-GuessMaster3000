import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.font_manager import FontProperties
import math


def get_distribution_parameters(m, n):
    """Get mean and standard deviation for the distribution."""
    mean = m * (1 / n)
    variance = m * (1 / n) * (1 - 1 / n)
    std_dev = np.sqrt(variance)
    return mean, std_dev


def plot_distribution(m, n):
    """Plot the distribution of scores for MCQ in a modern minimalistic style using a custom font."""

    # Load the custom font
    font_path = "Inter-Regular.ttf"
    font = FontProperties(fname=font_path)

    mean, std_dev = get_distribution_parameters(m, n)

    # Generate x values
    x = np.linspace(0, m, 1000)

    # Compute the bell curve (PDF) for these x values
    y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

    # Setting up a modern minimalistic theme
    sns.set_style("white")

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, lw=2)

    # Highlight mean and standard deviations
    plt.axvline(x=mean, color='grey', linestyle='--', lw=1)
    plt.axvline(x=mean - std_dev, color='grey', linestyle='--', lw=1)
    plt.axvline(x=mean + std_dev, color='grey', linestyle='--', lw=1)

    # Label vertical lines
    plt.text(mean, max(y) * 1.05, 'Mean', horizontalalignment='center', fontproperties=font)
    plt.text(mean - std_dev, max(y) * 1.05, 'σ -1', horizontalalignment='center', fontproperties=font)
    plt.text(mean + std_dev, max(y) * 1.05, 'σ +1', horizontalalignment='center', fontproperties=font)

    plt.title("Distribution of Scores for Randomly Picking MCQ Answers", fontproperties=font)
    plt.xlabel("Score", fontproperties=font)
    plt.ylabel("Probability Density", fontproperties=font)
    plt.xticks(fontproperties=font)
    plt.yticks(fontproperties=font)

    # Set y-axis and x-axis limits to start from 0
    plt.ylim(0, max(y) * 1.1)
    plt.xlim(0, m)

    # Removing the spines for minimalism
    sns.despine()

    # Calculate probability of getting above 60% marks

    print("Mean: ", mean)
    print("Standard Deviation: ", std_dev.round(2))

    plt.savefig("plot.png", dpi=300)
    plt.show()


# Get input
m = int(input("Enter number of MCQ questions: "))
n = int(input("Enter number of choices in one question: "))
print("")

plot_distribution(m, n)
