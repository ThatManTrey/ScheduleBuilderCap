import Vue from "vue";
import axios from "axios";
import jwt_decode from "jwt-decode";

export const store = Vue.observable({
  isLoggedIn: false,
  userId: -1
});

export const actions = {
  login(authToken) {
    var decodedToken = jwt_decode(authToken);
    store.userId = decodedToken.sub;

    localStorage.setItem("userInfo", authToken);

    store.isLoggedIn = true;
    axios.defaults.headers.common["Authorization"] = "Bearer " + authToken;
  },

  logout() {
    store.isLoggedIn = false;
    store.userId = -1;
    localStorage.removeItem("userInfo");
    delete axios.defaults.headers.common["Authorization"];
  }
};
