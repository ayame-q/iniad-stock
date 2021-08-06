<template>
	<div class="article-list">
		<article-list-article-view
			v-for="article of user.articles"
			v-bind:key="article.time"
			v-bind:article="article"
		/>
	</div>
</template>

<script>
export default {
	name: 'UserPage',
	layout: 'user',
	async asyncData ({ params, $http }) {
		const user = await $http.$get(`/api/users/${params.user}`)
		return {
			user,
		}
	},
	head () {
		return {
			title: `${this.user.name}さんのユーザーページ`,
		}
	},
	mounted () {
		this.$nuxt.$emit('updateUser', this.user)
	},
}
</script>
