<template>
	<div class="article-list">
		<article-list-article-view
			v-for="article of articles"
			v-bind:key="article.time"
			v-bind:article="article"
		/>
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
		articles () {
			const id = this.user.id
			return this.$store.getters['articles/getAll'].filter((element) => {
				return element.user.id === id
			})
		},
	},
	mounted () {
		this.$nuxt.$emit('updateUser', this.user)
	},
}
</script>
