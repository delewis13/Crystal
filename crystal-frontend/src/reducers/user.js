// Expenses Reducer

const usersDefaultState = {
  socialMedia: "",
  userPosts: "",
  loading: false
}

export default (state = usersDefaultState, action) => {
  switch (action.type) {
    case 'CHANGE_SOCIAL_MEDIA':
      return {...state, socialMedia: action.socialMedia}
    case 'ADD_USER_POSTS':
      return {...state, userPosts: action.posts}
    case 'LOADING':
      return {...state, loading: action.loading}
    default:
      return state
    }

}

