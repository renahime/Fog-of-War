import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import { useLocation } from 'react-router-dom'
import { useState, useEffect, createElement } from 'react';
import { getThreadThunk } from '../../store/threads';
import './SingleThread.css';
import OpenModalButton from "../OpenModalButton"
import DeleteThreadModal from './DeleteThreadModal';
import DeletePostModal from './DeletePostModal';
import { createPostThunk } from '../../store/threads';
import sanitizeHtml from 'sanitize-html';


function SingleThread() {
  const user = useSelector(state => state.session.user);
  let thread = useSelector(state => state.thread.singleThread);
  let location = useLocation()
  let [loading, setLoading] = useState(false)
  const [subject, setSubject] = useState('RE: ')
  const [text, setText] = useState('')
  let idQuery = location.state.id;
  let categoryQuery = location.state.category
  let dispatch = useDispatch()
  const [openThreadMenu, setopenThreadMenu] = useState(false)
  const [openPostMenu, setOpenPostMenu] = useState(false)
  const [errors, setErrors] = useState({})
  const history = useHistory()

  let showMenu = () => {
    setopenThreadMenu(!openThreadMenu)
  }

  let showPostMenu = () => {
    setOpenPostMenu(!openPostMenu)
  }

  const renderHtml = (dirtyHtmlContent) => {
    const clean = sanitizeHtml(dirtyHtmlContent, {
      allowedTags: sanitizeHtml.defaults.allowedTags.concat(['img'])
    });
    return createElement('div', {
      dangerouslySetInnerHTML: { __html: clean },
    });
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});
    const post = { subject, text };
    console.log(post);
    const newPost = dispatch(createPostThunk(post, idQuery))
      .then(newPost => { history.push({ pathname: `/threads/${categoryQuery}/${idQuery}`, state: { id: idQuery, category: categoryQuery } }) })
  }


  useEffect(() => {
    dispatch(getThreadThunk(idQuery)).then(() => setLoading(true))
    if (thread && Object.values(thread).length) {
      setSubject('RE: ' + thread.subject);
    }
  }, [dispatch])

  let menuClassName = openThreadMenu || openPostMenu ? "profile-menu" : "hidden profile-menu"

  return (!loading || !thread || !Object.values(thread).length ? <h1>Loading...</h1> :
    <div className='single-thread-main-body'>
      <div className='single-thread-title'>
        <h6>{thread.subject}</h6>
        {thread.user.id && user && thread.user.id == user.id ?
          <i onClick={showMenu} class="fas fa-cog"></i> : null}
        {openThreadMenu && <div className={menuClassName}>
          <NavLink style={{ textDecoration: 'none', width: "100%", textAlign: 'left', color: 'black' }} to={{
            pathname: `/threads/${categoryQuery}/edit`,
            state: {
              thread: thread,
              category: categoryQuery
            }
          }}> <div className="profile-dropdown-create">Edit</div> </NavLink>
          <div className="profile-dropdown-create" onClick={showMenu}>
            <div>
              <OpenModalButton
                buttonText="Delete"
                modalComponent={<DeleteThreadModal category={categoryQuery} threadId={thread.id} />} >
              </OpenModalButton>
            </div>
          </div>
        </div>}
      </div>
      <div className='single-thread-op-contents'>
        {thread.user.username}
      </div>
      <div className='single-thread-op-body-contents'>
        {thread.created_at}
        {renderHtml(thread.text)}
      </div>
      <div className='single-thread-posts-container'>
        {thread.posts.map((post) => {
          return <div className='single-thread-post-div'>
            <h6>{post.user.username}</h6>
            {user && post.user.id == user.id ?
              <i onClick={showPostMenu} class="fas fa-cog"> </i> : null}
            {openPostMenu && post.user.id === user.id ? <div className={menuClassName}>
              <NavLink style={{ textDecoration: 'none', width: "100%", textAlign: 'left', color: 'black' }} to={{
                pathname: `/threads/${categoryQuery}/${thread.id}/edit`,
                state: {
                  post: post,
                  category: categoryQuery,
                  id: thread.id,
                  subject: thread.subject
                }
              }}> <div className="profile-dropdown-create">Edit</div> </NavLink>
              <div className="profile-dropdown-create" onClick={showMenu}>
                <div>
                  <OpenModalButton
                    buttonText="Delete"
                    modalComponent={<DeletePostModal category={categoryQuery} postId={post.id} threadId={thread.id} />} >
                  </OpenModalButton>
                </div>
              </div>
            </div> : null}
            <h6>{post.created_at}</h6>
            <h6>{renderHtml(post.text)}</h6>
            <i class="fa-solid fa-quotes"></i>
            <i class="fa-sharp fa-solid fa-message"></i>
          </div>
        })}
      </div>
      <div>
        <NavLink to={{
          pathname: `/threads/${categoryQuery}/${thread.id}/new`,
          state: {
            id: thread.id,
            subject: thread.subject,
            category: categoryQuery
          }
        }}>
          <button style={{ float: 'right' }}>New Reply</button>
        </NavLink>
      </div>
      <div className='single-thread-reply'>
        <form onSubmit={handleSubmit}>
          <div className='quick-reply-title'></div>
          <h6 >Quick Reply</h6>
          <div className='quick-reply-text-container'>
            <h6>Message</h6>
            <h6>Type Your Reply Message Here</h6>
            <textarea onChange={(e) => setText(e.target.value)} placeholder='Speak your mind....'></textarea>
          </div>
          <div className='buttons'>
            <button type='submit'>Post Reply</button>
            <button>Preview Post</button>
          </div>
        </form>
      </div>
    </div >
  );
}

export default SingleThread;
