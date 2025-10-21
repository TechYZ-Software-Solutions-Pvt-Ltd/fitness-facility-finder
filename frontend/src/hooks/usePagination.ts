import { useState, useCallback, useMemo } from 'react';

export interface PaginationState {
  page: number;
  limit: number;
  total: number;
  totalPages: number;
}

export interface UsePaginationOptions {
  initialPage?: number;
  initialLimit?: number;
  total?: number;
}

export function usePagination(options: UsePaginationOptions = {}) {
  const { initialPage = 1, initialLimit = 10, total = 0 } = options;

  const [state, setState] = useState<PaginationState>({
    page: initialPage,
    limit: initialLimit,
    total,
    totalPages: Math.ceil(total / initialLimit),
  });

  const setPage = useCallback((page: number) => {
    setState(prev => ({
      ...prev,
      page: Math.max(1, Math.min(page, prev.totalPages)),
    }));
  }, []);

  const setLimit = useCallback((limit: number) => {
    setState(prev => {
      const newTotalPages = Math.ceil(prev.total / limit);
      return {
        ...prev,
        limit,
        totalPages: newTotalPages,
        page: Math.min(prev.page, newTotalPages),
      };
    });
  }, []);

  const setTotal = useCallback((total: number) => {
    setState(prev => ({
      ...prev,
      total,
      totalPages: Math.ceil(total / prev.limit),
    }));
  }, []);

  const nextPage = useCallback(() => {
    setState(prev => ({
      ...prev,
      page: Math.min(prev.page + 1, prev.totalPages),
    }));
  }, []);

  const prevPage = useCallback(() => {
    setState(prev => ({
      ...prev,
      page: Math.max(prev.page - 1, 1),
    }));
  }, []);

  const goToFirstPage = useCallback(() => {
    setState(prev => ({ ...prev, page: 1 }));
  }, []);

  const goToLastPage = useCallback(() => {
    setState(prev => ({ ...prev, page: prev.totalPages }));
  }, []);

  const reset = useCallback(() => {
    setState({
      page: initialPage,
      limit: initialLimit,
      total,
      totalPages: Math.ceil(total / initialLimit),
    });
  }, [initialPage, initialLimit, total]);

  const paginationInfo = useMemo(() => {
    const startItem = (state.page - 1) * state.limit + 1;
    const endItem = Math.min(state.page * state.limit, state.total);
    
    return {
      startItem,
      endItem,
      hasNextPage: state.page < state.totalPages,
      hasPrevPage: state.page > 1,
      isEmpty: state.total === 0,
    };
  }, [state]);

  return {
    ...state,
    setPage,
    setLimit,
    setTotal,
    nextPage,
    prevPage,
    goToFirstPage,
    goToLastPage,
    reset,
    ...paginationInfo,
  };
}
