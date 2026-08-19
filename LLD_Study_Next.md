# LLD Study Roadmap — What to Study Next

## Current Status

- OOP fundamentals — completed
- SOLID principles — completed
- Strategy Pattern — completed for Level 1/2 questions
- Factory Pattern — completed at the basic/interview-practice level

### Factory Pattern — What Was Practiced

Implemented a small Payment Processing System with:

- `PaymentInterface`
- `CreditCardPayment`
- `UPIPayment`
- `PayPalPayment`
- a Factory-like component responsible for object creation
- a Client that uses the abstraction instead of directly instantiating concrete payment classes

Key understanding:

> **Don't make the client decide which concrete object to instantiate. Let a Factory make that decision and return an abstraction.**

Important distinction learned:

- Interface/abstract class → defines the common contract
- Polymorphism → lets the client work with different implementations through that contract
- Factory → encapsulates/centralizes the decision of which concrete object to create

Also understood that a Factory does **not** have to be named `Factory`. Naming should reflect the component's responsibility.

## Next Pattern: Observer Pattern

Study these concepts:

1. **The problem Observer solves**
   - One object needs to notify multiple interested objects when its state changes.
   - Avoiding tight coupling between the source of an event and all notification/consumer implementations.
   - Supporting new observers without modifying the subject's core business logic.

2. **Subject / Observer relationship**
   - Subject maintains a collection of observers.
   - Observers subscribe/unsubscribe.
   - Subject notifies observers when relevant state changes.

3. **Push vs Pull notification**
   - Understand whether the Subject sends event data directly or Observers retrieve the changed state.

4. **Observer and SOLID**
   - Understand how Observer can reduce coupling and support Open/Closed Principle.

5. **Real-world use cases**
   - Order status notifications
   - Event systems
   - UI event listeners
   - Logging/monitoring subscribers

## What You Should Be Able to Answer

Before moving on, you should be able to explain:

- Why would I use Observer instead of directly calling every notification service?
- What responsibility belongs in the Subject?
- What responsibility belongs in an Observer?
- How does an Observer subscribe and unsubscribe?
- How does Observer reduce coupling?
- When would Observer become unnecessary overengineering?
- Can Observer and Strategy be used together? Give an example.

## Practice Method

For each new pattern, use the same learning loop:

**Learn concept → implement a tiny example → question the abstraction → solve an interview-style problem → review the design → move on.**

Do not try to memorize every pattern variation before solving a problem.

## Pattern Progression

Continue roughly in this order:

1. OOP fundamentals
2. SOLID
3. Strategy
4. Factory
5. Observer
6. Decorator
7. Adapter
8. State
9. Command
10. Composite

After these, start practicing problems that require combining multiple patterns rather than isolated pattern exercises.
