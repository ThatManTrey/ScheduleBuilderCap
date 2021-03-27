def get_reset_password_txt(token):
    # change to config setting
    url =  "http://localhost:8080/#/reset?token=" + token

    reset_password_txt = """We received a request to reset the password your
                            KSUCoursePlanner account.

                            Click the link below to select a new password.
                            
                            {}

                            If you did not create this request then please ignore this message.

                            - The KSU Course Planner Team
                            """.format(url)
    
    return reset_password_txt


def get_reset_password_html(token):
    # change to config setting
    url =  "http://localhost:8080/#/reset?token=" + token

    reset_password_html = """<p>We received a request to reset the password your
                            KSUCoursePlanner account.</p>

                            <a href="{}">Click here</a> to select a new password (this link will expire in 1 hour).</p>

                            <p>If you did not create this request then please ignore this message.</p>

                            </p>- The KSU Course Planner Team</p>
                            """.format(url)
    
    return reset_password_html


def get_confirm_email_txt(token):
    # change to config setting
    url =  "http://localhost:8080/#/confirm?token=" + token

    confirm_email_txt = """ Thanks for signing up for KSU Course Planner!

                            To be able to rate courses and reset your password, you'll have to verify your account first. You can do that by clicking opening the link below:

                            {}

                            - The KSU Course Planner Team
                            """.format(url)
    
    return confirm_email_txt


def get_confirm_email_html(token):
    # change to config setting
    url =  "http://localhost:8080/#/confirm?token=" + token

    confirm_email_html = """<p>Thanks for signing up for KSU Course Planner!</p>

                            <p>To be able to rate courses and reset your password, you'll have to verify your account first. You can do that by <a href="{}">clicking here</a>.</p>

                            <p>- The KSU Course Planner Team</p>
                            """.format(url)
    
    return confirm_email_html