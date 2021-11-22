<template>
	<div class="recents">
		<article-list-view v-model="articles" />
	</div>
</template>

<script>
export default {
	name: 'Recents',
	async asyncData ({ $http }) {
		const articles = await $http.$get('/api/articles/')
		return {
			articles,
		}
	},
	head () {
		return {
			title: '最新記事',
		}
	},
}
</script>
