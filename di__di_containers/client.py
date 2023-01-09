from typing import cast

from di__di_containers.injection_configuration import container
from di__di_containers.mail_providers import Mail, MailProvider


def run():
    mail_provider = cast(MailProvider, container.resolve(MailProvider))
    Mail(provider=mail_provider).send(to='to', subject='subject', message='message')
