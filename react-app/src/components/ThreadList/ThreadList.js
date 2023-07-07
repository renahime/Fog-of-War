import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import { useLocation } from 'react-router-dom'
import { useState, useEffect } from 'react';
import { getAllCategoriesThunk } from '../../store/category';
import './ThreadList.css';
import { grabHours } from '../HomePage/HomePage';

function ThreadList() {
  const user = useSelector(state => state.session.user);
  let location = useLocation()
  const dispatch = useDispatch()
  let category = location.state.category;
  let subcategory = location.state.subcategory;
  let categoryId = location.state.categoryId;
  let subcategoryId = location.state.subcategoryId

  let categoriesState = useSelector(state => state.category.categories)

  let [threads, setThreads] = useState();
  let [threadsArr, setThreadsArr] = useState([]);
  //let threadsArr;

  useEffect(() => {
    if (!categoriesState)
      dispatch(getAllCategoriesThunk())
  }, [dispatch])

  useEffect(() => {
    if (categoriesState) {
      setThreads(categoriesState[categoryId].subcategories[subcategoryId].threads);
    }
  }, [categoriesState]);

  useEffect(() => {
    if (threads) {
      setThreadsArr(Object.values(threads).sort((a, b) => {
        return new Date(b.latest_post.created_at) - new Date(a.latest_post.created_at)
      }));
    }
  }, [threads])

  useEffect(() => {
    if (threadsArr.length) {
      setThreadsArr(threadsArr.sort((a, b) => {
        return new Date(b.latest_post.created_at) - new Date(a.latest_post.created_at)
      }))
    }
  }, [threadsArr])

  return (!threadsArr ? <h1>Loading...</h1> :
    <div>
      <div className='pag-thread-container'>
        <div className='pagination'>
          <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
            <NavLink to={{
              pathname: `/${category}/${subcategory}/threads/new`,
              state: {
                category: category,
                subcategory: subcategory,
                categoryId: location.state.categoryId,
                subcategoryId: location.state.subcategoryId
              }
            }}>
              <button className='post-thread-button'>
                <div className='inside-button-container'>
                  <i class="fa-solid fa-pen-to-square fa-lg"></i>
                  <strong className='button-text-post-thread'>Post Thread</strong>
                </div>
              </button>
            </NavLink>
          </div>
          <div className='space-between'></div>
        </div>
        <div className='main-body'>
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
                      <strong>{grabHours(thread.latest_post.created_at)}</strong>
                      <strong>By: {thread.latest_post.username ? thread.latest_post.username : thread.latest_post.user.username}</strong>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div >
  );
}

export default ThreadList;
