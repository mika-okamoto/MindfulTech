import React, { useState, useEffect } from 'react';
import { chat } from '../services/driver';

const ChatComponent = ({ setIsChatbotVisible }) => {
  const [inputText, setInputText] = useState('');
  const [chatHistory, setChatHistory] = useState([]);

  // Load chat history from storage on component mount
  useEffect(() => {
    const savedChatHistory = JSON.parse(localStorage.getItem('chatHistory')) || [];
    setChatHistory(savedChatHistory);
  }, []);

  // Save chat history to storage whenever it changes
  useEffect(() => {
    localStorage.setItem('chatHistory', JSON.stringify(chatHistory));
  }, [chatHistory]);

  const sendMessage = async () => {
    const messageText = inputText.trim(); // Trim whitespace from the input text

    if (messageText === '') {
      return; // Don't send empty messages
    }

    try {
      // Add the user's message to the chat history
      const userMessage = { text: messageText, sender: 'User' };
      setChatHistory(prevHistory => [...prevHistory, userMessage]);
      setInputText(''); // Clear the input field

      // Get the response from ChatGPT
      const response = await chat({ text: messageText });

      // Extract the desired output from the JSON response
      const chatGPTMessageText = response.content;

      // Add the ChatGPT's response to the chat history
      const chatGPTMessage = { text: chatGPTMessageText, sender: 'MindfulAI' };
      setChatHistory(prevHistory => [...prevHistory, chatGPTMessage]); // Update chat history
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <div className="container mt-5 chatbot">
      <div className="row justify-content-center">
        <div className="col-md-6"> {/* Central container occupying 6 out of 12 columns */}
          <div className="card">
            <div className="card-body">
              <hr className="my-4" /> {/* Divider bar on top */}
              <div className="chat-history">
                {chatHistory.map((message, index) => (
                  <div key={index} className={`message ${message.sender}`}>
                    <div className={`message-content ${message.sender}`}>
                      {message.sender === 'User' ? (
                        <div className="alert alert-primary" role="alert">
                          <strong>User:</strong> {message.text}
                        </div>
                      ) : (
                        <div className="alert alert-secondary" role="alert">
                          <strong>MindfulAI:</strong> {message.text}
                        </div>
                      )}
                    </div>
                  </div>
                ))}
              </div>
              <div className="input-group mt-5"> {/* Increased spacing */}
                <input
                  type="text"
                  className="form-control"
                  placeholder="Type your message here..."
                  value={inputText}
                  onChange={(e) => setInputText(e.target.value)}
                />
                <div className="input-group-append">
                  <button className="btn btn-primary" type="button" onClick={sendMessage}>Send</button>
                </div>
                <button onClick={() => setIsChatbotVisible(false)}>Close</button>                
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatComponent;
