import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;
console.log("Loaded API_URL is:", API_URL);


export const fetchExpenses = () => axios.get(API_URL);
export const createExpense = (data) => axios.post(API_URL, data);
export const updateExpense = (id, data) => axios.put(`${API_URL}/${id}`, data);
export const deleteExpense = (id) => axios.delete(`${API_URL}/${id}`);
