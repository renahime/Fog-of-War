import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import { useLocation } from 'react-router-dom'
import { useState, useEffect } from 'react';
import { getThreadsListThunk } from '../../store/threads';
import './ThreadList.css';

function ThreadList() {
  const user = useSelector(state => state.session.user);
  let location = useLocation()
  const dispatch = useDispatch()
  let category = location.state.category;
  let subcategory = location.state.subcategory;
  let categoryId = location.state.categoryId;
  let subcategoryId = location.state.subcategoryId
  let threads = useSelector(state => state.category.categories[categoryId].subcategories[subcategoryId].threads)
  let threadsArr;
  if (threads)
    threadsArr = Object.values(threads)
  console.log(location)

  useEffect(() => {
    if (threadsArr.length) {
      threadsArr = threadsArr.sort((a, b) => {
        return new Date(b.latest_post.created_at) - new Date(a.latest_post.created_at)
      })
    }
  }, [threadsArr])



  return (
    <div>
      <NavLink to={{
        pathname: `/${category}/${subcategory}/threads/new`,
        state: {
          category: category,
          subcategory: subcategory,
          categoryId: location.state.categoryId,
          subcategoryId: location.state.subcategoryId
        }
      }}>
        <button style={{ float: 'right' }}>Post Thread</button>
      </NavLink>
      <h5>{subcategory}</h5>
      <div className='title-columns'>
        <h6>Thread/Author</h6>
        <h6>Replies</h6>
        <h6>Views</h6>
        <h6>Last Post</h6>
      </div>
      <div>
        {threadsArr.map((thread) => (
          <NavLink to={{
            pathname: `/${category}/${subcategory}/threads/${thread.id}`,
            state: {
              thread: thread,
              threadId: thread.id,
              category: category,
              subcategory: subcategory,
              threadId: thread.id,
              categoryId: location.state.categoryId,
              subcategoryId: location.state.subcategoryId,
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
