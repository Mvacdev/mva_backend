# using SendGrid's Python Library
from django.core.mail import get_connection, EmailMultiAlternatives
from python_http_client import HTTPError
from sendgrid import Header

from crm_proj.settings import SENDGRID_API_KEY, SENDER

# -- 1)
# html_message_client = loader.render_to_string(
#     '.html',
#     params
# )
# -- 2)
# send_html_mail_with_hidden_recipients(
#     sublist=['...@gmail.com'],
#     subject=subject, client=html_message_client
# )


def send_mass_html_mail(datatuple, fail_silently=False, auth_user=None,
                        auth_password=None, connection=None):
    """
    Given a datatuple of (subject, message, html_message, from_email,
    recipient_list), send each message to each recipient list.
    Return the number of emails sent.
    If from_email is None, use the DEFAULT_FROM_EMAIL setting.
    If auth_user and auth_password are set, use them to log in.
    If auth_user is None, use the EMAIL_HOST_USER setting.
    If auth_password is None, use the EMAIL_HOST_PASSWORD setting.
    """
    connection = connection or get_connection(
        username=auth_user,
        password=auth_password,
        fail_silently=fail_silently,
    )
    messages = [
        EmailMultiAlternatives(subject, message, sender, recipient,
                               alternatives=[(html_message, 'text/html')],
                               connection=connection)
        for subject, message, html_message, sender, recipient in datatuple
    ]
    return connection.send_messages(messages)


def send_html_mail_with_hidden_recipients(sublist: list, subject: str, client: str) -> None:
    from sendgrid.helpers.mail import Mail, Email, Content, Personalization
    from sendgrid import sendgrid

    mail = Mail()

    for to_email in sublist:
        # Create new instance for each email
        personalization = Personalization()
        # Add email addresses to personalization instance
        personalization.add_to(Email(to_email))
        # Add personalization instance to Mail object
        mail.add_personalization(personalization)

    # mail.add_header(
    #     header={
    #         'List-Unsubscribe': '<mailto:tech@price-bot-kz>'
    #     }
    # )
    # mail.set_headers({'X-Priority' : '2'}) #<=== To add priority
    mail.personalizations[0].add_header(Header("List-Unsubscribe", "<mailto:tech@price-bot.kz>"))

    mail.from_email = Email(SENDER)
    mail.subject = subject
    # mail.add_content(Content('text/plain', 'message_txt'))
    mail.add_content(Content('text/html', client))

    # Send
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    sg.client.mail.send.post(request_body=mail.get())


def send_web_api_message(to=None, subject=None, html=None):
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    message = Mail(
        from_email=SENDER,
        to_emails=to,
        subject=subject,
        html_content=html
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
    except HTTPError as e:
        print(e.to_dict)


#
# def sendgrid_message():
#     message = Mail(
#         from_email='from_email@example.com',
#         to_emails='to@example.com',
#         subject='Sending with Twilio SendGrid is Fun',
#         html_content='<strong>and easy to do anywhere, even with Python</strong>')
#     try:
#         sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#         response = sg.send(message)
#         print(response.status_code)
#         print(response.body)
#         print(response.headers)
#     except Exception as e:
#         print(e.message)
