# AWS IAM Hardening — Custom Password Policy

## Objective
Implement a custom AWS IAM password policy to strengthen identity security and reduce risk of weak credentials.

## Background
Weak password policies increase exposure to:
- Brute force attacks
- Credential stuffing
- Password spraying
- Long-lived compromised credentials

This project demonstrates baseline identity hardening in AWS.

---

## Configuration Steps

Navigated to:

IAM → Account Settings → Edit Password Policy

Configured the following controls:

- Custom password policy enabled
- Minimum length requirement enforced
- Uppercase, lowercase, numeric, and special character requirements enabled
- Password expiration enabled
- Password reuse prevention enabled
- Users allowed to change their own passwords
- ---

## Evidence

### IAM Account Settings

![IAM Account Settings](P2%20Pw%20Policy1.png)

### Custom Password Policy

![Custom Password Policy](P2%20Pw%20Policy2.png)

---

## Security Impact

This configuration strengthens authentication controls and reduces the likelihood of compromised credentials being reused or exploited.

---

## Next Steps

- Enforce MFA for IAM users
- Enable CloudTrail logging
- Monitor configuration changes using AWS Config
