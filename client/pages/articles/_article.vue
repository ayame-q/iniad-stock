<template>
	<div class="article-wrap">
		<article class="main-article">
			<article-head-view v-model="article" />
			<div class="content" v-html="$marked(article.text)" />
		</article>
		<div class="comment_wrap">
			<article-comment-editor-view v-bind:article-uuid="article.uuid" v-on:newComment="newComment" />
			<article-comment-list-comment-view v-for="comment of article.comments" v-bind:key="comment.time" v-bind:comment="comment" />
		</div>
	</div>
</template>

<script>
import 'highlight.js/styles/github.css'

export default {
	name: 'ArticlePage',
	layout: 'article',
	async asyncData ({ params, $http }) {
		const article = await $http.$get(`/api/articles/${params.article}`)
		return {
			article,
		}
	},
	head () {
		return {
			title: this.article.title,
		}
	},
	methods: {
		newComment (comment) {
			this.article.comments.unshift(comment)
		},
	},
}
</script>

<style lang="scss">

.article-wrap {
	display: flex;
	height: 100%;

	article.main-article {
		border: $main-color 1px solid;
		width: 100%;
		height: 100%;
		padding: 0 1.5rem;
		padding-bottom: 1rem;
		overflow-wrap: anywhere;
		min-width: 0;

		.content {
			h1,
			h2,
			h3,
			h4,
			h5,
			h6,
			p {
				margin: 1em 0;
			}
		}

		pre {
			overflow-x: scroll;
		}
	}

	.comment_wrap {
		margin-left: 20px;
		padding: 20px;
		border-top-left-radius: 20px;
		border-bottom-left-radius: 20px;
		flex-basis: calc(#{$side-width} - 20px);
		background-color: $box-color;
		flex-shrink: 0;
		flex-grow: 0;
		position: sticky;
		max-height: calc(100vh - 6rem - 3rem - 1rem);
		top: 5rem;
		right: 0;
		overflow-y: scroll;
	}
}

.article-list {
	article {
		margin: 1.2em 0;

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
	}
}
</style>
