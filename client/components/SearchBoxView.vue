<template>
	<form>
		<p class="search-box">
			<input type="search">
			<button><img v-bind:src="searchWhite" alt="検索"></button>
		</p>
	</form>
</template>

<script>
import SearchWhite from '@/assets/img/search-white.svg'
export default {
	name: 'SearchBoxView',
	computed: {
		searchWhite () {
			return SearchWhite
		},
	},
}
</script>

<style lang="scss" scoped>
.search-box {
	margin-bottom: 1em;
	position: relative;

	input[type=search] {
		background-color: $sub-color;
		border: none;
		width: calc(100% + 1rem);
		margin-left: -1rem;
		height: 2.6rem;
		border-radius: 0.8rem;
		padding: 0 1.2rem;
		padding-right: 3rem;
		color: #fff;
	}

	button {
		display: block;
		position: absolute;
		top: 50%;
		transform: translateY(-50%);
		right: 0.5em;
		background-color: transparent;
		border: none;

		img {
			width: 1.2em;
			display: block;
		}
	}
}
</style>
