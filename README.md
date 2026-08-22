# Low-Level Design (LLD) - Design Patterns

## Progress

### Completed

* **Strategy Pattern** - Implemented notification service with different notification strategies (Email and SMS)
* **Factory Pattern** - Implemented a payment processing system using a Factory to separate object creation from client usage
* **Observer Pattern** - Implemented stock price alerts and an order tracking/notification system using Subjects and Observers
* **Decorator Pattern** - Implemented an API Request Processing Pipeline using decorators to dynamically compose request-processing behaviors

### Current Understanding

#### Strategy Pattern

* Understand the core problem Strategy solves: encapsulating interchangeable behaviors behind a common interface.
* Completed Level 1/2 practice.
* Understand that Strategy answers the question:

  * **"How should this behavior be performed?"**

#### Factory Pattern

* Understand that Factory separates object creation from object usage.
* Client depends on an abstraction rather than directly instantiating concrete implementations.
* Understand the distinction between:

  * Interface/Abstract Class → common contract
  * Polymorphism → common way of using different implementations
  * Factory → decides which concrete object to create
* Understand that a Factory does not necessarily need to be named `Factory`; naming should reflect responsibility.
* Completed a basic interview-style implementation using a payment processing system.

#### Observer Pattern

* Understand the core problem Observer solves: notifying multiple interested objects when a Subject's state changes.
* Understand the Subject/Observer relationship.
* Subject maintains a collection of observers.
* Observers can subscribe and unsubscribe.
* Subject notifies observers when relevant state changes.
* Understand how Observer reduces coupling between the Subject and concrete consumers.
* Understand Push vs Pull notification.
* Understand that Pull allows an Observer to retrieve the state it needs from the Subject.
* Understand that Observer can be combined with Strategy.
* Completed Level 1/2 interview-style practice.
* Observer is considered complete for the current study level.

#### Decorator Pattern

* Understand the core problem Decorator solves: dynamically adding responsibilities to objects through composition.
* Understand the Component / Decorator relationship.
* Understand that a decorator wraps another component while preserving the common interface.
* Understand chaining multiple decorators around a component.
* Understand composition over inheritance for dynamically combining responsibilities.
* Implemented the API Request Processing Pipeline problem.
* Understand decorators for Authentication, Rate Limiting, Caching, Logging, and Metrics.
* Understand that different decorators can have different failure policies.
* Understand that a decorator can either stop the pipeline or delegate to the wrapped handler depending on its responsibility.
* Completed the current interview-style practice.
* Decorator is considered complete for the current study level.

### Next

* **Adapter Pattern** - Learn how to make incompatible interfaces work together through an adapter.

## Adapter Pattern — What to Study

* Understand the core problem Adapter solves: making an existing implementation with an incompatible interface work with the interface expected by the Client.
* Understand the four core roles:
  * Client
  * Target
  * Adapter
  * Adaptee
* Understand interface translation.
* Understand how an Adapter wraps an existing implementation.
* Understand composition-based Adapter.
* Understand how the Adapter translates calls from the Target interface into calls understood by the Adaptee.
* Understand the difference between Adapter and Decorator.
* Understand the difference between Adapter and Facade.
* Understand composition-based Adapter vs inheritance-based Adapter.
* Understand when Adapter should be used.
* Understand when Adapter is unnecessary.

### Adapter Completion Criteria

Consider Adapter complete once you can:

* Explain the problem it solves.
* Identify Client, Target, Adapter, and Adaptee.
* Implement an Adapter independently.
* Explain interface translation clearly.
* Explain composition-based Adapter.
* Distinguish Adapter from Decorator.
* Distinguish Adapter from Facade.
* Explain when Adapter is unnecessary.

## Study Approach

For each design pattern:

1. Understand the problem the pattern solves.
2. Implement a small example.
3. Question whether the abstraction is actually necessary.
4. Solve an interview-style problem without looking up the implementation.
5. Review the design and identify improvements.
6. Move on to the next pattern.

Avoid over-studying a pattern once you can:

* Explain the problem it solves.
* Identify when to use it.
* Implement it independently.
* Explain its tradeoffs.
* Distinguish it from similar patterns.

## Pattern Roadmap

1. Strategy
2. Factory
3. Observer
4. Decorator
5. **Adapter ← Current**
6. State
7. Command
8. Composite

After completing these patterns, start solving LLD problems that require combining multiple design patterns rather than practicing patterns in isolation.
