from crontab import CronTab

def update_cron(sintax_cron):
    cron = CronTab(user='raspberry')  # Cambia 'tu_usuario' al usuario que tiene la tarea cron
    interval_cron = cron[-1]
    interval_cron.setall(sintax_cron)
    cron.write()
    print('Cron updated')