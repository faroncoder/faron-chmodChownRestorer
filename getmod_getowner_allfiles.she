#!/bin/bash
startgreen=`date`

pathdir="$PWD"
locpath="$1"


 echo -n "collect (c) | end (e) :  "
 read commandget
 if [ $commandget == "c" ]
    then
        if [ -z $locpath ]
      	then
      	echo -n "path you need to collect?  only here (h) | everything from here (a) | ( enter folder name from here ) : "
      	read locpath
              if [ $locpath == "h" ]
                then
                    filelocpath="$pathdir"
                    echo -n "confirming: $filelocpath (y/n) ? "
                    read proceedcollection
                        if [ $proceedcollection == "y" ]
                          then
                              echo "collecting..."
                              find $filelocpath -maxdepth 0 -exec stat --format "chown %G:%G ${MPOINT}%n && chmod %a ${MPOINT}%n" {} \; >>  restore-chmod-chown.sh
                              echo "done!"
                        fi
                  getmod_getowner_allfiles
stopred=`date`; faronruntime=$(( $stopred - $startgreen )); echo "$0 | $startgreen | $stopred | $faronruntime " >> ~/.falcon/logs/scripts.log; exit 0
              fi
              fi
              if  [ $locpath == "a" ]
                    then
                      filelocpath="$pathdir"
                        echo -n "confirming: $filelocpath (y/n) ? "
                        read proceedcollection
                            if [ $proceedcollection == "y" ]
                              then
                                echo "collecting..."
                                find $filelocpath -exec stat --format "chown %G:%G ${MPOINT}%n && chmod %a ${MPOINT}%n" {} \; >>  restore-chmod-chown.sh
                                echo "done!"
                            fi
                  getmod_getowner_allfiles
stopred=`date`; faronruntime=$(( $stopred - $startgreen )); echo "$0 | $startgreen | $stopred | $faronruntime " >> ~/.falcon/logs/scripts.log; exit 0
              fi
              filelocpath="$pathdir/$locpath"
              echo -n "confirming: $filelocpath (y/n) ? "
              read proceedcollection
                  if [ $proceedcollection == "y" ]
                      then
                         echo "collecting..."
                         find $filelocpath -exec stat --format "chown %G:%G ${MPOINT}%n && chmod %a ${MPOINT}%n" {} \; >>  restore-chmod-chown.sh
                         echo "done!"
                  fi
                  getmod_getowner_allfiles
stopred=`date`; faronruntime=$(( $stopred - $startgreen )); echo "$0 | $startgreen | $stopred | $faronruntime " >> ~/.falcon/logs/scripts.log; exit 0
        fi      
  
  if [ $commandget == "e" ]
      then
      chmod +x $PWD/restore-chmod-chown.sh
stopred=`date`; faronruntime=$(( $stopred - $startgreen )); echo "$0 | $startgreen | $stopred | $faronruntime " >> ~/.falcon/logs/scripts.log; exit 0
  fi
  getmod_getowner_allfiles
stopred=`date`; faronruntime=$(( $stopred - $startgreen )); echo "$0 | $startgreen | $stopred | $faronruntime " >> ~/.falcon/logs/scripts.log; exit 0
