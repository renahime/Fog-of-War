import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import { useLocation } from 'react-router-dom'
import { useState, useEffect } from 'react';
import { getThreadsListThunk } from '../../store/threads';
import './ThreadList.css';

function ThreadList() {
  const sessionUser = useSelector(state => state.session.user);
  let threads = useSelector(state => state.thread.threadList);
  let threadArr = [];
  let location = useLocation()
  let [loading, setLoading] = useState(false)
  let categoryQuery = location.state.name;
  let dispatch = useDispatch()

  useEffect(() => {
    dispatch(getThreadsListThunk(categoryQuery)).then(() => setLoading(true))
  }, [dispatch])

  if (threads && (Object.values(threads).length > 1)) {
    threadArr = Object.values(threads)
  }

  console.log(threads);
  console.log(threadArr)
  return (!loading && threadArr.length < 1 ? <h1>Loading...</h1> :
    <div>
      <NavLink to={{
        pathname: `/threads/${categoryQuery.split(' ').join('_')}/new`,
        state: {
          category: categoryQuery
        }
      }}>
        <button style={{ float: 'right' }}>Post Thread</button>
      </NavLink>
      <h5>{categoryQuery}</h5>
      <div className='title-columns'>
        <h6>Thread/Author</h6>
        <h6>Replies</h6>
        <h6>Views</h6>
        <h6>Last Post</h6>
      </div>
      <div>
        {threadArr.map((thread) => (
          <NavLink to={{
            pathname: `/threads/${categoryQuery.split(' ').join('_')}/${thread.subject.split(' ').join('_')}`,
            state: {
              id: thread.id,
              category: categoryQuery
            }
          }}>
            <div className='thread-details' key={thread.id}>
              <h6>{thread.subject}</h6> <h6>{thread.user.username}</h6>
              <h6>{thread.name}</h6>
              <h6>{thread.views}</h6>
              <h6>{thread.post_count}</h6>
              <h6>{thread.latest_post.username}</h6>
            </div>
          </NavLink>
        ))}
      </div>
    </div >
  );
}

export default ThreadList;
