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