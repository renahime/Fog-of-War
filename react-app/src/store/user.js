const GET_USER = "user/GET_USER"
const CLEAR_PROFILE = "user/CLEAR_PROFILE"
const FOLLOW_THREAD = "user/FOLLOW_THREAD"
const UNFOLLOW_THREAD = "user/UNFOLLOW_THREAD"
const FOLLOWED_THREADS = "user/FOLLOWED_THREADS"

const getUser = (username) => ({
  type: GET_USER,
  username
})

const followThread = (userId, thread) => ({
  type: FOLLOW_THREAD,
  userId,
  thread
})

const unfollowThread = (userId, threadId) => ({
  type: UNFOLLOW_THREAD,
  userId,
  threadId
})

const getFollowedThreads = (threads) => ({
  type: FOLLOWED_THREADS,
  threads
})

export const getUserByUsername = (username) => async (dispatch) => {
  const response = await fetch(`/api/users/${username}`, {
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.ok) {
    let user = await response.json()
    dispatch(getUser(user))
  }
};

export const getFollowedThreadsThunk = (userId) => async (dispatch) => {
  const response = await fetch(`/api/users/${userId}/followed_threads`, {
    headers: { 'Content-Type': 'application/json' }
  })

  if (response.ok) {
    let threads = await response.json()
    dispatch(getFollowedThreads(threads))
  } else {
    let errors = response.json()
    return errors
  }
}

export const followThreadThunk = (userId, threadId) => async (dispatch) => {
  const response = await fetch(`/api/users/${userId}/follow_thread/${threadId}`, {
    method: 'POST',
    credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' },
  })

  if (response.ok) {
    let thread = await response.json()
    dispatch(followThread(userId, thread))
  } else {
    let errors = response.json()
    return errors
  }
}

export const unfollowThreadThunk = (userId, threadId) => async (dispatch) => {
  const response = await fetch(`/api/users/${userId}/unfollow_thread/${threadId}`, {
    method: 'DELETE',
    credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' },
  })

  if (response.ok) {
    let success = await response.json()
    dispatch(unfollowThread(userId, threadId))
  } else {
    let errors = response.json()
    return errors
  }
}



const initialState = { profile: null };

export default function user(state = initialState, action) {
  switch (action.type) {
    case GET_USER:
      return { profile: action.username };
    case CLEAR_PROFILE:
      return { profile: null };
    default:
      return state;
  }
}
