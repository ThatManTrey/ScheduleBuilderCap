<template lang="html">
    <div>
        <div class="container-fluid">
            <div class="row justify-content-center">
                <div class="col-10 col-sm-8 col-md-6 col-lg-5 col-xl-4 vertical-center justify-content-center">
                    <div class="card signin-box">
                        <div class="card-body">
                            <div>
                                <h2 class="text-center">KSU Course Planner</h2>
                                <p class="slogan-subtext">A better way to plan your degree</p>
                                <!-- put logo here maybe? -->
                            </div>
    
                            <div class="container mb-3">
                                <form>
                                    <div class="mb-3">
                                        <label for="exampleInputEmail1" class="form-label">Email Address</label>
                                        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                                    </div>
                                    <div class="mb-3">
                                        <label for="exampleInputPassword1" class="form-label">Password</label>
                                        <input type="password" class="form-control" id="exampleInputPassword1" aria-describedby="passHelp">
                                        <div id="passHelp" class="form-text">Passwords must be more than x characters long.</div>
                                    </div>
                                    <div class="mb-3">
                                        <label for="exampleInputPassword1" class="form-label">Re-enter Password</label>
                                        <input type="password" class="form-control" id="exampleInputPassword1">
                                    </div>
                                    <div class="mb-3 text-center">
                                        <p style="font-size: 0.9rem;">
                                            <a href="#">Return to login</a>
                                        </p>
                                    </div>
                                    <div class="mb-3 text-center">
                                        <button type="submit" class="btn btn-primary">Sign Up</button>
                                    </div>
                                </form>
                            </div>
    
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="js">

export default {
    name: 'register',
    props: [],
    components: {
    },
}
</script>

<style scoped>

</style>
