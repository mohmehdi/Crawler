# Job Crawler

### how to use it:
 `scrapy crawl jobsp -a urls="www.freelancer.com/projects/1 www.freelancer.com/projects/2" -a depth=2 --nolog -O out.json`

+ **`-a`** is for adding arguments to spider  
+ **`--nolog`** means no log obviously  
+ **`-o out.json`**  saves file in json format  
**`-O`** does the same and overwrites the json file
##### Adding URLs:
from [freelancer website](freelancer.com) take a job url   
use `-a urls=` and put it in these `" "` make sure to leave a space between them  like this --> **"** url1 url2 url3 **"**  
#####  Set Depth to Crawl
**`-a depth`** means how deep to crawl and if set to 0 it just crawls starting urls  , by defualt its 1

##### Using Crawled Data
for using crawled jobs run **main.py** (recommended to run it in a console)  
it just shows data in a more human friendly way

[githubpage](https://github.com/mohmehdi/Crawler)
