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
			<div class="profile-wrap">
				<div class="profile">
					<div class="about">
						<p class="user-icon">
							<img src="/img/user_icon_1.svg" alt="">
						</p>
						<div class="user-meta">
							<p class="username">
								{{ user.display_name }}
							</p>
							<p class="userid">
								@{{ user.screen_name }}
							</p>
							<p class="follows">
								<nuxt-link to="">
									フォロー 3
								</nuxt-link>
								<nuxt-link to="">
									フォロワー 3
								</nuxt-link>
							</p>
						</div>
					</div>
					<div class="comment">
						<p>{{ user.comment }}</p>
					</div>
					<ul class="links">
						<li><a href=""><img v-bind:src="githubSvg" alt="github" class="github"></a></li>
						<li><a href=""><img v-bind:src="gitlabSvg" alt="gitlab" class="gitlab"></a></li>
						<li><a href=""><img v-bind:src="twitterSvg" alt="twitter" class="twitter"></a></li>
						<li><a href=""><img v-bind:src="linkSvg" alt="link" class="link"></a></li>
					</ul>
					<div v-if="$route.name !== 'mypage'" class="follow">
						<p><button>フォロー</button></p>
					</div>
					<div v-if="$route.name === 'mypage'" class="profile-settings">
						<p>
							<button v-on:click="openUserProfileEdit">
								プロフィールを編集
							</button>
						</p>
					</div>
				</div>
				<nav>
					<ul>
						<li v-if="$route.path.startsWith('/mypage')" v-bind:class="{active: $route.name === 'mypage'}">
							<nuxt-link to="/mypage/">
								<MyPageSvg />
								MyPage
							</nuxt-link>
						</li>
						<li v-if="$route.path.startsWith('/mypage')">
							<nuxt-link to="/mypage/drafts">
								<DraftsSvg />
								Drafts
							</nuxt-link>
						</li>
						<li>
							<nuxt-link to="/">
								<PostsSvg />
								Posts
							</nuxt-link>
						</li>
						<li>
							<nuxt-link to="./stocked">
								<StockedSvg />
								Stocked
							</nuxt-link>
						</li>
					</ul>
					<search-box-view />
					<p class="title-logo">
						<nuxt-link to="/">
							<img v-bind:src="logoTitle" alt="INIAD Stock">
						</nuxt-link>
					</p>
				</nav>
			</div>
			<main>
				<Nuxt />
			</main>
			<div class="tag-list">
				<ul>
					<li v-for="tag of tags" v-bind:key="tag.uuid">
						<nuxt-link v-bind:to="`/tags/${tag.uuid}`">
							{{ tag.name }}
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
import MyPageSvg from '@/assets/img/mypage.svg?inline'
import DraftsSvg from '@/assets/img/drafts.svg?inline'
import PostsSvg from '@/assets/img/posts.svg?inline'
import StockedSvg from '@/assets/img/stocked.svg?inline'
import GithubSvg from '@/assets/img/github.svg'
import GitlabSvg from '@/assets/img/gitlab.svg'
import TwitterSvg from '@/assets/img/twitter.svg'
import LinkSvg from '@/assets/img/link.svg'
import LogoTitle from '~/assets/img/logo-title.svg'
import UserProfileEditView from '~/components/UserProfileEditView'
import initializeMyUser from '~/mixins/initializeMyUser'

export default {
	name: 'UserLayout',
	components: {
		MyPageSvg,
		DraftsSvg,
		PostsSvg,
		StockedSvg,
	},
	mixins: [initializeMyUser],
	data () {
		return {
			user: {},
			tags: [],
		}
	},
	async fetch () {
		if (!this.tags) {
			const response = await this.$http.get('/api/tags/')
			const tags = await response.json()
			if (!this.tags) {
				this.tags = tags
			}
		}
	},
	computed: {
		logoSmall () {
			return LogoSmall
		},
		logoTitle () {
			return LogoTitle
		},
		githubSvg () {
			return GithubSvg
		},
		gitlabSvg () {
			return GitlabSvg
		},
		twitterSvg () {
			return TwitterSvg
		},
		linkSvg () {
			return LinkSvg
		},
	},
	created () {
		this.$nuxt.$on('updateUser', (user) => {
			this.user = user
			this.tags = user.used_tags
		})
	},
	methods: {
		openUserProfileEdit () {
			this.$modal.show(
				UserProfileEditView,
				{
					user: this.user,
				},
				{
					width: '70%',
					height: '70%',
				},
			)
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

		.username {
			a {
				display: flex;
				align-items: center;
				width: 100%;
				justify-content: center;
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
		}
	}
}

.main-wrap {
	margin-top: 3rem;
	display: flex;
	flex-grow: 1;
	flex-shrink: 1;

	.profile-wrap {
		display: flex;
		flex-direction: column;
		position: sticky;
		top: 9rem;
		height: fit-content;
		width: $side-width;
		flex-shrink: 0;
		flex-grow: 0;
		padding-left: 50px;
		padding-right: 15px;
		background-color: #fff;

		.profile {
			flex-grow: 1;

			.about {
				display: flex;
				align-items: center;

				.user-icon {
					img {
						width: 2.8em;
						height: 2.8em;
						border-radius: 50%;
					}
				}

				.user-meta {
					margin-left: 0.5em;

					.username {
						margin-top: 0.8em;
					}

					.userid {
						font-size: 0.7em;
					}

					.follows {
						font-size: 0.7em;
						display: flex;

						a {
							text-decoration: none;

							&:not(:last-child) {
								margin-right: 0.5em;
							}

							&:hover {
								text-decoration: underline;
							}
						}
					}
				}
			}

			.comment {
				margin: 0.5em 0;

				p {
					margin: 0.5em 0;
				}
			}

			ul.links {
				display: flex;
				align-items: flex-end;
				list-style: none;
				margin: 0.5em 0;
				padding: 0;

				li {
					img {
						display: block;
						height: 1.2em;

						&.github {
							height: 1.4em;
						}
					}

					&:not(:last-child) {
						margin-right: 0.5em;
					}
				}
			}

			.follow,
			.profile-settings {
				margin: 0.8em 0;

				button {
					width: 100%;
					background-color: transparent;
					border: $main-color 1px solid;
					border-radius: 0.5em;
					padding: 0.2em 0;
				}
			}
		}

		nav {
			ul {
				list-style: none;
				padding: 0;
				margin-bottom: 1em;

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
