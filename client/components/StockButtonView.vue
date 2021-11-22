<template>
	<button v-bind:class="{stocked: value}" v-on:click="stock" />
</template>

<script>
export default {
	name: 'StockButtonView',
	props: {
		value: Boolean,
		articleUuid: String,
	},
	/*
	data () {
		return {
			value: false,
		}
	}, */
	methods: {
		async stock () {
			let promise
			if (!this.value) {
				promise = await this.$http.post(`/api/articles/${this.articleUuid}/stock/`, {}, {
					headers: {
						'X-CSRFToken': this.$cookies.get('csrftoken'),
					},
				})
			} else {
				promise = await this.$http.delete(`/api/articles/${this.articleUuid}/stock/`, {
					headers: {
						'X-CSRFToken': this.$cookies.get('csrftoken'),
					},
				})
			}
			const article = await promise.json()
			this.$emit('input', article.article.is_stocked)
		},
	},
}
</script>

<style lang="scss" scoped>
button {
	width: 100%;
	height: 0;
	padding-bottom: 50%;
	border: none;
	background-color: transparent;
	background-image: url("~/assets/img/stock-false.svg");
	background-size: 100%;
	background-repeat: no-repeat;

	&:hover {
		background-image: url("~/assets/img/stock-hover.svg");
		position: relative;

		&::before {
			content: "Stock";
			background-color: $subtext-color;
			color: #fff;
			font-size: 0.7em;
			position: absolute;
			bottom: 110%;
			left: 50%;
			transform: translateX(-50%);
			width: fit-content;
			padding: 0.2em 0.4em;
			border-radius: 0.4em;
			opacity: 0.8;
		}
	}

	&.stocked {
		&:hover::before {
			content: "Stocked!";
		}

		background-image: url("~/assets/img/stock-true.svg");
		background-color: transparent;
	}
}
</style>
