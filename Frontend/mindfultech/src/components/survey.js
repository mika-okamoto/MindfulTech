import React, { useState } from 'react';
import './survey.css'; // Import CSS file for styling
import { submitSurvey } from '../services/driver';
import ChatComponent from './chat.js';

const Survey = () => {
  const [age, setAge] = useState('');
  const [errors, setErrors] = useState({});
  
  const [isChatbotVisible, setIsChatbotVisible] = useState(false); // State for chatbot visibility

  const chatbotPopup = () => {
    setIsChatbotVisible(true); // Set chatbot visibility to true when button is clicked
  };

  // Additional questions state variables and handle change functions
  const [diagnosis, setDiagnosis] = useState('');
  const [question2, setQuestion2] = useState('');
  const [question3, setQuestion3] = useState('');
  const [question4, setQuestion4] = useState('');
  // const [question5, setQuestion5] = useState('');
  const [question6, setQuestion6] = useState('');
  const [question7, setQuestion7] = useState('');
  const [question8, setQuestion8] = useState('');
  const [question9, setQuestion9] = useState('');
  const [question10, setQuestion10] = useState('');
  const [question11, setQuestion11] = useState('');
  const [question12, setQuestion12] = useState('');
  // Add more state variables and handle change functions for each additional question
  
  const handleAgeChange = (event) => {
    setAge(event.target.value);
  };
  // Handle change functions for additional questions
  const handleQuestion2Change = (event) => {
    setQuestion2(event.target.value);
  };
  
  const handleQuestion3Change = (event) => {
    setQuestion3(event.target.value);
  };

  const handleQuestion4Change = (event) => {
    setQuestion4(event.target.value);
  };
  
  // const handleQuestion5Change = (event) => {
  //   setQuestion5(event.target.value);
  // };

  const handleQuestion6Change = (event) => {
    setQuestion6(event.target.value);
  };
  
  const handleQuestion7Change = (event) => {
    setQuestion7(event.target.value);
  };

  const handleQuestion8Change = (event) => {
    setQuestion8(event.target.value);
  };
  
  const handleQuestion9Change = (event) => {
    setQuestion9(event.target.value);
  };

  const handleQuestion10Change = (event) => {
    setQuestion10(event.target.value);
  };
  
  const handleQuestion11Change = (event) => {
    setQuestion11(event.target.value);
  };

  const handleQuestion12Change = (event) => {
    setQuestion12(event.target.value);
  };
  // Add more handle change functions for additional questions

  const handleSubmit = async (event) => {
    event.preventDefault();
    const errors = {};
    // Age validation
    if (!age || isNaN(age) || age < 0 || age > 150) {
      errors.age = '';
      // Please enter a valid age.
    }
    // Dropdown validation
    // if (!question5) {
    //   errors.question5 = 'Please select an option.';
    // }
    // Additional questions validation FIX
    // Implement validation for each additional question
  
    // If there are errors, set them and prevent form submission
    if (Object.keys(errors).length > 0) {
      setErrors(errors);
      return;
    }
    // If validation passes, handle form submission here FIX
    // console.log('Form submitted:', { age });
    // Reset form fields
    setAge('');
    // Reset additional questions fields
    setQuestion2('');
    setQuestion3('');
    setQuestion4('');
    //setQuestion5('');
    setQuestion6('');
    setQuestion7('');
    setQuestion8('');
    setQuestion9('');
    setQuestion10('');
    setQuestion11('');
    setQuestion12('');
    // Reset fields for each additional question
    setErrors({});

    try {
      const result = await submitSurvey({"1": age, "2" : question2,
      "3" : question3, "4" : question4, "5" : "no", "6" : question6,
      "7" : question7, "8" : question8, "9" : question9, "10" : question10,
      "11" : question11, "12" : question12})

      console.log(result.content)
      setDiagnosis(result.content)

    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <div id="bg">
      <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
      <br></br>
      <div id="survey-container">
      <div id="rcorners">
        
        <h1 >MindfulTech</h1>
        <form onSubmit={handleSubmit}>

        <div id="rcorners">
          <div id="left">
            <label htmlFor="age">Age:</label>
          </div> 
          <div id="right">
            <input 
              type="number" 
              id="age" 
              value={age} 
              onChange={handleAgeChange} 
            />
            
            {errors.age && <span className="error">{errors.age}</span>}
          </div>

            {/* Additional questions */}
            <div id="left">
              <label htmlFor="question2">Gender: </label>
            </div> 
            <div id="right">
              <select id="question2" value={question2} onChange={handleQuestion2Change}>
                <option value="">Select...</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
              </select>
              {/* Error message for question 2 */}
            </div>
            <div id="left">
              <label htmlFor="question3">How many employees does your company or organization have? </label>
            </div> 
            <div id="right">
              <select id="question3" value={question3} onChange={handleQuestion3Change}>
                <option value="">Select...</option>
                <option value="1-5">1-5</option>
                <option value="6-25">6-25</option>
                <option value="26-100">26-100</option>
                <option value="100-500">101-500</option>
                <option value="501-1000">501-1000</option>
                <option value="1000+">1000+</option>
              </select>
              {/* Error message for question 3 */}
            </div>
            <div id="left">
              <label htmlFor="question4">Do you work remotely? </label>
            </div> 
            <div id="right">
              <select id="question4" value={question4} onChange={handleQuestion4Change}>
                <option value="">Select...</option>
                <option value="always">Always</option>
                <option value="sometimes">Sometimes</option>
                <option value="never">Never</option>
              </select>
              {/* Error message for question 4 */}
            </div>
            {/* <div>
              <label htmlFor="question5">Do You have a mental health disorder?:</label>
              <select id="question5" value={question5} onChange={handleQuestion5Change}>
                <option value="">Select...</option>
                <option value="anxiety">Yes, General Anxiety Disorder</option>
                <option value="mood disorder">Yes, Mood Disorder</option>
                <option value="no">No</option>
              </select>
              {errors.question5 && <span className="error">{errors.question5}</span>}
            </div> */}
            <div id="left">
              <label htmlFor="question6">Do you have a family history of mental illness? </label>
            </div> 
            <div id="right">
              <select id="question6" value={question6} onChange={handleQuestion6Change}>
                <option value="">Select...</option>
                <option value="yes">Yes</option>
                <option value="no">No</option>
                <option value="i don't know">I don't know</option>
              </select>
              {/* Error message for question 6 */}
            </div>
            <div id="left">
              <label htmlFor="question7">Does your employer offer resources to learn more about mental health concerns and options for seeking help? </label>
            </div> 
            <div id="right">
              <select id="question7" value={question7} onChange={handleQuestion7Change}>
                <option value="">Select...</option>
                <option value="yes">Yes</option>
                <option value="no">No</option>
                <option value="i don't know">I don't know</option>
              </select>
              {/* Error message for question 7 */}
            </div>
            <div id="left">
              <label htmlFor="question8">Do you think that discussing a mental health disorder with your employer would have negative consequences? </label>
            </div> 
            <div id="right">
              <select id="question8" value={question8} onChange={handleQuestion8Change}>
                <option value="">Select...</option>
                <option value="yes">Yes</option>
                <option value="no">No</option>
                <option value="maybe">Maybe</option>
              </select>
              {/* Error message for question 8 */}
            </div>
            <div id="left">
              <label htmlFor="question9">Would you feel comfortable discussing a mental health disorder with your fellow employees? </label>
            </div> 
            <div id="right">
              <select id="question9" value={question9} onChange={handleQuestion9Change}>
                <option value="">Select...</option>
                <option value="yes">Yes</option>
                <option value="no">No</option>
                <option value="maybe">Maybe</option>
              </select>
              {/* Error message for question 9 */}
            </div>
            <div id="left">
              <label htmlFor="question10">Do you feel that being identified as a person with a mental health issue would hurt your career? </label>
            </div> 
            <div id="right">
              <select id="question10" value={question10} onChange={handleQuestion10Change}>
                <option value="">Select...</option>
                <option value="strong no">No, definitely not</option>
                <option value="little no">No, leaning maybe</option>
                <option value="maybe">Maybe</option>
                <option value="little yes">Yes, leaning maybe</option>
                <option value="strong yes">Yes, it definitely would</option>
              </select>
              {/* Error message for question 10 */}
            </div>
            <div id="left">
              <label htmlFor="question11">How willing would you be to share with friends and family that you have a mental illness? </label>
            </div> 
            <div id="right">
              <select id="question11" value={question11} onChange={handleQuestion11Change}>
                <option value="">Select...</option>
                <option value="n/a">N/A</option>
                <option value="not open at all">Not willing at all</option>
                <option value="somewhat not open">Somewhat not willing</option>
                <option value="neutral">Neutral</option>
                <option value="somewhat open">Somewhat willing</option>
                <option value="very open">Very willing</option>
              </select>
              {/* Error message for question 11 */}
            </div>
            <div id="left">
              <label htmlFor="question12">Do you believe your productivity/work is ever affected by a mental health issue? </label>
            </div> 
            <div id="right">
              <select id="question12" value={question12} onChange={handleQuestion12Change}>
                <option value="">Select...</option>
                <option value="n/a">N/A</option>
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="sometimes">Sometimes</option>
                <option value="often">Often</option>
              </select>
              {/* Error message for question 10 */}
            </div>
            <div id="left">
              <p></p>
            </div> 
            <div id="right">
              <button type="submit" >Submit</button>
            </div>
          </div>
          </form>
          
          <div>
            {!(diagnosis !== 'None' && diagnosis !== 'Anxiety' && diagnosis !== 'Mood') && diagnosis === 'None' && <h2>You are at low risk for mood and anxiety disorders.</h2>}
            {!(diagnosis !== 'None' && diagnosis !== 'Anxiety' && diagnosis !== 'Mood') && diagnosis !== 'None' && <h2>You may be at risk for: {diagnosis}</h2>}
            {diagnosis === 'None' && <p>We believe that given your responses, you’re at a low risk for the most common mood and anxiety disorders. If you feel that you need additional support, please speak to a mental health professional or ask our intelligent response service, MindfulAI, follow-up questions.</p>}
            {diagnosis === 'Anxiety' && <p>We believe that you’re at a heightened risk for anxiety disorders, such as general or social anxiety disorder. Work environments are important determinants of occupational and social wellness; poorly managed stress can truly take its toll on our bodies. If you feel that stress or anxiety prevents you from living your life to its fullest, please reach out to a mental health professional, or ask our intelligent response service, MindfulAI, follow-up questions.</p>}
            {diagnosis === 'Mood' && <p>We believe that you’re at a heightened risk for mood disorders, such as depression or seasonal affective disorder. Work-related stress, when poorly managed, can contribute to fatigue, anxiety, and other symptoms of depression – and given the intense stigma surrounding mental health in tech, it is often difficult for people to seek care. If you feel that your mood prevents you from living your life to its fullest, please reach out to a mental health professional, or ask our intelligent response service, MindfulAI, follow-up questions.</p>}
          </div>
          
        </div>
        </div>
        <br></br>
        {isChatbotVisible && <ChatComponent setIsChatbotVisible={setIsChatbotVisible} />}
          <div class='chatbot-icon'>
            <button class="material-symbols-outlined" onClick={chatbotPopup}>comment</button>
          </div>
        </div>
    
  );
};

export default Survey;
