# LLD Study Roadmap — What to Study Next

## Current Status

- OOP fundamentals — completed
- SOLID principles — completed
- Strategy Pattern — completed for Level 1/2 questions

## Next Pattern: Factory Pattern

Study these concepts:

1. **The problem Factory solves**
   - Object creation logic becoming scattered through client code.
   - Avoiding large `if/elif` or `match` blocks for choosing concrete classes.
   - Separating object creation from object usage.

2. **Simple Factory**
   - A single factory responsible for deciding which concrete object to create.
   - Understand that Simple Factory is commonly discussed as a pattern even though it is not one of the original GoF 23 patterns.

3. **Factory Method**
   - Understand the difference between Simple Factory and Factory Method.
   - Focus on why subclasses can decide which concrete object gets created.

4. **Abstract Factory**
   - Creating families of related objects.
   - Understand when this is useful and how it differs from Factory Method.

5. **Dependency Injection connection**
   - Understand why object creation can be moved outside business logic.
   - See how factories and dependency injection can complement each other.

## What You Should Be Able to Answer

Before moving on, you should be able to explain:

- Why would I use a Factory instead of directly calling a constructor?
- What responsibility belongs in the Factory?
- When does a Factory become unnecessary overengineering?
- What is the difference between Simple Factory and Factory Method?
- What problem does Abstract Factory solve?
- How does Factory support Open/Closed Principle?
- Can Factory and Strategy be used together? Give an example.

## Practice Method

For the next pattern, use the same learning loop:

**Learn concept → implement a tiny example → question the abstraction → solve an interview-style problem → review the design → move on.**

Do not try to memorize every pattern variation before solving a problem.

## After Factory

Continue roughly in this order:

1. Factory
2. Observer
3. Decorator
4. Adapter
5. State
6. Command
7. Composite

After these, start practicing problems that require combining multiple patterns rather than isolated pattern exercises.
