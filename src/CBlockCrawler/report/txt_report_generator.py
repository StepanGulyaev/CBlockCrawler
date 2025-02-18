from prettytable import PrettyTable
from prettytable import MARKDOWN
from CBlockCrawler.report.report_generator import ReportGenerator

class TXTReportGenerator(ReportGenerator):
    def generate_report(self):
        report_table = PrettyTable(align='l')
        report_table.set_style(MARKDOWN)
        report_table.max_width = 5
        report_table.field_names = self.fields
        
        for one_file_records in self.all_records:
            for i in range(len(one_file_records)):
                if i != len(one_file_records) - 1:
                    report_table.add_row(one_file_records[i])
                else:
                    report_table.add_row(one_file_records[i],divider=True)
        with open(self.name, "w") as report_file:
            report_file.write(report_table.get_string())



        


