from prettytable import PrettyTable
from prettytable import MARKDOWN
from CBlockCrawler.report.report_generator import ReportGenerator

class TXTReportGenerator(ReportGenerator):
    def generate_report(self):
        report_table = PrettyTable(align='l')
        report_table.set_style(MARKDOWN)
        report_table.max_width = 5
        report_table.field_names = self.fields
        for handler in self.cblock_handlers:
            for i in range(len(handler.blocks)):
                if i != len(handler.blocks) - 1:
                    report_table.add_row(handler.blocks[i].get_record())
                else:
                    report_table.add_row(handler.blocks[i].get_record(),divider=True)
        with open(self.name, "w") as report_file:
            report_file.write(report_table.get_string())



        


