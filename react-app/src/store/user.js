const GET_USER = "user/GET_USER"
const CLEAR_PROFILE = "user/CLEAR_PROFILE"
const FOLLOW_THREAD = "user/FOLLOW_THREAD"
const UNFOLLOW_THREAD = "user/UNFOLLOW_THREAD"

const getUser = (username) => ({
  type: GET_USER,
  username
})

export const followThreadProfile = (userId, threadId) => ({
  type: FOLLOW_THREAD,
  userId,
  threadId
})

export const unfollowThreadProfile = (userId, threadId) => ({
  type: UNFOLLOW_THREAD,
  userId,
  threadId
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

const initialState = { user: null };

export default function profile(state = initialState, action) {
  switch (action.type) {
    case GET_USER:
      return { user: action.username };
    case CLEAR_PROFILE:
      return { user: null };
    default:
      return state;
  }
}
