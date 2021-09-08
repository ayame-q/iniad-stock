<template>
	<form v-on:submit.prevent="submit">
		<p class="new-comment">
			<textarea v-model="text" placeholder="コメントを残す" v-on:input="resizeTextArea" />
			<button><img v-bind:src="commentSubmitSvg" alt="送信"></button>
		</p>
	</form>
</template>

<script>
import CommentSubmitSvg from '@/assets/img/comment-submit.svg'
export default {
	name: 'ArticleCommentEditorView',
	props: {
		articleUuid: String,
	},
	data () {
		return {
			text: '',
		}
	},
	computed: {
		commentSubmitSvg () {
			return CommentSubmitSvg
		},
	},
	methods: {
		resizeTextArea (event) {
			console.log(event.target)
			event.target.style.height = 'calc(1rem + 22px)'
			const height = event.target.scrollHeight
			event.target.style.height = height + 'px'
		},
		submit () {
			this.$http.$post('/api/comments/', {
				article: this.articleUuid,
				text: this.text,
			}, {
				headers: {
					'X-CSRFToken': this.$cookies.get('csrftoken'),
				},
			})
				.then((result) => {
					this.$emit('newComment', result)
				})
		},
	},
}
</script>

<style lang="scss" scoped>
.new-comment {
	position: relative;
	padding-bottom: calc(1rem + 22px + 24px);

	textarea {
		position: absolute;
		right: 0;
		width: 100%;
		max-width: 50vw;
		height: calc(1rem + 22px);
		max-height: 30vh;
		padding: 10px;
		padding-right: 33px;
		border: $main-color 1px solid;
		border-radius: 12px;
		resize: none;
		z-index: 2;
	}

	button {
		display: block;
		position: absolute;
		background-color: transparent;
		border: none;
		top: 8px;
		right: 3px;
		z-index: 3;
	}
}
</style>
