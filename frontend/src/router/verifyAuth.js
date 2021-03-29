import store from '../store';
import * as Toast from '../toast.js';

export default (to, from, next) => {
	if (!store.state.isAuthenticated) {
		next("/home");
		Toast.showErrorMessage(
			"You'll need to login before you can view that page."
		);
	} else next();
}