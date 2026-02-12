import React from 'react';
import Scene from './components/Scene';
import ChatInterface from './components/ChatInterface';

function App() {
  return (
    <div className="app-container">
      <Scene />
      <div className="interface-wrapper">
        <ChatInterface />
      </div>
    </div>
  );
}

export default App;
