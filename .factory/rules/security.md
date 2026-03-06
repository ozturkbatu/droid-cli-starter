# Security Requirements

## Secrets Management

### Never hardcode secrets
**Applies to**: All code  
**Rule**: Use environment variables for all secrets. Never commit secrets to version control.

```typescript
// ✅ Correct
const apiKey = process.env.API_KEY;
const dbUrl = process.env.DATABASE_URL;

// ❌ Never do this
const apiKey = 'YOUR_API_KEY_HERE';
const password = 'YOUR_PASSWORD_HERE';
```

**Rationale**: Secrets in code can be exposed through version control, logs, or error messages.

### Validate environment variables at startup
**Applies to**: Application initialization  
**Rule**: Validate required env vars exist at startup, fail fast if missing.

```typescript
// ✅ Correct
function requireEnv(name: string): string {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required environment variable: ${name}`);
  }
  return value;
}

const config = {
  apiKey: requireEnv('API_KEY'),
  dbUrl: requireEnv('DATABASE_URL'),
};

// ❌ Avoid
const apiKey = process.env.API_KEY; // May be undefined
```

### Use .env files, never commit them
**Applies to**: Local development  
**Rule**: Use `.env` for local secrets, add to `.gitignore`, provide `.env.example`.

```bash
# ✅ .gitignore
.env
.env.local

# ✅ .env.example (safe to commit)
API_KEY=your_api_key_here
DATABASE_URL=your_database_url_here
```

## Input Validation

### Validate all external input
**Applies to**: API routes, form handlers, query parameters  
**Rule**: Use Zod or similar to validate all input from users or external sources.

```typescript
// ✅ Correct
import { z } from 'zod';

const CreateUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  age: z.number().int().min(0).max(150),
});

export async function createUser(input: unknown) {
  const data = CreateUserSchema.parse(input); // Throws if invalid
  // data is now typed and validated
  return await db.user.create({ data });
}

// ❌ Avoid
export async function createUser(input: any) {
  return await db.user.create({ data: input }); // No validation!
}
```

### Sanitize user input
**Applies to**: User-provided strings displayed in UI  
**Rule**: Escape or sanitize user input before rendering.

```typescript
// ✅ Correct - React auto-escapes
<div>{userInput}</div>

// ⚠️ Dangerous - only if you know HTML is safe
<div dangerouslySetInnerHTML={{ __html: sanitizedHtml }} />

// ❌ Never
<div dangerouslySetInnerHTML={{ __html: userInput }} />
```

### Validate file uploads
**Applies to**: File upload endpoints  
**Rule**: Validate file type, size, and content.

```typescript
// ✅ Correct
const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB
const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/webp'];

function validateFile(file: File) {
  if (file.size > MAX_FILE_SIZE) {
    throw new Error('File too large');
  }
  if (!ALLOWED_TYPES.includes(file.type)) {
    throw new Error('Invalid file type');
  }
  // Additional validation: check file headers, scan for malware, etc.
}
```

## Authentication & Authorization

### Check authentication on every protected route
**Applies to**: All API routes requiring auth  
**Rule**: Verify authentication for every protected endpoint.

```typescript
// ✅ Correct
export async function GET(request: Request) {
  const session = await getSession(request);
  if (!session) {
    return new Response('Unauthorized', { status: 401 });
  }
  // Handle authenticated request
}

// ❌ Avoid
export async function GET(request: Request) {
  // Assuming auth without checking
  const user = await getUser();
}
```

### Verify authorization separately
**Applies to**: Operations on user resources  
**Rule**: Check both authentication (who are you) and authorization (what can you do).

```typescript
// ✅ Correct
export async function updatePost(postId: string, userId: string, data: PostUpdate) {
  const post = await db.post.findUnique({ where: { id: postId } });
  
  if (!post) {
    throw new Error('Post not found');
  }
  
  if (post.authorId !== userId) {
    throw new Error('Unauthorized: Not the post author');
  }
  
  return await db.post.update({ where: { id: postId }, data });
}
```

### Use secure session management
**Applies to**: Session handling  
**Rule**: Use httpOnly, secure, sameSite cookies for sessions.

```typescript
// ✅ Correct
const sessionCookie = {
  httpOnly: true,  // Prevents XSS
  secure: true,     // HTTPS only
  sameSite: 'lax',  // CSRF protection
  maxAge: 60 * 60 * 24 * 7, // 7 days
};
```

## SQL & Database

### Use parameterized queries
**Applies to**: All database queries  
**Rule**: Never concatenate user input into SQL queries. Use parameterized queries or ORMs.

```typescript
// ✅ Correct - with ORM
const user = await db.user.findUnique({
  where: { email: userEmail },
});

// ✅ Correct - with parameterized query
const user = await db.query(
  'SELECT * FROM users WHERE email = ?',
  [userEmail]
);

// ❌ NEVER DO THIS - SQL injection vulnerability
const user = await db.query(
  `SELECT * FROM users WHERE email = '${userEmail}'`
);
```

**Rationale**: Prevents SQL injection attacks.

## Error Handling

### Never expose internal errors to clients
**Applies to**: API error responses  
**Rule**: Log detailed errors server-side; return generic messages to clients.

```typescript
// ✅ Correct
try {
  await processPayment(data);
} catch (error) {
  console.error('Payment failed:', error); // Detailed log
  throw new ApiError('Payment processing failed', 500); // Generic message
}

// ❌ Avoid
catch (error) {
  throw new ApiError(error.message, 500); // May expose internals
}
```

### Don't leak sensitive info in error messages
**Applies to**: All error messages  
**Rule**: Avoid revealing system details in errors.

```typescript
// ✅ Correct
throw new Error('Invalid credentials');

// ❌ Avoid
throw new Error('User not found in database table "users"'); // Reveals structure
throw new Error('Connection failed to postgres://...'); // Reveals connection string
```

## HTTPS & Transport

### Always use HTTPS in production
**Applies to**: All production deployments  
**Rule**: Enforce HTTPS, redirect HTTP to HTTPS.

```typescript
// ✅ Correct - in middleware or server config
if (process.env.NODE_ENV === 'production' && !request.secure) {
  return redirect(`https://${request.hostname}${request.url}`);
}
```

### Set security headers
**Applies to**: All responses  
**Rule**: Use security headers to protect against common attacks.

```typescript
// ✅ Correct
const headers = {
  'Strict-Transport-Security': 'max-age=63072000; includeSubDomains',
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': 'DENY',
  'X-XSS-Protection': '1; mode=block',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
};
```

## CORS

### Configure CORS properly
**Applies to**: APIs accessed from browsers  
**Rule**: Explicitly allow trusted origins, never use `*` in production.

```typescript
// ✅ Correct
const corsOptions = {
  origin: ['https://yourdomain.com', 'https://app.yourdomain.com'],
  credentials: true,
};

// ❌ Avoid in production
const corsOptions = {
  origin: '*', // Allows any origin
};
```

## Rate Limiting

### Implement rate limiting on sensitive endpoints
**Applies to**: Auth, API endpoints  
**Rule**: Limit request rates to prevent brute force and DoS.

```typescript
// ✅ Correct
import rateLimit from 'express-rate-limit';

const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 attempts
  message: 'Too many login attempts, please try again later',
});

app.post('/api/login', loginLimiter, loginHandler);
```

## Dependency Security

### Keep dependencies updated
**Applies to**: All projects  
**Rule**: Regularly update dependencies and audit for vulnerabilities.

```bash
# Run regularly
npm audit
npm audit fix

# Or use automated tools
npm install -g npm-check-updates
ncu -u
```

### Review dependencies before adding
**Applies to**: New dependencies  
**Rule**: Check package reputation, maintenance, and security before adding.

**Check:**
- Weekly downloads (npmjs.com)
- Last updated date
- Open issues count
- Security advisories
- License compatibility

## Logging

### Never log sensitive data
**Applies to**: All logging  
**Rule**: Don't log passwords, tokens, PII, or payment info.

```typescript
// ✅ Correct
console.log('User login attempt', { userId: user.id });

// ❌ Never
console.log('User login', { password: password, token: sessionToken });
```

### Sanitize logs
**Applies to**: Error logging  
**Rule**: Remove sensitive data before logging.

```typescript
// ✅ Correct
function sanitizeForLog(obj: any) {
  const { password, token, ssn, ...safe } = obj;
  return safe;
}

console.error('Request failed', sanitizeForLog(requestData));
```
