import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import pandas as pd

def save_trade():
    try:
        # Get values from the entry fields
        trade_date = entry_date.get()
        trade_pair = entry_pair.get()
        trade_direction = entry_direction.get()
        entry_price = entry_entry_price.get()
        exit_price = entry_exit_price.get()
        position_size = entry_position_size.get()
        stop_loss = entry_stop_loss.get()
        take_profit = entry_take_profit.get()
        reasons = entry_reasons.get("1.0", tk.END)
        market_conditions = entry_market_conditions.get("1.0", tk.END)
        emotional_state = entry_emotional_state.get()
        outcome = entry_outcome.get()
        lessons_learned = entry_lessons_learned.get("1.0", tk.END)

        # Create a dictionary with trade details
        trade_entry = {
            "Trade Date": trade_date,
            "Currency/Stock Pair": trade_pair,
            "Trade Direction": trade_direction,
            "Entry Price": entry_price,
            "Exit Price": exit_price,
            "Position Size": position_size,
            "Stop Loss": stop_loss,
            "Take Profit": take_profit,
            "Reasons for the Trade": reasons.strip(),
            "Market Conditions": market_conditions.strip(),
            "Emotional State": emotional_state,
            "Trade Outcome": outcome,
            "Lessons Learned": lessons_learned.strip()
        }

        # Append the entry to the journal list
        trading_journal.append(trade_entry)

        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(trading_journal)

        # Save the DataFrame to an Excel file
        df.to_excel("trading_journal.xlsx", index=False)

        # Show a success message
        messagebox.showinfo("Success", "Trade entry saved successfully!\nData exported to Excel file.")

        # Clear the entry fields for the next trade
        clear_entries()

    except Exception as e:
        # Show an error message
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def clear_entries():
    entry_date.delete(0, tk.END)
    entry_pair.delete(0, tk.END)
    entry_direction.delete(0, tk.END)
    entry_entry_price.delete(0, tk.END)
    entry_exit_price.delete(0, tk.END)
    entry_position_size.delete(0, tk.END)
    entry_stop_loss.delete(0, tk.END)
    entry_take_profit.delete(0, tk.END)
    entry_reasons.delete("1.0", tk.END)
    entry_market_conditions.delete("1.0", tk.END)
    entry_emotional_state.delete(0, tk.END)
    entry_outcome.delete(0, tk.END)
    entry_lessons_learned.delete("1.0", tk.END)

# Create the main window
app = tk.Tk()
app.title("Trading Journal App")

# Apply a themed style
style = ttk.Style()
style.theme_use("clam")

# Create and place entry fields and labels
labels = ["Trade Date", "Currency/Stock Pair", "Trade Direction", "Entry Price",
          "Exit Price", "Position Size", "Stop Loss", "Take Profit",
          "Reasons for the Trade", "Market Conditions", "Emotional State",
          "Trade Outcome", "Lessons Learned"]

for i, label_text in enumerate(labels):
    label = ttk.Label(app, text=label_text)
    label.grid(row=i, column=0, padx=5, pady=5, sticky="e")

entry_date = ttk.Entry(app)
entry_date.grid(row=0, column=1, padx=5, pady=5)
entry_date.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

entry_pair = ttk.Entry(app)
entry_pair.grid(row=1, column=1, padx=5, pady=5)

entry_direction = ttk.Entry(app)
entry_direction.grid(row=2, column=1, padx=5, pady=5)

entry_entry_price = ttk.Entry(app)
entry_entry_price.grid(row=3, column=1, padx=5, pady=5)

entry_exit_price = ttk.Entry(app)
entry_exit_price.grid(row=4, column=1, padx=5, pady=5)

entry_position_size = ttk.Entry(app)
entry_position_size.grid(row=5, column=1, padx=5, pady=5)

entry_stop_loss = ttk.Entry(app)
entry_stop_loss.grid(row=6, column=1, padx=5, pady=5)

entry_take_profit = ttk.Entry(app)
entry_take_profit.grid(row=7, column=1, padx=5, pady=5)

entry_reasons = tk.Text(app, height=5, width=40)
entry_reasons.grid(row=8, column=1, padx=5, pady=5)

entry_market_conditions = tk.Text(app, height=5, width=40)
entry_market_conditions.grid(row=9, column=1, padx=5, pady=5)

entry_emotional_state = ttk.Entry(app)
entry_emotional_state.grid(row=10, column=1, padx=5, pady=5)

entry_outcome = ttk.Entry(app)
entry_outcome.grid(row=11, column=1, padx=5, pady=5)

entry_lessons_learned = tk.Text(app, height=5, width=40)
entry_lessons_learned.grid(row=12, column=1, padx=5, pady=5)

# Create and place buttons
save_button = ttk.Button(app, text="Save Trade", command=save_trade)
save_button.grid(row=13, column=0, columnspan=2, pady=10)

clear_button = ttk.Button(app, text="Clear Entries", command=clear_entries)
clear_button.grid(row=14, column=0, columnspan=2, pady=10)

# Create an empty list to store trade entries
trading_journal = []

# Run the app
app.mainloop()
