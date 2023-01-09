import punq as punq

from di__di_containers.mail_providers import MailProvider, UnioneProvider, MailgunProvider

container = punq.Container()
container.register(MailProvider, MailgunProvider)
