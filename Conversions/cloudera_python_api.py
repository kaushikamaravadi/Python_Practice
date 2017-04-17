from cm_api.api_client import ApiResource
import smtplib


import time
import datetime
cm_host = '104.198.165.120'
api = ApiResource(cm_host, 7180, username="admin", password='admin')
# Basic Usage

cdh5 = None
cdh4 = None
for cluster in api.get_all_clusters():
    print(cluster.name)
    if cluster.version == 'CDH5':
        cdh5 = cluster
    if cluster.version == 'CDH4':
        chd4 = cluster
# print cdh5
# print cdh4
# Inspecting a Service
hdfs = None
for s in cdh5.get_all_services():
    print s
    if s.type == "HDFS":
        hdfs = s

yarn = None


# for services in cdh5.get_all_services():
#     print services.name, services.healthSummary
#     print services.get_config(view='full')[0].items()



# print "Name: ", hdfs.name
# print "Status: ", hdfs.serviceState
# print "heath Summary: ", hdfs.healthSummary
# print "URL: ", hdfs.serviceUrl
# Inspect the HDFS service Health and status

# for check in hdfs.healthChecks:
    # print check['name'], check['summary']

# Inspecting a Role

namenode = None

# for role in hdfs.get_all_roles():
#     if role.type == "NAMENODE":
#         namenode = role
# print "Role name: %s\nState: %s\nHealth: %s\nHost: %s" % (namenode.name, namenode.roleState, namenode.healthSummary,
#                                                           namenode.hostRef.hostId)

# getting Metrics

# metrics = hdfs.get_metrics()
# print len(metrics)

# for metric in metrics:
#     print metric.name, metric.util
#
#
# from_time = datetime.datetime.fromtimestamp(time.time() - 1800)
# to_time = datetime.datetime.fromtimestamp(time.time())
# query = "select files_total, dfs_capacity_used " \
#         "where serviceName = HDFS-1 " \
#         "  and category = SERVICE"
#
# result = api.query_timeseries(query, from_time, to_time)
# ts_list = result[0]
# for ts in ts_list.timeSeries:
#     print "--- %s: %s ---" % (ts.metadata.entityName, ts.metadata.metricName)
#     for point in ts.data:
#         print "%s:\t%s" % (point.timestamp.isoformat(), point.value)

# Restart HDFS and namenode
# command = hdfs.restart()
# print command.active
#
# command = command.wait()
# command = hdfs.restart().wait()
# cmds = hdfs.restart_roles(nn.name)
# for cmd in cmds:
#     print cmd

# Configuring Serives and roles
hdfs_config = {}
for name, config in hdfs.get_config(view='full')[0].items():
    # print "%s - %s" % (name, config.description)
    hdfs_config[name] = config.description


print hdfs_config



