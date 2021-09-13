# Labs 7-8

## Screenshots of a successfully working stack (Promtail, Loki, Grafana)

- Working app

![Working app](https://i.ibb.co/SBbmnsM/Screenshot-2021-09-13-at-00-52-28.png)

- Running Loki service

![Running Loki service](https://i.ibb.co/NTpmjj2/Screenshot-2021-09-13-at-00-58-47.png)

- Configuration of Grafana with Loki

![Configuration of Grafana with Loki](https://i.ibb.co/dfDzcj7/Screenshot-2021-09-13-at-00-54-27.png)

- Grafana Log Browser

![Grafana Log Browser](https://i.ibb.co/Dbm4Jq4/Screenshot-2021-09-13-at-00-55-20.png)

- Grafana Dashboard

![Grafana Dashboard](https://i.ibb.co/wyXWzVb/Screenshot-2021-09-13-at-00-57-47.png)

## Basic best practices for logging

1. Use logging libraries to produce logs for your app.
2. Define the log level needed. 

I've chosen ```warn``` to monitor all events that can potentially become errors.

3. Log in machine parseable format.

So, my application sends logs in *JSON* format.

4. Don't log excessively or insufficiently. Find the balance.

So, in *docker-compose.yml* I specified that I want to get logs only from containers of Promtail, Loki, Grafana and my app. Also, I limited the maximum size of the log before it is rolled (```max-size```) and the maximum amount of present logs(```max-file```).

5. Don’t log sensitive information.

## Best practices for Promtail

1. Configure ```positions``` block.
This block is responsible for specifying a location where Promtail will save a file indicating how far it has read into a file. In case of a Promtail's restart, the file allows to proceed reading from where Promtail has stopped. Also, you need to performing corresponding mounting in *docker-compose.yml*. 

2. Configure how Promtail will scrape logs in ```scrape_configs```.

## Best practices for Grafana

1. Manage data sources by separate config files in *provisioning/datasources*.
2. Provide a separate file *config.monitoring* with log in cerdentials for Grafana.
3. Manage dashboards by separate config files in *provisioning/dashboards*.

## Acknowledgements

- [Basic Best Practices for Logging](https://www.scalyr.com/blog/the-10-commandments-of-logging/)
- [Configuring Promtail](https://grafana.com/docs/loki/latest/clients/promtail/configuration/)
- [Configuring Loki](https://grafana.com/docs/loki/latest/configuration/)
- [Configuring Grafana](https://grafana.com/docs/grafana/latest/administration/provisioning/)