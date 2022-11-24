INSERT into cite_title_keyword_organ_country_city
    (ref_id,ct,title,keyword,organ,country,city) 
    select ref_id,ct,title,keyword,organ,country,city 
        from cite_title_keyword_organ 
        left join id_country_city 
        on cite_title_keyword_organ.ref_id=id_country_city.uid


INSERT into cite_title_keyword_organ_country_city_abbr
    (ref_id,ct,title,keyword,organ,country,city,abbr) 
    select ref_id,ct,title,keyword,organ,
        cite_title_keyword_organ_country_city.country,city,abbr 
        from cite_title_keyword_organ_country_city left join abbr_country 
        on cite_title_keyword_organ_country_city.country=abbr_country.country
        
INSERT into cite_ct_countryabbr(ref_id,ct,abbr) 
    select ref_id,ct,abbr 
    from cite_title_keyword_organ_author_country_city_abbr GROUP BY ref_id,ct,abbr

INSERT into cite_10_countryabbr(ref_id,abbr) 
    select ref_id,abbr from cite_ct_countryabbr where ct>=10