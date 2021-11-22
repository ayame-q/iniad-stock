<template>
	<article class="initialize">
		<div class="title">
			<h2>INIAD Stockへようこそ</h2>
			<p>あなたが他の人にどのように見えるかを設定しましょう</p>
		</div>
		<form v-on:submit.prevent="submit">
			<p class="display-name">
				<label for="id_display-name">公開名</label>
				<input id="id_display-name" v-model="displayName" type="text">
			</p>
			<p class="screen-name">
				<label for="id_screen-name">ユーザーID</label>
				<input id="id_screen-name" v-model="screenName" type="text">
			</p>
			<p><input type="submit" value="登録"></p>
		</form>
	</article>
</template>

<script>
export default {
	name: 'InitializeModal',
	data () {
		return {
			screenName: null,
			displayName: null,
		}
	},
	fetch () {
		const myUser = this.$store.getters['myUser/get']
		this.screenName = myUser.screen_name
		this.displayName = myUser.display_name
	},
	methods: {
		submit () {
			this.$http.patch('/api/my_user', {
				screen_name: this.screenName,
				display_name: this.displayName,
			}, {
				headers: {
					'X-CSRFToken': this.$cookies.get('csrftoken'),
				},
			})
				.then((response) => {
					return response.json()
				})
				.then((myUser) => {
					this.$store.commit('myUser/update', myUser)
					this.$emit('close')
				})
		},
	},
}
</script>

<style lang="scss" scoped>
.initialize {
	margin: 1rem;
}

h2,
p {
	margin: 1rem 0;
}

.title {
	h2 {
		margin-bottom: 0;
	}

	p {
		margin-top: 0;
	}
}

form {
	p {
		label {
			display: block;
		}

		input {
			&[type=text] {
				display: block;
				border: none;
				border-bottom: $main-color solid 1px;
				padding: 0.5rem;
			}

			&[type=submit] {
				display: block;
				border: none;
				background-color: $main-color;
				color: #fff;
				padding: 0.7rem;
				width: 50%;
				border-radius: 0.2rem;
				margin-left: auto;
				margin-right: 0;
			}
		}

		&.display-name {
			input {
				font-size: 2rem;
			}
		}

		&.screen-name {
			position: relative;

			input {
				position: relative;
				font-size: 1.3rem;
				padding-left: 1.5rem;
			}

			&::before {
				display: block;
				width: fit-content;
				content: "@";
				position: absolute;
				left: 0.5rem;
				bottom: 0.5rem;
				z-index: 1;
			}
		}
	}
}

</style>
