# CBlockCrawler

This program is created for extracting required code parts from C source files. It's main purpose is finding module's parts that are added to code via preprocessor conditions. For example, nginx http_ssl module doesn't exist in a separate directory, it has it's code all over the place and added when #if (NGX_HTTP_SSL) condition is met.  
