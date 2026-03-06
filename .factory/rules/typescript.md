# TypeScript Conventions

## Type Definitions

### Use `interface` for object shapes
**Applies to**: All type definitions for objects  
**Rule**: Use `interface` for object types, `type` for unions, intersections, and primitives.

```typescript
// ✅ Correct
interface User {
  id: string;
  name: string;
  email: string;
}

type Status = 'active' | 'inactive' | 'pending';
type UserWithStatus = User & { status: Status };

// ❌ Avoid
type User = {
  id: string;
  name: string;
};
```

### Avoid `any`
**Applies to**: All TypeScript files  
**Rule**: Never use `any`. Use `unknown` with type guards, or define proper types.

```typescript
// ✅ Correct
function processData(data: unknown): string {
  if (typeof data === 'string') {
    return data.toUpperCase();
  }
  throw new Error('Expected string');
}

// ❌ Avoid
function processData(data: any): string {
  return data.toUpperCase();
}
```

**Rationale**: `any` disables type checking and hides bugs.

### Export types with implementations
**Applies to**: All exported functions and classes  
**Rule**: Export types alongside their implementations for better IDE support.

```typescript
// ✅ Correct
export interface CreateUserParams {
  name: string;
  email: string;
}

export function createUser(params: CreateUserParams) {
  // ...
}

// ❌ Avoid
function createUser(params: { name: string; email: string }) {
  // ...
}
export { createUser };
```

## Function Patterns

### Use early returns
**Applies to**: All functions with conditionals  
**Rule**: Return early for edge cases instead of nesting.

```typescript
// ✅ Correct
function processUser(user: User | null): string {
  if (!user) return 'No user';
  if (!user.active) return 'User inactive';
  return `Processing ${user.name}`;
}

// ❌ Avoid
function processUser(user: User | null): string {
  if (user) {
    if (user.active) {
      return `Processing ${user.name}`;
    } else {
      return 'User inactive';
    }
  } else {
    return 'No user';
  }
}
```

**Rationale**: Reduces nesting and improves readability.

### Named exports over default
**Applies to**: All module exports  
**Rule**: Use named exports for better refactoring and import clarity.

```typescript
// ✅ Correct
export function createUser() {}
export const USER_ROLES = ['admin', 'user'] as const;

// ❌ Avoid
export default function createUser() {}
```

**Rationale**: Named exports enable better IDE refactoring and prevent naming confusion.

### Use const assertions for literal types
**Applies to**: Constant arrays and objects  
**Rule**: Use `as const` to create readonly literal types.

```typescript
// ✅ Correct
export const STATUSES = ['pending', 'active', 'inactive'] as const;
export type Status = typeof STATUSES[number]; // 'pending' | 'active' | 'inactive'

// ❌ Avoid
export const STATUSES = ['pending', 'active', 'inactive'];
export type Status = string;
```

## Import Organization

### Group imports
**Applies to**: All TypeScript files  
**Rule**: Organize imports in this order:
1. React (if applicable)
2. External libraries
3. Internal modules (absolute imports)
4. Relative imports
5. Type-only imports

```typescript
// ✅ Correct
import { useState } from 'react';

import { format } from 'date-fns';
import { z } from 'zod';

import { Button } from '@/components/ui';
import { api } from '@/lib/api';

import { formatUserName } from './utils';

import type { User } from '@/types';
```

### Prefer absolute imports
**Applies to**: Cross-module imports  
**Rule**: Use absolute imports (`@/`) for imports outside the current directory.

```typescript
// ✅ Correct
import { Button } from '@/components/ui/Button';

// ❌ Avoid (unless within same directory)
import { Button } from '../../../components/ui/Button';
```

## Null Safety

### Use optional chaining
**Applies to**: Accessing potentially null/undefined properties  
**Rule**: Use `?.` instead of manual checks.

```typescript
// ✅ Correct
const userName = user?.profile?.name ?? 'Unknown';

// ❌ Avoid
const userName = user && user.profile && user.profile.name || 'Unknown';
```

### Use nullish coalescing
**Applies to**: Default values  
**Rule**: Use `??` instead of `||` for default values.

```typescript
// ✅ Correct
const count = userInput ?? 0; // Only uses 0 if userInput is null/undefined

// ❌ Avoid
const count = userInput || 0; // Also uses 0 if userInput is 0 or ''
```

## Error Handling

### Type errors properly
**Applies to**: All catch blocks  
**Rule**: Type errors as `unknown` and validate before use.

```typescript
// ✅ Correct
try {
  await riskyOperation();
} catch (error: unknown) {
  if (error instanceof Error) {
    console.error(error.message);
  } else {
    console.error('Unknown error occurred');
  }
}

// ❌ Avoid
try {
  await riskyOperation();
} catch (error: any) {
  console.error(error.message);
}
```

## Async/Await

### Always await promises
**Applies to**: All async operations  
**Rule**: Don't forget to await promises.

```typescript
// ✅ Correct
async function getUser(id: string): Promise<User> {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
}

// ❌ Avoid (missing await)
async function getUser(id: string): Promise<User> {
  const response = fetch(`/api/users/${id}`);
  return response.json();
}
```

### Handle promise rejections
**Applies to**: All async functions  
**Rule**: Wrap risky async operations in try-catch.

```typescript
// ✅ Correct
async function updateUser(id: string, data: UserUpdate) {
  try {
    const user = await api.updateUser(id, data);
    return { success: true, user };
  } catch (error) {
    console.error('Failed to update user:', error);
    return { success: false, error };
  }
}
```
