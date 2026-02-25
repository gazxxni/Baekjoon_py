select t.ITEM_ID, i.ITEM_NAME, i.RARITY 
from ITEM_INFO as i join ITEM_TREE as t on t.ITEM_ID = i.ITEM_ID 
where t.PARENT_ITEM_ID in (
    select ITEM_ID from ITEM_INFO
    where RARITY = 'RARE')
order by ITEM_ID desc