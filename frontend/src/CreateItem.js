import React, { useState } from 'react';
import { createItem } from './api';

export default function CreateItem() {
  const [form, setForm] = useState({ name: '', description: '' });
  const [msg, setMsg] = useState('');

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });
  const handleSubmit = async e => {
    e.preventDefault();
    const token = localStorage.getItem('token');
    if (!token) return setMsg('Not logged in');
    const res = await createItem(form, token);
    setMsg(res.detail || JSON.stringify(res));
  };

  return (
    <div>
      <h2>Create Item</h2>
      <form onSubmit={handleSubmit}>
        <input name="name" placeholder="Name" value={form.name} onChange={handleChange} />
        <input name="description" placeholder="Description" value={form.description} onChange={handleChange} />
        <button type="submit">Create</button>
      </form>
      {msg && <div>{msg}</div>}
    </div>
  );
}
