const GET_USER = "user/GET_USER"
const CLEAR_PROFILE = "user/CLEAR_PROFILE"

const getUser = (username) => ({
  type: GET_USER,
  username
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
