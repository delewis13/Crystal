// CHANGE_SOCIAL_MEDIA
// We use object destructuring to get our various expense variables from user
export const changeSocialMedia = (socialMedia) => ({
  type: 'CHANGE_SOCIAL_MEDIA',
  socialMedia
})

export const addUserPosts = (posts) => ({
  type: 'ADD_USER_POSTS',
  posts
})

export const loading = (loading) => ({
  type: 'LOADING',
  loading
})

export const selected = (selected) => ({
  type: 'SELECTED',
  selected
})