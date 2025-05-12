"""
Main entry point for running the Sabri Insights utilities.
"""

from utils_sabri import (
    get_byline,
    has_international_clients,
    get_years_in_operation,
    get_skills,
    get_satisfaction_scores,
    get_summary_stats
)

# Run the Sabri Insights report
print(get_byline())
print(f"Has International Clients: {has_international_clients()}")
print(f"Years in Operation: {get_years_in_operation()}")
print(f"Skills Offered: {get_skills()}")

scores = get_satisfaction_scores()
print(f"Client Satisfaction Scores: {scores}")

mean, std = get_summary_stats(scores)
print(f"Mean Satisfaction Score: {mean:.2f}")
print(f"Standard Deviation: {std:.2f}")
