import React, { useState } from 'react';
import { getItemById } from './api';

export default function GetItem() {
  const [itemId, setItemId] = useState('');
  const [msg, setMsg] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    const token = localStorage.getItem('token');
    if (!token) return setMsg('Not logged in');
    const res = await getItemById(itemId, token);
    setMsg(JSON.stringify(res));
  };

  return (
    <div>
      <h2>Get Item by ID</h2>
      <form onSubmit={handleSubmit}>
        <input value={itemId} onChange={e => setItemId(e.target.value)} placeholder="Item ID" />
        <button type="submit">Get Item</button>
      </form>
      {msg && <div>{msg}</div>}
    </div>
  );
}
