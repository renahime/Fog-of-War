import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { NavLink, useLocation } from 'react-router-dom/cjs/react-router-dom.min';
import { useState, useEffect } from 'react';

function ThreadForm() {
  const sessionUser = useSelector(state => state.session.user);
  const [subject, setSubject] = useState();
  const location = useLocation();
  let date = new Date()


  return (
    <div className='main-container'>
      <div className='thread-form-title'>
        <h6>Post a New Thread</h6>
      </div>
      <div className='form-container'>
        <form>
          <h6>Username:</h6>
          <h6>Thread Subject:</h6> <input type='text'></input>
          <h6>Your Message:</h6>
          <textarea></textarea>
          <button>Post Thread</button>
          <button>Preview Text</button>
        </form>
      </div>
    </div>
  );
}

export default ThreadForm;
