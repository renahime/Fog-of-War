const GET_ALL_CATEGORIES = "categories/all"

const getAllCategories = (categories) => ({
  type: GET_ALL_CATEGORIES,
  categories
})

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
      return { ...state, category: { ...action.categories } }
    default:
      return state;
  }
}
