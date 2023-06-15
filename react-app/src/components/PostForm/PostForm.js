import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom/cjs/react-router-dom.min';

function PostForm() {
  const sessionUser = useSelector(state => state.session.user);
  const location = useLocation();
  const idQuery = location.state.id;
  const [subject, setSubject] = useState('RE: ' + location.state.subject)

  return (
    <div className='main-container'>
      <div className='thread-form-title'>
        <h6>Post a New Thread</h6>
      </div>
      <div className='form-container'>
        <form>
          <h6>Username:</h6>
          <h6>Thread Subject:</h6> <input type='text' value={subject}></input>
          <h6>Your Message:</h6>
          <textarea></textarea>
          <button>Post Reply</button>
          <button>Preview Post</button>
        </form>
      </div>
    </div>
  );
}

export default PostForm;
