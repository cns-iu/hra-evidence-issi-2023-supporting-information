INSERT into cite_title_keyword_organ_author
    (ref_id,ct,title,keyword,organ,wos_standard) 
    select ref_id,ct,title,keyword,organ,wos_standard 
        from cite_title_keyword_organ left join wos_summary_names 
        on cite_title_keyword_organ.ref_id=wos_summary_names.uid

insert into cite_5_organ_author(organ,wos_standard,ct)
    select organ,wos_standard,count(*)as ct 
    from cite_title_keyword_organ_author GROUP BY organ,wos_standard 

insert into cite_5_organ_author_desc(organ,wos_standard,ct)
    select organ,wos_standard,ct from cite_5_organ_author order by ct desc