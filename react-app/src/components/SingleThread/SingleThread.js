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

  return (!thread || !Object.values(thread) ? <h1> loading </h1> :
    <div className='single-thread-main-body'>
      <div className='single-thread-title'>
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
      </div>
    </div >
  );
}

export default SingleThread;
