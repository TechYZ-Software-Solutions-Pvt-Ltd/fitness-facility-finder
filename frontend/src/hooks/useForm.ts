import { useState, useCallback, useMemo } from 'react';
import { validateForm, ValidationResult } from '../utils/formValidation';

export interface FormField {
  value: string;
  error: string;
  touched: boolean;
}

export interface FormState {
  [key: string]: FormField;
}

export interface UseFormOptions {
  initialValues?: Record<string, string>;
  validationRules?: Record<string, any>;
  onSubmit?: (values: Record<string, string>) => void | Promise<void>;
}

export function useForm(options: UseFormOptions = {}) {
  const { initialValues = {}, validationRules = {}, onSubmit } = options;

  const [formState, setFormState] = useState<FormState>(() => {
    const state: FormState = {};
    Object.keys(initialValues).forEach(key => {
      state[key] = {
        value: initialValues[key] || '',
        error: '',
        touched: false,
      };
    });
    return state;
  });

  const [isSubmitting, setIsSubmitting] = useState(false);

  const setFieldValue = useCallback((field: string, value: string) => {
    setFormState(prev => ({
      ...prev,
      [field]: {
        ...prev[field],
        value,
        error: '', // Clear error when user types
      },
    }));
  }, []);

  const setFieldError = useCallback((field: string, error: string) => {
    setFormState(prev => ({
      ...prev,
      [field]: {
        ...prev[field],
        error,
      },
    }));
  }, []);

  const setFieldTouched = useCallback((field: string, touched: boolean = true) => {
    setFormState(prev => ({
      ...prev,
      [field]: {
        ...prev[field],
        touched,
      },
    }));
  }, []);

  const validateField = useCallback((field: string, value: string) => {
    const rules = validationRules[field];
    if (!rules) return '';

    // Import validation function dynamically to avoid circular dependency
    const { validateField: validateFieldUtil } = require('../utils/formValidation');
    return validateFieldUtil(value, rules) || '';
  }, [validationRules]);

  const validateAllFields = useCallback(() => {
    const values = getValues();
    const validation = validateForm(values, validationRules);
    
    // Update form state with errors
    Object.keys(validation.errors).forEach(field => {
      setFieldError(field, validation.errors[field]);
    });

    return validation.isValid;
  }, [validationRules, setFieldError]);

  const getValues = useCallback(() => {
    const values: Record<string, string> = {};
    Object.keys(formState).forEach(key => {
      values[key] = formState[key].value;
    });
    return values;
  }, [formState]);

  const getFieldProps = useCallback((field: string) => {
    const fieldState = formState[field] || { value: '', error: '', touched: false };
    
    return {
      value: fieldState.value,
      error: !!fieldState.error,
      helperText: fieldState.error,
      onChange: (e: React.ChangeEvent<HTMLInputElement>) => {
        setFieldValue(field, e.target.value);
        // Validate field on change if it's been touched
        if (fieldState.touched) {
          const error = validateField(field, e.target.value);
          setFieldError(field, error);
        }
      },
      onBlur: () => {
        setFieldTouched(field);
        const error = validateField(field, fieldState.value);
        setFieldError(field, error);
      },
    };
  }, [formState, setFieldValue, setFieldError, setFieldTouched, validateField]);

  const handleSubmit = useCallback(async (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    
    // Mark all fields as touched
    Object.keys(formState).forEach(field => {
      setFieldTouched(field);
    });

    // Validate all fields
    const isValid = validateAllFields();
    if (!isValid) return;

    if (onSubmit) {
      setIsSubmitting(true);
      try {
        await onSubmit(getValues());
      } catch (error) {
        console.error('Form submission error:', error);
      } finally {
        setIsSubmitting(false);
      }
    }
  }, [formState, validateAllFields, onSubmit, getValues, setFieldTouched]);

  const reset = useCallback(() => {
    const newState: FormState = {};
    Object.keys(initialValues).forEach(key => {
      newState[key] = {
        value: initialValues[key] || '',
        error: '',
        touched: false,
      };
    });
    setFormState(newState);
    setIsSubmitting(false);
  }, [initialValues]);

  const isFormValid = useMemo(() => {
    return Object.values(formState).every(field => !field.error);
  }, [formState]);

  const hasErrors = useMemo(() => {
    return Object.values(formState).some(field => !!field.error);
  }, [formState]);

  const isDirty = useMemo(() => {
    return Object.keys(formState).some(key => {
      const currentValue = formState[key].value;
      const initialValue = initialValues[key] || '';
      return currentValue !== initialValue;
    });
  }, [formState, initialValues]);

  return {
    formState,
    isSubmitting,
    isFormValid,
    hasErrors,
    isDirty,
    getValues,
    getFieldProps,
    setFieldValue,
    setFieldError,
    setFieldTouched,
    validateField,
    validateAllFields,
    handleSubmit,
    reset,
  };
}
