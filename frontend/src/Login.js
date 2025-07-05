import React, { useState } from 'react';
import { loginUser } from './api';

export default function Login({ onLogin }) {
  const [form, setForm] = useState({ username: '', password: '' });
  const [msg, setMsg] = useState('');

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });
  const handleSubmit = async e => {
    e.preventDefault();
    const res = await loginUser(form);
    if (res.access_token) {
      localStorage.setItem('token', res.access_token);
      setMsg('Login successful!');
      if (onLogin) onLogin(res.access_token);
    } else {
      setMsg(res.detail || 'Login failed');
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input name="username" placeholder="Username" value={form.username} onChange={handleChange} />
        <input name="password" type="password" placeholder="Password" value={form.password} onChange={handleChange} />
        <button type="submit">Login</button>
      </form>
      {msg && <div>{msg}</div>}
    </div>
  );
}
