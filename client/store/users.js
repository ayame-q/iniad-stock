export const state = () => ({
	users: [
		{
			name: '花子',
			id: 'hanako',
			icon: '/img/icon_sample.png',
			comment: '花子です。',
			github: null,
			gitlab: null,
			twitter: 'hanako',
			website: null,
		},
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
		{
			name: 'けん',
			id: 'ken',
			icon: '/img/icon_sample.png',
			comment: '学部長です。',
			github: 'ken',
			gitlab: 'ken',
			twitter: 'ken',
			website: 'https://iniad.org/',
		},
	],
})

export const mutations = {
	add (state, user) {
		state.users.push(user)
	},
}

export const getters = {
	getAll (state) {
		return state.users
	},
}

export const actions = {
}
