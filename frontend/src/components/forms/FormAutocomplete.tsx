import React from 'react';
import { Autocomplete, AutocompleteProps, TextField, SxProps, Theme } from '@mui/material';

interface FormAutocompleteProps<T> extends Omit<AutocompleteProps<T, false, false, false>, 'renderInput' | 'sx'> {
  label: string;
  placeholder?: string;
  getOptionLabel: (option: T) => string;
  sx?: SxProps<Theme>;
}

const FormAutocomplete = <T,>({
  label,
  placeholder,
  getOptionLabel,
  sx,
  ...props
}: FormAutocompleteProps<T>) => {
  return (
    <Autocomplete
      disablePortal
      sx={{
        '& .MuiInputLabel-root': {
          fontSize: '1rem',
          fontWeight: 500
        },
        '& .MuiInputBase-input': {
          fontSize: '1rem',
          py: 1.5
        },
        '& .MuiOutlinedInput-root': {
          borderRadius: 1
        },
        ...sx
      }}
      ListboxProps={{
        sx: {
          '& .MuiPaper-root': {
            borderRadius: 0
          }
        }
      }}
      renderInput={(params) => (
        <TextField
          {...params}
          label={label}
          placeholder={placeholder}
          sx={{
            '& .MuiInputLabel-root': {
              fontSize: '1rem',
              fontWeight: 500
            },
            '& .MuiInputBase-input': {
              fontSize: '1rem',
              py: 1.5
            },
            '& .MuiFormHelperText-root': {
              fontSize: '0.875rem',
              fontWeight: 400
            },
            '& .MuiOutlinedInput-root': {
              borderRadius: 1
            }
          }}
        />
      )}
      getOptionLabel={getOptionLabel}
      {...props}
    />
  );
};

export default FormAutocomplete;
