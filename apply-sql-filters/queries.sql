SELECT *
FROM login_activity
WHERE login_type = 'failed_login'
AND login_time NOT BETWEEN '08:00:00' AND '17:00:00';
