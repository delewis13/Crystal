
// Expenses Reducer

const expensesReducerDefaultState = []

export default (state = expensesReducerDefaultState, action) => {
  switch (action.type) {
    case 'ADD_EXPENSE':
      // NOTE: we DO NOT use array.push, as this would change our array.
      // Instead we could use concat, as this reads and returns, but doens't change
      // Actually we hsall use the spread operator: ...arrayName
      return [...state, action.expense]
    case 'REMOVE_EXPENSE':
      // This is a little tricky. Normally we would pass in 'expense'
      // Here, we instead destructure expense, pulling out id only
      return state.filter(( { id }) => action.id !== id)
    case 'EDIT_EXPENSE':
      return state.map((expense) => {
        if (expense.id === action.id) {
          return {
            ...expense,
            ...action.updates
          }
        } else {
          return expense
        }
      })
    default:
      return state
  }
}

