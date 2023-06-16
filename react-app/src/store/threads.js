const GET_CATEGORY_THREAD = "threads/category"
const GET_SINGLE_THREAD = "threads/thread"
const CREATE_THREAD = "threads/create"

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

const initialState = { threadList: null, singleThread: null };


export default function thread(state = initialState, action) {
  switch (action.type) {
    case GET_CATEGORY_THREAD:
      return { ...state, threadList: { ...action.threads } }
    case GET_SINGLE_THREAD:
      return { ...state, singleThread: { ...action.thread } }
    case CREATE_THREAD:
      let createThreadState = { ...state, threadList: { ...state.threadList }, singleThread: { ...state.singleGroup } };
      createThreadState.singleThread = action.thread;
      createThreadState.threadList = { ...action.thread, ...state.threadList }
      return createThreadState
    default:
      return state;
  }
}
