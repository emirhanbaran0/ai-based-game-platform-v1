select * from partner_config  ---nS8LT5PZtU, S3Z7VsT8UM


select offer_key_id, count(*) from offer_subscribers group by offer_key_id  order by count(*) desc

select * from offers where offer_key_id='XYECvYWpZB'

select * from checkpoints where offer_key_id='XYECvYWpZB' and is_active=true

select * from checkpoints where offer_key_id in (select offer_key_id from  offers where bundleid='com.zombie.idleminertycoon' and offer_type!='quest') and is_active=true and is_iap=true

select * from playtime_events where  app_id='com.funtomic.matchmasters'

select event_type from events where offer_key_id= 'XYECvYWpZB' group by event_type

select * from events where event_type='ad' or event_type='ad_app'  and events.offer_key_id!='mf5hKab46M' order by ts_created desc limit 10

select * from events  where events.event_source='trackier' order by ts_created --singular

select partner_key_id from  offers where offer_key_id='dPlxHKeaI6'

select * from offers where partner_key_id='S3Z7VsT8UM'

select offer_key_id, count(*) from offer_subscribers where offer_key_id in (select offers.offer_key_id from offers where partner_key_id='S3Z7VsT8UM') group by offer_key_id order by count(*)

select * from offers where offer_key_id='8vtSTFVko0'




select id,event_type,is_iap,is_playtime,usd_reward_amount,checkpoint_type from checkpoints  where offer_key_id='8vtSTFVko0' and is_active=true

select user_key_id,country_code,age,sex from users where user_key_id in (select users.user_key_id from offer_subscribers where offer_key_id='0UpQ7jyZt2') and sex is not null  and age is not null ;
select count(*) from users where user_key_id in (select users.user_key_id from offer_subscribers where offer_key_id='0UpQ7jyZt2') and sex is not null  and age is not null ;
select event_type , count(*) from events where offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h' ) group by event_type
select count(*) from events where offer_key_id='0UpQ7jyZt2'
select * from offers where offer_key_id='0UpQ7jyZt2'
select id,event_type,usd_reward_amount,checkpoint_type from checkpoints  where offer_key_id='8vtSTFVko0' and is_active=true and checkpoint_type='level'
select * from playtime_events where app_id='com.zombie.idleminertycoon'

select * from offers where name like '%Idle Zombie%' and offer_type!='quest'

select user_key_id from users where user_key_id in ( select user_key_id from offer_subscribers where offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h'

    ));


--- Potansiyel oyunu bırakma noktalarının tespit edilmesi

--- User Country, Age, Sex

select user_key_id,country_code AS country ,age,sex from users where user_key_id in ( select user_key_id from offer_subscribers where offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h'

    ));

-- Offer First Install Date

Select user_key_id,ts_created AS first_time_login from offer_subscribers where user_key_id in (
    select user_key_id from users where user_key_id in ( select user_key_id from offer_subscribers where offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h'

    ))
    ) and package_name='com.zombie.idleminertycoon'

--- Session Count and Total Session Time


SELECT
  pe.user_key_id,
  COUNT(*) AS session_count,
  SUM(pe.play_time) AS total_session_time
FROM playtime_events pe
JOIN users u ON pe.user_key_id = u.user_key_id
JOIN offer_subscribers os ON u.user_key_id = os.user_key_id
WHERE pe.app_id = 'com.zombie.idleminertycoon'
  AND os.offer_key_id IN (
    '0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h'
  )
GROUP BY pe.user_key_id;

--- Gordugu reklam sayisi

Select user_key_id,count(*) as total_ad_viewed from events where user_key_id in (
    ( select user_key_id from offer_subscribers where offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h'

    ))
    ) and offer_key_id in ('0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h') and event_type in ('Ad_View') group by user_key_id , event_type


---- Uygulama Ici Satin Alim Sayisi Ve Toplam Harcadigi Para

select user_key_id,sum(usd_reward_amount) as total_spent_in_usd ,count(*) AS total_spent_time from claims_processed where checkpoint_id in (
select id from checkpoints where offer_key_id in (select offer_key_id from  offers where bundleid='com.zombie.idleminertycoon' and offer_type!='quest') and is_active=true and is_iap=true
) group by user_key_id


--- Bir leveli gecme ortalama suresi

select user_key_id, count(*) as level_completation_count  from claims_processed where checkpoint_id in (select id from checkpoints  where checkpoints.offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h'
    ) and is_active=true and checkpoint_type='level') and  user_key_id in (
    select user_key_id from users where user_key_id in ( select user_key_id from offer_subscribers where offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h'

    ))
    ) group by user_key_id order by  count(*) desc


SELECT
  pe.user_key_id,
  SUM(pe.play_time) AS total_session_time
FROM playtime_events pe
JOIN users u ON pe.user_key_id = u.user_key_id
JOIN offer_subscribers os ON u.user_key_id = os.user_key_id
WHERE pe.app_id = 'com.zombie.idleminertycoon'
  AND os.offer_key_id IN (
    '0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h'
  )
GROUP BY pe.user_key_id;


WITH level_completions AS (
  SELECT
    cp.user_key_id,
    COUNT(*) AS level_completion_count
  FROM claims_processed cp
  WHERE cp.checkpoint_id IN (
    SELECT c.id
    FROM checkpoints c
    WHERE c.offer_key_id IN (
      '0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h'
    )
    AND c.is_active = true
    AND c.checkpoint_type = 'level'
  )
  AND cp.user_key_id IN (
    SELECT os.user_key_id
    FROM offer_subscribers os
    WHERE os.offer_key_id IN (
      '0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h'
    )
  )
  GROUP BY cp.user_key_id
),

playtime AS (
  SELECT
    pe.user_key_id,
    SUM(pe.play_time) AS total_session_time
  FROM playtime_events pe
  JOIN users u ON pe.user_key_id = u.user_key_id
  JOIN offer_subscribers os ON u.user_key_id = os.user_key_id
  WHERE pe.app_id = 'com.zombie.idleminertycoon'
    AND os.offer_key_id IN (
      '0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h'
    )
  GROUP BY pe.user_key_id
)

SELECT
  pt.user_key_id,
  pt.total_session_time,
  lc.level_completion_count,
  CASE
    WHEN lc.level_completion_count > 0 THEN pt.total_session_time::FLOAT / lc.level_completion_count
    ELSE NULL
  END AS avg_level_completion_time
FROM playtime pt
JOIN level_completions lc ON pt.user_key_id = lc.user_key_id
ORDER BY avg_level_completion_time;

--- level zorluklarina gore tamamlama oranlari

select user_key_id,count(*)  from claims_processed where offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h') and checkpoint_id in (
        select id from checkpoints where offer_key_id in (select offer_key_id from  offers where bundleid='com.zombie.idleminertycoon' and offer_type!='quest') and is_active=true and checkpoint_type='level' and checkpoints.event_type!='Ad_View_30'
    ) group by user_key_id order by count(*) desc


SELECT
    user_key_id,

    -- Easy completion
    ROUND(LEAST(total_completed_level, 5) * 100.0 / 5, 2) AS easy_completion_rate,

    -- Medium completion
    ROUND(GREATEST(LEAST(total_completed_level - 5, 6), 0) * 100.0 / 6, 2) AS medium_completion_rate,

    -- Hard completion
    ROUND(GREATEST(total_completed_level - 11, 0) * 100.0 / 3, 2) AS hard_completion_rate

FROM (
    SELECT
        user_key_id,
        COUNT(*) AS total_completed_level
    FROM
        claims_processed
    WHERE
        offer_key_id IN ('0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h')
        AND checkpoint_id IN (
            SELECT id
            FROM checkpoints
            WHERE
                offer_key_id IN (
                    SELECT offer_key_id
                    FROM offers
                    WHERE
                        bundleid = 'com.zombie.idleminertycoon'
                        AND offer_type != 'quest'
                )
                AND is_active = true
                AND checkpoint_type = 'level'
                AND event_type != 'Ad_View_30'
        )
    GROUP BY user_key_id
) AS completed_data
ORDER BY total_completed_level DESC;

---- quit label

SELECT
  user_key_id,
  CASE
    WHEN MAX(ts_created) < CURRENT_DATE - INTERVAL '4 days' THEN 1
    ELSE 0
  END AS is_quit
FROM playtime_events
WHERE app_id = 'com.zombie.idleminertycoon'
AND user_key_id in (
    SELECT os.user_key_id
    FROM offer_subscribers os
    WHERE os.offer_key_id IN (
      '0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h'
    )
    )
GROUP BY user_key_id order by  is_quit;



----- Kişiselleştirilmiş Zorluk Seviyesi

--- User Country, Age, Sex

select user_key_id,country_code as country ,age,sex from users where user_key_id in ( select user_key_id from offer_subscribers where offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h'

    ));


---- Uygulama Ici Satin Alim Sayisi Ve Toplam Harcadigi Para

select user_key_id,sum(usd_reward_amount) as total_spent_in_usd ,count(*) AS iap_count from claims_processed where checkpoint_id in (
select id from checkpoints where offer_key_id in (select offer_key_id from  offers where bundleid='com.zombie.idleminertycoon' and offer_type!='quest') and is_active=true and is_iap=true
) group by user_key_id

----Oynama sıklığı (günlük/haftalık oturum sayısı)

SELECT
    user_key_id,
    DATE(ts_created AT TIME ZONE 'UTC') AS play_date,
    COUNT(*) AS session_count_in_a_day
FROM playtime_events
WHERE app_id = 'com.zombie.idleminertycoon'
GROUP BY app_id, user_key_id, DATE(ts_created AT TIME ZONE 'UTC')
ORDER BY user_key_id, play_date;


SELECT
    user_key_id,
    DATE_TRUNC('week', ts_created AT TIME ZONE 'UTC') AS week_start_date,
    COUNT(*) AS session_count_in_a_week
FROM playtime_events
WHERE app_id = 'com.zombie.idleminertycoon'
GROUP BY app_id, user_key_id, DATE_TRUNC('week', ts_created AT TIME ZONE 'UTC')
ORDER BY user_key_id, week_start_date;

---- Seviye zorluklari ve Gecme oranlari

select user_key_id,count(*)  from claims_processed where offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h') and checkpoint_id in (
        select id from checkpoints where offer_key_id in (select offer_key_id from  offers where bundleid='com.zombie.idleminertycoon' and offer_type!='quest') and is_active=true and checkpoint_type='level' and checkpoints.event_type!='Ad_View_30'
    ) group by user_key_id order by count(*) desc


SELECT
    user_key_id,

    -- Easy completion
    ROUND(LEAST(total_completed_level, 5) * 100.0 / 5, 2) AS easy_completion_rate,

    -- Medium completion
    ROUND(GREATEST(LEAST(total_completed_level - 5, 6), 0) * 100.0 / 6, 2) AS medium_completion_rate,

    -- Hard completion
    ROUND(GREATEST(total_completed_level - 11, 0) * 100.0 / 3, 2) AS hard_completion_rate

FROM (
    SELECT
        user_key_id,
        COUNT(*) AS total_completed_level
    FROM
        claims_processed
    WHERE
        offer_key_id IN ('0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h')
        AND checkpoint_id IN (
            SELECT id
            FROM checkpoints
            WHERE
                offer_key_id IN (
                    SELECT offer_key_id
                    FROM offers
                    WHERE
                        bundleid = 'com.zombie.idleminertycoon'
                        AND offer_type != 'quest'
                )
                AND is_active = true
                AND checkpoint_type = 'level'
                AND event_type != 'Ad_View_30'
        )
    GROUP BY user_key_id
) AS completed_data
ORDER BY total_completed_level DESC;



-----  Fiyatlandırma Stratejileri


--- User Country, Age, Sex

select user_key_id,country_code as country ,age,sex from users where user_key_id in ( select user_key_id from offer_subscribers where offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h'

    ));


---- Uygulama Ici Satin Alim Sayisi Ve Toplam Harcadigi Para

select user_key_id,sum(usd_reward_amount) as total_spent_in_usd ,count(*) AS iap_count from claims_processed where checkpoint_id in (
select id from checkpoints where offer_key_id in (select offer_key_id from  offers where bundleid='com.zombie.idleminertycoon' and offer_type!='quest') and is_active=true and is_iap=true
) group by user_key_id


--- Session Count and Total Session Time


SELECT
  pe.user_key_id,
  COUNT(*) AS playtime_event_count,
  SUM(pe.play_time) AS total_playtime_value
FROM playtime_events pe
JOIN users u ON pe.user_key_id = u.user_key_id
JOIN offer_subscribers os ON u.user_key_id = os.user_key_id
WHERE pe.app_id = 'com.zombie.idleminertycoon'
  AND os.offer_key_id IN (
    '0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h'
  )
GROUP BY pe.user_key_id;


---- Seviye zorluklari ve Gecme oranlari

SELECT
    user_key_id,

    -- Easy completion
    ROUND(LEAST(total_completed_level, 5) * 100.0 / 5, 2) AS easy_completion_rate,

    -- Medium completion
    ROUND(GREATEST(LEAST(total_completed_level - 5, 6), 0) * 100.0 / 6, 2) AS medium_completion_rate,

    -- Hard completion
    ROUND(GREATEST(total_completed_level - 11, 0) * 100.0 / 3, 2) AS hard_completion_rate

FROM (
    SELECT
        user_key_id,
        COUNT(*) AS total_completed_level
    FROM
        claims_processed
    WHERE
        offer_key_id IN ('0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h')
        AND checkpoint_id IN (
            SELECT id
            FROM checkpoints
            WHERE
                offer_key_id IN (
                    SELECT offer_key_id
                    FROM offers
                    WHERE
                        bundleid = 'com.zombie.idleminertycoon'
                        AND offer_type != 'quest'
                )
                AND is_active = true
                AND checkpoint_type = 'level'
                AND event_type != 'Ad_View_30'
        )
    GROUP BY user_key_id
) AS completed_data
ORDER BY total_completed_level DESC;




--- Reklam Sıklığı Optimizasyonu


--- User Country, Age, Sex

select user_key_id,country_code as country_code ,age,sex from users where user_key_id in ( select user_key_id from offer_subscribers where offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h'

    ));


--- Gordugu reklam sayisi

Select user_key_id,event_type,count(*) as ad_viev_count from events where user_key_id in (
    ( select user_key_id from offer_subscribers where offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h'

    ))
    ) and offer_key_id in ('0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h') and event_type in ('Ad_View') group by user_key_id , event_type


---- Seviye zorluklari ve Gecme oranlari

SELECT
    user_key_id,

    -- Easy completion
    ROUND(LEAST(total_completed_level, 5) * 100.0 / 5, 2) AS easy_completion_rate,

    -- Medium completion
    ROUND(GREATEST(LEAST(total_completed_level - 5, 6), 0) * 100.0 / 6, 2) AS medium_completion_rate,

    -- Hard completion
    ROUND(GREATEST(total_completed_level - 11, 0) * 100.0 / 3, 2) AS hard_completion_rate

FROM (
    SELECT
        user_key_id,
        COUNT(*) AS total_completed_level
    FROM
        claims_processed
    WHERE
        offer_key_id IN ('0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h')
        AND checkpoint_id IN (
            SELECT id
            FROM checkpoints
            WHERE
                offer_key_id IN (
                    SELECT offer_key_id
                    FROM offers
                    WHERE
                        bundleid = 'com.zombie.idleminertycoon'
                        AND offer_type != 'quest'
                )
                AND is_active = true
                AND checkpoint_type = 'level'
                AND event_type != 'Ad_View_30'
        )
    GROUP BY user_key_id
) AS completed_data
ORDER BY total_completed_level DESC;


--- Kullaninin aldigi toplam odul miktari

SELECT user_key_id,sum(usd_reward_amount) as total_earned_reward_amount_in_usd FROM claims_processed where offer_key_id in ('0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h') and user_key_id in (
     select user_key_id from offer_subscribers where offer_key_id in (
'0UpQ7jyZt2',
'xFkLHnnuqC',
'mxc8UCzRSs',
'UGVjpdWK3h'

    )) group by user_key_id


--- Session Count and Total Session Time - > ort bul


WITH level_completions AS (
  SELECT
    cp.user_key_id,
    COUNT(*) AS level_completion_count
  FROM claims_processed cp
  WHERE cp.checkpoint_id IN (
    SELECT c.id
    FROM checkpoints c
    WHERE c.offer_key_id IN (
      '0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h'
    )
    AND c.is_active = true
    AND c.checkpoint_type = 'level'
  )
  AND cp.user_key_id IN (
    SELECT os.user_key_id
    FROM offer_subscribers os
    WHERE os.offer_key_id IN (
      '0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h'
    )
  )
  GROUP BY cp.user_key_id
),

playtime AS (
  SELECT
    pe.user_key_id,
    SUM(pe.play_time) AS total_session_time
  FROM playtime_events pe
  JOIN users u ON pe.user_key_id = u.user_key_id
  JOIN offer_subscribers os ON u.user_key_id = os.user_key_id
  WHERE pe.app_id = 'com.zombie.idleminertycoon'
    AND os.offer_key_id IN (
      '0UpQ7jyZt2', 'xFkLHnnuqC', 'mxc8UCzRSs', 'UGVjpdWK3h'
    )
  GROUP BY pe.user_key_id
)

SELECT
  pt.user_key_id,
  pt.total_session_time,
  lc.level_completion_count,
  CASE
    WHEN lc.level_completion_count > 0 THEN pt.total_session_time::FLOAT / lc.level_completion_count
    ELSE NULL
  END AS avg_level_completion_time
FROM playtime pt
JOIN level_completions lc ON pt.user_key_id = lc.user_key_id
ORDER BY avg_level_completion_time;
