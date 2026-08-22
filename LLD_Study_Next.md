# LLD Study Roadmap — What to Study Next

## Current Status

* OOP fundamentals — completed
* SOLID principles — completed
* Strategy Pattern — completed for Level 1/2 questions
* Factory Pattern — completed at the basic/interview-practice level
* Observer Pattern — completed for Level 1/2 questions
* Decorator Pattern — completed for the current LLD study level

### Factory Pattern — What Was Practiced

Implemented a small Payment Processing System with:

* `PaymentInterface`
* `CreditCardPayment`
* `UPIPayment`
* `PayPalPayment`
* a Factory-like component responsible for object creation
* a Client that uses the abstraction instead of directly instantiating concrete payment classes

Key understanding:

> **Don't make the client decide which concrete object to instantiate. Let a Factory make that decision and return an abstraction.**

Important distinction learned:

* Interface/abstract class → defines the common contract
* Polymorphism → lets the client work with different implementations through that contract
* Factory → encapsulates/centralizes the decision of which concrete object to create

Also understood that a Factory does **not** have to be named `Factory`. Naming should reflect the component's responsibility.

---

## Observer Pattern — What Was Practiced

Implemented:

1. A basic Stock Price Alert System.
2. A more advanced Order Tracking & Notification System.

Key understanding:

* Observer solves the problem of notifying multiple interested objects when a Subject's state changes.
* The Subject maintains a collection of Observers.
* Observers can subscribe and unsubscribe dynamically.
* The Subject notifies Observers when relevant state changes.
* Observer reduces coupling between the source of an event and its consumers.
* New Observer implementations can be added without modifying the Subject's core business logic.
* Observer can support both Push and Pull notification models.

### Push vs Pull

**Push:**

```text
Subject
   |
   | update(old_state, new_state)
   ↓
Observer
```

The Subject sends the relevant event/state data directly.

**Pull:**

```text
Subject
   |
   | update(subject)
   ↓
Observer
   |
   | retrieves the state it needs
   ↓
Subject
```

The Subject announces that something changed and the Observer decides what information it needs.

### Observer + Strategy

Observer and Strategy can be composed.

For example:

```text
Order
  |
  | Observer
  ↓
CustomerNotification
  |
  | Strategy
  ↓
Email / SMS / Push
```

Observer answers:

> **When should the customer notification happen?**

Strategy answers:

> **How should the customer be notified?**

### Observer Completion

Observer is considered complete for the current LLD study level.

Do not spend time learning every advanced variation yet. Move forward and return to Observer when practicing multi-pattern system designs.

---

# Decorator Pattern — Completed

## What Was Practiced

Implemented the **Coffee / Beverage Customization System** using the Decorator Pattern.

The problem focused on dynamically combining a base beverage with multiple condiments without creating a separate subclass for every possible combination.

The core concepts covered were:

* Component interface
* Concrete components
* Decorator abstraction
* Concrete decorators
* Chaining decorators
* Composition over inheritance

### Key Understanding

Decorator allows additional responsibilities to be attached to an object dynamically by wrapping it with another object that follows the same interface.

Conceptually:

```text
WhippedCream
      ↓
  Caramel
      ↓
    Milk
      ↓
  Espresso
```

The final decorated object can still be treated as the original component type.

### Decorator vs Inheritance

The important design tradeoff is:

> **Use composition to build combinations dynamically instead of creating a subclass for every possible combination of features.**

### Decorator Completion

Decorator is considered complete for the current LLD study level.

Do not spend time learning every advanced variation yet. Return to Decorator later when solving multi-pattern system designs.

---

# Next Pattern: Adapter Pattern

## What to Study

### 1. The problem Adapter solves

Understand how to make two incompatible interfaces work together without modifying the existing classes.

### 2. Client / Target / Adapter / Adaptee

Understand the roles:

```text
Client
  ↓
Target Interface
  ↓
Adapter
  ↓
Adaptee
```

### 3. Interface incompatibility

The core problem is not that an existing class has bad behavior.

The problem is:

> **The existing class provides the functionality we need, but through an interface that our client does not understand.**

### 4. Wrapping an existing implementation

Understand how an Adapter translates one interface into another.

### 5. Adapter vs Decorator

Understand the difference:

* **Decorator** → adds behavior/responsibility while preserving the interface.
* **Adapter** → translates one interface into another.

---

## Adapter Interview Problem

### Payment Gateway Integration System

You are building an e-commerce payment system.

Your application expects every payment provider to implement:

```text
PaymentGateway
    pay(amount)
    refund(transaction_id)
```

Your application already has its own implementation:

```text
InternalPaymentGateway
```

However, the company wants to integrate several external payment providers.

The external providers have incompatible APIs.

### Provider 1 — Stripe-like Gateway

```text
create_payment(amount)
cancel_payment(transaction_id)
```

### Provider 2 — PayPal-like Gateway

```text
make_transaction(amount)
reverse_transaction(transaction_id)
```

### Provider 3 — Legacy Gateway

```text
process(amount_in_rupees)
void(transaction_reference)
```

You **cannot modify the existing third-party classes**.

The rest of your application should continue working with:

```text
PaymentGateway
```

### Requirements

1. Define a common `PaymentGateway` interface.

2. Existing application code should depend only on `PaymentGateway`.

3. Integrate all three external gateways.

4. Do not modify the external gateway classes.

5. The application should be able to switch between payment providers without changing its core payment-processing logic.

6. Adding another external payment provider should require adding an Adapter rather than modifying the existing application logic.

### Example

The client should be able to work with:

```text
PaymentGateway
      ↑
      |
StripeAdapter
      ↓
StripeAPI
```

and:

```text
PaymentGateway
      ↑
      |
PayPalAdapter
      ↓
PayPalAPI
```

The client should not need to know which external API is being used.

### Bonus Questions

After implementing the basic system, consider:

* Why can't we simply modify the third-party classes?
* Why is Adapter preferable to changing every client?
* Is Adapter adding behavior or translating behavior?
* When would inheritance-based Adapter be appropriate?
* What is the difference between Adapter and Facade?
* What is the difference between Adapter and Decorator?

---

## Practice Method

For each new pattern, use the same learning loop:

**Learn concept → implement a tiny example → question the abstraction → solve an interview-style problem → review the design → move on.**

Do not try to memorize every pattern variation before solving a problem.

---

## Pattern Progression

Continue roughly in this order:

1. OOP fundamentals
2. SOLID
3. Strategy
4. Factory
5. Observer
6. Decorator
7. **Adapter ← NEXT**
8. State
9. Command
10. Composite

After these, start practicing problems that require combining multiple patterns rather than isolated pattern exercises.
