# Generic System Documentation

This document outlines the comprehensive generic system implemented for the Facility Search application. The system provides reusable components, hooks, utilities, and services that can be used throughout the application and in future development.

## 🏗️ Architecture Overview

The generic system is organized into several key areas:

- **Hooks** - Custom React hooks for common functionality
- **Utils** - Utility functions for formatting, validation, and data processing
- **Services** - Generic API service layer
- **Types** - TypeScript type definitions
- **Components** - Reusable UI components
- **Layout** - Layout components for consistent page structure

## 📁 File Structure

```
src/
├── hooks/
│   ├── useApi.ts          # API state management
│   ├── useForm.ts         # Form handling
│   ├── useLocalStorage.ts # Local storage management
│   ├── usePagination.ts   # Pagination logic
│   ├── useDebounce.ts     # Debouncing utilities
│   └── index.ts
├── utils/
│   ├── formValidation.ts  # Form validation utilities
│   ├── formatting.ts      # Data formatting functions
│   ├── helpers.ts         # General helper functions
│   ├── constants.ts       # Application constants
│   └── index.ts
├── services/
│   ├── baseApi.ts         # Base API service
│   ├── genericService.ts  # Generic CRUD service
│   └── api.ts            # Existing API service
├── types/
│   ├── common.ts         # Common type definitions
│   └── index.ts
├── components/
│   ├── forms/            # Form components
│   ├── layout/           # Layout components
│   ├── ui/              # UI components
│   └── generic/         # Generic exports
└── GENERIC_SYSTEM.md    # This documentation
```

## 🎣 Custom Hooks

### useApi
Generic hook for API state management with loading, error, and data states.

```typescript
const { data, loading, error, execute, reset } = useApi(apiFunction, {
  immediate: true,
  onSuccess: (data) => console.log('Success:', data),
  onError: (error) => console.error('Error:', error)
});
```

### useForm
Comprehensive form handling with validation, field management, and submission.

```typescript
const form = useForm({
  initialValues: { name: '', email: '' },
  validationRules: { name: validationRules.required, email: validationRules.email },
  onSubmit: async (values) => { /* handle submission */ }
});

// Use in component
<FormTextField {...form.getFieldProps('name')} />
```

### useLocalStorage
Persistent state management with localStorage.

```typescript
const [value, setValue, removeValue] = useLocalStorage('key', defaultValue);
```

### usePagination
Pagination state management with helper methods.

```typescript
const pagination = usePagination({
  initialPage: 1,
  initialLimit: 10,
  total: 100
});
```

### useDebounce
Debounced values and callbacks.

```typescript
const debouncedValue = useDebounce(value, 300);
const debouncedCallback = useDebouncedCallback(callback, 500);
```

## 🛠️ Utility Functions

### Form Validation
```typescript
import { validateEmail, validatePassword, validateForm } from '../utils';

const emailError = validateEmail(email);
const validation = validateForm(data, rules);
```

### Formatting
```typescript
import { formatPhoneNumber, formatCurrency, formatDate } from '../utils';

const phone = formatPhoneNumber('1234567890'); // (123) 456-7890
const currency = formatCurrency(1234.56); // $1,234.56
const date = formatDate(new Date()); // January 1, 2024
```

### Helpers
```typescript
import { deepClone, groupBy, sortBy, unique } from '../utils';

const cloned = deepClone(original);
const grouped = groupBy(array, 'category');
const sorted = sortBy(array, 'name', 'asc');
const uniqueItems = unique(array);
```

## 🔌 Services

### Base API Service
```typescript
import { baseApi } from '../services/baseApi';

const response = await baseApi.get('/endpoint');
const data = await baseApi.post('/endpoint', payload);
```

### Generic Service
```typescript
import { createService } from '../services/genericService';

const userService = createService<User>('/users');
const users = await userService.getAll();
const user = await userService.getById('1');
```

## 🎨 Components

### Form Components
- `FormTextField` - Text input with consistent styling
- `FormSelect` - Dropdown with unified appearance
- `FormButton` - Button with positioning and styling
- `FormContainer` - Form wrapper with title support

### Layout Components
- `PageLayout` - Page container with responsive design
- `Section` - Content section with optional title
- `Grid` / `GridItem` - Responsive grid system

### UI Components
- `LoadingSpinner` - Loading indicator
- `EmptyState` - Empty state display
- `ErrorBoundary` - Error boundary wrapper

## 📝 TypeScript Types

### Common Types
```typescript
interface BaseEntity {
  id: string;
  createdAt: string;
  updatedAt: string;
}

interface ApiResponse<T> {
  data: T;
  message?: string;
  success: boolean;
  status: number;
}

interface PaginatedResponse<T> {
  data: T[];
  total: number;
  page: number;
  limit: number;
  totalPages: number;
}
```

## 🚀 Usage Examples

### Creating a New Form
```typescript
import { useForm, FormContainer, FormTextField, FormButton } from '../components/generic';

const MyForm = () => {
  const form = useForm({
    initialValues: { name: '', email: '' },
    validationRules: {
      name: { required: true, minLength: 2 },
      email: { required: true, pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/ }
    },
    onSubmit: async (values) => {
      // Handle form submission
    }
  });

  return (
    <FormContainer title="My Form">
      <form onSubmit={form.handleSubmit}>
        <FormTextField {...form.getFieldProps('name')} />
        <FormTextField {...form.getFieldProps('email')} />
        <FormButton type="submit" disabled={!form.isFormValid}>
          Submit
        </FormButton>
      </form>
    </FormContainer>
  );
};
```

### Creating a New API Service
```typescript
import { createService } from '../services/genericService';

interface Product extends BaseEntity {
  name: string;
  price: number;
  category: string;
}

const productService = createService<Product>('/products', (data) => ({
  ...data,
  price: parseFloat(data.price)
}));

// Usage
const products = await productService.getAll();
const product = await productService.create({ name: 'New Product', price: 99.99 });
```

### Using Layout Components
```typescript
import { PageLayout, Section, Grid, GridItem } from '../components/generic';

const MyPage = () => (
  <PageLayout maxWidth="lg" padding={3}>
    <Section title="Products" subtitle="Manage your products">
      <Grid spacing={3}>
        <GridItem xs={12} md={6}>
          {/* Content */}
        </GridItem>
        <GridItem xs={12} md={6}>
          {/* Content */}
        </GridItem>
      </Grid>
    </Section>
  </PageLayout>
);
```

## 🔧 Configuration

### Constants
All application constants are centralized in `utils/constants.ts`:

```typescript
import { API_ENDPOINTS, HTTP_STATUS, VALIDATION } from '../utils/constants';
```

### Environment Variables
```typescript
// .env
REACT_APP_API_URL=http://localhost:8000
REACT_APP_ENVIRONMENT=development
```

## 📋 Best Practices

1. **Always use generic components** when available
2. **Extend existing types** rather than creating new ones
3. **Use the generic service** for CRUD operations
4. **Leverage custom hooks** for state management
5. **Follow the established patterns** for consistency
6. **Add new utilities** to the appropriate utility files
7. **Document new components** with JSDoc comments

## 🔄 Migration Guide

### From Old Components to Generic Components

1. Replace direct MUI components with generic form components
2. Use `useForm` hook instead of manual state management
3. Replace custom API calls with generic service methods
4. Use layout components for consistent page structure
5. Leverage utility functions for common operations

### Example Migration

**Before:**
```typescript
const [name, setName] = useState('');
const [email, setEmail] = useState('');
const [errors, setErrors] = useState({});

<TextField
  value={name}
  onChange={(e) => setName(e.target.value)}
  error={!!errors.name}
  helperText={errors.name}
/>
```

**After:**
```typescript
const form = useForm({
  initialValues: { name: '', email: '' },
  validationRules: { name: validationRules.required }
});

<FormTextField {...form.getFieldProps('name')} />
```

## 🎯 Future Enhancements

- [ ] Add more form field types (date picker, file upload, etc.)
- [ ] Implement generic table component
- [ ] Add generic modal and drawer components
- [ ] Create generic notification system
- [ ] Add generic chart components
- [ ] Implement generic search and filter components

## 📞 Support

For questions or issues with the generic system, please refer to:
- This documentation
- Component source code with JSDoc comments
- TypeScript type definitions
- Example usage in existing components
