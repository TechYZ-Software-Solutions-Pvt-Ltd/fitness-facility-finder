import { baseApi } from './baseApi';
import { ApiResponse, PaginatedResponse, BaseEntity } from '../types';
import { useApi } from '../hooks';

export interface GenericServiceOptions {
  endpoint: string;
  transform?: (data: any) => any;
}

export class GenericService<T extends BaseEntity> {
  private endpoint: string;
  private transform?: (data: any) => T;

  constructor(options: GenericServiceOptions) {
    this.endpoint = options.endpoint;
    this.transform = options.transform;
  }

  private transformData(data: any): T {
    if (this.transform) {
      return this.transform(data);
    }
    return data;
  }

  private transformList(data: any[]): T[] {
    return data.map(item => this.transformData(item));
  }

  // CRUD operations
  async getAll(params?: Record<string, any>): Promise<ApiResponse<T[]>> {
    const response = await baseApi.get(this.endpoint, { params });
    return {
      ...response,
      data: this.transformList(response.data),
    };
  }

  async getById(id: string): Promise<ApiResponse<T>> {
    const response = await baseApi.get(`${this.endpoint}/${id}`);
    return {
      ...response,
      data: this.transformData(response.data),
    };
  }

  async create(data: Partial<T>): Promise<ApiResponse<T>> {
    const response = await baseApi.post(this.endpoint, data);
    return {
      ...response,
      data: this.transformData(response.data),
    };
  }

  async update(id: string, data: Partial<T>): Promise<ApiResponse<T>> {
    const response = await baseApi.put(`${this.endpoint}/${id}`, data);
    return {
      ...response,
      data: this.transformData(response.data),
    };
  }

  async patch(id: string, data: Partial<T>): Promise<ApiResponse<T>> {
    const response = await baseApi.patch(`${this.endpoint}/${id}`, data);
    return {
      ...response,
      data: this.transformData(response.data),
    };
  }

  async delete(id: string): Promise<ApiResponse<void>> {
    return await baseApi.delete(`${this.endpoint}/${id}`);
  }

  // Paginated operations
  async getPaginated(params: {
    page?: number;
    limit?: number;
    search?: string;
    sort?: string;
    filters?: Record<string, any>;
  }): Promise<ApiResponse<PaginatedResponse<T>>> {
    const response = await baseApi.get(this.endpoint, { params });
    return {
      ...response,
      data: {
        ...response.data,
        data: this.transformList(response.data.data),
      },
    };
  }

  // Search operations
  async search(query: string, params?: Record<string, any>): Promise<ApiResponse<T[]>> {
    const response = await baseApi.get(`${this.endpoint}/search`, {
      params: { q: query, ...params },
    });
    return {
      ...response,
      data: this.transformList(response.data),
    };
  }

  // Bulk operations
  async bulkCreate(data: Partial<T>[]): Promise<ApiResponse<T[]>> {
    const response = await baseApi.post(`${this.endpoint}/bulk`, data);
    return {
      ...response,
      data: this.transformList(response.data),
    };
  }

  async bulkUpdate(updates: Array<{ id: string; data: Partial<T> }>): Promise<ApiResponse<T[]>> {
    const response = await baseApi.put(`${this.endpoint}/bulk`, updates);
    return {
      ...response,
      data: this.transformList(response.data),
    };
  }

  async bulkDelete(ids: string[]): Promise<ApiResponse<void>> {
    return await baseApi.delete(`${this.endpoint}/bulk`, { data: { ids } });
  }

  // Custom endpoint operations
  async customGet<U = any>(customEndpoint: string, params?: Record<string, any>): Promise<ApiResponse<U>> {
    return await baseApi.get(`${this.endpoint}${customEndpoint}`, { params });
  }

  async customPost<U = any>(customEndpoint: string, data?: any): Promise<ApiResponse<U>> {
    return await baseApi.post(`${this.endpoint}${customEndpoint}`, data);
  }

  async customPut<U = any>(customEndpoint: string, data?: any): Promise<ApiResponse<U>> {
    return await baseApi.put(`${this.endpoint}${customEndpoint}`, data);
  }

  async customDelete<U = any>(customEndpoint: string): Promise<ApiResponse<U>> {
    return await baseApi.delete(`${this.endpoint}${customEndpoint}`);
  }
}

// Hook for using generic service
export function useGenericService<T extends BaseEntity>(
  service: GenericService<T>,
  options?: {
    immediate?: boolean;
    params?: Record<string, any>;
  }
) {
  return useApi(() => service.getAll(options?.params), {
    immediate: options?.immediate,
  });
}

// Factory function to create service instances
export function createService<T extends BaseEntity>(
  endpoint: string,
  transform?: (data: any) => T
): GenericService<T> {
  return new GenericService<T>({ endpoint, transform });
}
