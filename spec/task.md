#Problem statement
Write a program that will ingest log records to determine the overall health of the system. This test is based
on OpenTracing. Please refer to the OpenTracing docs (http://opentracing.io/documentation) for an overview of tracing.

Your program will need to read in the transaction log records in the provided log-data.json file to determine
the number of failed transactions and the causes of the failure.

A transaction can span multiple systems; a single trace_id is used for the entire transaction, while a new span_id is
used for each logical operation that is performed.

The log data is not in order as it is aggregated from multiple sources. It will need to be sorted.

Output should be printed to stdout (standard output)

Output the failure cause trace in the following format: - <time> <app> <component> <msg>. Child spans should be nested.

##For example:
- 2018-08-26T17:35:39+10:00 svc-app-1 auth.user.Login() starting login for bd5f12d5-130a-4ed3-bf21-0eff55c1a2af
- 2018-08-27T15:55:33+10:00 svc-app-2 auth.user.AuthCheck() checking auth creds for bd5f12d5-130a-4ed3-bf21-0eff55c1a2af
- 2018-08-28T00:44:18+10:00 svc-app-2 auth.user.AuthCheck() extracted subject from JWT token
- 2018-08-28T15:03:50+10:00 svc-app-2 auth.user.AuthCheck() verification of subject in JWT token failed: past expiry date
- 2018-08-28T15:03:50+15:00 svc-app-1 auth.user.Login() auth check provider returned auth failure for bd5f12d5-130a-4ed3-bf21-0eff55c1a2af
- 2018-08-29T11:53:35+10:00 svc-app-1 auth.user.Login() login failed for bd5f12d5-130a-4ed3-bf21-0eff55c1a2af

#Requirements
No libraries or frameworks are to be used; only the standard libraries available in the language chosen.

Please briefly document:
your design choices,
any assumptions you have made
comment on the runtime and memory complexity of your solution
Please provide the URL to the GitHub repo with your solution.