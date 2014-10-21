This script is to help you to restore your Unix system if you have accidentally executed `chmod -R user:user` or `chmod -R 777` in your unix system ('user' as as username for your system).

Usage:

Place the script inside the parent folder (`/` for whole system) then chmod this script:

    chmod +x getmod_getowner_allfiles.sh

then execute it:

    ./getmod_getowner_allfiles.sh
    
When this is being done - a new file will be created in name of 'restore-chmod-chown.sh' and it'll be already executable (`chmod +x restore-chmod-chown.sh` will be already perform by the script).  Place the new script right inside the parent folder of your system   i.e. `/` ).

Voila!

This will only work if you have performed this script earlier before the accident.  

Recommendation:  perform this script at the end of fresh installation of your system, and archive the newly created restore-chmod-chown.sh somewhere safe in your system (i.e. USB or cloud).
