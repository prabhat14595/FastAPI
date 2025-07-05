import React, { useState } from 'react';
import { healthcheck } from './api';

export default function Healthcheck() {
  const [msg, setMsg] = useState('');
  const handleClick = async () => {
    const res = await healthcheck();
    setMsg(JSON.stringify(res));
  };
  return (
    <div>
      <h2>Healthcheck</h2>
      <button onClick={handleClick}>Check</button>
      {msg && <div>{msg}</div>}
    </div>
  );
}
