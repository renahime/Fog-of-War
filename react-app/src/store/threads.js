const GET_CATEGORY_THREAD = "threads/category"
const GET_SINGLE_THREAD = "threads/thread"

const getThreadsList = (threads) => ({
  type: GET_CATEGORY_THREAD,
  threads
})

const getSingleThread = (thread) => ({
  type: GET_SINGLE_THREAD,
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
    default:
      return state;
  }
}
