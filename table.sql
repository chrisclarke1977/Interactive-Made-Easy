--
-- Table structure for table `tz_todo`
--

CREATE TABLE `tz_todo` (
  `id` int(8) unsigned NOT NULL auto_increment,
  `position` int(8) unsigned NOT NULL default '0',
  `text` varchar(255) collate utf8_unicode_ci NOT NULL default '',
  `dt_added` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`id`),
  KEY `position` (`position`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;