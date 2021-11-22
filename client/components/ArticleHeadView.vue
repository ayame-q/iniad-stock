<template>
	<header>
		<h2>{{ article.title }}</h2>
		<ul class="tags">
			<li v-for="(tag, index) of article.tags" v-bind:key="index">
				<nuxt-link v-bind:to="`/tags/${tag}`">
					{{ tag }}
				</nuxt-link>
			</li>
		</ul>
		<p class="username">
			<nuxt-link v-bind:to="`/users/${article.writer.uuid}`">
				<!--<img v-bind:src="article.user.icon" alt="">-->
				<img src="/img/user_icon_1.svg" alt="">
				<span>{{ article.writer.display_name }}</span>
			</nuxt-link>
		</p>
		<p class="time">
			<time>{{ article.time }}</time>
		</p>
		<div class="stock-button">
			<stock-button-view v-model="article.is_stocked" v-bind:article-uuid="article.uuid" />
		</div>
	</header>
</template>

<script>
export default {
	name: 'ArticleHeadView',
	props: {
		value: Object,
	},
	computed: {
		article: {
			get () {
				return this.value
			},
			set (input) {
				this.$emit('input', input)
			},
		},
	},
}
</script>

<style lang="scss" scoped>
header {
	margin: 1.2em 0;
	position: relative;

	a {
		text-decoration: none;
		font-size: 0.8rem;

		&:hover {
			color: $sub-color;
		}
	}

	.reason,
	.time,
	.username,
	.tags {
		color: $subtext-color;
	}

	.reason,
	.time {
		font-size: 0.8em;
	}

	ul.tags {
		list-style: none;
		padding: 0;
		display: flex;
		align-items: center;

		&::before {
			content: "";
			display: block;
			width: 1.1em;
			height: 1.1em;
			background-image: url("~/assets/img/tags.svg");
			background-size: 100%;
			background-repeat: no-repeat;
			margin-right: 0.3em;
		}

		li {
			&:not(:last-child) {
				&::after {
					content: ",";
					margin-right: 0.3em;
				}
			}

			a {
				display: inline-block;
			}
		}
	}

	.username {
		a {
			display: flex;
			align-items: center;

			img {
				width: 1.1em;
				height: 1.1em;
				border-radius: 50%;
				margin-right: 0.3em;
			}

			font-size: 0.9em;
		}
	}

	.stock-button {
		width: 80px;
		position: absolute;
		right: 0;
		bottom: 20px;
	}
}
</style>
