import React from 'react';
import { Link as MuiLink, LinkProps as MuiLinkProps, Box } from '@mui/material';
import { Link as RouterLink } from 'react-router-dom';

interface FormLinkProps extends Omit<MuiLinkProps, 'sx' | 'component'> {
  children: React.ReactNode;
  center?: boolean;
  to?: string;
  href?: string;
  sx?: any;
}

const FormLink: React.FC<FormLinkProps> = ({
  children,
  center = true,
  to,
  href,
  sx,
  ...props
}) => {
  const linkProps = to ? { component: RouterLink, to } : { href };
  
  return (
    <Box
      sx={{
        textAlign: center ? 'center' : 'left',
        mt: 2,
        ...sx
      }}
    >
      <MuiLink
        variant="body2"
        sx={{
          textDecoration: 'none',
          '&:hover': {
            textDecoration: 'underline'
          }
        }}
        {...linkProps}
        {...props}
      >
        {children}
      </MuiLink>
    </Box>
  );
};

export default FormLink;
