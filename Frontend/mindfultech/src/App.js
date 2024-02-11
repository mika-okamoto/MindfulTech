import logo from './logo.svg';
import './App.css';
import Survey from './components/survey.js'
import ChatComponent from './components/chat.js'

function App() {
  return (
    <div className="App noto-sans-font">  
      <link rel="preconnect" href="https://fonts.googleapis.com"/>
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
      <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet"></link>
      <Survey />
      {/* <ChatComponent /> */}
    </div>
  );
}

export default App;
