# Observer Pattern — Interview Problems

## Problem 1 — Stock Price Alert System

### Problem Statement

Design and implement a **Stock Price Alert System** using the **Observer Pattern**.

A stock market system maintains the current price of multiple stocks. Different users can subscribe to stocks they are interested in and should automatically receive notifications whenever the price of a subscribed stock changes.

### Requirements

#### Stock

A `Stock` has:

- `symbol` — e.g. `AAPL`, `TSLA`
- `price`

The price of a stock can change.

Whenever the price changes, all subscribers interested in that stock should be notified.

#### Observer

The system should support different types of subscribers.

Initially, implement:

- `MobileApp`
- `EmailAlert`

Both should implement a common `Observer` / `Subscriber` interface.

The system should allow additional observer types to be added later without modifying the `Stock` / Publisher implementation.

#### Subscription

A user should be able to:

- Subscribe to a stock
- Unsubscribe from a stock

For example:

```text
User A → AAPL
User A → TSLA

User B → AAPL

User C → TSLA
```

If AAPL's price changes, only observers subscribed to AAPL should be notified.

#### Multiple Stocks

The system must support multiple stocks simultaneously.

For example:

```text
AAPL → 3 observers
TSLA → 5 observers
GOOG → 2 observers
```

Updating AAPL should **not** notify observers subscribed only to TSLA or GOOG.

### Example Flow

Suppose:

```text
AAPL = $200
```

Two observers subscribe:

```text
MobileApp("Aryan")
EmailAlert("John")
```

Then:

```text
AAPL.set_price(210)
```

Both observers should receive an update equivalent to:

```text
AAPL price changed from $200 to $210
```

If the Email observer unsubscribes:

```text
AAPL.remove_subscriber(emailAlert)
```

and the price changes again:

```text
AAPL.set_price(220)
```

only the remaining observers should be notified.

### Design Constraints

1. `Stock` / Publisher should not depend on concrete observer classes such as `MobileApp` or `EmailAlert`.
2. Adding a new observer type such as `SMSAlert` should not require modifying the Publisher.
3. Observers should be able to subscribe/unsubscribe dynamically.
4. A stock can have multiple observers.
5. An observer can subscribe to multiple stocks.
6. Avoid polling. Observers should receive updates through notifications.

### Bonus Questions

- What happens if the same observer subscribes twice?
- Should setting the price to the same value trigger a notification?
- Should the observer receive the old and new price, or query the stock itself?
- What happens if an observer unsubscribes while notifications are being sent?
- Should notifications be synchronous or asynchronous?
- How would you support a subscriber interested only when a price crosses a threshold?

---

# Problem 2 — Order Tracking & Notification System

### Problem Statement

Design and implement an **Order Tracking & Notification System** using the **Observer Pattern**.

You are designing the notification system for an e-commerce platform.

Whenever an **order's status changes**, interested components of the system should be informed.

An order can move through states such as:

```text
PLACED
   ↓
CONFIRMED
   ↓
SHIPPED
   ↓
OUT_FOR_DELIVERY
   ↓
DELIVERED
```

An order can also be:

```text
CANCELLED
```

### Requirements

#### Order

An `Order` contains:

- `order_id`
- `customer_id`
- current status

The order should provide a way to change its status.

#### Different Consumers

The system initially has three consumers.

### Customer Notification

Sends a notification to the customer whenever the order status changes.

The notification system should support:

- Email
- SMS
- Push Notification

The design should allow additional notification channels to be added later.

### Inventory System

The Inventory System reacts only to certain order events.

For example:

```text
PLACED
    → Reserve inventory

CANCELLED
    → Release inventory
```

It does **not** need to react to every status change.

### Analytics System

The Analytics System tracks every status transition.

For example:

```text
ORDER_123

PLACED → CONFIRMED
CONFIRMED → SHIPPED
SHIPPED → DELIVERED
```

### Different Notification Requirements

Different consumers are interested in different events:

```text
Customer Notification
    → All status changes

Inventory System
    → PLACED
    → CANCELLED

Analytics
    → All status changes
```

The `Order` should **not** contain logic such as:

```text
if observer == inventory:
    ...
elif observer == analytics:
    ...
```

The Order should remain independent of concrete consumers.

### Subscription

Consumers should be able to register and unregister themselves dynamically.

The system should be extensible to support future consumers such as:

- Fraud Detection System
- Shipping System
- Recommendation System

without modifying the core `Order` implementation.

### Example

Suppose:

```text
Order #123
Status = PLACED
```

The order changes:

```text
PLACED → CONFIRMED
```

The appropriate consumers should react.

Then:

```text
CONFIRMED → SHIPPED
```

The appropriate consumers react again.

Then:

```text
SHIPPED → DELIVERED
```

The appropriate consumers react again.

### Design Constraints

1. Avoid tight coupling between `Order` and concrete consumer classes.
2. Allow consumers to subscribe/unsubscribe dynamically.
3. Allow different consumers to react to different status changes.
4. Allow new consumer types to be added without modifying `Order`.
5. Allow new notification channels to be added without modifying `Order`.
6. Avoid unnecessary notifications where possible.
7. Keep order business logic separate from notification/side-effect logic.
8. Invalid order status transitions should not be allowed.

### Bonus Questions

#### 1. Push vs Pull

Should the notification contain:

```text
order
old_status
new_status
```

or should consumers receive the `Order` and retrieve the information they need?

#### 2. Event Filtering

Where should filtering happen?

```text
Order → only notify relevant observers
```

or:

```text
Order → notify all observers
              ↓
       Observer filters
```

#### 3. Observer Failure

What happens if one consumer fails while others succeed?

```text
Customer Notification ✓
Inventory ✓
Analytics ✗
Shipping ✓
```

Should the Order update itself fail?

#### 4. Scale

What happens if the system has 10,000 observers?

Would synchronous notification still be appropriate?