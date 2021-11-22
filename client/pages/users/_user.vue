<template>
	<div class="article-list">
		<article-list-view v-model="user.articles" />
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
			title: `${this.user.display_name}さんのユーザーページ`,
		}
	},
	mounted () {
		this.$nuxt.$emit('updateUser', this.user)
	},
}
</script>
