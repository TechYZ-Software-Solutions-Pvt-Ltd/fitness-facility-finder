import React from 'react';
import { FormControl, InputLabel, Select, MenuItem, FormControlProps, SxProps, Theme } from '@mui/material';

interface FormSelectProps extends Omit<FormControlProps, 'sx' | 'onChange'> {
  label: string;
  value: string;
  onChange: (value: string) => void;
  options: Array<{ value: string; label: string }>;
  placeholder?: string;
  sx?: SxProps<Theme>;
}

const FormSelect: React.FC<FormSelectProps> = ({
  label,
  value,
  onChange,
  options,
  placeholder,
  sx,
  ...props
}) => {
  return (
    <FormControl
      variant="outlined"
      sx={{
        '& .MuiInputLabel-root': {
          fontSize: '1rem',
          fontWeight: 500
        },
        '& .MuiSelect-select': {
          fontSize: '1rem',
          py: 1.5
        },
        '& .MuiOutlinedInput-root': {
          borderRadius: 1
        },
        ...sx
      }}
      {...props}
    >
      <InputLabel id={`${label.toLowerCase().replace(/\s+/g, '-')}-label`}>
        {label}
      </InputLabel>
      <Select
        labelId={`${label.toLowerCase().replace(/\s+/g, '-')}-label`}
        label={label}
        value={value}
        onChange={(e) => onChange(e.target.value as string)}
        MenuProps={{
          PaperProps: {
            sx: {
              borderRadius: 0
            }
          }
        }}
      >
        {placeholder && (
          <MenuItem value="" disabled>
            {placeholder}
          </MenuItem>
        )}
        {options.map((option) => (
          <MenuItem 
            key={option.value} 
            value={option.value}
            sx={{ fontSize: '1rem' }}
          >
            {option.label}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
};

export default FormSelect;
