const GET_ALL_CATEGORIES = "categories/all"
const GET_CATEGORY_THREAD = "threads/category"
const GET_SINGLE_THREAD = "threads/thread"
const CREATE_THREAD = "threads/create"
const UPDATE_THREAD = "threads/update"
const CREATE_POST = "threads/post/new"
const UPDATE_POST = "threads/post/edit"
const REMOVE_THREAD = "threads/delete"
const REMOVE_POST = "threads/post/delete"
const ADD_VIEW = "threads/views/add"


const getAllCategories = (categories) => ({
  type: GET_ALL_CATEGORIES,
  categories
})

const getThreadsList = (threads) => ({
  type: GET_CATEGORY_THREAD,
  threads
})

const getSingleThread = (thread) => ({
  type: GET_SINGLE_THREAD,
  thread
})

const receiveThread = (thread, categoryId, subcategoryId) => ({
  type: CREATE_THREAD,
  thread,
  categoryId,
  subcategoryId
})

const updateThread = (thread, categoryId, subcategoryId) => ({
  type: UPDATE_THREAD,
  thread,
  categoryId,
  subcategoryId
})

const receivePost = (post, threadId, categoryId, subcategoryId) => ({
  type: CREATE_POST,
  post,
  threadId,
  categoryId,
  subcategoryId
})

const updatePost = (post, threadId, categoryId, subcategoryId) => ({
  type: UPDATE_POST,
  post,
  threadId,
  categoryId,
  subcategoryId
})

export const removeThread = (threadId, categoryId, subcategoryId) => ({
  type: REMOVE_THREAD,
  threadId,
  categoryId,
  subcategoryId
})

export const removePost = (postId, threadId, categoryId, subcategoryId) => ({
  type: REMOVE_POST,
  postId,
  threadId,
  categoryId,
  subcategoryId
})

export const addThreadView = (viewNum, threadId, categoryId, subcategoryId) => ({
  type: ADD_VIEW,
  viewNum,
  threadId,
  categoryId,
  subcategoryId,
})

export const addThreadViewThunk = (threadId, categoryId, subcategoryId) => async (dispatch) => {
  let res = await fetch(`/api/thread/${threadId}/view`, {
    method: 'PUT',
    credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' },
  })
  if (res.ok) {
    let viewNum = await res.json()
    dispatch(addThreadView(viewNum, threadId, categoryId, subcategoryId));
  } else {
    let errors = res.json()
    return errors;
  }
}


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

export const createThreadThunk = (thread, category, categoryId, subcategoryId) => async (dispatch) => {
  const response = await fetch(`/api/thread/${category}/${subcategoryId}/new`, {
    method: 'POST',
    credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(thread, categoryId, subcategoryId),
  })

  if (response.ok) {
    const newThread = await response.json();
    dispatch(receiveThread(newThread, categoryId, subcategoryId));
    return newThread;
  } else {
    const errors = await response.json();
    return errors;
  }
}

export const createPostThunk = (post, threadId, categoryId, subcategoryId) => async (dispatch) => {
  const response = await fetch(`/api/post/thread/${threadId}`, {
    method: 'POST',
    credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(post),
  })

  if (response.ok) {
    const newPost = await response.json();
    dispatch(receivePost(newPost, threadId, categoryId, subcategoryId));
    return newPost;
  } else {
    const errors = await response.json();
    return errors;
  }
}

export const editPostThunk = (post, threadId, categoryId, subcategoryId) => async (dispatch) => {
  const response = await fetch(`/api/post/${post.id}`, {
    method: 'PUT',
    credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(post),
  })

  if (response.ok) {
    const newPost = await response.json();
    dispatch(updatePost(newPost, threadId, categoryId, subcategoryId));
    return newPost;
  } else {
    const errors = await response.json();
    return errors;
  }
}



export const editThreadThunk = (thread, categoryId, subcategoryId) => async (dispatch) => {
  const response = await fetch(`/api/thread/${thread.id}`, {
    method: 'PUT',
    credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(thread),
  })

  if (response.ok) {
    const newThread = await response.json();
    dispatch(updateThread(newThread, categoryId, subcategoryId));
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

export const deleteThreadThunk = (threadId, categoryId, subcategoryId) => async (dispatch) => {
  const response = await fetch(`/api/thread/${threadId}`, {
    credentials: 'same-origin',
    method: 'DELETE',
  });
  if (response.ok) {
    dispatch(removeThread(threadId, categoryId, subcategoryId));
    return threadId;
  } else {
    const errors = await response.json();
    return errors;
  }
}

export const deletePostThunk = (postId, threadId, categoryId, subcategoryId) => async (dispatch) => {
  const response = await fetch(`/api/post/${postId}`, {
    credentials: 'same-origin',
    method: 'DELETE',
  });
  if (response.ok) {
    dispatch(removePost(postId, threadId, categoryId, subcategoryId));
    return postId;
  } else {
    const errors = await response.json();
    return errors;
  }
}


export const getAllCategoriesThunk = () => async (dispatch) => {
  let res = await fetch(`/api/category/`)
  if (res.ok) {
    let categories = await res.json()
    dispatch(getAllCategories(categories))
  } else {
    let errors = res.json()
    return errors
  }
}

const initialState = { categories: null };


export default function category(state = initialState, action) {
  switch (action.type) {
    case GET_ALL_CATEGORIES:
      return { ...state, categories: { ...action.categories } }
    case ADD_VIEW: {
      let addViewState = { ...state, categories: { ...state.categories } }
      addViewState.categories[action.categoryId].subcategories[action.subcategoryId].threads[action.threadId].views = action.viewNum.views
      return addViewState
    }
    case CREATE_THREAD: {
      let addThreadState = { ...state, categories: { ...state.categories } }
      addThreadState.categories[action.categoryId].subcategories[action.subcategoryId].threads[action.thread.id] = action.thread;
      addThreadState.categories[action.categoryId].youngest_post = action.thread;
      addThreadState.categories[action.categoryId].subcategories[action.subcategoryId].youngest_post = action.thread
      return addThreadState
    }
    case CREATE_POST: {
      let addPostState = { ...state, categories: { ...state.categories } }
      addPostState.categories[action.categoryId].subcategories[action.subcategoryId].threads[action.threadId].posts[action.post.id] = action.post
      addPostState.categories[action.categoryId].subcategories[action.subcategoryId].threads[action.threadId].latest_post = action.post
      addPostState.categories[action.categoryId].youngest_post = action.post
      addPostState.categories[action.categoryId].subcategories[action.subcategoryId].youngest_post = action.post
      return addPostState
    }
    case UPDATE_THREAD: {
      let updateThreadState = { ...state, categories: { ...state.categories } }
      updateThreadState.categories[action.categoryId].subcategories[action.subcategoryId].threads[action.thread.id] = action.thread
      return updateThreadState
    }
    case UPDATE_POST: {
      let updatePostState = { ...state, categories: { ...state.categories } }
      updatePostState.categories[action.categoryId].subcategories[action.subcategoryId].threads[action.threadId].posts[action.post.id] = action.post
      return updatePostState
    }
    case REMOVE_THREAD: {
      let removeThreadState = { ...state, categories: { ...state.categories } }
      delete removeThreadState.categories[action.categoryId].subcategories[action.subcategoryId].threads[action.threadId]
      return removeThreadState
    }
    case REMOVE_POST: {
      let removePostState = { ...state, categories: { ...state.categories } }
      delete removePostState.categories[action.categoryId].subcategories[action.subcategoryId].threads[action.threadId].posts[action.postId]
      return removePostState
    }
    default:
      return state;
  }
}
