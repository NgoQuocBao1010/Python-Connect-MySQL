use project;

DELETE FROM cgtrinh WHERE stt_ctr=9;
DELETE FROM chuthau WHERE tel='123';

select * from cgtrinh
order by kinh_phi;

select * from cgtrinh 
where tinh_thanh like '%can tho%' 
order by ten_ctr desc;

select * from ktrucsu k join thietke t 
on k.hoten_kts=t.hoten_kts 
where stt_ctr = 1;

select c.* from congnhan c join thamgia t 
on c.hoten_cn=t.hoten_cn 
where stt_ctr=1;