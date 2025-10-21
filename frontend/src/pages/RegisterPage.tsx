import React, { useState } from 'react';
import { Container, Alert, InputAdornment, IconButton } from '@mui/material';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import { useAuth } from '../contexts/AuthContext';
import { useNavigate } from 'react-router-dom';
import { 
  FormContainer, 
  FormTextField, 
  FormButton, 
  FormLink
} from '../components/forms';
import { validateEmail, validatePassword, validateUsername, validateFullName, validatePasswordMatch } from '../utils/formValidation';

const RegisterPage: React.FC = () => {
  const [formData, setFormData] = useState({
    email: '',
    username: '',
    password: '',
    confirmPassword: '',
    fullName: ''
  });
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirm, setShowConfirm] = useState(false);
  const [fieldErrors, setFieldErrors] = useState<Record<string, string>>({});
  
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleFieldChange = (field: string, value: string) => {
    setFormData(prev => ({ ...prev, [field]: value }));
    
    let error = '';
    switch (field) {
      case 'email':
        error = validateEmail(value) || '';
        break;
      case 'username':
        error = validateUsername(value) || '';
        break;
      case 'password':
        error = validatePassword(value) || '';
        break;
      case 'confirmPassword':
        error = validatePasswordMatch(formData.password, value) || '';
        break;
      case 'fullName':
        error = validateFullName(value) || '';
        break;
    }
    
    setFieldErrors(prev => ({ ...prev, [field]: error }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    // Validate all fields
    const emailError = validateEmail(formData.email);
    const usernameError = validateUsername(formData.username);
    const passwordError = validatePassword(formData.password);
    const confirmError = validatePasswordMatch(formData.password, formData.confirmPassword);
    const fullNameError = validateFullName(formData.fullName);

    if (emailError || usernameError || passwordError || confirmError || fullNameError) {
      setFieldErrors({
        email: emailError || '',
        username: usernameError || '',
        password: passwordError || '',
        confirmPassword: confirmError || '',
        fullName: fullNameError || ''
      });
      return;
    }

    setIsLoading(true);

    try {
      await register(formData.email, formData.username, formData.password, formData.fullName);
      setSuccess(true);
      setError('');
      // Redirect to login after showing success message
      setTimeout(() => navigate('/login'), 2500);
    } catch (err: any) {
      const backend = err?.response?.data?.detail;
      // Map common backend messages to friendlier hints
      let message = backend || err.message || 'Registration failed';
      if (/72 bytes/i.test(String(backend))) {
        message = 'Your password is too long. Please use up to 72 characters and avoid emoji or unusual symbols.';
      }
      setError(message);
      setSuccess(false);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Container maxWidth="sm" sx={{ py: 4 }}>
      <FormContainer title="Register">
        {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}
        {success && (
          <Alert severity="success" sx={{ mb: 2 }}>
            <strong>Registration Successful!</strong>
            <br />
            Your account has been created. Redirecting to login page...
          </Alert>
        )}

        <form onSubmit={handleSubmit}>
          <FormTextField
            fullWidth
            label="Full Name"
            value={formData.fullName}
            onChange={(e) => handleFieldChange('fullName', e.target.value)}
            error={!!fieldErrors.fullName}
            helperText={fieldErrors.fullName}
            required
            sx={{ mb: 3 }}
          />
          
          <FormTextField
            fullWidth
            label="Email"
            type="email"
            value={formData.email}
            onChange={(e) => handleFieldChange('email', e.target.value)}
            error={!!fieldErrors.email}
            helperText={fieldErrors.email}
            required
            sx={{ mb: 3 }}
          />
          
          <FormTextField
            fullWidth
            label="Username"
            value={formData.username}
            onChange={(e) => handleFieldChange('username', e.target.value)}
            error={!!fieldErrors.username}
            helperText={fieldErrors.username}
            required
            sx={{ mb: 3 }}
          />
          
          <FormTextField
            fullWidth
            label="Password"
            type={showPassword ? 'text' : 'password'}
            value={formData.password}
            onChange={(e) => handleFieldChange('password', e.target.value)}
            inputProps={{ maxLength: 72, minLength: 8 }}
            error={!!fieldErrors.password}
            helperText={fieldErrors.password || 'Password must be 8–72 characters. Avoid emoji or unusual symbols.'}
            required
            sx={{ mb: 3 }}
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton aria-label="toggle password visibility" onClick={() => setShowPassword(v => !v)} edge="end">
                    {showPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              )
            }}
          />
          
          <FormTextField
            fullWidth
            label="Confirm Password"
            type={showConfirm ? 'text' : 'password'}
            value={formData.confirmPassword}
            onChange={(e) => handleFieldChange('confirmPassword', e.target.value)}
            inputProps={{ maxLength: 72, minLength: 8 }}
            error={!!fieldErrors.confirmPassword}
            helperText={fieldErrors.confirmPassword}
            required
            sx={{ mb: 3 }}
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton aria-label="toggle confirm password visibility" onClick={() => setShowConfirm(v => !v)} edge="end">
                    {showConfirm ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              )
            }}
          />
          
          <FormButton
            type="submit"
            fullWidth
            disabled={isLoading || success}
            position="center"
            sx={{ mb: 2 }}
          >
            {isLoading ? 'Registering...' : success ? 'Registration Successful!' : 'Register'}
          </FormButton>
          
          <FormLink to="/login">
            Already have an account? Login here
          </FormLink>
        </form>
      </FormContainer>
    </Container>
  );
};

export default RegisterPage;