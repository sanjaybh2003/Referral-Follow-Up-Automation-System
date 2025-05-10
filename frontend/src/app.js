import React, { useState, useEffect } from 'react';
import { login, register, getExpenses, createExpense, getCategories, createCategory } from './api';
import './App.css';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [token, setToken] = useState('');
  const [expenses, setExpenses] = useState([]);
  const [categories, setCategories] = useState([]);
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    email: '',
    amount: '',
    description: '',
    category_id: '',
    category_name: ''
  });

  useEffect(() => {
    const storedToken = localStorage.getItem('token');
    if (storedToken) {
      setToken(storedToken);
      setIsAuthenticated(true);
      fetchData(storedToken);
    }
  }, []);

  const fetchData = async (authToken) => {
    try {
      const [expensesData, categoriesData] = await Promise.all([
        getExpenses(authToken),
        getCategories(authToken)
      ]);
      setExpenses(expensesData);
      setCategories(categoriesData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await login(formData);
      if (response.token) {
        localStorage.setItem('token', response.token);
        setIsAuthenticated(true);
      }
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const response = await register({
        username: formData.username,
        email: formData.email,
        password: formData.password
      });
      if (response.id) {
        alert('Registration successful! Please login.');
      }
    } catch (error) {
      console.error('Registration error:', error);
    }
  };

  const handleAddExpense = async (e) => {
    e.preventDefault();
    try {
      const response = await createExpense({
        amount: parseFloat(formData.amount),
        description: formData.description,
        category_id: parseInt(formData.category_id)
      }, token);
      setExpenses([...expenses, response]);
      setFormData({ ...formData, amount: '', description: '', category_id: '' });
    } catch (error) {
      console.error('Error adding expense:', error);
    }
  };

  const handleAddCategory = async (e) => {
    e.preventDefault();
    try {
      const response = await createCategory({
        name: formData.category_name
      }, token);
      setCategories([...categories, response]);
      setFormData({ ...formData, category_name: '' });
    } catch (error) {
      console.error('Error adding category:', error);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    setToken('');
    setIsAuthenticated(false);
    setExpenses([]);
    setCategories([]);
  };

  if (!isAuthenticated) {
    return (
      <div className="App">
        <h1>Expense Tracker</h1>
        <div className="auth-forms">
          <div className="login-form">
            <h2>Login</h2>
            <form onSubmit={handleLogin}>
              <input
                type="text"
                name="username"
                placeholder="Username"
                value={formData.username}
                onChange={handleInputChange}
              />
              <input
                type="password"
                name="password"
                placeholder="Password"
                value={formData.password}
                onChange={handleInputChange}
              />
              <button type="submit">Login</button>
            </form>
          </div>
          <div className="register-form">
            <h2>Register</h2>
            <form onSubmit={handleRegister}>
              <input
                type="text"
                name="username"
                placeholder="Username"
                value={formData.username}
                onChange={handleInputChange}
              />
              <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleInputChange}
              />
              <input
                type="password"
                name="password"
                placeholder="Password"
                value={formData.password}
                onChange={handleInputChange}
              />
              <button type="submit">Register</button>
            </form>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="App">
      <h1>Expense Tracker</h1>
      <button onClick={handleLogout}>Logout</button>
      
      <div className="expense-form">
        <h2>Add Expense</h2>
        <form onSubmit={handleAddExpense}>
          <input
            type="number"
            name="amount"
            placeholder="Amount"
            value={formData.amount}
            onChange={handleInputChange}
          />
          <input
            type="text"
            name="description"
            placeholder="Description"
            value={formData.description}
            onChange={handleInputChange}
          />
          <select
            name="category_id"
            value={formData.category_id}
            onChange={handleInputChange}
          >
            <option value="">Select Category</option>
            {categories.map(category => (
              <option key={category.id} value={category.id}>
                {category.name}
              </option>
            ))}
          </select>
          <button type="submit">Add Expense</button>
        </form>
      </div>

      <div className="category-form">
        <h2>Add Category</h2>
        <form onSubmit={handleAddCategory}>
          <input
            type="text"
            name="category_name"
            placeholder="Category Name"
            value={formData.category_name}
            onChange={handleInputChange}
          />
          <button type="submit">Add Category</button>
        </form>
      </div>

      <div className="expenses-list">
        <h2>Expenses</h2>
        <table>
          <thead>
            <tr>
              <th>Amount</th>
              <th>Description</th>
              <th>Category</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            {expenses.map(expense => (
              <tr key={expense.id}>
                <td>${expense.amount}</td>
                <td>{expense.description}</td>
                <td>
                  {categories.find(c => c.id === expense.category_id)?.name}
                </td>
                <td>{new Date(expense.date).toLocaleDateString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
