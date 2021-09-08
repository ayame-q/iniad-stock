<template>
	<div class="wrap">
		<header>
			<div class="title-column">
				<h1>
					<nuxt-link to="/">
						<img v-bind:src="logoSmall" alt="INIAD Stock">
					</nuxt-link>
				</h1>
			</div>
			<div class="main-column">
				<editor-view />
			</div>
			<div class="side-column">
				<header-user-view />
			</div>
		</header>
		<div class="main-wrap">
			<nav>
				<search-box-view />
				<ul>
					<li v-bind:class="{active: $route.name === 'index'}">
						<nuxt-link to="/">
							<HomeSvg />
							Home
						</nuxt-link>
					</li>
					<li v-bind:class="{active: $route.name === 'trends'}">
						<nuxt-link to="/trends">
							<TrendSvg />
							Trends
						</nuxt-link>
					</li>
					<li v-bind:class="{active: $route.name === 'recents'}">
						<nuxt-link to="/recents">
							<RecentsSvg />
							Recents
						</nuxt-link>
					</li>
					<li>
						<nuxt-link to="/new_comments">
							<CommentSvg />
							Comments
						</nuxt-link>
					</li>
					<li>
						<nuxt-link to="/friends">
							<FriendsSvg />
							Friends
						</nuxt-link>
					</li>
				</ul>
				<p class="title-logo">
					<nuxt-link to="/">
						<img v-bind:src="logoTitle" alt="INIAD Stock">
					</nuxt-link>
				</p>
			</nav>
			<main>
				<Nuxt />
			</main>
			<div class="tag-list">
				<ul>
					<li>
						<nuxt-link to="/">
							タグ1
						</nuxt-link>
					</li>
				</ul>
			</div>
		</div>
		<footer-view />
	</div>
</template>

<script>
import LogoSmall from '@/assets/img/logo-small.svg'
import LogoTitle from '@/assets/img/logo-title.svg'
import HomeSvg from '@/assets/img/home.svg?inline'
import TrendSvg from '@/assets/img/trend.svg?inline'
import RecentsSvg from '@/assets/img/recents.svg?inline'
import CommentSvg from '@/assets/img/comment.svg?inline'
import FriendsSvg from '@/assets/img/friends.svg?inline'
export default {
	name: 'DefaultLayout',
	components: {
		HomeSvg,
		TrendSvg,
		RecentsSvg,
		CommentSvg,
		FriendsSvg,
	},
	computed: {
		logoSmall () {
			return LogoSmall
		},
		logoTitle () {
			return LogoTitle
		},
	},
}
</script>

<style lang="scss" scoped>
.wrap {
	display: flex;
	height: 100%;
	flex-direction: column;
}

header {
	display: flex;
	align-items: center;

	.title-column {
		width: $side-width;
		flex-shrink: 0;
		flex-grow: 0;
	}

	h1 {
		width: $side-width;
		height: 6rem;
		padding-left: 50px;
		position: fixed;
		top: 0;
		display: flex;
		align-items: center;

		img {
			height: 32px;
		}
	}

	.main-column {
		width: 100%;
	}

	.side-column {
		padding-right: 30px;
		padding-left: 20px;
		width: $side-width;
		flex-shrink: 0;
		flex-grow: 0;
	}
}

.main-wrap {
	margin-top: 3rem;
	display: flex;
	flex-grow: 1;
	flex-shrink: 1;

	nav {
		position: sticky;
		top: 9rem;
		height: fit-content;
		width: $side-width;
		flex-shrink: 0;
		flex-grow: 0;
		padding-left: 50px;
		padding-right: 15px;
		background-color: #fff;

		ul {
			list-style: none;
			padding: 0;

			li {
				padding: 0.6rem 0;
				margin-left: -1rem;
				padding-left: 1rem;

				a {
					text-decoration: none;
					display: flex;
					align-items: center;

					svg {
						height: 1.5em;
						margin-right: 0.7em;
						fill: $text-color;
					}

					&:hover {
						color: $sub-color;

						svg {
							fill: $sub-color;
						}
					}
				}

				&.active {
					position: relative;
					z-index: 2;
					margin-right: -16px;
					background-color: #fff;
					border: $main-color 1px solid;
					border-right: none;

					a {
						color: $sub-color;

						svg {
							fill: $sub-color;
						}
					}
				}
			}
		}

		.title-logo {
			position: fixed;
			top: calc(100% - 50px);
			z-index: -1;

			img {
				width: 120px;
			}
		}
	}

	main {
		border: $main-color 1px solid;
		width: 100%;
		padding: 0 1.5rem;
	}

	.tag-list {
		padding-right: 30px;
		padding-left: 20px;
		width: $side-width;
		flex-shrink: 0;
		flex-grow: 0;

		ul {
			list-style: none;
			padding: 0;

			li {
				padding: 0.6rem 0;
				margin-right: -1rem;
				padding-right: 1rem;

				a {
					text-decoration: none;

					&:hover {
						color: $sub-color;
					}
				}

				&.active {
					position: relative;
					z-index: 2;
					margin-left: -16px;
					background-color: #fff;
					border: $main-color 1px solid;
					border-right: none;
				}
			}
		}
	}
}

</style>

<style lang="scss">

html,
body,
#__nuxt,
#__layout {
	height: 100%;
}
</style>
