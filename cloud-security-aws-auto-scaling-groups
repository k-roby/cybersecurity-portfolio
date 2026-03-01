# Implementing High Availability with Auto Scaling Groups (ASG)

## Project Overview

This project demonstrates how to implement high availability and scalability in AWS using:

- EC2 Launch Templates
- Auto Scaling Groups (ASG)
- Application Load Balancer (ALB)
- Multi–Availability Zone deployment

The goal is to ensure that application instances are automatically distributed across Availability Zones and can scale within defined capacity limits.

---

## Architecture Components

- Amazon EC2
- Launch Template
- Auto Scaling Group
- Application Load Balancer
- Target Group
- Multi-AZ Subnets (us-east-2a, us-east-2b, us-east-2c)

---

# Step-by-Step Implementation

---

## Step 1 – Create Auto Scaling Group

Created a new Auto Scaling Group named **DemoASG** and selected an existing Launch Template.

![Step 1 – Create Auto Scaling Group](./P7%20ASG1.png)

---

## Step 2 – Create Launch Template

Created a Launch Template named **DemoLaunchTemplate**.

Key configurations:
- Instance type: `t3.micro`
- Security group attached
- Key pair configured
- Auto Scaling guidance enabled

![Step 2 – Create Launch Template](./P7%20ASG%202.png)

---

## Step 3 – Confirm Launch Template Creation

Verified that the Launch Template was successfully created and assigned a Launch Template ID.

![Step 3 – Confirm Launch Template](./P7ASG3.png)

---

## Step 4 – Choose Instance Launch Options (Part 1)

Selected:
- Launch Template: DemoLaunchTemplate
- Default version
- VPC configuration

![Step 4 – Choose Instance Launch Options (1)](./P7ASG4.png)

---

## Step 5 – Choose Instance Launch Options (Part 2)

Configured:
- VPC
- Subnets across multiple Availability Zones
- Network settings

This ensures high availability across zones.

![Step 5 – Choose Instance Launch Options (2)](./P7ASG5.png)

---

## Step 6 – Integrate with Other Services (Part 1)

Integrated the Auto Scaling Group with:

- Existing Application Load Balancer
- Target Group: `demo-tg-alb`

This distributes incoming traffic across EC2 instances.

![Step 6 – Integrate with Other Services (1)](./P7%20ASG6.png)

---

## Step 7 – Integrate with Other Services (Part 2)

Enabled:
- Elastic Load Balancing health checks
- Health check grace period: 300 seconds
- Balanced best effort Availability Zone distribution

Unhealthy instances will be automatically replaced.

![Step 7 – Integrate with Other Services (2)](./P7%20ASG7.png)

---

## Step 8 – Configure Group Size and Scaling

Defined scaling configuration:

- Desired capacity: 1
- Minimum capacity: 1
- Maximum capacity: 4

This allows horizontal scaling within defined limits.

![Step 8 – Configure Group Size and Scaling](./P7%20ASG8.png)

---

## Step 9 – Add Notifications (Optional)

No SNS notifications were configured.

![Step 9 – Add Notifications](./P7%20ASG9.png)

---

## Step 10 – Add Tags (Optional)

No tags were added during configuration.

![Step 10 – Add Tags](./P7%20ASG10.png)

---

## Step 11 – Review Configuration (Part 1)

Reviewed:
- Launch Template
- VPC configuration
- Subnet distribution

![Step 11 – Review (1)](./P7%20ASG%2011.png)

---

## Step 12 – Review Configuration (Part 2)

Reviewed:
- Load Balancer integration
- Target group attachment

![Step 12 – Review (2)](./P7%20ASG%2012.png)

---

## Step 13 – Review Configuration (Part 3)

Reviewed:
- Scaling limits
- Instance maintenance policy

![Step 13 – Review (3)](./P7%20ASG%2013.png)

---

## Step 14 – Final Review

Confirmed all configurations before deployment.

![Step 14 – Final Review](./P7%20ASG%2014.png)

---

## Step 15 – Auto Scaling Group Successfully Created

Verified that:

- Auto Scaling Group is active
- Desired capacity is set
- Launch Template is attached
- Status shows updating capacity

![Step 15 – ASG Created](./P7%20ASG%2015.png)

---

# High Availability & Security Concepts Demonstrated

- Multi-Availability Zone deployment
- Elastic Load Balancer integration
- Automated health checks
- Automatic instance replacement
- Controlled scaling boundaries
- Launch template standardization

---

# Outcome

The Auto Scaling Group now:

- Maintains high availability across multiple AZs  
- Automatically replaces unhealthy instances  
- Scales between 1–4 instances  
- Distributes traffic using an Application Load Balancer  

This project demonstrates practical implementation of resilient, production-style AWS infrastructure.
