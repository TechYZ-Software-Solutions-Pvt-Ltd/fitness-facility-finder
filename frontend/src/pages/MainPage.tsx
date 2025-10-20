import React, { useState } from 'react';
import { Container, Box } from '@mui/material';
import SearchForm from '../components/SearchForm';
import ResultsDisplay from '../components/ResultsDisplay';

const MainPage: React.FC = () => {
  const [searchResults, setSearchResults] = useState(null);

  const handleSearch = (results: any) => {
    setSearchResults(results);
  };

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Box sx={{ maxWidth: '800px', mx: 'auto' }}>
        <SearchForm onSearch={handleSearch} />
        <ResultsDisplay results={searchResults} />
      </Box>
    </Container>
  );
};

export default MainPage;