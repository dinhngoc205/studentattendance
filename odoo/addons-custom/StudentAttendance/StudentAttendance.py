# -*- coding: utf-8 -*-
from odoo import models, fields, api, _, tools, SUPERUSER_ID

class sinh_vien(models.Model):
    _name = "sinh_vien"
    
    ten_sv = fields.Char('Tên sinh viên',require=True)
    ma_sv=fields.Char('Mã SV',require=True)
    
class nam_hoc(models.Model):
    _name = "nam.hoc"
    
    nam_hoc = fields.Char('Năm học')
       
class nien_khoa(models.Model):
    _name = "nien.khoa"
    
    nien_khoa = fields.Char('Niên Khóa')  

class nganh_hoc(models.Model):
    _name = "nganh.hoc"
    
    ten_nganh = fields.Char('Ngành học',require=True)

class hoc_ky(models.Model):
    _name = "hoc.ky"
    
    hoc_ky = fields.Char('Học kỳ',require=True)
    
class mon_hoc(models.Model):
    _name = "nam.hoc"
    
    mon_hoc = fields.Char('Môn học',require=True)
    ma_mon_hoc=fields.Char('Mã môn học',require=True)  

class giang_vien(models.Model):
    _name = "giang.vien"
    
    ten_giaovien = fields.Char('Tên giáo viên',require=True)
    ma_gv = fields.Char('Mã GV',require=True)
       
class tai_lieu(models.Model):
    _name = "tai.lieu"
    ten_tai_lieu = fields.Char('Tên Tài liệu',require=True)
    ma_tai_lieu=fields.Char('Mã TL',require=True)
class danh_sach_giang_vien(models.Model):
    _name = "danh.sach.giang.vien"
    
    vai_tro = fields.Selection([
        ('giang_vien', "Giảng viên chính"),
        ('tro_giang', "Trợ giảng")], 
        string='Vai trò',require=True)
    lop_hoc_id=fields.Many2one('lop_hoc',ondelete='set null')
    giang_vien_id=fields.Many2one('giang_vien', ondelete='set null')
class danh_sach_sinh_vien(models.Model):
    _name = "danh.sach.sinh.vien"
    
    trang_thai = fields.Selection([
        ('hieu_luc', "Hiệu lực"),
        ('huy_mon', "Hủy môn")], 
        string='Trạng thái',require=True)
    lop_hoc_id=fields.Many2one('lop_hoc',ondelete='set null')
    sinh_vien_id=fields.Many2one('sinh_vien', ondelete='set null')
class danh_sach_tai_lieu(models.Model):
    _name = "danh.sach.tai.lieu" 
    lich_hoc_id=fields.Many2one('lich_hoc',ondelete='set null')
    tai_lieu_id=fields.Many2one('tai_lieu', ondelete='set null')
    
class lich_hoc(models.Model):
    _name = "lich.hoc"
    
    buoi_hoc=fields.Char('Buổi học',require=True)
    gio_bat_dau=fields.Datetime('Ngày giờ bắt đầu')
    gio_ket_thuc=fields.Datetime('Ngày giờ kết thúc')
    lop_hoc_id=fields.Many2one('lop_hoc',ondelete='set null')
    tai_lieu_id=fields.One2many('danh_sach_tai_lieu', ondelete='set null')

class lop_hoc(models.Model):
    _name = "lop.hoc"
    
    ten_lop = fields.Char('Tên lớp',require=True)
    ma_lop=fields.Char('Mã lớp',require=True)
    nam_id=fields.Many2one('nam_hoc', ondelete='set null',require=True)
    nganh_id=fields.Many2one('nganh_hoc',ondelete='set null',require=True)
    hoc_ky_id=fields.Many2one('hoc_ky',ondelete='set null',require=True)
    mon_hoc_id=fields.Many2one('mon_hoc',ondelete='set null',require=True)
    danhsach_gv=fields.One2many('danh_sach_giang_vien','lop_hoc_id',string='Danh sách giảng viên')
    danhsach_sv=fields.One2many('danh_sach_sinh_vien','lop_hoc_id',string='Danh sách sinh viên')
    danhsach_lichhoc=fields.One2many('lich_hoc','lop_hoc_id',string="Lịch học")

class diem_danh(models.Model):
    _name = "diem.danh"
    sinh_vien_id=fields.Many2one('sinh_vien',require=True)
    lich_hoc_id=fields.Many2one('lich_hoc',require=True)
    gio_den=fields.Datetime('Ngày giờ đến')
    gio_ve=fields.Datetime('Ngày giờ kết thúc')
    danh_gia=fields.Char('Đánh giá',require=True)

class ket_qua_hoc_tap(models.Model):
    _name = "ket.qua.hoc.tap"
    sinh_vien_id=fields.Many2one('sinh_vien',require=True)
    lop_hoc_id=fields.Many2one('lop_hoc',require=True)
    diem_tong_ket=fields.Float('Điểm tổng kết',require=True)
    xep_loai = fields.Selection([
        ('gioi', "Giỏi"),
        ('khá', "Khá"),
        ('trung_binh', "Trung Bình"),
        ('rot', "Rớt")], 
        string='Xếp loại',require=True)
class cau_truc_diem(models.Model):
    _name = "cau_truc_diem"
    lop_hoc_id=fields.Many2one('lop_hoc',ondelete="set null",require=True)
    cau_truc=fields.Char('Cấu trúc điểm',require=True)
    ty_le=fields.Float('Tỷ lệ')
class ket_qua_hoc_tap_chi_tiet(models.Model):
    _name = "ket.qua.hoc.tap.chi.tiet"
    ket_qua_hoc_tap_id=fields.Many2one('ket_qua_hoc_tap',ondelete='set null')
    cau_truc_diem_id=fields.Many2one('cau_truc_diem',sondelete='set null')
    so_diem=fields.Float("Điểm")
    