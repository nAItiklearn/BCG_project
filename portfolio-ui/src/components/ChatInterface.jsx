import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import { Send, Bot, User, Sparkles } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import Graph from './Graph';

export default function ChatInterface() {
    const [messages, setMessages] = useState([
        {
            role: 'bot',
            text: "Hello! I'm your AI Financial Assistant. Ask me about Microsoft, Tesla, or Apple.",
            viz: null
        }
    ]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);
    const scrollRef = useRef(null);

    useEffect(() => {
        scrollRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

    const sendMessage = async () => {
        if (!input.trim()) return;

        const userMsg = { role: 'user', text: input };
        setMessages(prev => [...prev, userMsg]);
        setInput('');
        setLoading(true);

        try {
            const res = await axios.post('http://localhost:5000/chat', { query: input });
            const botMsg = {
                role: 'bot',
                text: res.data.text,
                viz: res.data.visualization ? {
                    type: res.data.visualization.type,
                    title: res.data.visualization.title,
                    data: res.data.visualization.data
                } : null
            };
            setMessages(prev => [...prev, botMsg]);
        } catch (err) {
            setMessages(prev => [...prev, { role: 'bot', text: "Sorry, I encountered an error connecting to the server." }]);
        }
        setLoading(false);
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') sendMessage();
    };

    return (
        <div className="chat-container">

            {/* Header */}
            <header className="chat-header">
                <div className="header-icon">
                    <Sparkles size={24} color="white" />
                </div>
                <div className="chat-title">
                    <h1>Financial AI Agent</h1>
                    <p>Powered by BCG GenAI</p>
                </div>
            </header>

            {/* Chat Area */}
            <div className="messages-area custom-scrollbar">
                <AnimatePresence>
                    {messages.map((msg, idx) => (
                        <motion.div
                            key={idx}
                            initial={{ opacity: 0, y: 20, scale: 0.95 }}
                            animate={{ opacity: 1, y: 0, scale: 1 }}
                            transition={{ duration: 0.3 }}
                            className={`message-row ${msg.role}`}
                        >
                            <div className={`avatar ${msg.role === 'user' ? 'user-avatar' : 'bot-avatar'}`}>
                                {msg.role === 'user' ? <User size={16} color="white" /> : <Bot size={16} color="white" />}
                            </div>

                            <div className="message-content">
                                <div className="message-bubble">
                                    {msg.text}
                                </div>

                                {msg.viz && (
                                    <Graph data={msg.viz.data} type={msg.viz.type} title={msg.viz.title} />
                                )}
                            </div>
                        </motion.div>
                    ))}
                    {loading && (
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            className="message-row bot"
                        >
                            <div className="avatar bot-avatar">
                                <Bot size={16} color="white" />
                            </div>
                            <div className="message-content">
                                <div className="message-bubble">
                                    <div className="loading-dots">
                                        <div className="dot"></div>
                                        <div className="dot"></div>
                                        <div className="dot"></div>
                                    </div>
                                </div>
                            </div>
                        </motion.div>
                    )}
                </AnimatePresence>
                <div ref={scrollRef} />
            </div>

            {/* Input Area */}
            <div className="input-container">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={handleKeyPress}
                    placeholder="Ask a question about Microsoft, Tesla, or Apple..."
                    className="chat-input"
                />
                <button
                    onClick={sendMessage}
                    disabled={!input.trim() || loading}
                    className="send-button"
                >
                    <Send size={20} />
                </button>
            </div>
        </div>
    );
}
