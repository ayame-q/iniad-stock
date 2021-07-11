export const state = () => ({
	myUser:
		{
			name: 'たろう',
			id: 'taro',
			icon: '/img/icon_sample.png',
			comment: 'たろうです。。',
			github: 'taro',
			gitlab: 's1f10190000',
			twitter: 'taro',
			website: 'https://taro.dayo/',
		},
})

export const mutations = {
	update (state, user) {
		state.myUser = user
	},
}

export const getters = {
	get (state) {
		return state.myUser
	},
}

export const actions = {
	getMyUser (context) {

	},
}
