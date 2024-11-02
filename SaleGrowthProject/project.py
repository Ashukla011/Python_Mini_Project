
import json
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  

# Load the JSON file
with open('data.json') as json_file:
    data = json.load(json_file)

regions = data['metadata']['regions']
sales = data['metadata']['sales']
growth = data['metadata']['growth']
# Check the structure of the data
print(data)  # Ensure the JSON data is correctly loaded

# Create the main application window
root = tk.Tk()
root.title("Data Visualization with JSON, Matplotlib & Seaborn")

# Global canvas variable
canvas = None  # Initialize it here as None so it's accessible in the functions

# Function to display bar chart using Matplotlib and Seaborn
def show_bar_chart():
    global canvas  # Declare canvas as global to modify it
    fig, ax = plt.subplots()
    sns.barplot(x=regions, y=sales, ax=ax)
    ax.set_title('Sales by Region')
    ax.set_xlabel('Regions')
    ax.set_ylabel('Sales')

    # Clear the previous plot and render the new one
    if canvas:  # Check if canvas is already defined to avoid errors
        canvas.get_tk_widget().pack_forget()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Function to display line chart using Matplotlib
def show_line_chart():
    global canvas  # Declare canvas as global to modify it
    fig, ax = plt.subplots()
    ax.plot(regions, growth, marker='o')
    ax.set_title('Growth by Region')
    ax.set_xlabel('Regions')
    ax.set_ylabel('Growth (%)')

    # Clear the previous plot and render the new one
    if canvas:  # Check if canvas is already defined to avoid errors
        canvas.get_tk_widget().pack_forget()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Frame to hold the plot
frame = tk.Frame(root)
frame.pack()

# Matplotlib canvas to display the charts (initially empty)
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=frame)  # Initialize the canvas once
canvas.draw()
canvas.get_tk_widget().pack()

# Dropdown menu to choose the chart type
chart_type = tk.StringVar(value="Bar Chart")
dropdown = ttk.Combobox(root, textvariable=chart_type, values=["Bar Chart", "Line Chart"])
dropdown.pack()

# Button to visualize data based on dropdown selection
def visualize_data():
    if chart_type.get() == "Bar Chart":
        show_bar_chart()
    elif chart_type.get() == "Line Chart":
        show_line_chart()

button = tk.Button(root, text="Visualize", command=visualize_data)
button.pack()

# Start the main loop of Tkinter
root.mainloop()

