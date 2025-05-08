import pandas as pd

data = pd.DataFrame({
    "Name": ["Sabri", "ChatGPT"],
    "Score": [100, 99]
})

print(data)


# main.py

"""
Main entry point for running the Sabri Insights utilities.
"""

from utils_sabri import main

# Run the main function from utils_sabri
main()
