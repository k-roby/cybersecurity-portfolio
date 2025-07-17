# Apply Filters to SQL Queries

This project demonstrates how to use SQL filters to retrieve specific security-related login events from a simulated employee activity database. It was completed as part of the Google Cybersecurity Certificate program.

## 🔍 Project Description

The goal of this project is to identify suspicious login attempts by filtering failed logins outside of business hours or on specific dates. The dataset is simulated and contains fabricated usernames, timestamps, and alerts.

## 🛠️ Skills Applied

- SQL querying
- Filtering data with `WHERE`, `AND`, and `BETWEEN`
- Simulated security analysis
- Pattern recognition in access logs

## 📁 Files Included

- `queries.sql` — Example SQL queries used in this analysis
- `screenshots/` — Screenshots of SQL output (optional)
- `README.md` — This documentation

## 🖼️ Sample Query

```sql
SELECT *
FROM login_activity
WHERE event_type = 'failed_login'
  AND login_time NOT BETWEEN '08:00:00' AND '17:00:00';
