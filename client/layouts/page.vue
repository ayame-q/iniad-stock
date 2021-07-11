<template>
	<div class="wrap">
		<header>
			<div class="title-column">
				<h1>
					<nuxt-link to="/">
						<img src="@/assets/img/logo.svg" alt="INIAD Stock">
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
				<ul>
					<li>
						<a href="#">
							<img src="@/assets/img/search.svg" alt="Search">
						</a>
					</li>
					<li>
						<nuxt-link to="/">
							<img src="@/assets/img/home.svg" alt="Home">
						</nuxt-link>
					</li>
					<li>
						<nuxt-link to="/trends">
							<img src="@/assets/img/trend.svg">
						</nuxt-link>
					</li>
				</ul>
			</nav>
			<main>
				<Nuxt />
			</main>
		</div>
		<footer-view />
	</div>
</template>

<script>
export default {
	name: 'PageLayout',
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
		width: 420px;
		flex-shrink: 0;
		flex-grow: 0;
	}

	h1 {
		width: 420px;
		height: 6rem;
		padding-left: 50px;
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

	nav {
		position: sticky;
		top: 3rem;
		height: fit-content;
		width: 86px;
		flex-shrink: 0;
		flex-grow: 0;
		padding-left: 50px;
		padding-right: 15px;
		background-color: #fff;

		.search-box {
			margin-bottom: 1em;
			position: relative;

			input[type=search] {
				background-color: $sub-color;
				border: none;
				width: calc(100% + 1rem);
				margin-left: -1rem;
				height: 2.6rem;
				border-radius: 0.8rem;
				padding: 0 1.2rem;
				padding-right: 3rem;
				color: #fff;
			}

			button {
				display: block;
				position: absolute;
				top: 50%;
				transform: translateY(-50%);
				right: 0.5em;
				background-color: transparent;
				border: none;

				img {
					width: 1.2em;
					display: block;
				}
			}
		}

		ul {
			list-style: none;
			padding: 0;

			li {
				padding: 0.6rem 0;
				margin-left: -1rem;
				padding-left: 1rem;

				a {
					text-decoration: none;

					&:hover {
						color: $sub-color;
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
					}
				}
			}
		}
	}

	main {
		width: 100%;
		height: 100%;
		border: $main-color 1px solid;
		margin-right: 50px;
		padding: 1rem;
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
