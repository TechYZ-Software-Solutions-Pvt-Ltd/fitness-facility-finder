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
import { validateUsername, validatePassword } from '../utils/formValidation';

const LoginPage: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [fieldErrors, setFieldErrors] = useState<Record<string, string>>({});
  
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleFieldChange = (field: string, value: string) => {
    if (field === 'username') {
      setUsername(value);
      const error = validateUsername(value) || '';
      setFieldErrors(prev => ({ ...prev, username: error }));
    } else if (field === 'password') {
      setPassword(value);
      const error = validatePassword(value) || '';
      setFieldErrors(prev => ({ ...prev, password: error }));
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    
    // Validate fields
    const usernameError = validateUsername(username);
    const passwordError = validatePassword(password);
    
    if (usernameError || passwordError) {
      setFieldErrors({
        username: usernameError || '',
        password: passwordError || ''
      });
      return;
    }

    setIsLoading(true);

    try {
      await login(username, password);
      navigate('/');
    } catch (err: any) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Container maxWidth="sm" sx={{ py: 4 }}>
      <FormContainer title="Login">
        {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}

        <form onSubmit={handleSubmit}>
          <FormTextField
            fullWidth
            label="Username"
            value={username}
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
            value={password}
            onChange={(e) => handleFieldChange('password', e.target.value)}
            error={!!fieldErrors.password}
            helperText={fieldErrors.password}
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
          
          <FormButton
            type="submit"
            fullWidth
            disabled={isLoading}
            position="center"
            sx={{ mb: 2 }}
          >
            {isLoading ? 'Logging in...' : 'Login'}
          </FormButton>
          
          <FormLink to="/register">
            Don't have an account? Register here
          </FormLink>
        </form>
      </FormContainer>
    </Container>
  );
};

export default LoginPage;