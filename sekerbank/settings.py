BOT_NAME = 'sekerbank'
SPIDER_MODULES = ['sekerbank.spiders']
NEWSPIDER_MODULE = 'sekerbank.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'sekerbank.pipelines.DatabasePipeline': 300,
}
