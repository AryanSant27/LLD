# LLD Study Roadmap — What to Study Next

## Current Status

* OOP fundamentals — completed
* SOLID principles — completed
* Strategy Pattern — completed for Level 1/2 questions
* Factory Pattern — completed at the basic/interview-practice level
* Observer Pattern — completed for Level 1/2 questions

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

# Next Pattern: Decorator Pattern

## What to Study

### 1. The problem Decorator solves

Understand how to add responsibilities or behavior to an object dynamically without modifying its original class.

### 2. Composition over inheritance

Understand why repeatedly creating subclasses for every combination of features can become problematic.

For example:

```text
Coffee
Coffee + Milk
Coffee + Sugar
Coffee + Milk + Sugar
Coffee + Milk + Caramel
Coffee + Sugar + Caramel
...
```

Decorator allows these combinations to be composed dynamically.

### 3. Component / Decorator relationship

Understand the common interface shared by:

* the original component
* concrete decorators

A decorator wraps another component and delegates to it while adding its own behavior.

### 4. Chaining Decorators

Understand how multiple decorators can wrap one another:

```text
Caramel
   ↓
Milk
   ↓
Coffee
```

The resulting object behaves as one component while accumulating behavior.

### 5. Decorator vs Inheritance

Understand when composition through decorators is preferable to creating many subclasses.

---

## Decorator Interview Problem

### Coffee / Beverage Customization System

Design and implement a beverage ordering system using the **Decorator Pattern**.

The system should support different base beverages:

* Espresso
* Cappuccino
* Latte
* Tea

Every beverage has:

* a description
* a base price

Customers can dynamically add condiments/toppings:

* Milk
* Sugar
* Caramel
* Whipped Cream
* Chocolate

Each condiment should modify the beverage's description and price.

For example:

```text
Espresso
    $100

Espresso + Milk
    $120

Espresso + Milk + Caramel
    $150

Espresso + Milk + Caramel + Whipped Cream
    $180
```

### Requirements

1. A beverage should expose:

   * `get_description()`
   * `get_cost()`

2. New beverages should be addable without modifying existing beverage classes.

3. New condiments should be addable without modifying existing beverage classes.

4. A customer should be able to combine condiments dynamically.

5. Avoid creating a separate class for every possible combination.

For example, do **not** create:

```text
EspressoWithMilk
EspressoWithMilkAndCaramel
EspressoWithMilkCaramelAndCream
...
```

6. The final decorated beverage should behave like a normal beverage.

### Example

The client should be able to construct something conceptually equivalent to:

```text
WhippedCream(
    Caramel(
        Milk(
            Espresso()
        )
    )
)
```

and obtain:

```text
Description:
Espresso, Milk, Caramel, Whipped Cream

Cost:
$180
```

### Bonus Questions

After the implementation, consider:

* Why is Decorator preferable to inheritance here?
* What happens if the customer adds the same condiment twice?
* Can decorators be applied in any order?
* What happens if a decorator needs additional configuration?
* How does Decorator differ from Strategy?

---

# Next Pattern After Decorator: Adapter Pattern

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
6. **Decorator ← NEXT**
7. **Adapter**
8. State
9. Command
10. Composite

After these, start practicing problems that require combining multiple patterns rather than isolated pattern exercises.
