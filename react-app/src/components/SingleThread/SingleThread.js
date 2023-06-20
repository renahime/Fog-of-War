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
import { createPostThunk } from '../../store/category';
import sanitizeHtml from 'sanitize-html';
import { addThreadViewThunk } from '../../store/category'

function SingleThread() {
  const user = useSelector(state => state.session.user);
  let location = useLocation()
  const history = useHistory()
  let dispatch = useDispatch()
  const thread = useSelector(state => state.category.categories[location.state.categoryId].subcategories[location.state.subcategoryId].threads[location.state.threadId])
  const [openThreadMenu, setopenThreadMenu] = useState(false)
  const [openPostMenu, setOpenPostMenu] = useState(false)
  const [errors, setErrors] = useState({})
  let postsArr = [];
  let id = location.state.threadId;
  let category = location.state.category
  let subcategory = location.state.subcategory
  let categoryId = location.state.categoryId
  let subcategoryId = location.state.subcategoryId
  const [subject, setSubject] = useState('RE: ' + thread?.subject)
  const [text, setText] = useState('')
  console.log(thread);

  if (thread)
    postsArr = Object.values(thread.posts);


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
    const newPost = dispatch(createPostThunk(post, id, categoryId, subcategoryId))
      .then(newPost => { history.push({ pathname: `/${category}/${subcategory}/threads/${id}`, state: { threadId: id, category: category, subcategory: subcategory, categoryId: categoryId, subcategoryId: subcategoryId } }) })
  }

  useEffect(() => {
    let addView
    if (thread)
      addView = dispatch(addThreadViewThunk(thread.id, categoryId, subcategoryId));
  }, [thread])


  let menuClassName = openThreadMenu || openPostMenu ? "profile-menu" : "hidden profile-menu"
  console.log(thread);

  return (!thread || !Object.values(thread) ? <h1> loading </h1> :
    <div className='single-thread-main-body'>
      <article>
        <center>
          <table className='single-thread'>
            <tbody>
              <tr className='single-thread-subject-title'>
                <td className='single-thread-subject-title-text'>
                  <div className='single-thread-owner-cog'>
                    {thread.user.id && user && thread.user.id == user.id ?
                      <i onClick={showMenu} class="fas fa-cog"></i> : null}
                    {openThreadMenu && <div className={menuClassName}>
                      <NavLink style={{ textDecoration: 'none', width: "100%", textAlign: 'left', color: 'black' }} to={{
                        pathname: `/${category}/${subcategory}/threads/edit`,
                        state: {
                          thread: thread,
                          category: category,
                          subcategory: subcategory,
                          categoryId: location.state.categoryId,
                          subcategoryId: location.state.subcategoryId,
                        }
                      }}> <div className="profile-dropdown-create">Edit</div> </NavLink>
                      <div className="profile-dropdown-create" onClick={showMenu}>
                        <div>
                          <OpenModalButton
                            buttonText="Delete"
                            modalComponent={<DeleteThreadModal category={category} threadId={thread.id} subcategory={subcategory} categoryId={location.state.categoryId} subcategoryId={location.state.subcategoryId} />} >
                          </OpenModalButton>
                        </div>
                      </div>
                    </div>}
                  </div>
                </td>
                <td className='text-thread-subject-single'>
                  {thread.subject}
                </td>
              </tr>
              <tr className='op-post-and-replies'>
                <td className='op-post-and-replies-cotainer'>
                  <div className='op-post-and-replies'>
                    <div className='op-post-and-info'>
                      <div className='single-thread-op-info-container'>
                        <div className='single-thread-op'>
                          <div className='profile-picture'>
                            <img className='profile-picture' src={thread.user.profile_image ? thread.user.profile_image : 'https://cdn.pixabay.com/photo/2013/07/13/10/04/detective-156465_1280.png'}>
                            </img>
                          </div>
                          <div className='thread-owner-username'>
                            <strong>{thread.user.username}</strong>
                          </div>
                          <div className='op-statistics'>
                            <div className='op-statistic-wrapper'>
                              <div className='op-statistic-row'>
                                <div className='op-posts-text'>
                                  Posts
                                </div>
                                <div className='op-posts-number'>
                                  {thread.user.post_count}
                                </div>
                              </div>
                              <div className='op-statistic-row'>
                                <div className='op-thread-text'>
                                  Threads
                                </div>
                                <div className='op-thread-number'>
                                  {thread.user.thread_count}
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div className='single-thread-op-post-content'>
                        <div className='op-post-head-date'>
                          {thread.created_at}
                        </div>
                        <div className='op-post-thread-body'>
                          {renderHtml(thread.text)}
                        </div>
                      </div>
                      <div className='single-thread-op-options-container'>
                        <div className='thread-owner-only-controls'>
                        </div>
                        <div style={{ float: 'right' }} className='thread-reply-controls'>
                          <i class="fa-sharp fa-solid fa-message"></i>
                        </div>
                      </div>
                    </div>
                    {postsArr.map((post) => (
                      <div className='post-user-info'>
                        <div className='post-wrapper'>
                          <div className='post-owner-info'>
                            <div className='post-owner-profile-picture'>
                              <img className='profile-picture' src={thread.user.profile_image ? thread.user.profile_image : 'https://cdn.pixabay.com/photo/2013/07/13/10/04/detective-156465_1280.png'}>
                              </img>
                            </div>
                            <div className='post-owner-info'>
                              <strong>{post.user.username}</strong>
                            </div>
                            <div className='post-owner-statistics'>
                              <div className='post-owner-statistic-wrapper'>
                                <div className='post-owner-statistic-row'>
                                  <div className='post-owner-posts-text'>
                                    Posts
                                  </div>
                                  <div className='post-owner-posts-number'>
                                    {post.user.post_count}
                                  </div>
                                </div>
                                <div className='post-owner-statistic-row'>
                                  <div className='post-owner-thread-text'>
                                    Threads
                                  </div>
                                  <div className='post-owner-thread-number'>
                                    {post.user.thread_count}
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div className='post-body-content'>
                              <div className='post-body-header'>
                                {post.created_at}
                              </div>
                              <div className='post-body-text'>
                                {renderHtml(post.text)}
                              </div>
                            </div>
                          </div>
                        </div>
                        <div className='post-control-buttons'>
                          <div className='post-owner-buttons'>
                            {user && post.user.id == user.id ?
                              <i onClick={showPostMenu} class="fas fa-cog"> </i> : null}
                            {openPostMenu && post.user.id === user.id ? <div className={menuClassName}>
                              <NavLink style={{ textDecoration: 'none', width: "100%", textAlign: 'left', color: 'black' }} to={{
                                pathname: `/${category}/${subcategory}/threads/${thread.id}/edit`,
                                state: {
                                  post: post,
                                  category: category,
                                  threadId: thread.id,
                                  subject: thread.subject,
                                  subcategory: subcategory,
                                  categoryId: location.state.categoryId,
                                  subcategoryId: location.state.subcategoryId
                                }
                              }}> <div className="profile-dropdown-create">Edit</div> </NavLink>
                              <div className="profile-dropdown-create" onClick={showMenu}>
                                <div>
                                  <OpenModalButton
                                    buttonText="Delete"
                                    modalComponent={<DeletePostModal category={category} postId={post.id} threadId={thread.id} subcategory={subcategory} categoryId={location.state.categoryId} subcategoryId={location.state.subcategoryId} />} >
                                  </OpenModalButton>
                                </div>
                              </div>
                            </div> : null}
                          </div>
                          <div style={{ float: 'right' }} className='post-reply-buttons'>
                            <i class="fa-sharp fa-solid fa-message"></i>
                          </div>
                          <div>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </td>
              </tr>
              <tr>
                <td className='thread-moving'>
                  <div className='thread-footer-container'>
                    <i class="fa-solid fa-circle-chevron-left"></i>
                    <strong>Next Oldest | Next Newest</strong>
                    <i class="fa-solid fa-circle-chevron-right"></i>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </center>
      </article>
      <div className='pagination'></div>
      <div className='space-between'></div>
      <div>
        <NavLink to={{
          pathname: `/${category}/${subcategory}/threads/${thread.id}/new`,
          state: {
            threadId: thread.id,
            subject: thread.subject,
            category: category,
            subcategory: subcategory,
            categoryId: location.state.categoryId,
            subcategoryId: location.state.subcategoryId
          }
        }}>
          <button style={{ float: 'right' }}>New Reply</button>
        </NavLink>
      </div>
      <div className='space-between'></div>
      <center>
        <form onSubmit={handleSubmit} className='quick-reply-form'>
          <table className='quick-reply-table'>
            <thead >
              <tr>
                <td className='quick-reply-title' colSpan={2}>
                  <strong className='quick-reply-title-text'>Quick Reply</strong>
                </td>
              </tr>
            </thead>
            <tbody className='quick-reply-body'>
              <tr>
                <td className='message-title-text'>
                  <div className='quick-reply-text-container'>
                    <strong>Message</strong>
                    <h5>Type your reply to this message here.</h5>
                  </div>
                </td>
                <td>
                  <div className='text-box-container'>
                    <textarea className='quick-reply-textarea-input' onChange={(e) => setText(e.target.value)} placeholder='Speak your mind....'></textarea>                  </div>
                </td>
              </tr>
              <tr>
                <td colSpan={2} className='quick-reply-buttons'>
                  <button type='submit'>Post Reply</button>
                  <button>Preview Post</button>
                </td>
              </tr>
            </tbody>
          </table>
        </form>
      </center>
      {/* <div className='single-thread-title'>
        <h6>{thread.subject}</h6>
        {thread.user.id && user && thread.user.id == user.id ?
          <i onClick={showMenu} class="fas fa-cog"></i> : null}
        {openThreadMenu && <div className={menuClassName}>
          <NavLink style={{ textDecoration: 'none', width: "100%", textAlign: 'left', color: 'black' }} to={{
            pathname: `/${category}/${subcategory}/threads/edit`,
            state: {
              thread: thread,
              category: category,
              subcategory: subcategory,
              categoryId: location.state.categoryId,
              subcategoryId: location.state.subcategoryId,
            }
          }}> <div className="profile-dropdown-create">Edit</div> </NavLink>
          <div className="profile-dropdown-create" onClick={showMenu}>
            <div>
              <OpenModalButton
                buttonText="Delete"
                modalComponent={<DeleteThreadModal category={category} threadId={thread.id} subcategory={subcategory} categoryId={location.state.categoryId} subcategoryId={location.state.subcategoryId} />} >
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
        {postsArr.map((post) => {
          return <div className='single-thread-post-div'>
            <h6>{post.user.username}</h6>
            {user && post.user.id == user.id ?
              <i onClick={showPostMenu} class="fas fa-cog"> </i> : null}
            {openPostMenu && post.user.id === user.id ? <div className={menuClassName}>
              <NavLink style={{ textDecoration: 'none', width: "100%", textAlign: 'left', color: 'black' }} to={{
                pathname: `/${category}/${subcategory}/threads/${thread.id}/edit`,
                state: {
                  post: post,
                  category: category,
                  threadId: thread.id,
                  subject: thread.subject,
                  subcategory: subcategory,
                  categoryId: location.state.categoryId,
                  subcategoryId: location.state.subcategoryId
                }
              }}> <div className="profile-dropdown-create">Edit</div> </NavLink>
              <div className="profile-dropdown-create" onClick={showMenu}>
                <div>
                  <OpenModalButton
                    buttonText="Delete"
                    modalComponent={<DeletePostModal category={category} postId={post.id} threadId={thread.id} subcategory={subcategory} categoryId={location.state.categoryId} subcategoryId={location.state.subcategoryId} />} >
                  </OpenModalButton>
                </div>
              </div>
            </div> : null}
            <h6>{post.created_at}</h6>
            {renderHtml(post.text)}
            <i class="fa-solid fa-quotes"></i>
            <i class="fa-sharp fa-solid fa-message"></i>
          </div>
        })}
      </div>
      <div>
        <NavLink to={{
          pathname: `/${category}/${subcategory}/threads/${thread.id}/new`,
          state: {
            threadId: thread.id,
            subject: thread.subject,
            category: category,
            subcategory: subcategory,
            categoryId: location.state.categoryId,
            subcategoryId: location.state.subcategoryId
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
      </div> */}
    </div >
  );
}

export default SingleThread;
