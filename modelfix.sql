/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     18/01/2017 18:01:03                          */
/*==============================================================*/


drop table if exists BARANG;

drop table if exists BARANG_PESANAN;

drop table if exists CUSTOMER;

drop table if exists DAFTAR_ALAMAT;

drop table if exists DETAIL_BARANG;

drop table if exists KOTA;

drop table if exists PROVINSI;

drop table if exists SIMPANWISHLIST;

drop table if exists TIPE_BARANG;

drop table if exists TRANSAKSI;

/*==============================================================*/
/* Table: BARANG                                                */
/*==============================================================*/
create table BARANG
(
   BAHAN                varchar(20) not null,
   KODE_BARANG          varchar(5) not null,
   KODE_TIPE            varchar(5) not null,
   NAMA_BARANG          varchar(15) not null,
   DESKRIPSI_BARANG_    varchar(1024) not null,
   HARGA_BARANG         numeric(8,0) not null,
   WAKTU_DATANG_KATALOG datetime not null,
   primary key (KODE_BARANG)
);

/*==============================================================*/
/* Table: BARANG_PESANAN                                        */
/*==============================================================*/
create table BARANG_PESANAN
(
   KODE_BARANG          varchar(5) not null,
   ID_DETAIL            char(3) not null,
   KODE_TRANSAKSI       char(10) not null,
   ID_BARANG_PESANAN    char(2) not null,
   primary key (KODE_BARANG, ID_DETAIL, KODE_TRANSAKSI, ID_BARANG_PESANAN)
);

/*==============================================================*/
/* Table: CUSTOMER                                              */
/*==============================================================*/
create table CUSTOMER
(
   EMAIL                varchar(20) not null,
   NAMA_CUSTOMER        varchar(30) not null,
   TELP_CUSTOMER        varchar(12) not null,
   PASSWORD             varchar(15) not null,
   primary key (EMAIL)
);

/*==============================================================*/
/* Table: DAFTAR_ALAMAT                                         */
/*==============================================================*/
create table DAFTAR_ALAMAT
(
   ID_ALAMAT            varchar(6) not null,
   EMAIL                varchar(20) not null,
   ID_KOTA              char(5) not null,
   ALAMAT               varchar(25) not null,
   KODE_POS             char(5) not null,
   primary key (ID_ALAMAT)
);

/*==============================================================*/
/* Table: DETAIL_BARANG                                         */
/*==============================================================*/
create table DETAIL_BARANG
(
   KODE_BARANG          varchar(5) not null,
   ID_DETAIL            char(3) not null,
   WARNA                varchar(50) not null,
   FOTO_BARANG          varchar(1024) not null,
   STOCK                smallint,
   UKURAN               varchar(8) not null,
   primary key (KODE_BARANG, ID_DETAIL)
);

/*==============================================================*/
/* Table: KOTA                                                  */
/*==============================================================*/
create table KOTA
(
   ID_KOTA              char(5) not null,
   ID_PROVINSI          char(2) not null,
   NAMA_KOTA            varchar(30) not null,
   primary key (ID_KOTA)
);

/*==============================================================*/
/* Table: PROVINSI                                              */
/*==============================================================*/
create table PROVINSI
(
   ID_PROVINSI          char(2) not null,
   NAMA_PROVINSI        varchar(25) not null,
   primary key (ID_PROVINSI)
);

/*==============================================================*/
/* Table: SIMPANWISHLIST                                        */
/*==============================================================*/
create table SIMPANWISHLIST
(
   EMAIL                varchar(20) not null,
   KODE_BARANG          varchar(5) not null,
   ID_WISHLIST          char(2) not null,
   primary key (EMAIL, KODE_BARANG, ID_WISHLIST)
);

/*==============================================================*/
/* Table: TIPE_BARANG                                           */
/*==============================================================*/
create table TIPE_BARANG
(
   KODE_TIPE            varchar(5) not null,
   TIPE_BARANG          varchar(6) not null,
   primary key (KODE_TIPE)
);

/*==============================================================*/
/* Table: TRANSAKSI                                             */
/*==============================================================*/
create table TRANSAKSI
(
   KODE_TRANSAKSI       char(10) not null,
   ID_ALAMAT            varchar(6) not null,
   EMAIL                varchar(20) not null,
   WAKTU_PEMESANAN      datetime not null,
   KUANTITAS_BARANG     smallint,
   WAKTU_DIBAYAR        datetime,
   BANK_TUJUAN_BAYAR    varchar(10),
   REK_PENGIRIM         char(12),
   STATUS_KONFIRMASI    bool not null,
   TOTAL_PEMBELIAN      numeric(8,0),
   STATUS_KADALUWARSA   bool not null,
   primary key (KODE_TRANSAKSI)
);

alter table BARANG add constraint FK_BERTIPE foreign key (KODE_TIPE)
      references TIPE_BARANG (KODE_TIPE) on delete restrict on update restrict;

alter table BARANG_PESANAN add constraint FK_BARANGDIPESAN foreign key (KODE_BARANG, ID_DETAIL)
      references DETAIL_BARANG (KODE_BARANG, ID_DETAIL) on delete restrict on update restrict;

alter table BARANG_PESANAN add constraint FK_PESANANTRANSAKSI foreign key (KODE_TRANSAKSI)
      references TRANSAKSI (KODE_TRANSAKSI) on delete restrict on update restrict;

alter table DAFTAR_ALAMAT add constraint FK_BERKOTA foreign key (ID_KOTA)
      references KOTA (ID_KOTA) on delete restrict on update restrict;

alter table DAFTAR_ALAMAT add constraint FK_MEMILIKI foreign key (EMAIL)
      references CUSTOMER (EMAIL) on delete restrict on update restrict;

alter table DETAIL_BARANG add constraint FK_MEMPUNYAI foreign key (KODE_BARANG)
      references BARANG (KODE_BARANG) on delete restrict on update restrict;

alter table KOTA add constraint FK_BERPROVINSI foreign key (ID_PROVINSI)
      references PROVINSI (ID_PROVINSI) on delete restrict on update restrict;

alter table SIMPANWISHLIST add constraint FK_BARANGWISHLIST foreign key (KODE_BARANG)
      references BARANG (KODE_BARANG) on delete restrict on update restrict;

alter table SIMPANWISHLIST add constraint FK_CUSTWISHLIST foreign key (EMAIL)
      references CUSTOMER (EMAIL) on delete restrict on update restrict;

alter table TRANSAKSI add constraint FK_BERTRANSAKSI foreign key (EMAIL)
      references CUSTOMER (EMAIL) on delete restrict on update restrict;

alter table TRANSAKSI add constraint FK_DIKIRIMKANKE foreign key (ID_ALAMAT)
      references DAFTAR_ALAMAT (ID_ALAMAT) on delete restrict on update restrict;

