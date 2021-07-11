<template>
	<div class="user-wrap">
		<div class="username">
			<nuxt-link to="/mypage">
				<span>{{ myUserName }}</span>
				<img src="/img/icon_sample.png" alt="">
			</nuxt-link>
			<nav class="user-menu">
				<ul>
					<li>
						<nuxt-link to="/mypage">
							マイページ
						</nuxt-link>
					</li>
					<!--
					<li>
						<nuxt-link to="/config">
							ユーザー設定
						</nuxt-link>
					</li>
					-->
					<li>
						<nuxt-link to="/logout">
							ログアウト
						</nuxt-link>
					</li>
				</ul>
			</nav>
		</div>
	</div>
</template>

<script>
export default {
	name: 'HeaderUserView',
	computed: {
		myUserName () {
			return this.$store.getters['myUser/get'].name
		},
	},
}
</script>

<style lang="scss" scoped>
.user-wrap {
	position: relative;
	z-index: 1;

	.username {
		a {
			display: flex;
			align-items: center;
			width: 100%;
			justify-content: flex-end;
			text-decoration: none;

			&:hover {
				color: $sub-color;
			}

			span {
				margin-right: 0.3em;
			}

			img {
				width: 2.5em;
				height: 2.5em;
				border-radius: 50%;
			}
		}

		&:hover .user-menu {
			visibility: visible;
			opacity: 1;
		}

		.user-menu {
			visibility: hidden;
			opacity: 0;
			transition: 0.3s;
			position: absolute;
			top: 100%;
			right: 0;
			padding-top: 1rem;
			z-index: 1;

			ul {
				padding: 0;
				list-style: none;
				text-align: right;

				li {
					border: $main-color solid 1px;

					&:not(:last-child) {
						border-bottom: none;
					}

					a {
						text-decoration: none;
						padding: 0.8rem 0.6rem;
						width: 180px;
						background-color: #fff;
						display: block;

						&:hover {
							text-decoration: underline;
						}
					}
				}
			}
		}
	}
}
</style>
