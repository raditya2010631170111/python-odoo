from odoo import models, fields, _


class ReportWorkOrderXLSX(models.AbstractModel):
    _name = 'report.fik_equipment_maintenance.report_work_order_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, objects):
        for obj in objects:

            sheet = workbook.add_worksheet('MWO')
            sheet.set_margins(0.5, 0.5, 0.5, 0.5)
            currency_header_format = workbook.add_format({'bold': True, 'num_format': '[$Rp-421]#,##0.00', 'font_size': 10})
            currency_header_format.set_bottom(1)
            currency_header_format.set_top(1)
            table_header = workbook.add_format ({'border' :1, 'align': 'center', 'valign': 'vcenter', 'text_wrap': True, 'font_size': 11})
            table_body = workbook.add_format({'border': 1, 'text_wrap': True, 'font_size': 10})
            table_body_center = workbook.add_format({'border': 1, 'align': 'center', 'valign': 'vcenter', 'text_wrap': True, 'font_size': 10})
            header_title_center = workbook.add_format({'bold': True, 'font_size': 28, 'align': 'center', 'valign': 'vcenter'})
            header_title_left = workbook.add_format({'bold': True, 'font_size': 24})
            title_style = workbook.add_format({'font_name': 'Times', 'font_size': 11})
            header_style = workbook.add_format({'font_name': 'Times', 'font_size': 11, 'border': 1, 'align': 'center', 'valign': 'vcenter'})
            header_ttd = workbook.add_format({'font_name': 'Times', 'font_size': 11, 'border': 1, 'align': 'center', 'valign': 'vcenter'})
            year_format = workbook.add_format({'num_format': 'yyyy', 'font_size': 11, 'align': 'left' ,})
            
            sheet.set_column('A:A', 5)
            sheet.set_column('B:B', 15)
            sheet.set_column('C:C', 15)
            sheet.set_column('D:D', 15)
            sheet.set_column('E:E', 15)
            sheet.set_column('F:F', 20)
            sheet.set_column('G:G', 20)
            sheet.set_column('H:H', 20)
            sheet.set_column('I:I', 10)
            sheet.set_column('J:J', 10)
            sheet.set_column('K:K', 10)
            sheet.set_column('L:L', 10)
            sheet.set_column('M:M', 10)
            sheet.set_column('N:N', 10)
            sheet.set_column('O:O', 10)
            sheet.set_column('P:P', 10)
            sheet.set_column('Q:Q', 10)
            sheet.set_column('R:R', 10)
            sheet.set_column('S:S', 10)
            sheet.set_column('T:T', 10)
            sheet.set_column('U:U', 10)
            sheet.set_column('V:W', 15)
            sheet.set_row(0, 10)
            
            sheet.merge_range('A1:B2', 'CKWI', header_title_left)
            sheet.merge_range('F1:H2', 'LAPORAN MASALAH MESIN', header_title_center)
            sheet.write('A3', obj.company_id.name, title_style)
            sheet.merge_range('A5:B5', 'BAGIAN', title_style)
            sheet.merge_range('A6:B6', 'TAHUN', title_style)
            sheet.merge_range('AO1:AR1', 'DISETUJUI', header_style)
            sheet.merge_range('AO2:AR5', '', header_style)
            sheet.merge_range('AS1:AV1', 'DIPERIKSA', header_style)
            sheet.merge_range('AS2:AV5', '', header_style)
            sheet.merge_range('AW1:AZ1', 'DIPERIKSA', header_style)
            sheet.merge_range('AW2:AZ5', '', header_style)
            
            sheet.merge_range('A8:A9', 'NO', table_header)
            sheet.merge_range('B8:B9', 'TANGGAL', table_header)
            sheet.merge_range('C8:C9', 'NAMA MESIN', table_header)
            sheet.merge_range('D8:D9', 'NO MESIN', table_header)
            sheet.merge_range('E8:E9', 'BAGIAN', table_header)
            sheet.merge_range('F8:F9', 'MASALAH', table_header)
            sheet.merge_range('G8:G9', 'ANALISA', table_header)
            sheet.merge_range('H8:H9', 'PENYELESAIAN', table_header)
            sheet.merge_range('I8:K8', 'WAKTU', table_header)
            sheet.merge_range('L8:O8', 'MAN POWER', table_header)
            sheet.merge_range('P8:U8', 'SPARE PART', table_header)
            sheet.merge_range('V8:W9', 'KETERANGAN', table_header)
            sheet.write('I9', 'MULAI', table_header)
            sheet.write('J9', 'SELESAI', table_header)
            sheet.write('K9', 'TOTAL', table_header)
            sheet.write('L9', 'WHO', table_header)
            sheet.write('M9', 'TOTAL', table_header)
            sheet.write('N9', 'PRICE', table_header)
            sheet.write('O9', 'IDR', table_header)
            sheet.write('P9', 'KODE BARANG', table_header)
            sheet.write('Q9', 'NAMA BARANG', table_header)
            sheet.write('R9', 'PRICE', table_header)
            sheet.write('S9', 'QTY', table_header)
            sheet.write('T9', 'SATUAN', table_header)
            sheet.write('U9', 'IDR', table_header)

            

           