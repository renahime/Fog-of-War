import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import { useLocation } from 'react-router-dom'
import { useState, useEffect } from 'react';
import { getThreadThunk } from '../../store/threads';
import './SingleThread.css';

function SingleThread() {
  const user = useSelector(state => state.session.user);
  let thread = useSelector(state => state.thread.singleThread);
  let location = useLocation()
  let [loading, setLoading] = useState(false)
  let idQuery = location.state.id;
  let categoryQuery = location.state.category
  console.log(categoryQuery)
  let dispatch = useDispatch()

  useEffect(() => {
    dispatch(getThreadThunk(idQuery)).then(() => setLoading(true))
  }, [dispatch])

  return (!loading || !thread || !Object.values(thread).length ? <h1>Loading...</h1> :
    <div className='single-thread-main-body'>
      <div className='single-thread-title'>
        <h6>{thread.subject}</h6>
        {thread.user.id && user && thread.user.id == user.id ? <i class="fas fa-cog"></i> : null}
      </div>
      <div className='single-thread-op-contents'>
        {thread.user.username}
      </div>
      <div className='single-thread-op-body-contents'>
        {thread.created_at}
        {thread.text}
      </div>
      <div className='single-thread-posts-container'>
        {thread.posts.map((post) => {
          return <div className='single-thread-post-div'>
            <h6>{post.user.username}</h6>
            {user && post.user.id == user.id ? <i class="fas fa-cog"></i> : null}
            <h6>{post.created_at}</h6>
            <h6>{post.text}</h6>
            <i class="fa-solid fa-quotes"></i>
            <i class="fa-sharp fa-solid fa-message"></i>
          </div>
        })}
      </div>
      <div>
        <NavLink to={{
          pathname: `/threads/${categoryQuery.split(' ').join('_')}/${thread.id}/new`,
          state: {
            id: thread.id,
            subject: thread.subject
          }
        }}>
          <button style={{ float: 'right' }}>New Reply</button>
        </NavLink>
      </div>
      <div className='single-thread-reply'>
        <form>
          <div className='quick-reply-title'></div>
          <h6 >Quick Reply</h6>
          <div className='quick-reply-text-container'>
            <h6>Message</h6>
            <h6>Type Your Reply Message Here</h6>
            <textarea placeholder='Speak your mind....'></textarea>
          </div>
          <div className='buttons'>
            <button>Post Reply</button>
            <button>Preview Post</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default SingleThread;
