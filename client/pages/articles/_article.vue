<template>
	<div class="article-wrap">
		<article class="main-article">
			<article-head-view v-bind:article="article" />
			<div class="content" v-html="$marked(this.article.text)" />
		</article>
		<div class="comment_wrap">
			<form>
				<p class="new-comment">
					<input type="text" placeholder="コメントを残す">
					<button><img src="@/assets/img/comment-submit.svg" alt="送信"></button>
				</p>
			</form>
			<article-comment-view v-for="comment of article.comments" v-bind:key="comment.time" v-bind:comment="comment" />
		</div>
	</div>
</template>

<script>
import DOMPurify from 'dompurify'
import marked from 'marked'
import highlightjs from 'highlight.js'
import 'highlight.js/styles/github.css'

export default {
	name: 'ArticlePage',
	layout: 'article',
	head () {
		return {
			title: this.article.title,
		}
	},
	computed: {
		article () {
			const uuid = this.$route.params.article
			return this.$store.getters['articles/getAll'].find((element) => {
				return element.uuid === uuid
			})
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
	}

	.comment_wrap {
		padding-right: 30px;
		padding-left: 20px;
		width: $side-width;
		flex-shrink: 0;
		flex-grow: 0;
		position: relative;

		.new-comment {
			position: relative;

			input {
				width: 100%;
				padding: 10px;
				padding-right: 33px;
				border: $main-color 1px solid;
				border-radius: 12px;
				margin-bottom: 24px;
			}

			button {
				display: block;
				position: absolute;
				background-color: transparent;
				border: none;
				top: 8px;
				right: 3px;
			}
		}
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
