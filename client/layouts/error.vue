<template>
	<div>
		<div v-if="error.statusCode === 404">
			<h2>404 Not Found</h2>
			<p>
				申し訳ありません。<br>
				お探しのページは見つかりませんでした。
			</p>
			<p>
				もし、このあとあなたの求めるものが見つかりましたら<br>
				INIAD Stockに残しませんか？
			</p>
		</div>
		<div v-else>
			<h2>エラーが発生しました</h2>
			<p>
				申し訳ありません。<br>
				不明なエラーが発生しました。
			</p>
			<p>
				このエラーが続く場合は<br>
				お手数ですが<a v-bind:href="`mailto:iniad.stock@gmail.com?body=%0D%0A%0D%0A%0D%0A%EF%BC%88%E3%81%93%E3%81%93%E3%82%88%E3%82%8A%E4%B8%8B%E3%81%AF%E7%B7%A8%E9%9B%86%E3%81%97%E3%81%AA%E3%81%84%E3%81%A7%E3%81%8F%E3%81%A0%E3%81%95%E3%81%84%EF%BC%89%0D%0A%E3%80%90ErrorInformation%E3%80%91%0D%0ACode%3A${error.statusCode}%0D%0ATime%3A${nowStr}`">こちら</a>よりご連絡ください。
			</p>
		</div>
		<nuxt-link to="/">
			ホームへ
		</nuxt-link>
	</div>
</template>

<script>
import dayjs from 'dayjs'
export default {
	name: 'Error',
	layout: 'page',
	props: {
		error: Object,
	},
	computed: {
		nowStr () {
			return dayjs().toISOString()
		},
	},
}
</script>

<style lang="scss" scoped>
p {
	margin: 1em;
}
</style>
