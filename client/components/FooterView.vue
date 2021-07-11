<template>
	<footer>
		<nav>
			<p class="logo">
				<nuxt-link to="/">
					<img src="@/assets/img/logo-white.svg" alt="INIAD Stock">
				</nuxt-link>
			</p>
			<ul>
				<li>
					<nuxt-link to="/">
						ホーム
					</nuxt-link>
				</li>
				<li>
					<nuxt-link to="/">
						タグ一覧
					</nuxt-link>
				</li>
				<li>
					<nuxt-link to="/">
						マイページ
					</nuxt-link>
				</li>
			</ul>
			<ul>
				<li>
					<nuxt-link to="/">
						トレンド
					</nuxt-link>
				</li>
				<li>
					<nuxt-link to="/">
						最新記事
					</nuxt-link>
				</li>
				<li>
					<nuxt-link to="/">
						最近のコメント
					</nuxt-link>
				</li>
				<li>
					<nuxt-link to="/">
						フレンド記事
					</nuxt-link>
				</li>
			</ul>
			<ul>
				<li>
					<nuxt-link to="/">
						プライバシーポリシー
					</nuxt-link>
				</li>
				<li>
					<nuxt-link to="/">
						利用規約
					</nuxt-link>
				</li>
				<li>
					<a href="mailto:iniad.stock@gmail.com">
						お問い合わせ
					</a>
				</li>
			</ul>
		</nav>
		<p class="footer-bottom twitter">
			<a href="https://twitter.com/INIADStock"><img src="@/assets/img/twitter-white.svg" alt="INIAD Stock 公式Twitter"></a>
		</p>
		<p class="footer-bottom">
			<small>&copy; 2021 INIAD Stock</small>
		</p>
	</footer>
</template>

<script>
export default {
	name: 'FooterView',
}
</script>

<style lang="scss" scoped>
footer {
	background-color: $box-color;
	color: #fff;
	margin-top: 3rem;
	padding-top: 2rem;
	padding-bottom: 1rem;
	position: relative;

	.logo {
		align-self: center;
		padding-left: 50px;

		img {
			width: 12vw;
		}
	}

	a {
		color: #fff;
		text-decoration: none;

		&:hover {
			text-decoration: underline;
		}
	}

	nav {
		display: flex;
		margin-bottom: 2rem;
	}

	ul {
		list-style: none;
		padding-left: 10vw;
		font-size: 0.9em;

		li {
			margin: 0.5em 0;
		}
	}

	.footer-bottom {
		text-align: center;
		margin: 0.6rem 0;
	}

	.twitter {
		img {
			width: 2em;
		}
	}
}
</style>
