<template>
	<div class="index">
		<article-list-view v-model="articles" />
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
