export const state = () => ({
	myUser:
		{
			display_name: 'たろう',
			id: 'taro',
			icon: '/img/icon_sample.png',
			comment: 'たろうです。。',
			github: 'taro',
			gitlab: 's1f10190000',
			twitter: 'taro',
			website: 'https://taro.dayo/',
			articles: [],
		},
	isUpdated: false,
})

export const mutations = {
	update (state, user) {
		state.myUser = user
		state.isUpdated = true
	},
	updateArticles (state, articles) {
		state.myUser.articles = articles
	},
	updateStocks (state, stocks) {
		state.myUser.stocks = stocks
	},
}

export const getters = {
	get (state) {
		return state.myUser
	},
	getMyArticle (state) {
		return state.myUser.articles
	},
	getMyStocks (state) {
		return state.myUser.stocks
	},
	getIsUpdated (state) {
		return state.isUpdated
	},
}

export const actions = {
	async getMyUser (context) {
		const myUser = await this.$http.get('/api/my_user')
		context.commit('update', await myUser.json())
	},
}
