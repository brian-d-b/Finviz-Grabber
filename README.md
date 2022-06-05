# Finviz-Grabber
 Grabs and uploads the Finviz SNP500 Heatmap
![image](https://user-images.githubusercontent.com/31077794/172039661-c93798b6-4093-42c0-af0c-981f21ead0e7.png)


# Google Cloud Storage
Uploads the image to two separate buckets: current-finviz-image and finviz-heatmaps.

current-finviz-image bucket is used for my stock-webapp project that is also public

finviz-heatmaps is a bucket that stores all of these charts with a timestamp. Will be used for future web-applications and fun charting

# Environment

This is ran 10:30AM-4:30PM M-F on an hourly basis (market hours) on a spare, headless Windows 10 PC.
This is scheduled through Task Scheduler
