<template>
	<div class="index">
		<article-list-view v-model="articles" />
	</div>
</template>

<script>
export default {
	name: 'Stocked',
	layout: 'user',
	head () {
		return {
			title: 'ストックした記事 - マイページ',
		}
	},
	computed: {
		user () {
			return this.$store.getters['myUser/get']
		},
		articles: {
			get () {
				return this.$store.getters['myUser/getMyStocks']
			},
			set (input) {
				this.$store.commit('myUser/updateStocks', input)
			},
		},
	},
	mounted () {
		this.$store.dispatch('myUser/getMyUser')
		this.$nuxt.$emit('updateUser', this.user)
	},
}
</script>
