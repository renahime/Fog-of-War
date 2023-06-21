import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, useHistory, Redirect } from 'react-router-dom/cjs/react-router-dom.min';
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
import SignUpPage from '../SignUpPage/SignUpPage';

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
    if (!user) {
      alert("You must be signed up to post!");
    }
    e.preventDefault();
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
    const post = { subject, text };
    console.log(post);
    const newPost = dispatch(createPostThunk(post, id, categoryId, subcategoryId))
      .then(newPost => { history.push({ pathname: `/${category}/${subcategory}/threads/${id}`, state: { threadId: id, category: category, subcategory: subcategory, categoryId: categoryId, subcategoryId: subcategoryId } }) })
    setErrors({});
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
                    <strong>{thread.subject}
                    </strong>
                    {thread.user.id && user && thread.user.id == user.id ?
                      <i onClick={showMenu} style={{ float: 'right' }} class="fas fa-cog"></i> : null}
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
                              <div className='op-statistic-posts-row'>
                                <div className='op-posts-text'>
                                  <strong>
                                    Posts
                                  </strong>
                                </div>
                                <div className='op-posts-number'>
                                  <strong> {thread.user.post_count}</strong>
                                </div>
                              </div>
                              <div className='op-statistic-thread-row'>
                                <div className='op-thread-text'>
                                  <strong>
                                    Threads</strong>
                                </div>
                                <div className='op-thread-number'>
                                  <strong>
                                    {thread.user.thread_count}
                                  </strong>
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
                    </div>
                    <div className='single-thread-op-options-container'>
                      <div className='thread-owner-only-controls'>
                      </div>
                      <div style={{ float: 'right' }} className='thread-reply-controls'>
                        <i class="fa-sharp fa-solid fa-message"></i>
                      </div>
                    </div>
                    {postsArr.map((post) => (
                      <div className='post-user-info'>
                        <div className='post-wrapper'>
                          <div className='post-owner-info'>
                            <div className='post-owner-info-container'>
                              <div className='post-owner-profile-picture'>
                                <img className='profile-picture' src={thread.user.profile_image ? thread.user.profile_image : 'https://cdn.pixabay.com/photo/2013/07/13/10/04/detective-156465_1280.png'}>
                                </img>
                              </div>
                            </div>
                            <div className='post-owner-username'>
                              <strong>{post.user.username}</strong>
                            </div>
                            <div className='post-owner-statistics'>
                              <div className='post-owner-statistic-wrapper'>
                                <div className='post-owner-statistic-row'>
                                  <div className='post-owner-posts-text'>
                                    <strong>
                                      Posts
                                    </strong>
                                  </div>
                                  <div className='post-owner-posts-number'>
                                    <strong>
                                      {post.user.post_count}
                                    </strong>
                                  </div>
                                </div>
                                <div className='post-owner-statistic-row'>
                                  <div className='post-owner-thread-text'>
                                    <strong>
                                      Threads
                                    </strong>
                                  </div>
                                  <div className='post-owner-thread-number'>
                                    <strong>
                                      {post.user.thread_count}
                                    </strong>
                                  </div>
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
                        <div className='post-control-buttons'>
                          <div className='single-thread-post-reply-settings-container'></div>
                          <div className='post-owner-buttons'>
                            <div style={{ float: 'right' }} className='post-reply-buttons'>
                              <i class="fa-sharp fa-solid fa-message"></i>
                            </div>
                            {user && post.user.id == user.id ?
                              <i onClick={showPostMenu} style={{ float: 'right' }} class="post-ownerfa-cog fas fa-cog"> </i> : null}
                            {openPostMenu && post.user.id === user.id ? <div className={menuClassName}>
                              <NavLink style={{ textDecoration: 'none', width: "100%", textAlign: 'right', color: 'black' }} to={{
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
                                <div className='delete-modal' style={{ float: 'right' }}>
                                  <OpenModalButton style={{ width: "100%", textAlign: 'right', color: 'white' }}
                                    buttonText="Delete"
                                    modalComponent={<DeletePostModal category={category} postId={post.id} threadId={thread.id} subcategory={subcategory} categoryId={location.state.categoryId} subcategoryId={location.state.subcategoryId} />} >
                                  </OpenModalButton>
                                </div>
                              </div>
                            </div> : null}
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
          <button className='post-reply-button'>
            <div className='inside-button-container'>
              <i class="fa-solid fa-pen-to-square fa-lg"></i>
              <strong className='button-text-post-thread'>New Reply</strong>
            </div>
          </button>
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
                    <strong style={{ float: 'right' }} className='error-check'>{text && text.length < 10000 ? 10000 - text.length : null}</strong>
                    {text && text.length > 10000 ? <strong className='form-errors' style={{ float: 'right' }}> Oops! Your post is too long!</strong> : null}
                    {errors && errors.text ? <strong className='form-errors'>{errors.text}</strong> : null}
                  </div>
                </td>
                <td className='area-text-t-d'>
                  <div className='text-box-container'>
                    <textarea className='quick-reply-textarea-input' onChange={(e) => setText(e.target.value)} placeholder='Speak your mind....'></textarea>                  </div>
                </td>
              </tr>
              <tr>
                <td colSpan={2} className='quick-reply-buttons'>
                  <center>
                    <div className='quick-reply-buttons-container'>
                      <button className='quick-reply-submit-button' type='submit'>Post Reply</button>
                      <button className='quick-reply-preview-button'>Preview Post</button>
                    </div>
                  </center>
                </td>
              </tr>
            </tbody>
          </table>
        </form>
      </center>
    </div >
  );
}

export default SingleThread;
