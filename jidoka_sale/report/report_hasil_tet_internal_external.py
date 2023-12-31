from odoo import models, fields, _


class ReportHasilTesInternalExternalXLSX(models.AbstractModel):
    _name = 'report.jidoka_sale.report_hasil_tes_internal_external_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, objects):
        for obj in objects:
            report_name = obj.name
            # One sheet by partner
            sheet = workbook.add_worksheet('INTERNAL & EXTERNAL TEST')
            sheet.set_row(0, 30)
            sheet.set_row(2, 25)
            sheet.set_row(3, 25)
            sheet.set_row(4, 25)
            sheet.set_column(7, 14, 5)
            sheet.set_column(0, 0, 1)
            sheet.set_column(1, 1, 4)
            sheet.set_column(2, 2, 15)
            sheet.set_column(3, 3, 10)
            sheet.set_column(4, 5, 4)
            sheet.set_column(6, 6, 20)
            sheet.set_column(7, 14, 5)
            sheet.set_column(17, 21, 4)
            sheet.set_column(22, 22, 15)
            bold_header = workbook.add_format({'bold':True,'align':'center','valign':'vcenter','font_size':20})
            table_header = workbook.add_format({'bold':True,'border':1,'align':'center','valign':'vcenter','text_wrap':True,'font_size':10})
            body = workbook.add_format({'border':1,'align':'center','valign':'vcenter'})
            sheet.merge_range('B1:W1','INTERNAL & EXTERNAL TEST',bold_header)
            sheet.merge_range('B3:B5','NO',table_header)
            sheet.merge_range('C3:C5','ITEM',table_header)
            sheet.merge_range('D3:D5','NO SR',table_header)
            sheet.merge_range('E3:F3','QTY',table_header)
            sheet.merge_range('E4:E5','PCS',table_header)
            sheet.merge_range('F4:F5','CTN',table_header)
            sheet.merge_range('G3:G5','BUYER',table_header)
            sheet.merge_range('H3:O3','JENIS TEST',table_header)
            sheet.merge_range('H4:H5','KONS',table_header)
            sheet.merge_range('I4:I5','PACK',table_header)
            sheet.merge_range('J4:J5','DROP',table_header)
            sheet.merge_range('K4:L4','PRE PROD',table_header)
            sheet.write('K5','KONS',table_header)
            sheet.write('L5','PACK',table_header)  
            sheet.merge_range('M4:M5','PROD TEST',table_header)
            sheet.merge_range('N4:N5','TEST ISTA 6A',table_header)
            sheet.merge_range('O4:O5','PROD TEST MOCK-UP',table_header)
            sheet.merge_range('P3:Q3','TANGGAL',table_header)
            sheet.merge_range('P4:P5','KIRIM',table_header)
            sheet.merge_range('Q4:Q5','SELESAI',table_header)
            sheet.merge_range('R3:S3','TUJUAN',table_header)
            sheet.merge_range('R4:R5','IN',table_header)
            sheet.merge_range('S4:S5','EX',table_header)
            sheet.merge_range('T3:U3','HASIL',table_header)
            sheet.merge_range('T4:T5','FAIL',table_header)
            sheet.merge_range('U4:U5','OKE',table_header)
            sheet.merge_range('V3:W4','KETERANGAN',table_header)
            sheet.write('V5','PE',table_header)
            sheet.write('W5','KETERANGAN',table_header)
            idx = 5
            for line in range(1,196):
                sheet.write(idx,1,'',body)
                sheet.write(idx,2,'',body)
                sheet.write(idx,3,'',body)
                sheet.write(idx,4,'',body)
                sheet.write(idx,5,'',body)
                sheet.write(idx,6,'',body)
                sheet.write(idx,7,'',body)
                sheet.write(idx,8,'',body)
                sheet.write(idx,9,'',body)
                sheet.write(idx,10,'',body)
                sheet.write(idx,11,'',body)
                sheet.write(idx,12,'',body)
                sheet.write(idx,13,'',body)
                sheet.write(idx,14,'',body)
                sheet.write(idx,15,'',body)
                sheet.write(idx,16,'',body)
                sheet.write(idx,17,'',body)
                sheet.write(idx,18,'',body)
                sheet.write(idx,19,'',body)
                sheet.write(idx,20,'',body)
                sheet.write(idx,21,'',body)
                sheet.write(idx,22,'',body)
                idx = idx + 1