<template>
	<article class="comment">
		<div class="content">
			<p>{{ comment.text }}</p>
		</div>
		<p class="time">
			<time>{{ comment.time }}</time>
		</p>
		<img class="arrow" v-bind:src="commentArrowSvg" alt="">
		<!--<img class="user-icon" v-bind:src="comment.user.icon" alt="">-->
		<img class="user-icon" src="/img/user_icon_1.svg" alt="">
		<p class="username">
			<nuxt-link v-bind:to="`/users/${comment.writer.uuid}`">
				{{ comment.writer.display_name }}
			</nuxt-link>
		</p>
	</article>
</template>

<script>
import CommentArrowSvg from '@/assets/img/comment-arrow.svg'
export default {
	name: 'ArticleCommentListCommentView',
	props: {
		comment: Object,
	},
	computed: {
		commentArrowSvg () {
			return CommentArrowSvg
		},
	},
}
</script>

<style lang="scss" scoped>
article.comment {
	position: relative;
	border: $main-color 1px solid;
	border-radius: 12px;
	background-color: #fff;
	padding: 10px;
	margin-bottom: 60px;

	h1,
	h2,
	h3,
	h4,
	h5,
	h6,
	p {
		margin: 0.5rem 0;
	}

	.content {
		font-size: 0.8em;
		white-space: pre-line;
		word-wrap: break-word;
	}

	.time {
		text-align: right;
		font-size: 0.6em;
		color: $subtext-color;
		margin-bottom: 0;
	}

	.arrow {
		position: absolute;
		display: block;
		right: 50px;
		top: 100%;
	}

	.user-icon {
		position: absolute;
		display: block;
		right: 12px;
		top: calc(100% + 14px);
		width: 30px;
		height: 30px;
		border-radius: 50%;
	}

	.username {
		position: absolute;
		display: block;
		width: fit-content;
		font-size: 0.6em;
		right: 50px;
		top: calc(100% + 26px);
		margin: 0;

		a {
			color: #fff;
		}
	}
}
</style>
