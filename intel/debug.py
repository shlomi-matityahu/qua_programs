
# Single QUA script generated at 2025-12-29 15:59:22.330014
# QUA library version: 1.2.3


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    a1 = declare(fixed, value=[0.9608096366924677, 0.8116090970210574, 0.9120602891827444, 0.9703728234629101, 0.9840870153125396, 0.9814686225290505, 0.8242267465082262, 0.8009093120375654, 0.9350328026815258, 0.9666244671365354, 0.893937698336686, 0.7766499960494337, 0.9648571195880735, 0.9548126623393512, 0.8143938259372328, 0.8223037742678051, 0.8389431715093804, 0.9989152675688575, 0.8166772163814461, 0.8115364158582489])
    v1 = declare(int, )
    v2 = declare(int, value=113348641)
    v3 = declare(int, )
    v4 = declare(int, value=215777257)
    v5 = declare(int, )
    v6 = declare(int, value=151465040)
    v7 = declare(int, )
    v8 = declare(int, value=100952771)
    v9 = declare(int, )
    v10 = declare(int, value=161755581)
    v11 = declare(int, )
    v12 = declare(int, value=195404722)
    v13 = declare(int, )
    v14 = declare(int, value=226860705)
    v15 = declare(int, )
    v16 = declare(int, value=219329245)
    v17 = declare(int, )
    v18 = declare(int, value=163791203)
    v19 = declare(int, )
    v20 = declare(int, value=181525532)
    v21 = declare(int, )
    v22 = declare(int, value=181410941)
    v23 = declare(int, )
    v24 = declare(int, value=12579076)
    v25 = declare(int, )
    v26 = declare(int, value=51336099)
    v27 = declare(int, )
    v28 = declare(int, value=259391873)
    v29 = declare(int, )
    v30 = declare(int, value=200891060)
    v31 = declare(int, )
    v32 = declare(int, value=236860985)
    v33 = declare(int, )
    v34 = declare(int, value=4703667)
    v35 = declare(int, )
    v36 = declare(int, value=216617973)
    v37 = declare(int, )
    v38 = declare(int, value=64236182)
    v39 = declare(int, )
    v40 = declare(int, value=177963649)
    v41 = declare(int, )
    v42 = declare(int, value=133246767)
    v43 = declare(int, )
    v44 = declare(int, value=160818857)
    v45 = declare(int, )
    v46 = declare(int, value=191201379)
    v47 = declare(int, )
    v48 = declare(int, value=122559635)
    v49 = declare(int, )
    v50 = declare(int, value=171659559)
    v51 = declare(int, )
    v52 = declare(int, value=172764781)
    v53 = declare(int, )
    v54 = declare(int, value=54870033)
    v55 = declare(int, )
    v56 = declare(int, value=7504102)
    v57 = declare(int, )
    v58 = declare(int, value=201503411)
    v59 = declare(int, )
    v60 = declare(int, value=80281932)
    v61 = declare(int, )
    v62 = declare(int, value=229449802)
    v63 = declare(int, )
    v64 = declare(int, value=180751625)
    v65 = declare(int, )
    v66 = declare(int, value=16426225)
    v67 = declare(int, )
    v68 = declare(int, value=102369635)
    v69 = declare(int, )
    v70 = declare(int, value=24899746)
    v71 = declare(int, )
    v72 = declare(int, value=31848685)
    v73 = declare(int, )
    v74 = declare(int, value=85403389)
    v75 = declare(int, )
    v76 = declare(int, value=6589455)
    v77 = declare(int, )
    v78 = declare(int, value=229954762)
    v79 = declare(int, )
    v80 = declare(int, value=215161003)
    v81 = declare(int, )
    v82 = declare(int, value=172813860)
    v83 = declare(int, )
    v84 = declare(int, value=111289998)
    v85 = declare(int, )
    v86 = declare(int, value=113169463)
    v87 = declare(int, )
    v88 = declare(int, value=264366462)
    v89 = declare(int, )
    v90 = declare(int, value=13936917)
    v91 = declare(int, )
    v92 = declare(int, value=136009668)
    v93 = declare(int, )
    v94 = declare(int, value=28227185)
    v95 = declare(int, )
    v96 = declare(int, value=254904429)
    v97 = declare(int, )
    v98 = declare(int, value=167270463)
    v99 = declare(int, )
    v100 = declare(int, value=228586543)
    v101 = declare(int, )
    v102 = declare(int, value=172104395)
    v103 = declare(int, )
    v104 = declare(int, value=17161143)
    v105 = declare(int, )
    v106 = declare(int, value=4173822)
    v107 = declare(int, )
    v108 = declare(int, value=2952185)
    v109 = declare(int, )
    v110 = declare(int, value=223841845)
    v111 = declare(int, )
    v112 = declare(int, value=185081947)
    v113 = declare(int, )
    v114 = declare(int, value=134095331)
    v115 = declare(int, )
    v116 = declare(int, value=32195910)
    v117 = declare(int, )
    v118 = declare(int, value=249436872)
    v119 = declare(int, )
    v120 = declare(int, value=10360430)
    v121 = declare(int, )
    v122 = declare(int, value=181229702)
    v123 = declare(int, )
    v124 = declare(int, value=244406068)
    v125 = declare(int, )
    v126 = declare(int, value=11792816)
    v127 = declare(int, )
    v128 = declare(int, value=7622593)
    with infinite_loop_():
        with for_(v1,0,(v1<1000),(v1+1)):
            play("cw"*amp((0.5*a1[Random(v2).rand_int(20)])), "qubit1", duration=2)
            play("cw"*amp((-0.25*a1[Random(v2).rand_int(20)])), "qubit1", duration=5)
    with infinite_loop_():
        with for_(v3,0,(v3<1000),(v3+1)):
            play("cw"*amp((0.5*a1[Random(v4).rand_int(20)])), "qubit2", duration=2)
            play("cw"*amp((-0.25*a1[Random(v4).rand_int(20)])), "qubit2", duration=5)
    with infinite_loop_():
        with for_(v5,0,(v5<1000),(v5+1)):
            play("cw"*amp((0.5*a1[Random(v6).rand_int(20)])), "qubit3", duration=2)
            play("cw"*amp((-0.25*a1[Random(v6).rand_int(20)])), "qubit3", duration=5)
    with infinite_loop_():
        with for_(v7,0,(v7<1000),(v7+1)):
            play("cw"*amp((0.5*a1[Random(v8).rand_int(20)])), "qubit4", duration=2)
            play("cw"*amp((-0.25*a1[Random(v8).rand_int(20)])), "qubit4", duration=5)
    with infinite_loop_():
        with for_(v9,0,(v9<1000),(v9+1)):
            play("cw"*amp((0.5*a1[Random(v10).rand_int(20)])), "qubit5", duration=2)
            play("cw"*amp((-0.25*a1[Random(v10).rand_int(20)])), "qubit5", duration=5)
    with infinite_loop_():
        with for_(v11,0,(v11<1000),(v11+1)):
            play("cw"*amp((0.5*a1[Random(v12).rand_int(20)])), "qubit6", duration=2)
            play("cw"*amp((-0.25*a1[Random(v12).rand_int(20)])), "qubit6", duration=5)
    with infinite_loop_():
        with for_(v13,0,(v13<1000),(v13+1)):
            play("cw"*amp((0.5*a1[Random(v14).rand_int(20)])), "qubit7", duration=2)
            play("cw"*amp((-0.25*a1[Random(v14).rand_int(20)])), "qubit7", duration=5)
    with infinite_loop_():
        with for_(v15,0,(v15<1000),(v15+1)):
            play("cw"*amp((0.5*a1[Random(v16).rand_int(20)])), "qubit8", duration=2)
            play("cw"*amp((-0.25*a1[Random(v16).rand_int(20)])), "qubit8", duration=5)
    with infinite_loop_():
        with for_(v17,0,(v17<1000),(v17+1)):
            play("cw"*amp((0.5*a1[Random(v18).rand_int(20)])), "qubit9", duration=2)
            play("cw"*amp((-0.25*a1[Random(v18).rand_int(20)])), "qubit9", duration=5)
    with infinite_loop_():
        with for_(v19,0,(v19<1000),(v19+1)):
            play("cw"*amp((0.5*a1[Random(v20).rand_int(20)])), "qubit10", duration=2)
            play("cw"*amp((-0.25*a1[Random(v20).rand_int(20)])), "qubit10", duration=5)
    with infinite_loop_():
        with for_(v21,0,(v21<1000),(v21+1)):
            play("cw"*amp((0.5*a1[Random(v22).rand_int(20)])), "qubit11", duration=2)
            play("cw"*amp((-0.25*a1[Random(v22).rand_int(20)])), "qubit11", duration=5)
    with infinite_loop_():
        with for_(v23,0,(v23<1000),(v23+1)):
            play("cw"*amp((0.5*a1[Random(v24).rand_int(20)])), "qubit12", duration=2)
            play("cw"*amp((-0.25*a1[Random(v24).rand_int(20)])), "qubit12", duration=5)
    with infinite_loop_():
        with for_(v25,0,(v25<1000),(v25+1)):
            play("cw"*amp((0.5*a1[Random(v26).rand_int(20)])), "qubit13", duration=2)
            play("cw"*amp((-0.25*a1[Random(v26).rand_int(20)])), "qubit13", duration=5)
    with infinite_loop_():
        with for_(v27,0,(v27<1000),(v27+1)):
            play("cw"*amp((0.5*a1[Random(v28).rand_int(20)])), "qubit14", duration=2)
            play("cw"*amp((-0.25*a1[Random(v28).rand_int(20)])), "qubit14", duration=5)
    with infinite_loop_():
        with for_(v29,0,(v29<1000),(v29+1)):
            play("cw"*amp((0.5*a1[Random(v30).rand_int(20)])), "qubit15", duration=2)
            play("cw"*amp((-0.25*a1[Random(v30).rand_int(20)])), "qubit15", duration=5)
    with infinite_loop_():
        with for_(v31,0,(v31<1000),(v31+1)):
            play("cw"*amp((0.5*a1[Random(v32).rand_int(20)])), "qubit16", duration=2)
            play("cw"*amp((-0.25*a1[Random(v32).rand_int(20)])), "qubit16", duration=5)
    with infinite_loop_():
        with for_(v33,0,(v33<1000),(v33+1)):
            play("cw"*amp((0.5*a1[Random(v34).rand_int(20)])), "qubit17", duration=2)
            play("cw"*amp((-0.25*a1[Random(v34).rand_int(20)])), "qubit17", duration=5)
    with infinite_loop_():
        with for_(v35,0,(v35<1000),(v35+1)):
            play("cw"*amp((0.5*a1[Random(v36).rand_int(20)])), "qubit18", duration=2)
            play("cw"*amp((-0.25*a1[Random(v36).rand_int(20)])), "qubit18", duration=5)
    with infinite_loop_():
        with for_(v37,0,(v37<1000),(v37+1)):
            play("cw"*amp((0.5*a1[Random(v38).rand_int(20)])), "qubit19", duration=2)
            play("cw"*amp((-0.25*a1[Random(v38).rand_int(20)])), "qubit19", duration=5)
    with infinite_loop_():
        with for_(v39,0,(v39<1000),(v39+1)):
            play("cw"*amp((0.5*a1[Random(v40).rand_int(20)])), "qubit20", duration=2)
            play("cw"*amp((-0.25*a1[Random(v40).rand_int(20)])), "qubit20", duration=5)
    with infinite_loop_():
        with for_(v41,0,(v41<1000),(v41+1)):
            play("cw"*amp((0.5*a1[Random(v42).rand_int(20)])), "qubit21", duration=2)
            play("cw"*amp((-0.25*a1[Random(v42).rand_int(20)])), "qubit21", duration=5)
    with infinite_loop_():
        with for_(v43,0,(v43<1000),(v43+1)):
            play("cw"*amp((0.5*a1[Random(v44).rand_int(20)])), "qubit22", duration=2)
            play("cw"*amp((-0.25*a1[Random(v44).rand_int(20)])), "qubit22", duration=5)
    with infinite_loop_():
        with for_(v45,0,(v45<1000),(v45+1)):
            play("cw"*amp((0.5*a1[Random(v46).rand_int(20)])), "qubit23", duration=2)
            play("cw"*amp((-0.25*a1[Random(v46).rand_int(20)])), "qubit23", duration=5)
    with infinite_loop_():
        with for_(v47,0,(v47<1000),(v47+1)):
            play("cw"*amp((0.5*a1[Random(v48).rand_int(20)])), "qubit24", duration=2)
            play("cw"*amp((-0.25*a1[Random(v48).rand_int(20)])), "qubit24", duration=5)
    with infinite_loop_():
        with for_(v49,0,(v49<1000),(v49+1)):
            play("cw"*amp((0.5*a1[Random(v50).rand_int(20)])), "qubit25", duration=2)
            play("cw"*amp((-0.25*a1[Random(v50).rand_int(20)])), "qubit25", duration=5)
    with infinite_loop_():
        with for_(v51,0,(v51<1000),(v51+1)):
            play("cw"*amp((0.5*a1[Random(v52).rand_int(20)])), "qubit26", duration=2)
            play("cw"*amp((-0.25*a1[Random(v52).rand_int(20)])), "qubit26", duration=5)
    with infinite_loop_():
        with for_(v53,0,(v53<1000),(v53+1)):
            play("cw"*amp((0.5*a1[Random(v54).rand_int(20)])), "qubit27", duration=2)
            play("cw"*amp((-0.25*a1[Random(v54).rand_int(20)])), "qubit27", duration=5)
    with infinite_loop_():
        with for_(v55,0,(v55<1000),(v55+1)):
            play("cw"*amp((0.5*a1[Random(v56).rand_int(20)])), "qubit28", duration=2)
            play("cw"*amp((-0.25*a1[Random(v56).rand_int(20)])), "qubit28", duration=5)
    with infinite_loop_():
        with for_(v57,0,(v57<1000),(v57+1)):
            play("cw"*amp((0.5*a1[Random(v58).rand_int(20)])), "qubit29", duration=2)
            play("cw"*amp((-0.25*a1[Random(v58).rand_int(20)])), "qubit29", duration=5)
    with infinite_loop_():
        with for_(v59,0,(v59<1000),(v59+1)):
            play("cw"*amp((0.5*a1[Random(v60).rand_int(20)])), "qubit30", duration=2)
            play("cw"*amp((-0.25*a1[Random(v60).rand_int(20)])), "qubit30", duration=5)
    with infinite_loop_():
        with for_(v61,0,(v61<1000),(v61+1)):
            play("cw"*amp((0.5*a1[Random(v62).rand_int(20)])), "qubit31", duration=2)
            play("cw"*amp((-0.25*a1[Random(v62).rand_int(20)])), "qubit31", duration=5)
    with infinite_loop_():
        with for_(v63,0,(v63<1000),(v63+1)):
            play("cw"*amp((0.5*a1[Random(v64).rand_int(20)])), "qubit32", duration=2)
            play("cw"*amp((-0.25*a1[Random(v64).rand_int(20)])), "qubit32", duration=5)
    with infinite_loop_():
        with for_(v65,0,(v65<1000),(v65+1)):
            play("cw"*amp((0.5*a1[Random(v66).rand_int(20)])), "qubit33", duration=2)
            play("cw"*amp((-0.25*a1[Random(v66).rand_int(20)])), "qubit33", duration=5)
    with infinite_loop_():
        with for_(v67,0,(v67<1000),(v67+1)):
            play("cw"*amp((0.5*a1[Random(v68).rand_int(20)])), "qubit34", duration=2)
            play("cw"*amp((-0.25*a1[Random(v68).rand_int(20)])), "qubit34", duration=5)
    with infinite_loop_():
        with for_(v69,0,(v69<1000),(v69+1)):
            play("cw"*amp((0.5*a1[Random(v70).rand_int(20)])), "qubit35", duration=2)
            play("cw"*amp((-0.25*a1[Random(v70).rand_int(20)])), "qubit35", duration=5)
    with infinite_loop_():
        with for_(v71,0,(v71<1000),(v71+1)):
            play("cw"*amp((0.5*a1[Random(v72).rand_int(20)])), "qubit36", duration=2)
            play("cw"*amp((-0.25*a1[Random(v72).rand_int(20)])), "qubit36", duration=5)
    with infinite_loop_():
        with for_(v73,0,(v73<1000),(v73+1)):
            play("cw"*amp((0.5*a1[Random(v74).rand_int(20)])), "qubit37", duration=2)
            play("cw"*amp((-0.25*a1[Random(v74).rand_int(20)])), "qubit37", duration=5)
    with infinite_loop_():
        with for_(v75,0,(v75<1000),(v75+1)):
            play("cw"*amp((0.5*a1[Random(v76).rand_int(20)])), "qubit38", duration=2)
            play("cw"*amp((-0.25*a1[Random(v76).rand_int(20)])), "qubit38", duration=5)
    with infinite_loop_():
        with for_(v77,0,(v77<1000),(v77+1)):
            play("cw"*amp((0.5*a1[Random(v78).rand_int(20)])), "qubit39", duration=2)
            play("cw"*amp((-0.25*a1[Random(v78).rand_int(20)])), "qubit39", duration=5)
    with infinite_loop_():
        with for_(v79,0,(v79<1000),(v79+1)):
            play("cw"*amp((0.5*a1[Random(v80).rand_int(20)])), "qubit40", duration=2)
            play("cw"*amp((-0.25*a1[Random(v80).rand_int(20)])), "qubit40", duration=5)
    with infinite_loop_():
        with for_(v81,0,(v81<1000),(v81+1)):
            play("cw"*amp((0.5*a1[Random(v82).rand_int(20)])), "qubit41", duration=2)
            play("cw"*amp((-0.25*a1[Random(v82).rand_int(20)])), "qubit41", duration=5)
    with infinite_loop_():
        with for_(v83,0,(v83<1000),(v83+1)):
            play("cw"*amp((0.5*a1[Random(v84).rand_int(20)])), "qubit42", duration=2)
            play("cw"*amp((-0.25*a1[Random(v84).rand_int(20)])), "qubit42", duration=5)
    with infinite_loop_():
        with for_(v85,0,(v85<1000),(v85+1)):
            play("cw"*amp((0.5*a1[Random(v86).rand_int(20)])), "qubit43", duration=2)
            play("cw"*amp((-0.25*a1[Random(v86).rand_int(20)])), "qubit43", duration=5)
    with infinite_loop_():
        with for_(v87,0,(v87<1000),(v87+1)):
            play("cw"*amp((0.5*a1[Random(v88).rand_int(20)])), "qubit44", duration=2)
            play("cw"*amp((-0.25*a1[Random(v88).rand_int(20)])), "qubit44", duration=5)
    with infinite_loop_():
        with for_(v89,0,(v89<1000),(v89+1)):
            play("cw"*amp((0.5*a1[Random(v90).rand_int(20)])), "qubit45", duration=2)
            play("cw"*amp((-0.25*a1[Random(v90).rand_int(20)])), "qubit45", duration=5)
    with infinite_loop_():
        with for_(v91,0,(v91<1000),(v91+1)):
            play("cw"*amp((0.5*a1[Random(v92).rand_int(20)])), "qubit46", duration=2)
            play("cw"*amp((-0.25*a1[Random(v92).rand_int(20)])), "qubit46", duration=5)
    with infinite_loop_():
        with for_(v93,0,(v93<1000),(v93+1)):
            play("cw"*amp((0.5*a1[Random(v94).rand_int(20)])), "qubit47", duration=2)
            play("cw"*amp((-0.25*a1[Random(v94).rand_int(20)])), "qubit47", duration=5)
    with infinite_loop_():
        with for_(v95,0,(v95<1000),(v95+1)):
            play("cw"*amp((0.5*a1[Random(v96).rand_int(20)])), "qubit48", duration=2)
            play("cw"*amp((-0.25*a1[Random(v96).rand_int(20)])), "qubit48", duration=5)
    with infinite_loop_():
        with for_(v97,0,(v97<1000),(v97+1)):
            play("cw"*amp((0.5*a1[Random(v98).rand_int(20)])), "qubit49", duration=2)
            play("cw"*amp((-0.25*a1[Random(v98).rand_int(20)])), "qubit49", duration=5)
    with infinite_loop_():
        with for_(v99,0,(v99<1000),(v99+1)):
            play("cw"*amp((0.5*a1[Random(v100).rand_int(20)])), "qubit50", duration=2)
            play("cw"*amp((-0.25*a1[Random(v100).rand_int(20)])), "qubit50", duration=5)
    with infinite_loop_():
        with for_(v101,0,(v101<1000),(v101+1)):
            play("cw"*amp((0.5*a1[Random(v102).rand_int(20)])), "qubit51", duration=2)
            play("cw"*amp((-0.25*a1[Random(v102).rand_int(20)])), "qubit51", duration=5)
    with infinite_loop_():
        with for_(v103,0,(v103<1000),(v103+1)):
            play("cw"*amp((0.5*a1[Random(v104).rand_int(20)])), "qubit52", duration=2)
            play("cw"*amp((-0.25*a1[Random(v104).rand_int(20)])), "qubit52", duration=5)
    with infinite_loop_():
        with for_(v105,0,(v105<1000),(v105+1)):
            play("cw"*amp((0.5*a1[Random(v106).rand_int(20)])), "qubit53", duration=2)
            play("cw"*amp((-0.25*a1[Random(v106).rand_int(20)])), "qubit53", duration=5)
    with infinite_loop_():
        with for_(v107,0,(v107<1000),(v107+1)):
            play("cw"*amp((0.5*a1[Random(v108).rand_int(20)])), "qubit54", duration=2)
            play("cw"*amp((-0.25*a1[Random(v108).rand_int(20)])), "qubit54", duration=5)
    with infinite_loop_():
        with for_(v109,0,(v109<1000),(v109+1)):
            play("cw"*amp((0.5*a1[Random(v110).rand_int(20)])), "qubit55", duration=2)
            play("cw"*amp((-0.25*a1[Random(v110).rand_int(20)])), "qubit55", duration=5)
    with infinite_loop_():
        with for_(v111,0,(v111<1000),(v111+1)):
            play("cw"*amp((0.5*a1[Random(v112).rand_int(20)])), "qubit56", duration=2)
            play("cw"*amp((-0.25*a1[Random(v112).rand_int(20)])), "qubit56", duration=5)
    with infinite_loop_():
        with for_(v113,0,(v113<1000),(v113+1)):
            play("cw"*amp((0.5*a1[Random(v114).rand_int(20)])), "qubit57", duration=2)
            play("cw"*amp((-0.25*a1[Random(v114).rand_int(20)])), "qubit57", duration=5)
    with infinite_loop_():
        with for_(v115,0,(v115<1000),(v115+1)):
            play("cw"*amp((0.5*a1[Random(v116).rand_int(20)])), "qubit58", duration=2)
            play("cw"*amp((-0.25*a1[Random(v116).rand_int(20)])), "qubit58", duration=5)
    with infinite_loop_():
        with for_(v117,0,(v117<1000),(v117+1)):
            play("cw"*amp((0.5*a1[Random(v118).rand_int(20)])), "qubit59", duration=2)
            play("cw"*amp((-0.25*a1[Random(v118).rand_int(20)])), "qubit59", duration=5)
    with infinite_loop_():
        with for_(v119,0,(v119<1000),(v119+1)):
            play("cw"*amp((0.5*a1[Random(v120).rand_int(20)])), "qubit60", duration=2)
            play("cw"*amp((-0.25*a1[Random(v120).rand_int(20)])), "qubit60", duration=5)
    with infinite_loop_():
        with for_(v121,0,(v121<1000),(v121+1)):
            play("cw"*amp((0.5*a1[Random(v122).rand_int(20)])), "qubit61", duration=2)
            play("cw"*amp((-0.25*a1[Random(v122).rand_int(20)])), "qubit61", duration=5)
    with infinite_loop_():
        with for_(v123,0,(v123<1000),(v123+1)):
            play("cw"*amp((0.5*a1[Random(v124).rand_int(20)])), "qubit62", duration=2)
            play("cw"*amp((-0.25*a1[Random(v124).rand_int(20)])), "qubit62", duration=5)
    with infinite_loop_():
        with for_(v125,0,(v125<1000),(v125+1)):
            play("cw"*amp((0.5*a1[Random(v126).rand_int(20)])), "qubit63", duration=2)
            play("cw"*amp((-0.25*a1[Random(v126).rand_int(20)])), "qubit63", duration=5)
    with infinite_loop_():
        with for_(v127,0,(v127<1000),(v127+1)):
            play("cw"*amp((0.5*a1[Random(v128).rand_int(20)])), "qubit64", duration=2)
            play("cw"*amp((-0.25*a1[Random(v128).rand_int(20)])), "qubit64", duration=5)

config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "1": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                    },
                },
                "2": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                    },
                },
                "3": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                    },
                },
                "4": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                    },
                },
                "5": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                    },
                },
                "6": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                    },
                },
                "7": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                    },
                },
                "8": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "qubit1": {
            "singleInput": {
                "port": ('con1', 1, 1),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit2": {
            "singleInput": {
                "port": ('con1', 1, 2),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit3": {
            "singleInput": {
                "port": ('con1', 1, 3),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit4": {
            "singleInput": {
                "port": ('con1', 1, 4),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit5": {
            "singleInput": {
                "port": ('con1', 1, 5),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit6": {
            "singleInput": {
                "port": ('con1', 1, 6),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit7": {
            "singleInput": {
                "port": ('con1', 1, 7),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit8": {
            "singleInput": {
                "port": ('con1', 1, 8),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit9": {
            "singleInput": {
                "port": ('con1', 2, 1),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit10": {
            "singleInput": {
                "port": ('con1', 2, 2),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit11": {
            "singleInput": {
                "port": ('con1', 2, 3),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit12": {
            "singleInput": {
                "port": ('con1', 2, 4),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit13": {
            "singleInput": {
                "port": ('con1', 2, 5),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit14": {
            "singleInput": {
                "port": ('con1', 2, 6),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit15": {
            "singleInput": {
                "port": ('con1', 2, 7),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit16": {
            "singleInput": {
                "port": ('con1', 2, 8),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit17": {
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit18": {
            "singleInput": {
                "port": ('con1', 3, 2),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit19": {
            "singleInput": {
                "port": ('con1', 3, 3),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit20": {
            "singleInput": {
                "port": ('con1', 3, 4),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit21": {
            "singleInput": {
                "port": ('con1', 3, 5),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit22": {
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit23": {
            "singleInput": {
                "port": ('con1', 3, 7),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit24": {
            "singleInput": {
                "port": ('con1', 3, 8),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit25": {
            "singleInput": {
                "port": ('con1', 4, 1),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit26": {
            "singleInput": {
                "port": ('con1', 4, 2),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit27": {
            "singleInput": {
                "port": ('con1', 4, 3),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit28": {
            "singleInput": {
                "port": ('con1', 4, 4),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit29": {
            "singleInput": {
                "port": ('con1', 4, 5),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit30": {
            "singleInput": {
                "port": ('con1', 4, 6),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit31": {
            "singleInput": {
                "port": ('con1', 4, 7),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit32": {
            "singleInput": {
                "port": ('con1', 4, 8),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit33": {
            "singleInput": {
                "port": ('con1', 5, 1),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit34": {
            "singleInput": {
                "port": ('con1', 5, 2),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit35": {
            "singleInput": {
                "port": ('con1', 5, 3),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit36": {
            "singleInput": {
                "port": ('con1', 5, 4),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit37": {
            "singleInput": {
                "port": ('con1', 5, 5),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit38": {
            "singleInput": {
                "port": ('con1', 5, 6),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit39": {
            "singleInput": {
                "port": ('con1', 5, 7),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit40": {
            "singleInput": {
                "port": ('con1', 5, 8),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit41": {
            "singleInput": {
                "port": ('con1', 6, 1),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit42": {
            "singleInput": {
                "port": ('con1', 6, 2),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit43": {
            "singleInput": {
                "port": ('con1', 6, 3),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit44": {
            "singleInput": {
                "port": ('con1', 6, 4),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit45": {
            "singleInput": {
                "port": ('con1', 6, 5),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit46": {
            "singleInput": {
                "port": ('con1', 6, 6),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit47": {
            "singleInput": {
                "port": ('con1', 6, 7),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit48": {
            "singleInput": {
                "port": ('con1', 6, 8),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit49": {
            "singleInput": {
                "port": ('con1', 7, 1),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit50": {
            "singleInput": {
                "port": ('con1', 7, 2),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit51": {
            "singleInput": {
                "port": ('con1', 7, 3),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit52": {
            "singleInput": {
                "port": ('con1', 7, 4),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit53": {
            "singleInput": {
                "port": ('con1', 7, 5),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit54": {
            "singleInput": {
                "port": ('con1', 7, 6),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit55": {
            "singleInput": {
                "port": ('con1', 7, 7),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit56": {
            "singleInput": {
                "port": ('con1', 7, 8),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit57": {
            "singleInput": {
                "port": ('con1', 8, 1),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit58": {
            "singleInput": {
                "port": ('con1', 8, 2),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit59": {
            "singleInput": {
                "port": ('con1', 8, 3),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit60": {
            "singleInput": {
                "port": ('con1', 8, 4),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit61": {
            "singleInput": {
                "port": ('con1', 8, 5),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit62": {
            "singleInput": {
                "port": ('con1', 8, 6),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit63": {
            "singleInput": {
                "port": ('con1', 8, 7),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit64": {
            "singleInput": {
                "port": ('con1', 8, 8),
            },
            "intermediate_frequency": 0.0,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "const_pulse_single": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "sqrt_pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "sqrt_wf",
                "Q": "zero_wf",
            },
        },
        "sqrt_pulse_single": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "sqrt_wf",
            },
        },
        "long_pulse": {
            "operation": "control",
            "length": 100000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "long_pulse_single": {
            "operation": "control",
            "length": 100000,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "gaussian_pulse": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "I": "gauss_wf",
                "Q": "zero_wf",
            },
        },
        "gaussian_pulse_single": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "single": "gauss_wf",
            },
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": 500,
            "waveforms": {
                "I": "readout_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
        "readout_pulse_single": {
            "operation": "measurement",
            "length": 500,
            "waveforms": {
                "single": "readout_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
        "readout_pulse_timetagging": {
            "operation": "measurement",
            "length": 3800,
            "waveforms": {
                "single": "zero_wf",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {
            "type": "constant",
            "sample": 2.4,
        },
        "sqrt_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.044946657497549475, 0.06356417261637282, 0.0778498944161523, 0.08989331499509895, 0.10050378152592121, 0.11009637651263605, 0.11891767800211263, 0.12712834523274563, 0.13483997249264842, 0.14213381090374028, 0.14907119849998599, 0.1556997888323046, 0.16205747826813258, 0.16817499303650435, 0.17407765595569785, 0.1797866299901979, 0.18531981638085643, 0.19069251784911845, 0.19591793788175288, 0.20100756305184242, 0.2059714602177749, 0.21081851067789195, 0.21555659689428774, 0.2201927530252721, 0.22473328748774735, 0.22918388365077622, 0.23354968324845687, 0.23783535600422526, 0.2420451581541316, 0.24618298195866548, 0.25025239784318276, 0.25425669046549126, 0.2581988897471611, 0.26208179770229884, 0.26590801173915524, 0.26967994498529685, 0.2733998440882415, 0.27706980486454447, 0.2806917861068948, 0.28426762180748055, 0.2877990320141519, 0.29128763250176765, 0.2947349434130383, 0.29814239699997197, 0.30151134457776363, 0.30484306278689194, 0.30813875924572515, 0.3113995776646092, 0.3146266024828463, 0.3178208630818641, 0.3209833376209784, 0.32411495653626515, 0.32721660573801425, 0.3302891295379082, 0.3333333333333333, 0.3363499860730087, 0.33933982252531925, 0.3423035453683137, 0.34524182711820883, 0.3481553119113957, 0.3510446171533232, 0.35391033504621655, 0.35675303400633784, 0.3595732599803958, 0.36237153766973934, 0.3651483716701107, 0.3679042475339682, 0.37063963276171286, 0.37335497772755005, 0.37605071654517747, 0.378727267878012, 0.3813850356982369, 0.384024409998567, 0.38664576746028073, 0.3892494720807615, 0.39183587576350576, 0.39440531887330776, 0.3969581307590985, 0.39949463024671505, 0.40201512610368484, 0.40451991747794525, 0.4070092943122622, 0.40948353773597257, 0.4119429204355498, 0.41438770700537403, 0.4168181542799854, 0.4192345116490003, 0.4216370213557839, 0.4240259187808922, 0.4264014327112209, 0.42876378559573314, 0.4311131937885755, 0.4334498677803327, 0.4357740124181224, 0.4380858271151806, 0.4403855060505442, 0.44267323835939754, 0.44494920831460977, 0.4472135954999579],
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "gauss_wf": {
            "type": "arbitrary",
            "samples": [0.02681429344289374, 0.04706055058005065, 0.07758973075218877, 0.12017332585185451, 0.17485115738056387, 0.23899319596590535, 0.3068733380356567, 0.3701599030793991, 0.4194461215617874] + [0.4464980722171096] * 2 + [0.4194461215617874, 0.3701599030793991, 0.3068733380356567, 0.23899319596590535, 0.17485115738056387, 0.12017332585185451, 0.07758973075218877, 0.04706055058005065, 0.02681429344289374],
        },
        "readout_wf": {
            "type": "constant",
            "sample": 0.2,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "sine_weights": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
    },
}

loaded_config = {
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "1": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                    },
                },
                "2": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                    },
                },
                "3": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                    },
                },
                "4": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                    },
                },
                "5": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                    },
                },
                "6": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                    },
                },
                "7": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                    },
                },
                "8": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "6": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                                "exponential_dc_gain": None,
                            },
                            "crosstalk": {},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "qubit1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 1, 1),
            },
            "intermediate_frequency": 0,
        },
        "qubit2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 1, 2),
            },
            "intermediate_frequency": 0,
        },
        "qubit3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 1, 3),
            },
            "intermediate_frequency": 0,
        },
        "qubit4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 1, 4),
            },
            "intermediate_frequency": 0,
        },
        "qubit5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 1, 5),
            },
            "intermediate_frequency": 0,
        },
        "qubit6": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 1, 6),
            },
            "intermediate_frequency": 0,
        },
        "qubit7": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 1, 7),
            },
            "intermediate_frequency": 0,
        },
        "qubit8": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 1, 8),
            },
            "intermediate_frequency": 0,
        },
        "qubit9": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 2, 1),
            },
            "intermediate_frequency": 0,
        },
        "qubit10": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 2, 2),
            },
            "intermediate_frequency": 0,
        },
        "qubit11": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 2, 3),
            },
            "intermediate_frequency": 0,
        },
        "qubit12": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 2, 4),
            },
            "intermediate_frequency": 0,
        },
        "qubit13": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 2, 5),
            },
            "intermediate_frequency": 0,
        },
        "qubit14": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 2, 6),
            },
            "intermediate_frequency": 0,
        },
        "qubit15": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 2, 7),
            },
            "intermediate_frequency": 0,
        },
        "qubit16": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 2, 8),
            },
            "intermediate_frequency": 0,
        },
        "qubit17": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "intermediate_frequency": 0,
        },
        "qubit18": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 2),
            },
            "intermediate_frequency": 0,
        },
        "qubit19": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 3),
            },
            "intermediate_frequency": 0,
        },
        "qubit20": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 4),
            },
            "intermediate_frequency": 0,
        },
        "qubit21": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 5),
            },
            "intermediate_frequency": 0,
        },
        "qubit22": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "intermediate_frequency": 0,
        },
        "qubit23": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 7),
            },
            "intermediate_frequency": 0,
        },
        "qubit24": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 8),
            },
            "intermediate_frequency": 0,
        },
        "qubit25": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 4, 1),
            },
            "intermediate_frequency": 0,
        },
        "qubit26": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 4, 2),
            },
            "intermediate_frequency": 0,
        },
        "qubit27": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 4, 3),
            },
            "intermediate_frequency": 0,
        },
        "qubit28": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 4, 4),
            },
            "intermediate_frequency": 0,
        },
        "qubit29": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 4, 5),
            },
            "intermediate_frequency": 0,
        },
        "qubit30": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 4, 6),
            },
            "intermediate_frequency": 0,
        },
        "qubit31": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 4, 7),
            },
            "intermediate_frequency": 0,
        },
        "qubit32": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 4, 8),
            },
            "intermediate_frequency": 0,
        },
        "qubit33": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 1),
            },
            "intermediate_frequency": 0,
        },
        "qubit34": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 2),
            },
            "intermediate_frequency": 0,
        },
        "qubit35": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 3),
            },
            "intermediate_frequency": 0,
        },
        "qubit36": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 4),
            },
            "intermediate_frequency": 0,
        },
        "qubit37": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 5),
            },
            "intermediate_frequency": 0,
        },
        "qubit38": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 6),
            },
            "intermediate_frequency": 0,
        },
        "qubit39": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 7),
            },
            "intermediate_frequency": 0,
        },
        "qubit40": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 8),
            },
            "intermediate_frequency": 0,
        },
        "qubit41": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 6, 1),
            },
            "intermediate_frequency": 0,
        },
        "qubit42": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 6, 2),
            },
            "intermediate_frequency": 0,
        },
        "qubit43": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 6, 3),
            },
            "intermediate_frequency": 0,
        },
        "qubit44": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 6, 4),
            },
            "intermediate_frequency": 0,
        },
        "qubit45": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 6, 5),
            },
            "intermediate_frequency": 0,
        },
        "qubit46": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 6, 6),
            },
            "intermediate_frequency": 0,
        },
        "qubit47": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 6, 7),
            },
            "intermediate_frequency": 0,
        },
        "qubit48": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 6, 8),
            },
            "intermediate_frequency": 0,
        },
        "qubit49": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 7, 1),
            },
            "intermediate_frequency": 0,
        },
        "qubit50": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 7, 2),
            },
            "intermediate_frequency": 0,
        },
        "qubit51": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 7, 3),
            },
            "intermediate_frequency": 0,
        },
        "qubit52": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 7, 4),
            },
            "intermediate_frequency": 0,
        },
        "qubit53": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 7, 5),
            },
            "intermediate_frequency": 0,
        },
        "qubit54": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 7, 6),
            },
            "intermediate_frequency": 0,
        },
        "qubit55": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 7, 7),
            },
            "intermediate_frequency": 0,
        },
        "qubit56": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 7, 8),
            },
            "intermediate_frequency": 0,
        },
        "qubit57": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 8, 1),
            },
            "intermediate_frequency": 0,
        },
        "qubit58": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 8, 2),
            },
            "intermediate_frequency": 0,
        },
        "qubit59": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 8, 3),
            },
            "intermediate_frequency": 0,
        },
        "qubit60": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 8, 4),
            },
            "intermediate_frequency": 0,
        },
        "qubit61": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 8, 5),
            },
            "intermediate_frequency": 0,
        },
        "qubit62": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 8, 6),
            },
            "intermediate_frequency": 0,
        },
        "qubit63": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 8, 7),
            },
            "intermediate_frequency": 0,
        },
        "qubit64": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_single",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 8, 8),
            },
            "intermediate_frequency": 0,
        },
    },
    "pulses": {
        "const_pulse": {
            "length": 100,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "const_pulse_single": {
            "length": 100,
            "waveforms": {
                "single": "const_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "sqrt_pulse": {
            "length": 100,
            "waveforms": {
                "I": "sqrt_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "sqrt_pulse_single": {
            "length": 100,
            "waveforms": {
                "single": "sqrt_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "long_pulse": {
            "length": 100000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "long_pulse_single": {
            "length": 100000,
            "waveforms": {
                "single": "const_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "gaussian_pulse": {
            "length": 20,
            "waveforms": {
                "I": "gauss_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "gaussian_pulse_single": {
            "length": 20,
            "waveforms": {
                "single": "gauss_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "readout_pulse": {
            "length": 500,
            "waveforms": {
                "I": "readout_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "readout_pulse_single": {
            "length": 500,
            "waveforms": {
                "single": "readout_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "readout_pulse_timetagging": {
            "length": 3800,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {},
            "operation": "measurement",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {
            "type": "constant",
            "sample": 2.4,
        },
        "sqrt_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.044946657497549475, 0.06356417261637282, 0.0778498944161523, 0.08989331499509895, 0.10050378152592121, 0.11009637651263605, 0.11891767800211263, 0.12712834523274563, 0.13483997249264842, 0.14213381090374028, 0.14907119849998599, 0.1556997888323046, 0.16205747826813258, 0.16817499303650435, 0.17407765595569785, 0.1797866299901979, 0.18531981638085643, 0.19069251784911845, 0.19591793788175288, 0.20100756305184242, 0.2059714602177749, 0.21081851067789195, 0.21555659689428774, 0.2201927530252721, 0.22473328748774735, 0.22918388365077622, 0.23354968324845687, 0.23783535600422526, 0.2420451581541316, 0.24618298195866548, 0.25025239784318276, 0.25425669046549126, 0.2581988897471611, 0.26208179770229884, 0.26590801173915524, 0.26967994498529685, 0.2733998440882415, 0.27706980486454447, 0.2806917861068948, 0.28426762180748055, 0.2877990320141519, 0.29128763250176765, 0.2947349434130383, 0.29814239699997197, 0.30151134457776363, 0.30484306278689194, 0.30813875924572515, 0.3113995776646092, 0.3146266024828463, 0.3178208630818641, 0.3209833376209784, 0.32411495653626515, 0.32721660573801425, 0.3302891295379082, 0.3333333333333333, 0.3363499860730087, 0.33933982252531925, 0.3423035453683137, 0.34524182711820883, 0.3481553119113957, 0.3510446171533232, 0.35391033504621655, 0.35675303400633784, 0.3595732599803958, 0.36237153766973934, 0.3651483716701107, 0.3679042475339682, 0.37063963276171286, 0.37335497772755005, 0.37605071654517747, 0.378727267878012, 0.3813850356982369, 0.384024409998567, 0.38664576746028073, 0.3892494720807615, 0.39183587576350576, 0.39440531887330776, 0.3969581307590985, 0.39949463024671505, 0.40201512610368484, 0.40451991747794525, 0.4070092943122622, 0.40948353773597257, 0.4119429204355498, 0.41438770700537403, 0.4168181542799854, 0.4192345116490003, 0.4216370213557839, 0.4240259187808922, 0.4264014327112209, 0.42876378559573314, 0.4311131937885755, 0.4334498677803327, 0.4357740124181224, 0.4380858271151806, 0.4403855060505442, 0.44267323835939754, 0.44494920831460977, 0.4472135954999579],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "gauss_wf": {
            "type": "arbitrary",
            "samples": [0.02681429344289374, 0.04706055058005065, 0.07758973075218877, 0.12017332585185451, 0.17485115738056387, 0.23899319596590535, 0.3068733380356567, 0.3701599030793991, 0.4194461215617874] + [0.4464980722171096] * 2 + [0.4194461215617874, 0.3701599030793991, 0.3068733380356567, 0.23899319596590535, 0.17485115738056387, 0.12017332585185451, 0.07758973075218877, 0.04706055058005065, 0.02681429344289374],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "readout_wf": {
            "type": "constant",
            "sample": 0.2,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "sine_weights": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
    },
    "mixers": {},
}


