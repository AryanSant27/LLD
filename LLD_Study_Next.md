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

Implemented an **API Request Processing Pipeline** using the Decorator Pattern.

The problem involved a backend API gateway where every incoming API request can pass through a configurable set of behaviors:

* Authentication
* Rate Limiting
* Caching
* Logging
* Metrics

The objective was to dynamically compose these behaviors around a base request handler without modifying the original handler.

The base abstraction was:

```python
class RequestHandler:

    def handle_request(self, request):
        pass
```

### Key Understanding

Decorator allows additional responsibilities to be attached to an object dynamically by wrapping it with another object that follows the same interface.

Conceptually:

```text
Metrics
   ↓
Logging
   ↓
Caching
   ↓
RateLimiting
   ↓
Authentication
   ↓
BaseRequestHandler
```

Each decorator can perform its own responsibility and delegate to the wrapped handler.

### Composition Over Inheritance

The important design idea is:

> **Use composition to dynamically build a processing pipeline instead of modifying the original handler or creating subclasses for every possible combination of behaviors.**

### Decorator Failure Policies

A key part of the problem was understanding that decorators do not necessarily have identical failure behavior.

For example:

* Authentication failure may need to stop the entire pipeline.
* Rate limiting failure may reject the request immediately.
* Logging may record the request and still allow processing to continue.
* Metrics may observe the request regardless of whether downstream processing succeeds.

Therefore, the decorator chain is not simply about "adding functionality." Each decorator can define how its responsibility interacts with the downstream handler.

### Decorator Completion

Decorator is considered complete for the current LLD study level.

Do not spend time learning every advanced variation yet. Return to Decorator later when solving multi-pattern system designs.

---

# Next Pattern: Adapter Pattern

## What to Study

### 1. The Problem Adapter Solves

Understand how to make two incompatible interfaces work together without modifying the existing classes.

The key problem is:

> **The existing class provides the functionality we need, but through an interface that our client does not understand.**

### 2. Client / Target / Adapter / Adaptee

Understand the four core roles:

```text
Client
  ↓
Target Interface
  ↓
Adapter
  ↓
Adaptee
```

* **Client** → the code that expects a particular interface.
* **Target** → the interface the Client understands and works with.
* **Adapter** → translates the Target interface into calls understood by the Adaptee.
* **Adaptee** → the existing class with the incompatible interface.

### 3. Interface Translation

Understand that Adapter is primarily about **interface translation**.

The Adapter receives a call expressed through the Target interface and translates it into the corresponding operation on the Adaptee.

Conceptually:

```text
Client
   |
   | target_method()
   ↓
Adapter
   |
   | adaptee_method()
   ↓
Adaptee
```

### 4. Wrapping Existing Implementations

Understand how an Adapter can wrap an existing object rather than modifying it.

The existing implementation remains unchanged while the Adapter makes it compatible with the interface expected by the Client.

### 5. Composition-Based Adapter

Understand the common object-composition approach:

```text
Adapter
   |
   └── Adaptee
```

The Adapter holds a reference to the Adaptee and delegates translated operations to it.

### 6. Adapter vs Decorator

Understand the fundamental distinction:

* **Decorator** → adds behavior/responsibility while preserving the interface.
* **Adapter** → changes/translates the interface so incompatible objects can work together.

Decorator:

```text
Client
  ↓
Common Interface
  ↓
Decorator
  ↓
Same Interface
  ↓
Component
```

Adapter:

```text
Client
  ↓
Target Interface
  ↓
Adapter
  ↓
Different Interface
  ↓
Adaptee
```

### 7. Adapter vs Facade

Understand the difference:

* **Adapter** → makes one existing interface compatible with another expected interface.
* **Facade** → provides a simpler interface over a complex subsystem.

### 8. Adapter vs Inheritance

Understand that Adapter can be implemented through:

* Object composition
* Inheritance / class adaptation

Know why composition is generally the more flexible approach when adapting existing objects.

### 9. When to Use Adapter

Be able to identify Adapter when:

* You have an existing class that already provides the required functionality.
* Its interface does not match the interface your application expects.
* You cannot or do not want to modify the existing class.
* You want the rest of the application to remain independent of the incompatible implementation.

### 10. When Adapter Is Not Needed

Understand that Adapter is unnecessary when the existing class already implements the interface expected by the Client.

Do not introduce an Adapter merely for the sake of using the pattern.

---

## Adapter Completion Criteria

Consider Adapter complete once you can:

* Explain the problem it solves.
* Identify Client, Target, Adapter, and Adaptee.
* Implement an Adapter independently.
* Explain interface translation clearly.
* Explain composition-based Adapter.
* Distinguish Adapter from Decorator.
* Distinguish Adapter from Facade.
* Explain when Adapter is unnecessary.

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
