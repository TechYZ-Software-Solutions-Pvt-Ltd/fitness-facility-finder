// Generic form validation utilities
export interface ValidationRule {
  required?: boolean;
  minLength?: number;
  maxLength?: number;
  pattern?: RegExp;
  custom?: (value: string) => string | null;
  message?: string;
}

export interface ValidationResult {
  isValid: boolean;
  errors: Record<string, string>;
}

export const validationRules = {
  email: {
    required: true,
    pattern: /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/i,
    message: 'Please enter a valid email address'
  },
  password: {
    required: true,
    minLength: 8,
    maxLength: 72,
    custom: (value: string) => {
      const byteLength = new TextEncoder().encode(value).length;
      if (byteLength > 72) {
        return 'Password is too long. Please use up to 72 characters and avoid emoji or unusual symbols.';
      }
      return null;
    },
    message: 'Password must be 8–72 characters. Avoid emoji or unusual symbols.'
  },
  username: {
    required: true,
    minLength: 3,
    maxLength: 50,
    pattern: /^[a-zA-Z0-9_]+$/,
    message: 'Username must be 3-50 characters and contain only letters, numbers, and underscores'
  },
  fullName: {
    required: true,
    minLength: 2,
    maxLength: 100,
    message: 'Full name must be 2-100 characters'
  },
  apiKey: {
    required: true,
    minLength: 20,
    pattern: /^AIza[A-Za-z0-9_-]{35}$/,
    message: 'Please enter a valid Google Places API key'
  }
};

export const validateField = (value: string, rules: ValidationRule): string | null => {
  if (rules.required && (!value || value.trim() === '')) {
    return 'This field is required';
  }

  if (value && rules.minLength && value.length < rules.minLength) {
    return `Must be at least ${rules.minLength} characters`;
  }

  if (value && rules.maxLength && value.length > rules.maxLength) {
    return `Must be no more than ${rules.maxLength} characters`;
  }

  if (value && rules.pattern && !rules.pattern.test(value)) {
    return rules.message || 'Invalid format';
  }

  if (value && rules.custom) {
    return rules.custom(value);
  }

  return null;
};

export const validateForm = (data: Record<string, string>, rules: Record<string, ValidationRule>): ValidationResult => {
  const errors: Record<string, string> = {};
  let isValid = true;

  Object.keys(rules).forEach(field => {
    const error = validateField(data[field] || '', rules[field]);
    if (error) {
      errors[field] = error;
      isValid = false;
    }
  });

  return { isValid, errors };
};

export const validatePasswordMatch = (password: string, confirmPassword: string): string | null => {
  if (password !== confirmPassword) {
    return 'Passwords do not match';
  }
  return null;
};

export const validateEmail = (email: string): string | null => {
  return validateField(email, validationRules.email);
};

export const validatePassword = (password: string): string | null => {
  return validateField(password, validationRules.password);
};

export const validateUsername = (username: string): string | null => {
  return validateField(username, validationRules.username);
};

export const validateFullName = (fullName: string): string | null => {
  return validateField(fullName, validationRules.fullName);
};

export const validateApiKey = (apiKey: string): string | null => {
  return validateField(apiKey, validationRules.apiKey);
};
