// Expenses Reducer

const usersDefaultState = {
  socialMedia: ""
}

export default (state = usersDefaultState, action) => {
  console.log('Within user reducer')
  switch (action.type) {
    case 'CHANGE_SOCIAL_MEDIA':
      return {...state, socialMedia: action.socialMedia}
    default:
      return state
    }

}

