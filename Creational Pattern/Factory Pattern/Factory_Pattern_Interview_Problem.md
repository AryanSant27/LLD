# Factory Pattern — Interview Practice Problem

## Problem: Payment Processing System

You're building a backend service for an e-commerce application.

The application supports multiple payment methods:

- Credit Card
- UPI
- PayPal

Each payment method has different implementation details, but the client should be able to interact with all of them through a common interface.

## Requirements

1. Every payment method must support:
   - `pay(amount)`
   - `refund(amount)`

2. Implement:
   - `CreditCardPayment`
   - `UPIPayment`
   - `PayPalPayment`

3. Create a component responsible for obtaining the appropriate payment implementation based on the payment type requested by the client.

4. The client code **should not directly instantiate** `CreditCardPayment`, `UPIPayment`, or `PayPalPayment`.

The client should be able to conceptually do:

```python
payment = PaymentFactory().create("UPI")

payment.pay(500)
payment.refund(200)
```

rather than:

```python
payment = UPIPayment()
```

## Constraints

- Use an interface/abstract class for the common payment behavior.
- Use a Factory to handle object creation.
- The client should depend on the abstraction, not concrete payment classes.
- Don't worry about databases, APIs, authentication, or actual payment processing.
- Keep it small — roughly 5–7 classes is enough.

## Design Question

Suppose tomorrow we add:

`NetBankingPayment`

Ask yourself:

> What code should I have to change?

A simple Factory implementation may require modifying the Factory itself. That is acceptable for this exercise. The goal is to understand the separation of object creation from object usage before exploring more advanced Factory variants.

## Practice Instructions

Implement this in **Python from scratch**.

Do not look up a Factory Pattern implementation.

Choose your own:

- folder structure
- class names
- interface design
- Factory design

Then review the solution for:

- Factory responsibility
- abstraction and polymorphism
- coupling
- SOLID principles
- whether the Factory is actually justified
- whether the design can accommodate another payment method

## Learning Goal

The key mental model is:

> **Don't make the client decide which concrete object to instantiate. Let a Factory make that decision and return an abstraction.**

Factory is about **decoupling object creation from object usage**.
