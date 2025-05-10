import axios from 'axios';

const API_BASE_URL = 'https://5211-117-244-2-65.ngrok-free.app';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add request interceptor to add token to requests
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export const login = async (credentials) => {
    const response = await api.post('/api/users/login', credentials);
    return response.data;
};

export const register = async (userData) => {
    const response = await api.post('/api/users/register', userData);
    return response.data;
};

export const getExpenses = async () => {
    const response = await api.get('/api/expenses');
    return response.data;
};

export const createExpense = async (expenseData) => {
    const response = await api.post('/api/expenses', expenseData);
    return response.data;
};

export const getCategories = async () => {
    const response = await api.get('/api/categories');
    return response.data;
};

export const createCategory = async (categoryData) => {
    const response = await api.post('/api/categories', categoryData);
    return response.data;
};
