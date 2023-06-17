import React from 'react';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import { createThreadThunk } from '../../store/threads';
import { editThreadThunk } from '../../store/threads';
import CkEditor from '../ckEditor';

function ThreadForm({ thread, formType, category }) {
  const sessionUser = useSelector(state => state.session.user);
  const dispatch = useDispatch()
  const history = useHistory()
  const [subject, setSubject] = useState(thread?.subject);
  const [text, setText] = useState(thread?.text);
  const [errors, setErrors] = useState();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});
    thread = { ...thread, subject, text };
    if (formType == "Create Thread") {
      const newThread = dispatch(createThreadThunk(thread, category))
        .then(newThread => { history.push({ pathname: `/threads/${category}/${newThread.id}`, state: { id: newThread.id, category: category } }) })
    }
    else if (formType == 'Update Thread') {
      const editedThread = dispatch(editThreadThunk(thread)).then(editedThread => { history.push({ pathname: `/threads/${category}/${editedThread.id}`, state: { id: editedThread.id, category: category } }) })
    }
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
          <CkEditor setText={setText} text={text}></CkEditor>
          {/* <textarea value={text} onChange={(e) => setText(e.target.value)} ></textarea> */}
          {(formType == 'Create Thread') ? (<div className='buttonContainer'>
            <button className='submitButton' type="submit" >Post Thread</button>
            <button className='submitButton' type="submit" >Preview Text</button> </div>) : (<div className='buttonContainer'>
              <button className='submitButton' type="submit" >Update Thread</button>
              <button className='submitButton' type="submit" >Preview Text</button> </div>)}
        </form>
      </div>
    </div>
  );
}

export default ThreadForm
