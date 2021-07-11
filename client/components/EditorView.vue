<template>
	<div>
		<form v-bind:class="{fullscreen: isEditorFullScreen, optionsFolded: !isOptionsOpen}" v-on:click="editorFullScreen">
			<p class="title" v-bind:class="{fullscreen: isEditorFullScreen}">
				<input type="text" placeholder="タイトル">
			</p>
			<vue-easymde
				v-bind:configs="easyMDEConfigs"
				v-on:initialized="easyMDEInitialized"
				v-on:input="editorFullScreen"
			/>
			<div class="options" v-bind:class="{fullscreen: isEditorFullScreen, folded: !isOptionsOpen}">
				<div class="fold-button" v-bind:class="{folded: !isOptionsOpen}" v-on:click="toggleOptionsOpen" />
				<div class="tags">
					<vue-tags-input
						v-model="tag"
						v-bind:tags="tags"
						placeholder="タグを追加"
						v-on:tags-changed="newTags => tags = newTags"
					/>
				</div>
				<p class="submit-wrap">
					<span><input id="only-iniad" type="checkbox"><label for="only-iniad">学内限定公開</label></span>
					<input type="button" value="下書き保存" class="draft-save">
					<input type="submit" value="投稿" class="submit">
				</p>
			</div>
		</form>
		<div class="close-button" v-bind:class="{fullscreen: isEditorFullScreen}" v-on:click="editorFold" />
	</div>
</template>

<script>
export default {
	name: 'EditorView',
	data () {
		return {
			tag: [],
			isEditorFullScreen: false,
			isOptionsOpen: true,
			easyMDE: null,
			easyMDEConfigs: {
				spellChecker: false,
				status: false,
				placeholder: 'あなたの経験・知識を残しましょう',
				toolbar: [
					'bold',
					'italic',
					'heading',
					'|',
					'quote',
					'unordered-list',
					'ordered-list',
				],
			},
		}
	},
	mounted () {
		window.addEventListener('keyup', (event) => {
			if (event.key === 'Escape') {
				this.editorFold()
			}
		})
	},
	methods: {
		editorFullScreen () {
			if (!this.easyMDE.isFullscreenActive()) {
				this.easyMDE.toggleSideBySide()
			}
			this.isEditorFullScreen = true
		},
		editorFold () {
			if (this.easyMDE.isFullscreenActive()) {
				this.easyMDE.toggleFullScreen()
			}
			this.isEditorFullScreen = false
		},
		easyMDEInitialized (easyMDE) {
			this.easyMDE = easyMDE
		},
		toggleOptionsOpen () {
			this.isOptionsOpen = !this.isOptionsOpen
		},
	},
}
</script>

<style lang="scss" scoped>
.title {
	display: none;

	&.fullscreen {
		input {
			width: 100vw;
			height: 50px;
			background-color: #fff;
			border: none;
			border-bottom: $main-color solid 1px;
			padding: 0 15px;
		}

		z-index: 99;
		display: block;
		position: fixed;
		top: 0;
		left: 0;
	}
}

.close-button {
	display: none;
	position: fixed;
	top: 20px;
	right: 20px;
	z-index: 999;
	background-color: #fff;
	border-radius: 1em;
	width: 60px;
	height: 60px;
	border: $main-color 1px solid;
	background-image: url("~/assets/img/close.svg");
	background-size: 45%;
	background-repeat: no-repeat;
	background-position: center;

	&.fullscreen {
		display: block;
	}
}

.options {
	display: none;
	transition: bottom 0.3s;

	&.fullscreen {
		background: #fff;
		display: block;
		position: fixed;
		bottom: 0;
		right: 0;
		width: 50vw;
		border-left: $main-color solid 1px;
		z-index: 999;
	}

	&.folded {
		bottom: -110px;
	}

	.fold-button {
		width: 100%;
		background-color: $main-color;
		height: 25px;

		&::before {
			display: block;
			content: "▼";
			text-align: center;
			width: 100%;
			color: white;
		}

		&.folded {
			&::before {
				content: "▲";
			}
		}
	}

	.tags {
		::v-deep {
			.vue-tags-input {
				width: 100%;
				max-width: none;

				.ti-input {
					width: 100%;
					height: 40px;
					background-color: #fff;
					border: none;
					border-bottom: $main-color solid 1px;
					padding: 0 15px;
				}

				.ti-tag {
					background-color: $main-color;

					&.ti-deletion-mark {
						background-color: $subtext-color;
					}
				}
			}
		}
	}

	.submit-wrap {
		padding: 10px;
		display: flex;
		justify-content: flex-end;
		align-items: center;

		input {
			&[type=submit],
			&[type=button] {
				border: $main-color solid 1px;
				height: 50px;
				border-radius: 0.3em;
				background-color: #fff;

				&:not(:last-child) {
					margin-right: 1em;
				}

				&.draft-save {
					width: 25%;
				}

				&.submit {
					width: 50%;
					color: #fff;
					background-color: $main-color;
				}
			}

			&[type=checkbox] {
				margin-right: 0.5em;

				+ label {
					margin-right: 1em;
				}
			}
		}
	}
}
</style>

<style lang="scss">
.EasyMDEContainer {
	.editor-toolbar {
		&.fullscreen {
			top: 50px;
		}

		button {
			color: $text-color !important;

			&.active,
			&:hover {
				border: $main-color solid 1px;
			}
		}

		i.separator {
			border-left: $placeholder-color solid 1px;
		}

		&:not(.fullscreen) {
			display: none;
		}
	}

	.CodeMirror {
		color: $text-color !important;

		&:not(.CodeMirror-fullscreen) {
			border: $main-color solid 1px;
			border-radius: 0;
			min-height: auto;
			height: 6rem;
			padding-left: 1rem;
		}

		&.CodeMirror-fullscreen {
			top: 100px;
			border-top: $main-color solid 1px;
			border-right: $main-color solid 1px;
		}
	}

	.editor-preview-side {
		top: 100px;
		bottom: 135px;
		transition: bottom 0.3s;
		border-top: $main-color solid 1px;
		border-left: $main-color solid 1px;
		border-bottom: none;
	}

	.editor-preview {
		background-color: $sub-background-color;
	}

	.CodeMirror-placeholder {
		color: $placeholder-color !important;
	}
}

.optionsFolded {
	.EasyMDEContainer {
		.editor-preview-side {
			bottom: 25px;
		}
	}
}
</style>
