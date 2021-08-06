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
	name: 'Index',
	async asyncData ({ $http }) {
		const articles = await $http.$get('/api/articles/')
		return {
			articles,
		}
	},
	head () {
		return {
			title: 'INIAD Stock | INIAD生の情報ストックサイト',
			titleTemplate: '',
		}
	},
}
</script>
