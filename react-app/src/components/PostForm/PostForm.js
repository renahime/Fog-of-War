import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom/cjs/react-router-dom.min';
import { createPostThunk } from '../../store/category';
import { editPostThunk } from '../../store/category';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import SignUpPage from '../SignUpPage/SignUpPage';
import CkEditor from '../ckEditor';

function PostForm({ post, formType, threadId, threadSubject, category, subcategory, subcategoryId, categoryId, thread }) {
  const user = useSelector(state => state.session.user);
  const location = useLocation();
  const history = useHistory();
  const dispatch = useDispatch()
  const [text, setText] = useState(post?.text)
  const [subject, setSubject] = useState(post?.subject || 'RE: ' + threadSubject)
  const [errors, setErrors] = useState({})

  if (!user) {
    alert("You must be signed up to post!")
    return <SignUpPage></SignUpPage>
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});
    let validationErrors = {}

    if (text.length > 10000) {
      validationErrors.text = "Oops! Your post is too long!"
    } else if (!text.length) {
      validationErrors.text = "Oops! You didn't enter anything in your post"
    }

    if (subject.length > 225) {
      validationErrors.subject = "Oops! Your subject is too long"
    } else if (!subject.length) {
      validationErrors.subject = "Oops! You didn't enter a subject"
    }

    if (Object.values(validationErrors).length) {
      setErrors(validationErrors)
      return
    }

    post = { ...post, subject, text };
    if (formType == "Create Post") {
      const newPost = dispatch(createPostThunk(post, threadId, categoryId, subcategoryId))
        .then(newPost => { history.push({ pathname: `/${category}/${subcategory}/threads/${threadId}`, state: { threadId: threadId, category: category, subcategory: subcategory, categoryId: categoryId, subcategoryId: subcategoryId } }) })
    }
    else if (formType == 'Update Post') {
      const editedPost = dispatch(editPostThunk(post, threadId, categoryId, subcategoryId))
        .then(editedPost => { history.push({ pathname: `/${category}/${subcategory}/threads/${threadId}`, state: { threadId: threadId, category: category, subcategory: subcategory, categoryId: categoryId, subcategoryId: subcategoryId } }) })
      post = editedPost
    }
  }


  return (
    <div className='main-container'>
      <center>
        <form onSubmit={handleSubmit}>
          <table className='thread-form-table'>
            <tbody>
              <tr>
                <td colSpan={2} className='thread-form-title'>
                  <strong>Reply to a Thread</strong>
                </td>
              </tr>
              <tr>
                <td className='thread-form-username' style={{ width: '20%' }}>
                  <strong>Username: </strong>
                </td>
                <td style={{ width: '80%' }} className='thread-form-username-text'>
                  <strong>{user.username}</strong>
                </td>
              </tr>
              <tr>
                <td className='thread-subject-text'>
                  <strong>Subject: </strong>
                  <strong style={{ float: 'right' }} className='error-check'>{subject && subject.length < 225 ? 225 - subject.length : null}</strong>
                  {subject && subject.length > 225 ? <strong className='form-errors' style={{ float: 'right' }}> Oops! Your subject is too long!</strong> : null}
                  {errors && errors.subject ? <strong className='form-errors'>{errors.subject}</strong> : null}
                </td>
                <td className='thread-subject-input-container'>
                  <input className='thread-input' value={subject} onChange={(e) => setSubject(e.target.value)} type='text'></input>
                </td>
              </tr>
              <tr className='editor-input-container'>
                <td className='thread-text-title'>
                  <strong>Your Message:</strong>
                  <strong style={{ float: 'right' }} className='error-check'>{text && text.length < 10000 ? 10000 - text.length : null}</strong>
                  {text && text.length > 10000 ? <strong className='form-errors' style={{ float: 'right' }}> Oops! Your post is too long!</strong> : null}
                  {errors && errors.text ? <strong className='form-errors'>{errors.text}</strong> : null}
                </td>
                <td className='ck-editor-container'>
                  <CkEditor className='ck-editor-thread-form' setText={setText} text={text}></CkEditor>
                </td>
              </tr>
            </tbody>
          </table>
          <div className='space-between'></div>
          <div className='thread-form-button-container'>
            {(formType == 'Create Post') ? (<div className='buttonContainer'>
              <button className='submitButton' type="submit" >Post Reply</button>
              <button className='submitButton' type="submit" >Preview Text</button> </div>) : (<div className='buttonContainer'>
                <button className='submitButton' type="submit" >Update Reply</button>
                {/* <button className='submitButton' type="submit" >Preview Text</button>  */}
              </div>)}
          </div>
        </form>
      </center>
    </div>
  );
}

export default PostForm;
