import React, { useState, useEffect } from 'react';
import ExpenseForm from './components/ExpenseForm';
import ExpenseList from './components/ExpenseList';
import Dashboard from './components/Dashboard';
import { fetchExpenses, deleteExpense } from './api';
import './App.css';

function App() {
  const [expenses, setExpenses] = useState([]);
  const [editing, setEditing] = useState(false);
  const [toEdit, setToEdit] = useState(null);

  const load = async () => {
    const res = await fetchExpenses();
    setExpenses(res.data);
    setEditing(false);
  };

  useEffect(() => { load(); }, []);

  const handleEdit = expense => {
    setToEdit(expense);
    setEditing(true);
  };

  const handleDelete = async id => {
    await deleteExpense(id);
    load();
  };

  return (
    <div className="app-container">
      <h1>Expense Tracker</h1>
      <ExpenseForm editing={editing} expenseToEdit={toEdit} onSaved={load} />
      <ExpenseList expenses={expenses} onEdit={handleEdit} onDelete={handleDelete} />
      <Dashboard expenses={expenses} />
    </div>
  );
}

export default App;
