# Author: Matthias Maderer
# E-Mail: edvler@edvler-blog.de
# URL: https://github.com/edvler/check_mk_urbackup-check
# License: GPLv2

register_check_parameters(
    RulespecGroupCheckParametersApplications,
    "cobian",
    _("Backup Cobian"),
    Dictionary(
        elements = [
            ("check_backup",
             DropdownChoice(
                 title = _("Enable (default) or disable check of backup"),
                 help=_("If disabled is choosen, the check will always return OK. To enable checks of the backup, select enable. This is usefull if you have Backup-Jobs, for which no regular backups are done and you dont want them to be checked."),
                 choices = [
                     ("ignore", _("disable")),
                     ("check", _("enable")),
                 ]
             )
            ),
            ("ignore_vss",
             DropdownChoice(
                 title = _("Ignore VSS errors."),
                 help=_("If ignore is choosen, the check will return OK instead of change to error if VSS fails. This is usefull if you have Backup-Jobs, which has VSS fails that occur always and you want to ignore them."),
                 choices = [
                     ("ignore", _("ignore")),
                     ("check", _("check vss errors")),
                 ]
             )
            ),
            ("error_count_limits",
             Tuple(
                 title = "Limits of Backup-Job errors before changing to warn or error.",
                     elements = [
                         Integer(
                                 title = _("Change to warn if Backup-Job error count is above than"),
                                 help = _("If Backup-Job error count is above the given number change to warn."),
                                 minvalue = 0,
                                 default_value = 0
                         ),
                         Integer(
                                 title = _("Change to error if Backup-Job error count is above than"),
                                 help = _("If Backup-Job error count is above the given number change to error."),
                                 minvalue = 0,
                                 default_value = 0
                         ),
                     ]
                 )
            ),

            ("processed_files_limits",
             Tuple(
                 title = "Change to warn or error if processed files below given file counts",
                     elements = [
                         Integer(
                                 title = _("Change to warn if Backup-Job processed less or equal files than"),
                                 help = _("If Backup-Job processed less or equal files than the given number change to warn."),
                                 minvalue = 0,
                         ),
                         Integer(
                                 title = _("Change to error if Backup-Job processed less or equal files than"),
                                 help = _("If Backup-Job processed less or equal files than the given number change to error."),
                                 minvalue = 0,
                         ),
                     ]
                 )
            ),

            ("copyied_files_limits",
             Tuple(
                 title = "Change to warn or error if copyied files below given file counts",
                     elements = [
                         Integer(
                                 title = _("Change to warn if Backup-Job copyied less or equal files than"),
                                 help = _("If Backup-Job copyied less or equal files than the given number change to warn."),
                                 minvalue = 0,
                         ),
                         Integer(
                                 title = _("Change to error if Backup-Job copyied less or equal files than"),
                                 help = _("If Backup-Job copyied less or equal files than the given number change to error."),
                                 minvalue = 0,
                         ),
                     ]
                 )
            ),
            ( "backup_duration",
                Tuple(
                    title = _("Backup duration"),
                    elements = [
                      Age(title = _("Warning if backup is running longer as"),
                         default_value = 18000,        
                         help=_("If the backup is longer as the given time the check changes to warn.")
                      ),
                      Age(title = _("Critical if backup is running longer as"),
                         default_value = 21600,        
                         help=_("If the backup is longer as the given time the check changes to error.")
                      ),
                    ]
                )
            ),

            ('backup_age',
             Tuple(
                 title = "Age of Backup before changing to warn (default 26h) or error (default 30h).",
                 elements = [
                     Age(title=_("Warning at or above a backupage of"),
                         default_value = 93600,        
                         help=_("If the backup is older than the specified time, the check changes to warning. (24h=1440m; 26h=1560m)")
                     ),
                     Age(title=_("Critical at or above a backupage of"),
                         default_value = 108000,        
                         help=_("If the backup is older than the specified time, the check changes to critical. (24h=1440m; 26h=1560m)")
                     ),
                 ]
             )
            ),
        ]
    ),
    TextAscii(
        title = _("Description"),
        allow_empty = True
    ),
    match_type = "dict",
)
