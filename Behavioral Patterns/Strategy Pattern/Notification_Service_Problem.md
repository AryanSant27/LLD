# LLD Interview Problem — Notification Delivery System

## Problem Statement

You are building a notification service for an application.

The application needs to send notifications to users. Currently, it supports:

- Email
- SMS
- Push Notification

Each notification mechanism works differently:

- Email requires an SMTP/email provider.
- SMS requires an SMS gateway.
- Push notifications require a push provider such as Firebase/APNs.

The application should have a central `NotificationService` through which other parts of the application can send notifications.

Conceptually:

```text
OrderService
     |
     v
NotificationService
     |
     v
     ???
```

## Requirements

1. `NotificationService` should be able to send a notification through different mechanisms.
2. Adding a new notification mechanism should require minimal changes to existing code.
3. `NotificationService` should not need to know the implementation details of Email, SMS, or Push.
4. The caller should be able to choose which notification mechanism to use.
5. Different mechanisms may have different internal implementations and dependencies.
6. The system should be designed so that additional mechanisms can be added later, such as:
   - WhatsApp
   - Slack
   - Microsoft Teams

## Your Task

Design the classes/interfaces for this system.

Do not worry about implementing actual SMTP, Firebase, SMS, or other external APIs. Model the LLD and the relationships between the classes.

Think about:

```text
What classes do I need?
What interface(s) do I need?
Who owns/references what?
Where does the Strategy Pattern fit?
```

## Interview Follow-Ups

### Follow-up 1

Why did you create an interface?

What guarantees does it give you?

What would happen if Email and SMS had completely different requirements?

### Follow-up 2

Tomorrow we introduce WhatsApp notifications, but WhatsApp requires a completely different workflow.

Does your abstraction still make sense?

If not, where would you change the abstraction?

### Follow-up 3

Suppose Email can be sent through multiple providers:

- SMTP
- SendGrid
- AWS SES

Would you create:

```text
SendGridEmailNotification
AWSSESEmailNotification
SMTPEmailNotification
```

or:

```text
EmailNotification
       |
       v
  EmailGateway
    /   |   \
 SMTP  SES  SendGrid
```

Explain your choice.

### Follow-up 4

What if the notification mechanism is selected dynamically based on the user's preferences?

For example:

```text
User prefers:
1. Push
2. SMS
3. Email
```

How would your design select the appropriate strategy?

## Constraints

- Use Python.
- Keep the external gateways as simple stubs/mocks.
- Focus on class design, responsibilities, dependencies, and extensibility.
- Do not use a pattern just because the problem statement mentions one. Be prepared to justify every abstraction.

## Goal

The interviewer is primarily evaluating whether you can:

- Identify varying behavior.
- Encapsulate that behavior.
- Choose appropriate abstractions.
- Keep the main service decoupled from concrete implementations.
- Extend the system without unnecessarily modifying existing code.
- Explain why your design is appropriate.
