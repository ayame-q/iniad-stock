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
	name: 'UserPage',
	layout: 'user',
	head () {
		return {
			title: `${this.user.name}さんのユーザーページ`,
		}
	},
	computed: {
		user () {
			const id = this.$route.params.user
			return this.$store.getters['users/getAll'].find((element) => {
				return element.id === id
			})
		},
		articles () {
			const id = this.$route.params.user
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
