import React from 'react';
import { Paper, PaperProps, Box } from '@mui/material';

interface FormContainerProps extends PaperProps {
  title?: string;
  subtitle?: string;
  children: React.ReactNode;
}

const FormContainer: React.FC<FormContainerProps> = ({
  title,
  subtitle,
  children,
  ...props
}) => {
  return (
    <Paper
      elevation={0}
      sx={{
        p: { xs: 3, sm: 4 },
        mb: 4,
        borderRadius: 0,
        border: '1px solid rgba(0,0,0,0.06)'
      }}
      {...props}
    >
      {title && (
        <Box sx={{ mb: 3 }}>
          <h2
            style={{
              fontSize: '1.75rem',
              fontWeight: 700,
              color: '#6750A4',
              letterSpacing: '-0.02em',
              margin: 0,
              marginBottom: subtitle ? '8px' : '0'
            }}
          >
            {title}
          </h2>
          {subtitle && (
            <p
              style={{
                fontSize: '1rem',
                color: '#666',
                margin: 0,
                fontWeight: 400
              }}
            >
              {subtitle}
            </p>
          )}
        </Box>
      )}
      {children}
    </Paper>
  );
};

export default FormContainer;
