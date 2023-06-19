import React from 'react';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import { createThreadThunk } from '../../store/category';
import { editThreadThunk } from '../../store/category';
import CkEditor from '../ckEditor';

function ThreadForm({ thread, formType, category, subcategory, subcategoryId, categoryId }) {
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
      const newThread = dispatch(createThreadThunk(thread, category, categoryId, subcategoryId))
        .then(newThread => { history.push({ pathname: `/${category}/${subcategory}/threads/${newThread.id}`, state: { threadId: newThread.id, category: category, subcategory: subcategory, categoryId: categoryId, subcategoryId, subcategoryId } }) })
    }
    else if (formType == 'Update Thread') {
      const editedThread = dispatch(editThreadThunk(thread, categoryId, subcategoryId)).then(editedThread => { history.push({ pathname: `/${category}/${subcategory}/threads/${editedThread.id}`, state: { threadId: editedThread.id, category: category, subcategory: subcategory, categoryId: categoryId, subcategoryId, subcategoryId } }) })
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
