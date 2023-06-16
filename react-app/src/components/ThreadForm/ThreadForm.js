import React from 'react';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import { createThreadThunk } from '../../store/threads';

function ThreadForm({ thread, formType, category }) {
  const sessionUser = useSelector(state => state.session.user);
  const dispatch = useDispatch()
  const history = useHistory()
  const [subject, setSubject] = useState();
  const [text, setText] = useState();
  const [errors, setErrors] = useState();
  console.log(category)

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});
    thread = { ...thread, subject, text };
    if (formType == "Create Thread") {
      const newThread = dispatch(createThreadThunk(thread, category))
        .then(newThread => { history.push(`/thread/${category}/${newThread.subject.split(' ').join('_')}`) })
    }
    // else if (formType == 'Update Thread') {
    //   const editedGroup = dispatch(updateGroup(group)).then(editedGroup => { history.push(`/groups/${editedGroup.id}`) }).catch(async (res) => {
    //     const data = await res.json();
    //     setErrors(data.errors);
    //   });
    //   group = editedGroup
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
