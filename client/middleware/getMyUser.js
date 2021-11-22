export default async ({ store, modal }) => {
	if (!store.getters['myUser/getIsUpdated']) {
		await store.dispatch('myUser/getMyUser')
	}

	const myUser = store.getters['myUser/get']
	if (myUser.is_authenticated && !myUser.is_initialized) {
		console.log(modal)
	}
}
