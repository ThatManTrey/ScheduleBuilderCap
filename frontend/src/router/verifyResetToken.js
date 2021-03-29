import axios from 'axios';
import * as Toast from '../toast.js';

export default (to, from, next) => {
    var resetPassToken = to.query.token;

    if (resetPassToken) {
        axios
            .get("/auth/verify/reset-pass", {
                headers: { Authorization: "Bearer " + resetPassToken }
            })
            .then(() => {
                next({
                    query: {
                        token: resetPassToken
                    }
                });
            })
            .catch(() => {
                next("/home");
                Toast.showErrorMessage(
                    "Invalid or expired reset password link. Request another and try again."
                );
            });
    } else {
        next("/home");
        Toast.showErrorMessage("Invalid reset password link.");
    }
}