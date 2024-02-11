import React, { useState } from 'react';
import './survey.css'; // Import CSS file for styling

const Survey = () => {
  const [age, setAge] = useState('');
  const [hasDisorder, setHasDisorder] = useState('');
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
  // Add more state variables and handle change functions for each additional question
  
  const handleAgeChange = (event) => {
    setAge(event.target.value);
  };

  const handleHasDisorderChange = (event) => {
    setHasDisorder(event.target.value);
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
  // Add more handle change functions for additional questions

  const handleSubmit = (event) => {
    event.preventDefault();
    const errors = {};
    // Age validation
    if (!age || isNaN(age) || age < 0 || age > 150) {
      errors.age = 'Please enter a valid age.';
    }
    // Dropdown validation
    if (!hasDisorder) {
      errors.hasDisorder = 'Please select an option.';
    }
    // Additional questions validation
    // Implement validation for each additional question
  
    // If there are errors, set them and prevent form submission
    if (Object.keys(errors).length > 0) {
      setErrors(errors);
      return;
    }
    // If validation passes, handle form submission here FIX
    console.log('Form submitted:', { age, hasDisorder });
    // Reset form fields
    setAge('');
    setHasDisorder('');
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
        <div>
          <label htmlFor="hasDisorder">Do you have a:</label>
          <select id="hasDisorder" value={hasDisorder} onChange={handleHasDisorderChange}>
            <option value="">Select...</option>
            <option value="anxiety">General Anxiety Disorder</option>
            <option value="mood disorder">Mood Disorder</option>
            <option value="computer">Computer</option>
            <option value="none">None of the above</option>
          </select>
          {errors.hasDisorder && <span className="error">{errors.hasDisorder}</span>}
        </div>
        {/* Additional questions */}
        <div>
          <label htmlFor="question2">Question 2:</label>
          <select id="question2" value={question2} onChange={handleQuestion2Change}>
            <option value="">Select...</option>
            <option value="none">None of the above</option>
          </select>
          {/* Error message for question 2 */}
        </div>
        <div>
          <label htmlFor="question3">Question 3:</label>
          <select id="question3" value={question3} onChange={handleQuestion3Change}>
            <option value="">Select...</option>
            <option value="none">None of the above</option>
          </select>
          {/* Error message for question 3 */}
        </div>
        <div>
          <label htmlFor="question4">Question 4:</label>
          <select id="question4" value={question4} onChange={handleQuestion4Change}>
            <option value="">Select...</option>
            <option value="none">None of the above</option>
          </select>
          {/* Error message for question 4 */}
        </div>
        <div>
          <label htmlFor="question5">Question 5:</label>
          <select id="question5" value={question5} onChange={handleQuestion5Change}>
            <option value="">Select...</option>
            <option value="none">None of the above</option>
          </select>
          {/* Error message for question 5 */}
        </div>
        <div>
          <label htmlFor="question6">Question 6:</label>
          <select id="question6" value={question6} onChange={handleQuestion6Change}>
            <option value="">Select...</option>
            <option value="none">None of the above</option>
          </select>
          {/* Error message for question 6 */}
        </div>
        <div>
          <label htmlFor="question7">Question 7:</label>
          <select id="question7" value={question7} onChange={handleQuestion7Change}>
            <option value="">Select...</option>
            <option value="none">None of the above</option>
          </select>
          {/* Error message for question 7 */}
        </div>
        <div>
          <label htmlFor="question8">Question 8:</label>
          <select id="question8" value={question8} onChange={handleQuestion8Change}>
            <option value="">Select...</option>
            <option value="none">None of the above</option>
          </select>
          {/* Error message for question 8 */}
        </div>
        <div>
          <label htmlFor="question9">Question 9:</label>
          <select id="question9" value={question9} onChange={handleQuestion9Change}>
            <option value="">Select...</option>
            <option value="none">None of the above</option>
          </select>
          {/* Error message for question 9 */}
        </div>
        <div>
          <label htmlFor="question10">Question 10:</label>
          <select id="question10" value={question10} onChange={handleQuestion10Change}>
            <option value="">Select...</option>
            <option value="none">None of the above</option>
          </select>
          {/* Error message for question 10 */}
        </div>
        <div>
          <label htmlFor="question11">Question 11:</label>
          <select id="question11" value={question11} onChange={handleQuestion11Change}>
            <option value="">Select...</option>
            <option value="none">None of the above</option>
          </select>
          {/* Error message for question 11 */}
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Survey;
