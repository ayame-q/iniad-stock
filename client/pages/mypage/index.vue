<template>
	<div class="index">
		<article-list-view v-model="articles" />
	</div>
</template>

<script>
export default {
	name: 'Mypage',
	layout: 'user',
	head () {
		return {
			title: 'マイページ',
		}
	},
	computed: {
		user () {
			return this.$store.getters['myUser/get']
		},
		articles: {
			get () {
				return this.$store.getters['myUser/getMyArticle']
			},
			set (input) {
				this.$store.commit('myUser/updateArticles', input)
			},
		},
	},
	mounted () {
		this.$store.dispatch('myUser/getMyUser')
		this.$nuxt.$emit('updateUser', this.user)
	},
}
</script>
