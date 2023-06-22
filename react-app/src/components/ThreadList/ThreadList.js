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
  
  

  useEffect(() => {
    if (threadsArr.length) {
      threadsArr = threadsArr.sort((a, b) => {
        return new Date(b.latest_post.created_at) - new Date(a.latest_post.created_at)
      })
    }
  }, [threadsArr])



  return (
    <div>
      <div className='pag-thread-container'>
        <div className='pagination'>
          <NavLink to={{
            pathname: `/${category}/${subcategory}/threads/new`,
            state: {
              category: category,
              subcategory: subcategory,
              categoryId: location.state.categoryId,
              subcategoryId: location.state.subcategoryId
            }
          }}>
            <center>
              <button className='post-thread-button'>
                <div className='inside-button-container'>
                  <i class="fa-solid fa-pen-to-square fa-lg"></i>
                  <strong className='button-text-post-thread'>Post Thread</strong>
                </div>
              </button>
            </center>
          </NavLink>
          <div className='space-between'></div>
        </div>
        <div className='main-body'>
          <center>
            <table className='thread-table'>
              <tbody>
                <tr>
                  <td className='thread-subcategory-title' colSpan={6}>
                    <h1>{subcategory}</h1>
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
                      <i class="fa-solid fa-file-lines"></i>
                    </td>
                    <td colSpan={2} className='thread-title-and-user'>
                      <div className='thread-title-user-container'>
                        <NavLink
                          to={{
                            pathname: `/${category}/${subcategory}/threads/${thread.id}`,
                            state: {
                              threadId: thread.id,
                              category: category,
                              subcategory: subcategory,
                              categoryId: location.state.categoryId,
                              subcategoryId: location.state.subcategoryId,
                            }
                          }}>
                          <div className='subject-and-link'>
                            <i class="fa-solid fa-arrow-up-right-from-square fa-xs"></i>
                            <strong>{thread.subject}</strong>
                          </div>
                        </NavLink>
                        <strong>{thread.user.username}</strong>
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
                        <strong>(insert time here)</strong>
                        <strong>{thread.latest_post.username}</strong>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </center>
        </div>
      </div>
    </div >
  );
}

export default ThreadList;
