# Solution Documentation

## Overview

This project implements a simplified Personal Finance Manager while demonstrating multiple Object-Oriented Design Patterns. The solution was designed to keep the application flexible, maintainable, and easy to extend while satisfying the functional requirements of tracking transactions, adapting external data sources, monitoring balance changes, and processing financial events.

---

# Design Patterns Implemented

## 1. Singleton Pattern (Creational)

### Class

- Balance

### Purpose

The application should maintain a single source of truth for the current account balance. Creating multiple balance objects could result in inconsistent financial data.

### Implementation

The Balance class was implemented as a Singleton, ensuring only one instance exists throughout the application. All transactions update the same balance object regardless of where they originate.

### Benefits

- Prevents duplicate balance tracking
- Ensures application-wide consistency
- Provides centralized state management

---

## 2. Adapter Pattern (Structural)

### Class

- TransactionAdapter

### Purpose

External systems often provide data in formats that do not match the application's internal models.

### Implementation

ExternalFreelanceIncome represents data received from a third-party source. The TransactionAdapter converts that object into the application's standard Transaction format without modifying either class.

### Benefits

- Supports integration with external systems
- Reduces coupling between internal and external models
- Enables future data source expansion

---

## 3. Observer Pattern (Behavioral)

### Classes

- IBalanceObserver
- PrintObserver
- LowBalanceAlertObserver

### Purpose

The application needs to react automatically when balance changes occur.

### Implementation

The Balance object acts as the subject and maintains a collection of observers. Whenever a transaction is applied, registered observers are notified.

Examples include:

- Displaying balance updates
- Monitoring low-balance conditions

### Benefits

- Encourages loose coupling
- Simplifies event-driven behavior
- Makes future notifications easy to add

---

## 4. Command Pattern (Behavioral)

### Classes

- ApplyTransactionCommand
- TransactionProcessor

### Purpose

Transaction execution should be separated from transaction creation.

### Implementation

Each transaction is wrapped inside a command object responsible for executing a specific action against the Balance. A TransactionProcessor executes commands and maintains a processing history.

### Benefits

- Encapsulates business operations
- Enables transaction history tracking
- Provides a foundation for future enhancements such as auditing, queuing, or undo functionality

---

# Pattern Classification Summary

| Pattern   | Category   |
| --------- | ---------- |
| Singleton | Creational |
| Adapter   | Structural |
| Observer  | Behavioral |
| Command   | Behavioral |

This solution demonstrates all three major design pattern categories:

- Creational
- Structural
- Behavioral

---

# Design Considerations

The goal of the implementation was to apply design patterns only where they provided practical value.

- Singleton ensures consistent balance management.
- Adapter supports external system integration.
- Observer enables event-driven notifications.
- Command separates execution logic from transaction data.

Together, these patterns improve extensibility while keeping the overall solution simple and maintainable.

---

# Conclusion

This project demonstrates how object-oriented design patterns can be used together to solve different architectural concerns. Each pattern addresses a specific problem while keeping the system modular, reusable, and easier to evolve over time.
