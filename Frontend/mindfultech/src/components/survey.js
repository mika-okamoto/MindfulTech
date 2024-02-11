import React, { useState } from 'react';
import './survey.css'; // Import CSS file for styling

const Survey = () => {
  const [age, setAge] = useState('');
  const [errors, setErrors] = useState({});
  
  // Additional questions state variables and handle change functions
  const [question2, setQuestion2] = useState('');
  const [question3, setQuestion3] = useState('');
  const [question4, setQuestion4] = useState('');
  const [question5, setQuestion5] = useState('');
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
  
  const handleQuestion5Change = (event) => {
    setQuestion5(event.target.value);
  };

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

  const handleSubmit = (event) => {
    event.preventDefault();
    const errors = {};
    // Age validation
    if (!age || isNaN(age) || age < 0 || age > 150) {
      errors.age = 'Please enter a valid age.';
    }
    // Dropdown validation
    if (!question5) {
      errors.question5 = 'Please select an option.';
    }
    // Additional questions validation FIX
    // Implement validation for each additional question
  
    // If there are errors, set them and prevent form submission
    if (Object.keys(errors).length > 0) {
      setErrors(errors);
      return;
    }
    // If validation passes, handle form submission here FIX
    console.log('Form submitted:', { age, question5 });
    // Reset form fields
    setAge('');
    // Reset additional questions fields
    setQuestion2('');
    setQuestion3('');
    setQuestion4('');
    setQuestion5('');
    setQuestion6('');
    setQuestion7('');
    setQuestion8('');
    setQuestion9('');
    setQuestion10('');
    setQuestion11('');
    setQuestion12('');
    // Reset fields for each additional question
    setErrors({});
  };

  return (
    <div>
      <h1>Survey</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="age">Age:</label>
          <input 
            type="number" 
            id="age" 
            value={age} 
            onChange={handleAgeChange} 
          />
          {errors.age && <span className="error">{errors.age}</span>}
        </div>
        {/* Additional questions */}
        <div>
          <label htmlFor="question2">Gender:</label>
          <select id="question2" value={question2} onChange={handleQuestion2Change}>
            <option value="">Select...</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select>
          {/* Error message for question 2 */}
        </div>
        <div>
          <label htmlFor="question3">How many employees does your company or organization have?:</label>
          <select id="question3" value={question3} onChange={handleQuestion3Change}>
            <option value="">Select...</option>
            <option value="1-5">1-5</option>
            <option value="6-25">6-25</option>
            <option value="26-100">26-100</option>
            <option value="100-500">101-500</option>
            <option value="500-1000">501-1000</option>
            <option value="1000+">1000+</option>
          </select>
          {/* Error message for question 3 */}
        </div>
        <div>
          <label htmlFor="question4">Do you work remotely?:</label>
          <select id="question4" value={question4} onChange={handleQuestion4Change}>
            <option value="">Select...</option>
            <option value="always">Always</option>
            <option value="sometimes">Sometimes</option>
            <option value="never">Never</option>
          </select>
          {/* Error message for question 4 */}
        </div>
        <div>
          <label htmlFor="question5">Do You have a mental health disorder?:</label>
          <select id="question5" value={question5} onChange={handleQuestion5Change}>
            <option value="">Select...</option>
            <option value="anxiety">Yes, General Anxiety Disorder</option>
            <option value="mood disorder">Yes, Mood Disorder</option>
            <option value="no">No</option>
          </select>
          {errors.question5 && <span className="error">{errors.question5}</span>}
        </div>
        <div>
          <label htmlFor="question6">Do you have a family history of mental illness?:</label>
          <select id="question6" value={question6} onChange={handleQuestion6Change}>
            <option value="">Select...</option>
            <option value="yes">Yes</option>
            <option value="no">No</option>
            <option value="i don't know">I don't know</option>
          </select>
          {/* Error message for question 6 */}
        </div>
        <div>
          <label htmlFor="question7">Does your employer offer resources to learn more about mental health concerns and options for seeking help?:</label>
          <select id="question7" value={question7} onChange={handleQuestion7Change}>
            <option value="">Select...</option>
            <option value="yes">Yes</option>
            <option value="no">No</option>
            <option value="i don't know">I don't know</option>
          </select>
          {/* Error message for question 7 */}
        </div>
        <div>
          <label htmlFor="question8">Do you think that discussing a mental health disorder with your employer would have negative consequences?:</label>
          <select id="question8" value={question8} onChange={handleQuestion8Change}>
            <option value="">Select...</option>
            <option value="yes">Yes</option>
            <option value="no">No</option>
            <option value="maybe">Maybe</option>
          </select>
          {/* Error message for question 8 */}
        </div>
        <div>
          <label htmlFor="question9">Would you feel comfortable discussing a mental health disorder with your fellow employees?:</label>
          <select id="question9" value={question9} onChange={handleQuestion9Change}>
            <option value="">Select...</option>
            <option value="yes">Yes</option>
            <option value="no">No</option>
            <option value="maybe">Maybe</option>
          </select>
          {/* Error message for question 9 */}
        </div>
        <div>
          <label htmlFor="question10">Do you feel that being identified as a person with a mental health issue would hurt your career?:</label>
          <select id="question10" value={question10} onChange={handleQuestion10Change}>
            <option value="">Select...</option>
            <option value="strong no">Strong no</option>
            <option value="little no">Little no</option>
            <option value="maybe">Maybe</option>
            <option value="little yes">Little yes</option>
            <option value="strong yes">Strong yes</option>
          </select>
          {/* Error message for question 10 */}
        </div>
        <div>
          <label htmlFor="question11">How willing would you be to share with friends and family that you have a mental illness?:</label>
          <select id="question11" value={question11} onChange={handleQuestion11Change}>
            <option value="">Select...</option>
            <option value="n/a">N/A</option>
            <option value="not open at all">Not open at all</option>
            <option value="somewhat not open">Somewhat not open</option>
            <option value="neutral">Neutral</option>
            <option value="somewhat open">Somewhat open</option>
            <option value="very open">Very open</option>
          </select>
          {/* Error message for question 11 */}
        </div>
        <div>
          <label htmlFor="question12">Do you believe your productivity/work is ever affected by a mental health issue?:</label>
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
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Survey;
