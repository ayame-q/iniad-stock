<template>
	<div class="article-list">
		<article-list-article-view
			v-for="article of articles"
			v-bind:key="article.time"
			v-bind:article="article"
			v-on:updateArticle="updateArticle"
		/>
	</div>
</template>

<script>
export default {
	name: 'ArticleListView',
	props: {
		value: Array,
	},
	computed: {
		articles () {
			return this.value
		},
	},
	methods: {
		updateArticle (article) {
			const articles = Array.from(this.articles)
			const index = articles.findIndex((item) => {
				return item.uuid === article.uuid
			})
			articles[index] = article
			this.$emit('input', articles)
			// this.$set(articles, index, article)
		},
	},
}
</script>
