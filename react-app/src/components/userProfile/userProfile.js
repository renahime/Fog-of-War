import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import { useLocation } from 'react-router-dom'
import { useState, useEffect } from 'react';
import { getUserByUsername } from '../../store/user';
import { useParams } from 'react-router-dom/cjs/react-router-dom.min';
import './userProfile.css';
import { grabHours } from '../HomePage/HomePage';


function UserProfile() {
  const user = useSelector(state => state.session.user);
  const grabProfile = useSelector(state => state.user.profile)
  const [loading, setLoading] = useState(false)
  const [allActivity, setAllActivity] = useState([])
  const [filteredPosts, setFilteredPosts] = useState([])
  const [viewActivity, setViewActivity] = useState(true)
  const { username } = useParams()
  const dispatch = useDispatch()

  const setPreview = (string) => {
    let returnString = ""
    let tagCheck = "<"
    let tagDone = ">"
    let tagFlag = false
    for (let i = 0; i < 150; i++) {
      if (i > string.length - 1) {
        break
      }
      if (string[i] == tagDone) {
        tagFlag = false;
        continue
      } else if (string[i] == tagCheck || tagFlag) {
        tagFlag = true;
        continue
      }
      returnString = returnString + string[i]
    }
    if (string.length > 150) {
      return returnString + "..."
    } else {
      return returnString
    }
  }


  const threadCheck = (post) => {
    if ("thread_id" in post)
      return true

    return false
  }

  useEffect(() => {
    dispatch(getUserByUsername(username)).then(() => setLoading(true))
  }, [dispatch])

  return !loading ? <h1>loading...</h1> :
    <div className='main-profile-body'>
      <div className='user-info-and-nav'>
        <div className='profile-container'>
          <div className='block-body'>
            <div className='profile-banner-and-user'>
              <div className='profile-banner'>
                <div className='profile-image' style={{ float: 'left', padding: '16px' }}>
                  <img className='profile-picture' src={grabProfile.profile_image ? grabProfile.profile_image : 'https://cdn.pixabay.com/photo/2013/07/13/10/04/detective-156465_1280.png'}></img></div>
              </div>
              <div className='user-info'>
                <h2 className='user-info-username'>{grabProfile.username}</h2>
                <div className='user-stats'>
                  <div className='posting-stats'>
                    <strong><dl><dt>Threads</dt><center><dd className='stat-num'>{grabProfile.thread_count}</dd></center></dl></strong>
                    <strong> <dl><dt>Posts</dt><center><dd className='stat-num'>{grabProfile.post_count}</dd></center></dl></strong>
                    <strong> <dl><dt>Following</dt><center><dd className='stat-num'>{grabProfile.followed_threads.length}</dd></center></dl></strong>
                  </div>
                  <div className='join-stats'>
                    <h2 className='user-info-join'>Joined: {grabProfile.created_at.slice(0, 16)}</h2>
                    <h2 className='user-info-last'>Last Seen: {grabProfile.last_login.slice(0, 16)}</h2>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className='space-between'></div>
      <div className='navigation-buttons'>
        <button className='activity-button'>Latest Activity</button>
      </div>
      <div className='space-between'></div>
      <div className='activity-container'>
        {viewActivity ? grabProfile.all_activity.map((post) =>
          threadCheck(post) ? <div className='activity-list'>
            <ul className='unordered-listing'>
              <li className='listing-info'>
                <NavLink
                  to={{
                    pathname: `/${post.category.name}/${post.subcategory.name}/threads/${post.thread_id}`,
                    state: {
                      threadId: post.thread_id,
                      category: post.category.name,
                      subcategory: post.subcategory.name,
                      categoryId: post.category.id,
                      subcategoryId: post.subcategory.id,
                    }
                  }}>
                  <div className='posting-title'><h4>{grabProfile.username} replied to the thread {post.thread_subject}</h4></div>
                  <div className='content-text'><h4>{setPreview(post.text)}</h4></div>
                  <div className='content-time'><h4>{grabHours(post.created_at)}</h4></div>
                </NavLink>
              </li>
            </ul>
          </div> : <div className='activity-list'>
            <ul className='unordered-listing'>
              <li className='listing-info'>
                <NavLink
                  to={{
                    pathname: `/${post.category.name}/${post.subcategory.name}/threads/${post.id}`,
                    state: {
                      threadId: post.id,
                      category: post.category.name,
                      subcategory: post.subcategory.name,
                      categoryId: post.category.id,
                      subcategoryId: post.subcategory.id,
                    }
                  }}>
                  <div className='content-text'><h4>{grabProfile.username} created a thread {post.subject}</h4></div>
                  <div className='posting-title'><h4>{setPreview(post.text)}</h4></div>
                  <div className='content-time'><h4>{grabHours(post.created_at)}</h4></div>
                </NavLink>
              </li>
            </ul></div>
        ) : null}
      </div>
    </div>
}

export default UserProfile
