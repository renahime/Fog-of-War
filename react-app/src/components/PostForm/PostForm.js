import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom/cjs/react-router-dom.min';
import { createPostThunk } from '../../store/threads';
import { editPostThunk } from '../../store/threads';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import CkEditor from '../ckEditor';

function PostForm({ post, formType, threadId, threadSubject, category }) {
  const user = useSelector(state => state.session.user);
  const location = useLocation();
  const history = useHistory();
  const dispatch = useDispatch()
  const [text, setText] = useState(post?.text)
  const [subject, setSubject] = useState(post?.subject || 'RE: ' + threadSubject)
  const [errors, setErrors] = useState({})

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});
    post = { ...post, subject, text };
    if (formType == "Create Post") {
      const newPost = dispatch(createPostThunk(post, location.state.id))
        .then(newPost => { history.push({ pathname: `/threads/${category}/${threadId}`, state: { id: threadId, category: category } }) })
    }
    else if (formType == 'Update Post') {
      const editedPost = dispatch(editPostThunk(post, location.state.id)).then(editedPost => { history.push({ pathname: `/threads/${category}/${threadId}`, state: { id: threadId, category: category } }) })
      post = editedPost
    }
  }


  return (
    <div className='main-container'>
      <div className='thread-form-title'>
        <h6>Post a New Thread</h6>
      </div>
      <div className='form-container'>
        <form onSubmit={handleSubmit}>
          <h6>Username:</h6> <h6>{user.username}</h6>
          <h6>Thread Subject:</h6> <input value={subject} onChange={(e) => setSubject(e.target.value)} type='text'></input>
          <h6>Your Message:</h6>
          <CkEditor setText={setText} text={text}></CkEditor>
          {/* <textarea value={text} onChange={(e) => setText(e.target.value)} ></textarea> */}
          {(formType == 'Create Post') ? (<div className='buttonContainer'>
            <button className='submitButton' type="submit" >Post Reply</button>
            <button className='submitButton' type="submit" >Preview Text</button> </div>) : (<div className='buttonContainer'>
              <button className='submitButton' type="submit" >Update Reply</button>
              <button className='submitButton' type="submit" >Preview Text</button> </div>)}
        </form>
      </div>
    </div>
  );
}

export default PostForm;
