<template>
	<article>
		<nuxt-link v-bind:to="`/articles/${article.uuid}`">
			<p v-if="article.reason" class="reason">
				{{ article.reason }}
			</p>
			<h2>{{ article.title }}</h2>
			<ul class="tags">
				<li v-for="(tag, index) of article.tags" v-bind:key="index">
					<span>{{ tag }}</span>
				</li>
			</ul>
			<p class="username">
				<!--<img v-bind:src="article.user.icon" alt="">-->
				<img src="/img/user_icon_1.svg" alt="">
				<span>{{ article.writer.display_name }}</span>
			</p>
			<p class="time">
				<time>{{ article.time }}</time>
			</p>
		</nuxt-link>
		<div class="stock-button">
			<stock-button-view v-model="isStocked" v-bind:article-uuid="article.uuid" />
		</div>
	</article>
</template>

<script>
export default {
	name: 'ArticleListArticleView',
	props: {
		article: Object,
	},
	computed: {
		isStocked: {
			get () {
				return this.article.is_stocked
			},
			set (value) {
				const article = Object.assign({}, this.article)
				article.is_stocked = value
				this.$emit('updateArticle', article)
			},
		},
	},
}
</script>

<style lang="scss" scoped>
article {
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

			span {
				display: inline-block;
			}
		}
	}

	.username {
		display: flex;
		align-items: center;

		img {
			width: 1.1em;
			height: 1.1em;
			border-radius: 50%;
			margin-right: 0.3em;
		}
	}

	.stock-button {
		width: 60px;
		position: absolute;
		right: 0;
		bottom: 10px;
	}
}
</style>
