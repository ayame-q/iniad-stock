<template>
	<div class="trends">
		<article-list-view v-model="articles" />
	</div>
</template>

<script>
export default {
	name: 'Trends',
	async asyncData ({ $http }) {
		const articles = await $http.$get('/api/articles/')
		return {
			articles,
		}
	},
	head () {
		return {
			title: 'トレンド',
		}
	},
}
</script>
