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
	name: 'Trends',
	head () {
		return {
			title: 'トレンド',
			titleTemplate: '',
		}
	},
	computed: {
		articles () {
			return this.$store.getters['articles/getAll'].filter((item) => {
				return Math.random() < 0.6
			})
		},
	},
}
</script>
