# Testing Conventions

## File Organization

### Colocate test files
**Applies to**: All tests except E2E  
**Rule**: Place test files next to source files.

```
src/
└── components/
    └── UserCard/
        ├── UserCard.tsx
        ├── UserCard.test.tsx    # ✅ Colocated
        └── index.ts
```

### E2E tests in dedicated directory
**Applies to**: End-to-end tests  
**Rule**: Place E2E tests in `e2e/` or `tests/e2e/` at project root.

```
project/
├── src/
├── e2e/
│   ├── auth.spec.ts
│   └── checkout.spec.ts
└── tests/
    └── integration/
```

## Test Structure

### Descriptive test names
**Applies to**: All test cases  
**Rule**: Format as "should [action] when [condition]" or describe the behavior clearly.

```typescript
// ✅ Correct
it('should display error message when login fails', () => {});
it('should redirect to dashboard when login succeeds', () => {});
describe('UserCard', () => {
  it('should render user name and avatar', () => {});
});

// ❌ Avoid
it('login error', () => {});
it('works', () => {});
it('test 1', () => {});
```

### One assertion per test (guideline)
**Applies to**: Unit tests  
**Rule**: Test one behavior per test case. Multiple assertions OK if testing same behavior.

```typescript
// ✅ Correct - testing one behavior
it('should format user name correctly', () => {
  const result = formatUserName({ first: 'John', last: 'Doe' });
  expect(result).toBe('John Doe');
});

// ✅ Also correct - same behavior, multiple aspects
it('should return complete user object', () => {
  const user = createUser('John');
  expect(user.id).toBeDefined();
  expect(user.name).toBe('John');
  expect(user.createdAt).toBeInstanceOf(Date);
});

// ❌ Avoid - testing multiple unrelated behaviors
it('should handle user operations', () => {
  expect(createUser('John').name).toBe('John');
  expect(deleteUser('123')).toBe(true);
  expect(listUsers()).toHaveLength(0);
});
```

### Arrange-Act-Assert pattern
**Applies to**: All unit tests  
**Rule**: Structure tests with clear AAA sections.

```typescript
// ✅ Correct
it('should calculate total with discount', () => {
  // Arrange
  const items = [{ price: 100 }, { price: 200 }];
  const discount = 0.1;
  
  // Act
  const total = calculateTotal(items, discount);
  
  // Assert
  expect(total).toBe(270);
});
```

## Setup and Teardown

### Use beforeEach for common setup
**Applies to**: Test suites with repeated setup  
**Rule**: Use `beforeEach` for setup, not `beforeAll` unless necessary.

```typescript
// ✅ Correct
describe('UserService', () => {
  let service: UserService;
  
  beforeEach(() => {
    service = new UserService();
  });
  
  it('should create user', () => {
    // Test uses fresh service instance
  });
});

// ⚠️ Use carefully - can cause test interdependence
beforeAll(() => {
  // Only for expensive setup that doesn't need reset
});
```

### Clean up after tests
**Applies to**: Tests that create side effects  
**Rule**: Use `afterEach` to reset mocks and clean up.

```typescript
// ✅ Correct
describe('API Tests', () => {
  afterEach(() => {
    vi.clearAllMocks();
    localStorage.clear();
  });
  
  it('should call API', () => {
    // Test with mocks
  });
});
```

## Mocking

### Mock at boundaries
**Applies to**: All mocked dependencies  
**Rule**: Mock external APIs and services, not internal functions.

```typescript
// ✅ Correct - mock external API
vi.mock('@/lib/api', () => ({
  fetchUser: vi.fn().mockResolvedValue({ id: '1', name: 'John' }),
}));

// ❌ Avoid - mocking internal implementation
vi.mock('@/utils/formatName', () => ({
  formatName: vi.fn().mockReturnValue('John'),
}));
```

**Rationale**: Testing implementation details makes tests fragile.

### Use MSW for API mocking
**Applies to**: Integration tests needing API responses  
**Rule**: Use Mock Service Worker instead of mocking fetch directly.

```typescript
// ✅ Correct
import { http, HttpResponse } from 'msw';
import { setupServer } from 'msw/node';

const server = setupServer(
  http.get('/api/users', () => {
    return HttpResponse.json([{ id: '1', name: 'John' }]);
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

// ❌ Avoid
global.fetch = vi.fn().mockResolvedValue({
  json: () => Promise.resolve([{ id: '1', name: 'John' }]),
});
```

### Reset mocks between tests
**Applies to**: All mocked functions  
**Rule**: Clear or reset mocks in `afterEach`.

```typescript
// ✅ Correct
afterEach(() => {
  vi.clearAllMocks();
});

// Or for specific mocks
afterEach(() => {
  mockFunction.mockClear();
});
```

## Test Coverage

### Aim for high coverage of critical paths
**Applies to**: All new code  
**Rule**: Test critical business logic, error paths, and edge cases.

**Priority order:**
1. Critical business logic (payment, auth, data mutations)
2. Error handling and edge cases
3. Happy paths
4. UI interactions

### Don't test implementation details
**Applies to**: All tests  
**Rule**: Test behavior, not implementation.

```typescript
// ✅ Correct - testing behavior
it('should show error when email is invalid', async () => {
  render(<LoginForm />);
  fireEvent.change(screen.getByLabelText('Email'), { target: { value: 'invalid' } });
  fireEvent.click(screen.getByRole('button', { name: 'Submit' }));
  expect(await screen.findByText('Invalid email')).toBeInTheDocument();
});

// ❌ Avoid - testing implementation
it('should call validateEmail function', () => {
  const spy = vi.spyOn(utils, 'validateEmail');
  render(<LoginForm />);
  // ...
  expect(spy).toHaveBeenCalled();
});
```

## Async Testing

### Always await async assertions
**Applies to**: All async tests  
**Rule**: Use `await` or return promises in async tests.

```typescript
// ✅ Correct
it('should load user data', async () => {
  render(<UserProfile userId="123" />);
  expect(await screen.findByText('John Doe')).toBeInTheDocument();
});

// ❌ Avoid
it('should load user data', () => {
  render(<UserProfile userId="123" />);
  expect(screen.findByText('John Doe')).toBeInTheDocument(); // Missing await
});
```

### Use proper async utilities
**Applies to**: Testing library queries  
**Rule**: Use `findBy*` for async queries, `getBy*` for immediate queries.

```typescript
// ✅ Correct - async element
expect(await screen.findByText('Loaded')).toBeInTheDocument();

// ✅ Correct - immediate element
expect(screen.getByText('Static Text')).toBeInTheDocument();

// ❌ Avoid - wrong query type
await waitFor(() => {
  expect(screen.getByText('Loaded')).toBeInTheDocument();
});
```

## Performance

### Keep tests fast
**Applies to**: All tests  
**Rule**: Tests should run in milliseconds, not seconds.

**Tips:**
- Mock expensive operations
- Avoid real network calls
- Use `vi.useFakeTimers()` for timers
- Minimize DOM rendering in unit tests

### Avoid test interdependence
**Applies to**: All test suites  
**Rule**: Tests should pass in any order.

```typescript
// ✅ Correct - independent tests
describe('Calculator', () => {
  it('should add numbers', () => {
    expect(add(1, 2)).toBe(3);
  });
  
  it('should subtract numbers', () => {
    expect(subtract(5, 3)).toBe(2);
  });
});

// ❌ Avoid - tests depend on order
let result;
it('test 1', () => {
  result = calculate();
});
it('test 2', () => {
  expect(result).toBe(10); // Depends on test 1
});
```
