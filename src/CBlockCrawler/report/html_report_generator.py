from CBlockCrawler.report.report_generator import ReportGenerator
import re

#import logging
#
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)  
#
#console_handler = logging.StreamHandler()
#console_handler.setLevel(logging.DEBUG)  
#
#formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
#console_handler.setFormatter(formatter)
#
#logger.addHandler(console_handler)

class HTMLReportGenerator(ReportGenerator):
    def generate_report(self):
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report</title>
    <style>
        :root {
            font-family: Arial, sans-serif;
        }
        h2 {
            text-align: center;
            color: #333;
        }
        table {
            width: 100%%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 18px;
            text-align: left;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
        }
        td {
            word-wrap: break-word;   
            white-space: normal;               
            overflow-wrap: break-word; 
        }

        th {
            background-color:   #d7ebd8;
        }
        tr:hover {
             background-color:   #f2fff9;
        }
        .divider-row td {
            height: 5px;
            background-color: #f9f9f9;
            border: none;
            padding: 2px;
        }
    </style>
    <script>
        function sortTable(columnIndex, isNumeric) {
            // later
        }
    </script>
</head>
<body>
    <h2>Report</h2>
    <table>
        <thead>
            <tr class="head"> 
                %s
            </tr>
        </thead>
        <tbody class="content">
            %s
        </tbody>
    </table>
</body>
</html>
"""
        header_row = "".join(f"<th>{field}</th>" for field in self.fields)
        

        rows = []

        for one_file_records in self.all_records:
            for i in range(len(one_file_records)):
                row_data = "".join(
                    f"<td>{re.sub('"', '', re.sub(',', '<br>', value)) if idx == 4 else value}</td>"
                    for idx, value in enumerate(one_file_records[i])
                )
                #logger.info(row_data)
                rows.append(f"<tr>{row_data}</tr>")
                
                if i == len(one_file_records) - 1:
                    rows.append(f"<tr class='divider-row'><td colspan='100%'>&nbsp;</td></tr>")

        table_body = "\n".join(rows)
        full_html = html_content % (header_row, table_body)

        with open(self.name, "w", encoding="utf-8") as report_file:
            report_file.write(full_html)

# python3 src/CBlockCrawler/main.py -p ~/nginx/ -s "#if \(.*NGX_HTTP_SSL.*\)\s*" -e "#endif\s*" -i "^#if(?:def|ndef)?"   -f html -n report.html