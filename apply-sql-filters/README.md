# Apply filters to SQL queries

## Project Description

The goal of this project is to identify suspicious login attempts by filtering failed logins outside of business hours or on specific dates. The dataset is simulated and contains fabricated usernames, timestamps, and alerts.

## Skills Applied

* SQL querying
* Filtering data with `WHERE`, `AND`, and `BETWEEN`
* Simulated security analysis
* Pattern recognition in access logs

## Files Included

* `queries.sql` — Example SQL queries used in this analysis
* `screenshots/` — Screenshots of SQL output (optional)
* `README.md` — This documentation

---

## Retrieve after hours failed login attempts

There was a potential security incident that occurred after business hours (after 18:00). All after-hours login attempts that failed need to be investigated. The following code demonstrates how I created a SQL query to filter for failed login attempts that occurred after business hours.

![Failed logins after 18:00](https://github.com/k-roby/cybersecurity-portfolio/blob/main/apply-sql-filters/ca874e5a-a15c-47c6-a460-c486603e16f9.png)

This query filters for failed login attempts that occurred after 18:00. First, I selected all data from the `log_in_attempts` table. Then, I used a `WHERE` clause with an `AND` operator to filter my results to output only login attempts that occurred after 18:00 and were unsuccessful. The first condition is `login_time > '18:00'`, and the second is `success = FALSE`.

---

## Retrieve login attempts on specific dates

A suspicious event occurred on 2022-05-09. Any login activity that happened on 2022-05-09 or on the day before needs to be investigated.

![Logins on specific dates](https://github.com/k-roby/cybersecurity-portfolio/blob/main/apply-sql-filters/70ed22fa-9c8b-425b-aa18-487816e9cad1.png)

This query returns all login attempts that occurred on 2022-05-09 or 2022-05-08. I selected all data from the `log_in_attempts` table and used a `WHERE` clause with an `OR` operator to filter for both dates.

---

## Retrieve login attempts outside of Mexico

After investigating login attempts, I believed there was an issue with attempts outside of Mexico. These login attempts needed to be investigated.

![Logins outside Mexico](https://github.com/k-roby/cybersecurity-portfolio/blob/main/apply-sql-filters/439c0b21-1562-4446-bd09-5a02e323ac4b.png)

This query returned all login attempts that occurred in countries other than Mexico. I used `WHERE NOT` and `LIKE 'MEX%'` because the dataset lists Mexico as both `MEX` and `MEXICO`. The percent sign (%) is a wildcard.

---

## Retrieve employees in Marketing

The next step was to update computers for employees in the Marketing department in the East building. I needed to gather this employee information.

![Marketing in East offices](https://github.com/k-roby/cybersecurity-portfolio/blob/main/apply-sql-filters/378e005e-1986-414c-9b5a-a136bcea150d.png)

This query returns employees in the Marketing department and in the East building. I filtered the `employees` table with a `WHERE` clause using `AND`, with `department = 'Marketing'` and `office LIKE 'East%'`.

---

## Retrieve employees in Finance or Sales

Machines for employees in the Finance and Sales departments also needed to be updated.

![Finance or Sales](https://github.com/k-roby/cybersecurity-portfolio/blob/main/apply-sql-filters/2275a15d-16ff-4b4b-9251-a164ff87f6ac.png)

This query returns employees in either Finance or Sales. I used `department = 'Finance' OR department = 'Sales'` to pull employees from both departments.

---

## Retrieve all employees not in IT

I needed to make one more security update — but only for employees not in the Information Technology department.

![Not in IT](https://github.com/k-roby/cybersecurity-portfolio/blob/main/apply-sql-filters/0d3d7ed8-f803-4364-8d0e-5f1b487672c3.png)

This query returned employees from any department *except* Information Technology. I used `WHERE NOT department = 'Information Technology'`.

---

## Summary

I applied filters to SQL queries to get specific information on login attempts and employee machines in a simulated scenario. I used two different tables, `log_in_attempts` and `employees`. I used the `AND`, `OR`, and `NOT` operators to filter for the specific information needed for each task. I also used `LIKE` and the `%` wildcard to filter for patterns.
