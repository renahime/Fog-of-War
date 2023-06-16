import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom/cjs/react-router-dom.min';

function PostForm({ post, formType, id, threadSubject }) {
  const sessionUser = useSelector(state => state.session.user);
  const location = useLocation();
  const idQuery = id;
  const [text, setText] = useState()
  const [subject, setSubject] = useState('RE: ' + threadSubject)

  const handleSubmit = async (e) => {
    // e.preventDefault();
    // setErrors({});
    // thread = { ...thread, subject, text };
    // if (formType == "Create Thread") {
    //   const newThread = dispatch(createThreadThunk(thread, category))
    //     .then(newThread => { history.push({ pathname: `/threads/${category}/${newThread.subject.split(' ').join('_')}`, state: { id: newThread.id, category: category } }) })
    // }
    // else if (formType == 'Update Thread') {
    //   const editedThread = dispatch(updatedThread(group)).then(editedThread => { history.push(`/threads/${category}/${editedThread.subject.split(' ').join('_')}`) })
    //   thread = editedThread
    // }
  }


  return (
    <div className='main-container'>
      <div className='thread-form-title'>
        <h6>Post a New Thread</h6>
      </div>
      <div className='form-container'>
        <form onSubmit={handleSubmit}>
          <h6>Username:</h6>
          <h6>Thread Subject:</h6> <input value={subject} onChange={(e) => setSubject(e.target.value)} type='text'></input>
          <h6>Your Message:</h6>
          <textarea value={text} onChange={(e) => setText(e.target.value)} ></textarea>
          {(formType == 'Create Post') ? (<div className='buttonContainer'>
            <button className='submitButton' type="submit" >Post Thread</button>
            <button className='submitButton' type="submit" >Preview Text</button> </div>) : (<div className='buttonContainer'>
              <button className='submitButton' type="submit" >Update Thread</button>
              <button className='submitButton' type="submit" >Preview Text</button> </div>)}
        </form>
      </div>
    </div>
  );
}

export default PostForm;
