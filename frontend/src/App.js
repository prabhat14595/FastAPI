import logo from './logo.svg';
import './App.css';
import Register from './Register';
import Login from './Login';
import Protected from './Protected';
import Healthcheck from './Healthcheck';
import CreateItem from './CreateItem';
import GetItem from './GetItem';
import React, { useState } from 'react';

function App() {
  const [view, setView] = useState('home');
  const [token, setToken] = useState(localStorage.getItem('token') || '');

  const handleLogin = t => {
    setToken(t);
    setView('home');
  };

  return (
    <div className="App">
      <nav style={{ margin: 20 }}>
        <button onClick={() => setView('home')}>Home</button>
        <button onClick={() => setView('register')}>Register</button>
        <button onClick={() => setView('login')}>Login</button>
        <button onClick={() => setView('protected')}>Protected</button>
        <button onClick={() => setView('healthcheck')}>Healthcheck</button>
        <button onClick={() => setView('createitem')}>Create Item</button>
        <button onClick={() => setView('getitem')}>Get Item</button>
      </nav>
      {view === 'home' && <h1>Welcome to FastAPI React Frontend</h1>}
      {view === 'register' && <Register />}
      {view === 'login' && <Login onLogin={handleLogin} />}
      {view === 'protected' && <Protected />}
      {view === 'healthcheck' && <Healthcheck />}
      {view === 'createitem' && <CreateItem />}
      {view === 'getitem' && <GetItem />}
    </div>
  );
}

export default App;
