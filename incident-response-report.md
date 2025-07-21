# INCIDENT RESPONSE FINAL REPORT

## Executive Summary

The organization experienced a security incident on **October 29th, 2024, at 8:36 a.m., EST**, when a malicious actor was able to gain unauthorized access to customer personal identifiable information (PII) and financial information. Approximately **60,000 customer records** were affected. The financial impact of the incident is estimated to be **$140,000** in direct costs and potential loss of revenue. The incident is now closed and a thorough investigation has been conducted.

---

## Timeline

At approximately **2:26 p.m., EST, on October 23, 2024**, an employee received an email from an external email address. The email sender claimed they had successfully stolen customer data. In exchange for not releasing the data to public forums, the sender demanded a **$30,000 payment in cryptocurrency**. The employee assumed the email was spam and deleted it.

On **October 29, 2024**, the same employee received another email from the same sender. This email included a sample of the stolen customer data and an increased payment demand of **$60,000**.

After receiving the second email on October 29, the employee immediately notified the security team, who began their investigation into the incident. Between **October 29 and October 31, 2024**, the security team concentrated on determining how the data was stolen and the extent of the theft.

---

## Investigation

The security team received the alert and traveled on-site to begin the investigation.

The root cause of the incident was identified as a **vulnerability in the e-commerce web application**, which allowed the attacker to perform a **forced browsing attack** and access customer transaction data by modifying the order number included in the URL string of a purchase confirmation page. This vulnerability allowed the attacker to access customer purchase confirmation pages, exposing customer data, which the attacker then collected and exfiltrated.

After confirming the web application vulnerability, the security team analyzed the web application access logs. The logs indicated the attacker accessed the information of thousands of purchase confirmation pages.

---

## Response and Remediation

The organization collaborated with the public relations department to disclose the data breach to its customers. Additionally, the organization offered **free identity protection services** to customers affected by the incident.

After the security team reviewed the associated web server logs, the cause of the attack was clear. There was a single log source showing an exceptionally high volume of sequentially listed customer orders.

---

## Recommendations

To prevent future recurrences, we are taking the following actions:

- Perform routine **vulnerability scans** and **penetration testing**.
- Implement the following access control mechanisms:
  - **Allowlisting** to allow access to a specified set of URLs and automatically block all requests outside of this URL range.
  - Use the **principle of least privilege**, ensuring only authenticated users are authorized to access content.
