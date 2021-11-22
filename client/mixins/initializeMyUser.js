import InitializeModal from '~/components/InitializeModal'

export default {
	mounted () {
		const myUser = this.$store.getters['myUser/get']
		if (myUser.is_authenticated && !myUser.is_initialized) {
			this.$modal.show(InitializeModal, {}, {
				width: '80%',
				height: '80%',
				draggable: false,
				clickToClose: false,
			})
		}
	},
}
