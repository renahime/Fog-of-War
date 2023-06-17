const GET_CATEGORY_THREAD = "threads/category"
const GET_SINGLE_THREAD = "threads/thread"
const CREATE_THREAD = "threads/create"
const UPDATE_THREAD = "threads/update"
const CREATE_POST = "threads/post/new"
const UPDATE_POST = "threads/post/edit"
const REMOVE_THREAD = "threads/delete"
const REMOVE_POST = "threads/post/delete"

const getThreadsList = (threads) => ({
  type: GET_CATEGORY_THREAD,
  threads
})

const getSingleThread = (thread) => ({
  type: GET_SINGLE_THREAD,
  thread
})

const receiveThread = (thread) => ({
  type: CREATE_THREAD,
  thread
})

const updateThread = (thread) => ({
  type: UPDATE_THREAD,
  thread
})

const receivePost = (post, threadId) => ({
  type: CREATE_POST,
  post,
  threadId
})

const updatePost = (post, threadId) => ({
  type: UPDATE_POST,
  post,
  threadId
})

export const removeThread = (threadId) => ({
  type: REMOVE_THREAD,
  threadId,
})

export const removePost = (postId) => ({
  type: REMOVE_POST,
  postId,
})


export const getThreadsListThunk = (category) => async (dispatch) => {
  let res = await fetch(`/api/thread/${category}`)
  if (res.ok) {
    let threads = await res.json()
    dispatch(getThreadsList(threads))
  } else {
    let errors = res.json()
    return errors
  }
}

export const createThreadThunk = (thread, category) => async (dispatch) => {
  const response = await fetch(`/api/thread/${category}/new`, {
    method: 'POST',
    credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(thread),
  })

  if (response.ok) {
    const newThread = await response.json();
    dispatch(receiveThread(newThread));
    return newThread;
  } else {
    const errors = await response.json();
    return errors;
  }
}

export const createPostThunk = (threadId, post) => async (dispatch) => {
  const response = await fetch(`/api/post/thread/${threadId}`, {
    method: 'POST',
    credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(post),
  })

  if (response.ok) {
    const newPost = await response.json();
    dispatch(receivePost(newPost));
    return newPost;
  } else {
    const errors = await response.json();
    return errors;
  }
}

export const editPostThunk = (post) => async (dispatch) => {
  const response = await fetch(`/api/post/${post.id}`, {
    method: 'POST',
    credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(post),
  })

  if (response.ok) {
    const newPost = await response.json();
    dispatch(updatePost(newPost));
    return newPost;
  } else {
    const errors = await response.json();
    return errors;
  }
}



export const editThreadThunk = (thread) => async (dispatch) => {
  const response = await fetch(`/api/thread/${thread.id}`, {
    method: 'PUT',
    credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(thread),
  })

  if (response.ok) {
    const newThread = await response.json();
    dispatch(updateThread(newThread));
    return newThread;
  } else {
    const errors = await response.json();
    return errors;
  }
}


export const getThreadThunk = (id) => async (dispatch) => {
  let res = await fetch(`/api/thread/${id}`)
  if (res.ok) {
    let thread = await res.json()
    dispatch(getSingleThread(thread))
  } else {
    let errors = res.json()
    return errors
  }
}

export const deleteThreadThunk = (threadId) => async (dispatch) => {
  const response = await fetch(`/api/thread/${threadId}`, {
    credentials: 'same-origin',
    method: 'DELETE',
  });
  if (response.ok) {
    dispatch(removeThread(threadId));
    return threadId;
  } else {
    const errors = await response.json();
    return errors;
  }
}

export const deletePostThunk = (postId) => async (dispatch) => {
  const response = await fetch(`/api/thread/${postId}`, {
    credentials: 'same-origin',
    method: 'DELETE',
  });
  if (response.ok) {
    dispatch(removePost(postId));
    return postId;
  } else {
    const errors = await response.json();
    return errors;
  }
}

const initialState = { threadList: null, singleThread: null };


export default function thread(state = initialState, action) {
  switch (action.type) {
    case GET_CATEGORY_THREAD:
      return { ...state, threadList: { ...action.threads } }
    case GET_SINGLE_THREAD:
      return { ...state, singleThread: { ...action.thread } }
    case CREATE_THREAD:
      let createThreadState = { ...state, threadList: { ...state.threadList }, singleThread: { ...state.singleThread } };
      createThreadState.singleThread = action.thread;
      createThreadState.threadList[action.thread.id] = action.thread;
      return createThreadState
    case UPDATE_THREAD: {
      let updatedThreadState = { ...state, threadList: { ...state.threadList }, singleThread: { ...state.singleThread } };
      updatedThreadState.singleThread = action.thread;
      updatedThreadState.threadList[action.thread.id] = action.thread;
      return updatedThreadState
    }
    case REMOVE_THREAD: {
      let deleteThreadState = { ...state, threadList: { ...state.threadList }, singleThread: { ...state.singleThread } }
      delete deleteThreadState.threadList[action.threadId]
      delete deleteThreadState.singleThread[action.threadId]
      return deleteThreadState
    }
    default:
      return state;
  }
}
