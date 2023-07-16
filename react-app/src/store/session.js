// constants
const SET_USER = "session/SET_USER";
const REMOVE_USER = "session/REMOVE_USER";
const FOLLOW_THREAD = "session/FOLLOW_THREAD"
const UNFOLLOW_THREAD = "session/UNFOLLOW_THREAD"


const setUser = (user) => ({
	type: SET_USER,
	payload: user,
});

const removeUser = () => ({
	type: REMOVE_USER,
});

const followThread = (thread) => ({
	type: FOLLOW_THREAD,
	thread
})

const unfollowThread = (threadId) => ({
	type: UNFOLLOW_THREAD,
	threadId
})

const initialState = { user: null };

export const authenticate = () => async (dispatch) => {
	const response = await fetch("/api/auth/", {
		headers: {
			"Content-Type": "application/json",
		},
	});
	if (response.ok) {
		const data = await response.json();
		if (data.errors) {
			return;
		}

		dispatch(setUser(data));
	}
};

export const login = (email, password) => async (dispatch) => {
	const response = await fetch("/api/auth/login", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			email,
			password,
		}),
	});

	if (response.ok) {
		const data = await response.json();
		dispatch(setUser(data));
		return null;
	} else if (response.status < 500) {
		const data = await response.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
};

export const logout = () => async (dispatch) => {
	const response = await fetch("/api/auth/logout", {
		headers: {
			"Content-Type": "application/json",
		},
	});

	if (response.ok) {
		dispatch(removeUser());
	}
};

export const signUp = (username, email, password) => async (dispatch) => {
	const response = await fetch("/api/auth/signup", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			username,
			email,
			password,
		}),
	});

	if (response.ok) {
		const data = await response.json();
		dispatch(setUser(data));
		return null;
	} else if (response.status < 500) {
		const data = await response.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
};


export const followThreadThunk = (userId, threadId) => async (dispatch) => {
	const response = await fetch(`/api/users/${userId}/follow_thread/${threadId}`, {
		method: 'POST',
		credentials: 'same-origin',
		headers: { 'Content-Type': 'application/json' },
	})

	if (response.ok) {
		let thread = await response.json()
		dispatch(followThread(thread))
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
		dispatch(unfollowThread(threadId))
		return threadId
	} else {
		let errors = response.json()
		return errors
	}
}



export default function reducer(state = initialState, action) {
	switch (action.type) {
		case SET_USER:
			return { user: action.payload };
		case REMOVE_USER:
			return { user: null };
		case FOLLOW_THREAD:
			const followState = { ...state, user: { ...state.user } }
			followState.user.followed_threads[action.thread.id] = action.thread
			return followState
		case UNFOLLOW_THREAD:
			const unfollowState = { ...state, user: { ...state.user } }
			console.log(unfollowState)
			delete unfollowState.user.followed_threads[action.threadId]
			return unfollowState
		default:
			return state;
	}
}
