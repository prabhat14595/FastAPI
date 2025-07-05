import React, { useState } from 'react';
import { getProtected } from './api';

export default function Protected() {
  const [msg, setMsg] = useState('');
  const handleClick = async () => {
    const token = localStorage.getItem('token');
    if (!token) return setMsg('Not logged in');
    const res = await getProtected(token);
    setMsg(res.detail || JSON.stringify(res));
  };
  return (
    <div>
      <h2>Protected Endpoint</h2>
      <button onClick={handleClick}>Access Protected</button>
      {msg && <div>{msg}</div>}
    </div>
  );
}
