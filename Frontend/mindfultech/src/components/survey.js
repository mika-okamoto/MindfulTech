import React, { useState } from 'react';
import './Survey.css'; // Import CSS file for styling

const Survey = () => {
  const [age, setAge] = useState('');
  const [hasItem, setHasItem] = useState('');
  const [errors, setErrors] = useState({});

  const handleAgeChange = (event) => {
    setAge(event.target.value);
  };

  const handleHasItemChange = (event) => {
    setHasItem(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const errors = {};
    // Age validation
    if (!age || isNaN(age) || age < 0 || age > 150) {
      errors.age = 'Please enter a valid age.';
    }
    // Dropdown validation
    if (!hasItem) {
      errors.hasItem = 'Please select an option.';
    }
    // If there are errors, set them and prevent form submission
    if (Object.keys(errors).length > 0) {
      setErrors(errors);
      return;
    }
    // If validation passes, handle form submission here
    console.log('Form submitted:', { age, hasItem });
    // Reset form fields
    setAge('');
    setHasItem('');
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
          <label htmlFor="hasItem">Do you have a:</label>
          <select id="hasItem" value={hasItem} onChange={handleHasItemChange}>
            <option value="">Select...</option>
            <option value="car">Car</option>
            <option value="bike">Bike</option>
            <option value="computer">Computer</option>
            <option value="phone">Phone</option>
            <option value="none">None of the above</option>
          </select>
          {errors.hasItem && <span className="error">{errors.hasItem}</span>}
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Survey;
