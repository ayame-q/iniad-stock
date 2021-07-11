<template>
	<form class="profile-edit">
		<div class="about">
			<p class="user-icon">
				<img src="/img/icon_sample.png" alt="">
			</p>
			<div class="user-meta">
				<p class="username">
					<input type="text" v-bind:value="user.name" placeholder="ユーザー名">
				</p>
				<p class="userid">
					<input type="text" v-bind:value="user.id" placeholder="ID">
				</p>
			</div>
		</div>
		<div class="comment">
			<p>
				<textarea v-bind:value="user.comment" />
			</p>
		</div>
		<ul class="links">
			<li>
				<label for="github-id">Github ID</label>
				<input id="github-id" type="text" v-bind:value="user.github">
			</li>
			<li>
				<label for="gitlab-id">GitLab ID</label>
				<input id="gitlab-id" type="text" v-bind:value="user.gitlab">
			</li>
			<li class="twitter">
				<label for="twitter-id">Twitter ID</label>
				<input id="twitter-id" type="text" v-bind:value="user.twitter">
			</li>
			<li>
				<label for="link-id">Website</label>
				<input id="link-id" type="text" v-bind:value="user.website">
			</li>
		</ul>
		<p class="submit">
			<input type="submit" value="保存">
		</p>
		<div class="close-button" v-on:click="$emit('close')" />
	</form>
</template>

<script>
export default {
	name: 'UserProfileEditView',
	props: {
		user: Object,
	},
}
</script>

<style lang="scss" scoped>
.profile-edit {
	width: 100%;
	height: 100%;
	display: flex;
	flex-direction: column;
	position: relative;

	input,
	textarea {
		border: none;
		border-bottom: $main-color solid 1px;
		border-radius: 0;
		resize: none;
		padding: 0.8em;

		&:first-child {
			border-top: $main-color solid 1px;
		}
	}

	.about {
		display: flex;
		align-items: center;

		.user-icon {
			padding: 2vw;

			img {
				width: 10vw;
				height: 10vw;
				border-radius: 50%;
			}
		}

		.user-meta {
			input {
				border-top: none;
			}

			.username {
				input {
					font-size: 1.5em;
				}
			}

			.userid {
				position: relative;

				&::before {
					content: "@";
					position: absolute;
					left: 0;
					top: 0;
					padding: 0.4em 0;
				}

				input {
					padding-left: 1.3em;
				}
			}
		}
	}

	.comment {
		flex-grow: 1;
		flex-shrink: 1;

		p {
			width: 100%;
			height: 100%;

			textarea {
				width: 100%;
				height: 100%;
			}
		}
	}

	ul.links {
		list-style: none;
		padding: 0;

		li {
			display: flex;
			align-items: center;

			label {
				padding-left: 0.8em;
				width: 6.5em;
				flex-shrink: 0;
			}

			input {
				width: 100%;
				flex-shrink: 1;
				border-left: $main-color solid 1px;
			}

			&.twitter {
				position: relative;

				input {
					padding-left: 2.2em;
				}

				&::before {
					content: "@";
					position: absolute;
					left: 7.2em;
					top: 0;
					padding: 0.4em 0;
				}
			}
		}
	}

	.submit {
		display: flex;
		justify-content: flex-end;

		input[type=submit] {
			width: 50%;
			background-color: $main-color;
			color: #fff;
			border-radius: 0.5em;
			margin: 0.5em;
		}
	}

	.close-button {
		position: absolute;
		top: 20px;
		right: 20px;
		z-index: 999;
		width: 45px;
		height: 45px;
		background-image: url("~/assets/img/close.svg");
		background-size: 45%;
		background-repeat: no-repeat;
		background-position: center;
		cursor: pointer;

		&.fullscreen {
			display: block;
		}
	}
}
</style>
