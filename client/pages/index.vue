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
	head () {
		return {
			title: 'INIAD Stock | INIAD生の情報ストックサイト',
			titleTemplate: '',
		}
	},
	computed: {
		articles () {
			return this.$store.getters['articles/getAll']
		},
	},
}
</script>
