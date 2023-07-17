import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, useHistory, Redirect } from 'react-router-dom/cjs/react-router-dom.min';
import { useLocation } from 'react-router-dom'
import { useState, useEffect, createElement } from 'react';
import { grabHours } from '../HomePage/HomePage';
import { unfollowThreadThunk } from '../../store/session';
import './FollowPage.css';


function FollowPage() {
  const user = useSelector(state => state.session.user);
  const [threadsArr, setThreadsArr] = useState([])
  const dispatch = useDispatch()
  useEffect(() => {
    if (Object.values(user.followed_threads).length) {
      console.log("hi")
      setThreadsArr(Object.values(user.followed_threads).sort((a, b) => {
        return new Date(b.latest_post.created_at) - new Date(a.latest_post.created_at)
      }))
    }
  }, [user.followed_threads])
  const handleUnfollow = async (e) => {
    const unfollow = dispatch(unfollowThreadThunk(user.id, e.target.id))
    if (unfollow) {
      return
    }
  }
  return (!Object.values(user.followed_threads).length ? <h1>You aren't following any threads... :c</h1> : <div>
    <div className='pag-thread-container'>
      <div className='pagination'>
        <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
        </div>
        <div className='space-between'></div>
      </div>
      <div className='main-body'>
        <table className='thread-table'>
          <tbody>
            <tr>
              <td className='thread-subcategory-title' colSpan={6}>
                <h1>Threads Followed</h1>
              </td>
            </tr>
            <tr className='thread-list-titles'>
              <td colSpan={3} className='thread-author-title'>
                <strong>Thread/Author</strong>
              </td>
              <td className='replies-title'>
                <strong>Replies</strong>
              </td>
              <td className='views-title'>
                <strong>Views</strong>
              </td>
              <td className='last-post-title-thread'>
                <strong>Last Post</strong>
              </td>
            </tr>
            {threadsArr.map((thread) => (
              <tr className='thread-row'>
                <td className='font-awesome-thread'>
                  <center>
                    <button id={`${thread.id}`} className={`unfollow-button`} onClick={handleUnfollow}>Unfollow</button>
                  </center>
                </td>
                <td colSpan={2} className='thread-title-and-user'>
                  <div className='thread-title-user-container'>
                    <NavLink
                      to={{
                        pathname: `/category/${thread.category.name}/${thread.subcategory.name}/threads/${thread.id}`,
                        state: {
                          threadId: thread.id,
                          category: thread.category.name,
                          subcategory: thread.subcategory.name,
                          categoryId: thread.category.id,
                          subcategoryId: thread.subcategory.id,
                        }
                      }}>
                      <div className='subject-and-link'>
                        <i style={{ display: 'flex', justifyContent: 'center' }} class="fa-solid fa-arrow-up-right-from-square fa-xs"></i>
                        <strong>{thread.subject}</strong>
                      </div>
                    </NavLink>
                    <NavLink
                      to={{
                        pathname: `/profile/${thread.user.username}`
                      }}>
                      <strong>{thread.user.username}</strong>
                    </NavLink>
                  </div>
                </td>
                <td className='thread-replies'>
                  <strong>{thread.post_count ? thread.post_count : 0}</strong>
                </td>
                <td className='thread-views'>
                  <strong>{thread.views}</strong>
                </td>
                <td className='thread-last-post'>
                  <div className='last-post-thread-container'>
                    <strong>{grabHours(thread.latest_post.created_at)}</strong>
                    <strong>By: {thread.latest_post.username ?
                      <NavLink
                        to={{
                          pathname: `/profile/${thread.latest_post.username}`
                        }}>
                        {thread.latest_post.username}
                      </NavLink> : <NavLink
                        to={{
                          pathname: `/profile/${thread.latest_post.user.username}`
                        }}>
                        {thread.latest_post.user.username}
                      </NavLink>}</strong>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  </div >
  )
}

export default FollowPage
