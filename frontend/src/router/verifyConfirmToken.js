import axios from 'axios';
import * as Toast from '../toast.js';

export default (to, from, next) => {
    var confirmationToken = to.query.token;

    if (confirmationToken) {
        axios
            .get("/auth/verify/confirm", {
                headers: { Authorization: "Bearer " + confirmationToken }
            })
            .then(() => {
                next("/home");
                Toast.showSuccessMessage(
                    "Your email has been confirmed successfully!"
                );
            })
            .catch(() => {
                next("/home");
                Toast.showErrorMessage("You have already confirmed your email.");
            });
    } else {
        next("/home");
        Toast.showErrorMessage("Invalid email confirmation link.");
    }
}