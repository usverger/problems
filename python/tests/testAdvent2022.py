import unittest
from typing import List
import python.advent2022 as advent2022

class TestAdvent2022(unittest.TestCase):
    
    def test_day07_part1(self):
        text = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

        s = advent2022.Day07.Solution(text.splitlines())

        s.buildTree()
        s.calculateTotalSize(s.root)
        print('\n')
        s.printTree(s.root, 0)

        sum = s.findPart1()
        print('Sum: ' + str(sum))

    def test_day07_part1_puzzle(self):
        text = '''$ cd /
$ ls
dir bzgf
199775 dngdnvv.qdf
dir fhhwv
dir gzlpvdhd
dir htczftcn
23392 lbcgmm
251030 lsw.jgr
305227 nflgvsgz
dir qcqg
dir qtqpw
dir qzcdscbp
dir rfgvg
dir rzb
202033 zqzlbvgl
$ cd bzgf
$ ls
80802 htczftcn.bdr
$ cd ..
$ cd fhhwv
$ ls
dir bjml
274615 bzmwfgf.wwp
dir ddpf
dir jngvpc
220692 lbcgmm
dir pffdg
dir prwpzhb
21309 qtqpw.mhb
12989 vbvt
46352 vhnsp.dhg
$ cd bjml
$ ls
307491 bzmwfgf.wwp
dir cwghv
164053 dngdnvv.qdf
144223 jbc.zgp
274358 mcqbcttc.mwr
dir pffdg
573 spbw.mnt
dir vdd
dir zzvs
$ cd cwghv
$ ls
298079 htczftcn
33689 nflgvsgz
287144 svfqpfm.bgs
dir tdgw
164244 tzrz.hms
52508 zmm.ndc
$ cd tdgw
$ ls
195017 htczftcn.cnl
$ cd ..
$ cd ..
$ cd pffdg
$ ls
64762 bbqh.wzf
dir bgzdv
56148 bhrw.jls
dir hqwmfdj
28260 htczftcn.lvs
dir lzhz
dir nbmsrl
91675 qtqpw.hsj
$ cd bgzdv
$ ls
205543 srzlfd.hnq
$ cd ..
$ cd hqwmfdj
$ ls
37910 dzpgcrn.rbj
290553 mrrngcdr
175411 nflgvsgz.tsj
$ cd ..
$ cd lzhz
$ ls
73620 bbtdnpvf
dir jbc
$ cd jbc
$ ls
125475 tzrz.hms
$ cd ..
$ cd ..
$ cd nbmsrl
$ ls
106099 dngdnvv.qdf
$ cd ..
$ cd ..
$ cd vdd
$ ls
136746 vlc.vcp
$ cd ..
$ cd zzvs
$ ls
8406 dngdnvv.qdf
dir nflgvsgz
55902 qtqpw.lcc
dir vmbrt
269256 whjmbnm.ngd
$ cd nflgvsgz
$ ls
dir mdgzvzbs
dir nlzc
$ cd mdgzvzbs
$ ls
88913 ggvd
$ cd ..
$ cd nlzc
$ ls
37916 rww
$ cd ..
$ cd ..
$ cd vmbrt
$ ls
194547 dwvbcvw.tmv
54334 htczftcn.bqh
299821 jnqgz
$ cd ..
$ cd ..
$ cd ..
$ cd ddpf
$ ls
dir plv
$ cd plv
$ ls
178177 dzsns
$ cd ..
$ cd ..
$ cd jngvpc
$ ls
276675 dcgmtcb
108711 htczftcn.dsr
dir jbc
280837 rqprcth.dhp
84724 tzrz.hms
$ cd jbc
$ ls
dir htczftcn
74153 tzrz.hms
$ cd htczftcn
$ ls
dir nflgvsgz
$ cd nflgvsgz
$ ls
208092 nnrd.zrj
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd pffdg
$ ls
264811 htczftcn
$ cd ..
$ cd prwpzhb
$ ls
181249 fstwrdqp
dir jbc
140710 nflgvsgz
dir pffdg
103710 qlqfc.qbm
dir qtqpw
15917 sqgmfl
dir zhcs
171467 zls.tmj
$ cd jbc
$ ls
12337 tzrz.hms
$ cd ..
$ cd pffdg
$ ls
302369 cshb.fbd
251192 htczftcn.vnn
dir msdtpqqd
dir sgtqmfgq
$ cd msdtpqqd
$ ls
42614 mptlnbp
$ cd ..
$ cd sgtqmfgq
$ ls
81125 jbc.szn
$ cd ..
$ cd ..
$ cd qtqpw
$ ls
160846 dngdnvv.qdf
$ cd ..
$ cd zhcs
$ ls
166883 vtz.bvb
$ cd ..
$ cd ..
$ cd ..
$ cd gzlpvdhd
$ ls
dir ffvz
$ cd ffvz
$ ls
74736 jvb.ppb
$ cd ..
$ cd ..
$ cd htczftcn
$ ls
dir dqbml
149343 gqjgvz
112647 lbcgmm
dir lbm
192438 mpdzgzm
dir nflgvsgz
dir pffdg
dir qtqpw
149952 qtqpw.gdv
dir rcnwghg
134076 rvdsldpf.zqc
dir sglgqlp
dir wrfmf
$ cd dqbml
$ ls
dir bphwp
303757 gglsqjbz.ffb
dir htczftcn
dir hwm
56134 pml.pmq
dir rsv
108298 tzrz.hms
201663 wqqdrml.wsl
$ cd bphwp
$ ls
94931 dngdnvv.qdf
90517 jsgl
118142 pzl
7387 tzrz.hms
$ cd ..
$ cd htczftcn
$ ls
300063 ctfgqld
dir htczftcn
dir jhldlsc
dir nflgvsgz
125403 pffdg
25617 pffdg.zdg
dir qddqn
dir tpmbzslr
$ cd htczftcn
$ ls
dir zzpnff
$ cd zzpnff
$ ls
79133 ssznrqlz.llw
$ cd ..
$ cd ..
$ cd jhldlsc
$ ls
dir swcbqqd
$ cd swcbqqd
$ ls
11202 htczftcn.cjs
111869 htczftcn.nvb
$ cd ..
$ cd ..
$ cd nflgvsgz
$ ls
37140 bffzwn.gqj
dir glmvgr
233206 lpclj
79112 lpqh.ldp
254611 qtqpw
dir rmbwlbt
206666 tgbdwgn
$ cd glmvgr
$ ls
115043 nflgvsgz.jgl
$ cd ..
$ cd rmbwlbt
$ ls
dir pffdg
$ cd pffdg
$ ls
92779 tzrz.hms
$ cd ..
$ cd ..
$ cd ..
$ cd qddqn
$ ls
dir jbc
$ cd jbc
$ ls
268367 cdcs
$ cd ..
$ cd ..
$ cd tpmbzslr
$ ls
dir dbfcp
dir lgsdbjz
$ cd dbfcp
$ ls
23450 nflgvsgz.nsl
$ cd ..
$ cd lgsdbjz
$ ls
248980 cqzqzb.nfh
248463 tzrz.hms
$ cd ..
$ cd ..
$ cd ..
$ cd hwm
$ ls
174410 jbc.rvr
310669 tzrz.hms
$ cd ..
$ cd rsv
$ ls
dir rsdnfh
$ cd rsdnfh
$ ls
276060 dngdnvv.qdf
137576 zsznp.ccq
$ cd ..
$ cd ..
$ cd ..
$ cd lbm
$ ls
201564 pffdg.rpv
$ cd ..
$ cd nflgvsgz
$ ls
dir jbc
dir svmmm
dir zfjdnbs
$ cd jbc
$ ls
dir jbc
dir mzt
dir qzth
dir scwdmwj
$ cd jbc
$ ls
71570 hhdt
dir ldzjsrm
27263 qtqpw.tcg
$ cd ldzjsrm
$ ls
217073 mlmwjq
172121 nflgvsgz
39275 pzrrlgt
$ cd ..
$ cd ..
$ cd mzt
$ ls
130917 tzrz.hms
$ cd ..
$ cd qzth
$ ls
280896 dngdnvv.qdf
6736 jbc.mtm
dir nfsbdfv
293220 nvzjz
dir pffdg
88075 ppmr
$ cd nfsbdfv
$ ls
58157 bzmwfgf.wwp
dir gmhbnffd
65369 gmq.zvb
dir htczftcn
dir qmc
278485 tvs.csj
$ cd gmhbnffd
$ ls
195493 lbcgmm
264234 mvqbqprp
268782 rtqts.zls
$ cd ..
$ cd htczftcn
$ ls
dir lnhjgl
$ cd lnhjgl
$ ls
80056 ffsrvl
$ cd ..
$ cd ..
$ cd qmc
$ ls
29571 hqftnv.vwn
$ cd ..
$ cd ..
$ cd pffdg
$ ls
dir bfdmm
244334 ppf
dir rggmf
$ cd bfdmm
$ ls
296551 nflgvsgz.bch
77180 tzrz.hms
$ cd ..
$ cd rggmf
$ ls
187569 dngdnvv.qdf
$ cd ..
$ cd ..
$ cd ..
$ cd scwdmwj
$ ls
dir fhwnjp
191201 gztswt.cvn
dir jsbdjv
dir nflgvsgz
dir pffdg
55401 qtqpw.hfv
$ cd fhwnjp
$ ls
200583 tqrqsmwt
$ cd ..
$ cd jsbdjv
$ ls
46882 fgjhsb.szs
156238 qtqpw.ctw
$ cd ..
$ cd nflgvsgz
$ ls
216012 nrfchlbs.wlw
75316 qtqpw
218733 vzldr
$ cd ..
$ cd pffdg
$ ls
75020 htczftcn.trw
6370 snnvrrwb.qmm
281520 vwstfbzg.jgq
$ cd ..
$ cd ..
$ cd ..
$ cd svmmm
$ ls
dir bgh
22016 czchmpc
294397 dngdnvv.qdf
14175 gdhtprt
dir nclpsp
dir pffdg
dir qtqpw
dir rwhq
138882 smqdrdjs
174171 vqjztp.zlr
$ cd bgh
$ ls
172183 fhsfhhjn
209572 phpdrzm
$ cd ..
$ cd nclpsp
$ ls
41222 bzmwfgf.wwp
134164 dqbqvg
dir dqtgwjn
dir htczftcn
210868 htczftcn.cjp
dir jbc
185752 lfrdq.wrm
dir pwvbnc
dir qhrtrsvm
235340 rljlr.lfs
$ cd dqtgwjn
$ ls
dir lbft
118196 tpl.qgw
83985 wbjmdmjm
$ cd lbft
$ ls
187172 vrd
$ cd ..
$ cd ..
$ cd htczftcn
$ ls
210604 hzlf
154916 nflgvsgz
115688 pffdg.ptz
$ cd ..
$ cd jbc
$ ls
122033 bzmwfgf.wwp
105912 dngdnvv.qdf
16049 nflgvsgz
43497 slmwmtfn
69357 tcsc.fgf
$ cd ..
$ cd pwvbnc
$ ls
10200 pfvsnqp.fwr
$ cd ..
$ cd qhrtrsvm
$ ls
193675 djmhdr.vcc
108939 qtqpw
$ cd ..
$ cd ..
$ cd pffdg
$ ls
dir dbtmdvq
$ cd dbtmdvq
$ ls
127568 vhnqsm.ghq
$ cd ..
$ cd ..
$ cd qtqpw
$ ls
dir crpzfdn
$ cd crpzfdn
$ ls
135177 lpzrl.qvj
dir qtldnjtd
$ cd qtldnjtd
$ ls
88481 rlbzbjt.rrz
$ cd ..
$ cd ..
$ cd ..
$ cd rwhq
$ ls
87944 bzmwfgf.wwp
70798 dngdnvv.qdf
dir hgqbmgch
dir lrvncpvz
dir nflgvsgz
$ cd hgqbmgch
$ ls
293841 bzmwfgf.wwp
286937 lwpf
dir smfbjhw
dir smqh
103844 vmpqmzf.dnf
$ cd smfbjhw
$ ls
186167 crgrnf.dns
dir htczftcn
$ cd htczftcn
$ ls
11324 gssn.rlt
46905 tzrz.hms
$ cd ..
$ cd ..
$ cd smqh
$ ls
dir pffdg
dir zbg
$ cd pffdg
$ ls
3570 bzmwfgf.wwp
3335 fvpd.bct
$ cd ..
$ cd zbg
$ ls
108877 bzmwfgf.wwp
310302 drhsdtcv.rrw
152250 wfvvsg
$ cd ..
$ cd ..
$ cd ..
$ cd lrvncpvz
$ ls
206419 nflgvsgz.tvr
$ cd ..
$ cd nflgvsgz
$ ls
286461 tzrz.hms
$ cd ..
$ cd ..
$ cd ..
$ cd zfjdnbs
$ ls
dir htczftcn
dir nflgvsgz
dir scvzpf
$ cd htczftcn
$ ls
dir jznspqtr
dir tpz
$ cd jznspqtr
$ ls
86738 hqftnv.vwn
$ cd ..
$ cd tpz
$ ls
126506 nflgvsgz.qnh
$ cd ..
$ cd ..
$ cd nflgvsgz
$ ls
248446 gwjgdb.vrr
$ cd ..
$ cd scvzpf
$ ls
dir fpbbjmjf
173634 gbpql
141796 jzncpqb.pgc
69394 rpvnchs
65500 tzrz.hms
$ cd fpbbjmjf
$ ls
224020 hhrjc
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd pffdg
$ ls
101444 clwdmcz.thc
58211 dngdnvv.qdf
dir mnj
dir ncwh
153413 nflgvsgz
dir qtqpw
141829 rrfs.ffn
$ cd mnj
$ ls
298654 qtqpw
$ cd ..
$ cd ncwh
$ ls
133042 bmthlszz.mtr
dir nflgvsgz
dir nrsqtdz
201720 wqhnfz
$ cd nflgvsgz
$ ls
dir bqqmlffw
115991 hsljpqpf
dir htczftcn
$ cd bqqmlffw
$ ls
49001 wltpcszs.bvj
$ cd ..
$ cd htczftcn
$ ls
264620 sfdssh.dnj
260432 vgvzjl
$ cd ..
$ cd ..
$ cd nrsqtdz
$ ls
258978 htczftcn
dir jbc
dir nsqlmlqp
28767 pffdg.blw
172773 tzrz.hms
$ cd jbc
$ ls
dir ztphfs
$ cd ztphfs
$ ls
dir gpps
$ cd gpps
$ ls
74744 bzmwfgf.wwp
$ cd ..
$ cd ..
$ cd ..
$ cd nsqlmlqp
$ ls
dir zvwvdzlv
$ cd zvwvdzlv
$ ls
218727 hsjm.qgm
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd qtqpw
$ ls
171370 sdmhwctq.gzr
$ cd ..
$ cd ..
$ cd qtqpw
$ ls
dir csqvzqdc
131580 jbc.ppb
126635 jbc.sbm
302398 pbjd
74429 vnpj
dir zhmp
$ cd csqvzqdc
$ ls
150923 jbc.grw
dir lthhrqnn
240950 pffdg.qbt
dir rgzqq
$ cd lthhrqnn
$ ls
123194 czl
17546 pffdg
$ cd ..
$ cd rgzqq
$ ls
156566 jbc.hpw
$ cd ..
$ cd ..
$ cd zhmp
$ ls
291659 dngdnvv.qdf
309738 nflgvsgz.wmc
$ cd ..
$ cd ..
$ cd rcnwghg
$ ls
108285 hvhlggsn
308801 sgstjfqq.hln
$ cd ..
$ cd sglgqlp
$ ls
dir gnvnlrz
dir nchq
dir nlrbnwp
dir zpg
$ cd gnvnlrz
$ ls
62071 lgqrm
dir pvt
dir srdqwtcs
$ cd pvt
$ ls
dir fpfddfw
dir jbc
dir jzrb
$ cd fpfddfw
$ ls
257231 rgccj.dwc
$ cd ..
$ cd jbc
$ ls
118252 dsvsmgm.hdm
$ cd ..
$ cd jzrb
$ ls
157243 gcrfg.svt
86860 pblts.jtd
$ cd ..
$ cd ..
$ cd srdqwtcs
$ ls
267482 bzzghfpq.gmh
dir cbd
dir gwqzndrt
288249 hhdmlslr
286213 lwmhd
dir rfvmgch
121131 vbm.rbp
$ cd cbd
$ ls
238535 jpbzwvd.rrw
246606 wgl.gfg
$ cd ..
$ cd gwqzndrt
$ ls
dir twtpbh
262912 vcmv.qcs
$ cd twtpbh
$ ls
245819 dngdnvv.qdf
295823 ghrnmd
308384 pffdg.ptr
231669 sqhnt.grn
$ cd ..
$ cd ..
$ cd rfvmgch
$ ls
306719 cwr.jsm
6449 hqftnv.vwn
$ cd ..
$ cd ..
$ cd ..
$ cd nchq
$ ls
137003 qtqpw
267253 zrgvq
146047 zww.nrr
$ cd ..
$ cd nlrbnwp
$ ls
91151 tzrz.hms
$ cd ..
$ cd zpg
$ ls
68248 bzmwfgf.wwp
$ cd ..
$ cd ..
$ cd wrfmf
$ ls
dir cdlwfjhp
16673 dsctg
304187 jbc
dir lchrdvm
dir nflgvsgz
dir qtqpw
dir rgdc
306410 tzrz.hms
dir zqzzg
$ cd cdlwfjhp
$ ls
dir clshzcrc
dir lplgpg
$ cd clshzcrc
$ ls
191491 tzrz.hms
$ cd ..
$ cd lplgpg
$ ls
169864 cmhrmh.pjp
$ cd ..
$ cd ..
$ cd lchrdvm
$ ls
149068 chwbr.spd
250029 hqftnv.vwn
23399 jbc
69746 nflgvsgz.nmp
dir pldctfcf
dir vngv
251416 zhf.qtz
$ cd pldctfcf
$ ls
297722 bcpwcn
276738 cspls
dir gghvnc
80690 htczftcn
dir pffdg
97610 qfjs.gps
dir tvc
106070 tzrz.hms
$ cd gghvnc
$ ls
93770 dngdnvv.qdf
$ cd ..
$ cd pffdg
$ ls
180916 bzmwfgf.wwp
$ cd ..
$ cd tvc
$ ls
11724 gtgzwsq
$ cd ..
$ cd ..
$ cd vngv
$ ls
92840 qtqpw.gcl
$ cd ..
$ cd ..
$ cd nflgvsgz
$ ls
dir htczftcn
dir lcjqzrwm
54961 lfn.rmz
dir plvbmb
dir vdfwfg
$ cd htczftcn
$ ls
dir gflz
dir mpp
292374 rzm
$ cd gflz
$ ls
dir qpdn
$ cd qpdn
$ ls
258037 ddqb.jhd
$ cd ..
$ cd ..
$ cd mpp
$ ls
248628 pffdg.spt
$ cd ..
$ cd ..
$ cd lcjqzrwm
$ ls
249155 mbz.gsq
291857 nngm.nft
100136 zwvwlg.hrs
$ cd ..
$ cd plvbmb
$ ls
dir nnrnwp
163552 pffdg
$ cd nnrnwp
$ ls
289041 bzmwfgf.wwp
29165 nvcwzfpr
$ cd ..
$ cd ..
$ cd vdfwfg
$ ls
264391 hqftnv.vwn
309071 htczftcn.mrd
dir wtqrrvvr
$ cd wtqrrvvr
$ ls
230331 swhpd
$ cd ..
$ cd ..
$ cd ..
$ cd qtqpw
$ ls
292434 hbjlsrw
$ cd ..
$ cd rgdc
$ ls
dir hqldlpg
$ cd hqldlpg
$ ls
188809 rvjwsmnz.hqt
$ cd ..
$ cd ..
$ cd zqzzg
$ ls
250923 qtqpw.zrb
$ cd ..
$ cd ..
$ cd ..
$ cd qcqg
$ ls
309875 tzrz.hms
$ cd ..
$ cd qtqpw
$ ls
dir rcnp
$ cd rcnp
$ ls
131725 bzmwfgf.wwp
46663 chwfd
$ cd ..
$ cd ..
$ cd qzcdscbp
$ ls
dir mtqt
$ cd mtqt
$ ls
27367 llbt.pth
dir mcrddwgp
$ cd mcrddwgp
$ ls
77221 bzmwfgf.wwp
37941 lrwlhz
dir tcmrv
85568 tzrz.hms
$ cd tcmrv
$ ls
dir hprvr
$ cd hprvr
$ ls
59831 qbchdjw.gjg
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd rfgvg
$ ls
dir qlg
$ cd qlg
$ ls
142825 dngdnvv.qdf
$ cd ..
$ cd ..
$ cd rzb
$ ls
250575 dngdnvv.qdf
dir jbc
dir lbg
187509 plblzt.zzz
dir qwjlvqdp
237529 rrrqcl.pvt
dir rsjg
$ cd jbc
$ ls
253304 lpdndfn
$ cd ..
$ cd lbg
$ ls
dir fml
$ cd fml
$ ls
106624 shm.fgh
$ cd ..
$ cd ..
$ cd qwjlvqdp
$ ls
dir htczftcn
$ cd htczftcn
$ ls
dir gnnzlzwd
272143 jbc.ldg
dir sztdtpjt
$ cd gnnzlzwd
$ ls
218355 tzrz.hms
$ cd ..
$ cd sztdtpjt
$ ls
53466 tzrz.hms
$ cd ..
$ cd ..
$ cd ..
$ cd rsjg
$ ls
101889 cct.sfg'''

        s = advent2022.Day07.Solution(text.splitlines())

        s.buildTree()
        s.calculateTotalSize(s.root)
        print('\n')
        s.printTree(s.root, 0)

        sum = s.findPart1()
        print('Sum: ' + str(sum))
        self.assertEqual(sum, 2104783)

    def test_day07_part2(self):
        text = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

        s = advent2022.Day07.Solution(text.splitlines())

        s.buildTree()
        s.calculateTotalSize(s.root)
        print('\n')
        
        minSize = s.findPart2()
        print('Min size: ' + str(minSize))
        self.assertEqual(minSize, 24933642)

    def test_day07_part2_puzzle(self):
        text = '''$ cd /
$ ls
dir bzgf
199775 dngdnvv.qdf
dir fhhwv
dir gzlpvdhd
dir htczftcn
23392 lbcgmm
251030 lsw.jgr
305227 nflgvsgz
dir qcqg
dir qtqpw
dir qzcdscbp
dir rfgvg
dir rzb
202033 zqzlbvgl
$ cd bzgf
$ ls
80802 htczftcn.bdr
$ cd ..
$ cd fhhwv
$ ls
dir bjml
274615 bzmwfgf.wwp
dir ddpf
dir jngvpc
220692 lbcgmm
dir pffdg
dir prwpzhb
21309 qtqpw.mhb
12989 vbvt
46352 vhnsp.dhg
$ cd bjml
$ ls
307491 bzmwfgf.wwp
dir cwghv
164053 dngdnvv.qdf
144223 jbc.zgp
274358 mcqbcttc.mwr
dir pffdg
573 spbw.mnt
dir vdd
dir zzvs
$ cd cwghv
$ ls
298079 htczftcn
33689 nflgvsgz
287144 svfqpfm.bgs
dir tdgw
164244 tzrz.hms
52508 zmm.ndc
$ cd tdgw
$ ls
195017 htczftcn.cnl
$ cd ..
$ cd ..
$ cd pffdg
$ ls
64762 bbqh.wzf
dir bgzdv
56148 bhrw.jls
dir hqwmfdj
28260 htczftcn.lvs
dir lzhz
dir nbmsrl
91675 qtqpw.hsj
$ cd bgzdv
$ ls
205543 srzlfd.hnq
$ cd ..
$ cd hqwmfdj
$ ls
37910 dzpgcrn.rbj
290553 mrrngcdr
175411 nflgvsgz.tsj
$ cd ..
$ cd lzhz
$ ls
73620 bbtdnpvf
dir jbc
$ cd jbc
$ ls
125475 tzrz.hms
$ cd ..
$ cd ..
$ cd nbmsrl
$ ls
106099 dngdnvv.qdf
$ cd ..
$ cd ..
$ cd vdd
$ ls
136746 vlc.vcp
$ cd ..
$ cd zzvs
$ ls
8406 dngdnvv.qdf
dir nflgvsgz
55902 qtqpw.lcc
dir vmbrt
269256 whjmbnm.ngd
$ cd nflgvsgz
$ ls
dir mdgzvzbs
dir nlzc
$ cd mdgzvzbs
$ ls
88913 ggvd
$ cd ..
$ cd nlzc
$ ls
37916 rww
$ cd ..
$ cd ..
$ cd vmbrt
$ ls
194547 dwvbcvw.tmv
54334 htczftcn.bqh
299821 jnqgz
$ cd ..
$ cd ..
$ cd ..
$ cd ddpf
$ ls
dir plv
$ cd plv
$ ls
178177 dzsns
$ cd ..
$ cd ..
$ cd jngvpc
$ ls
276675 dcgmtcb
108711 htczftcn.dsr
dir jbc
280837 rqprcth.dhp
84724 tzrz.hms
$ cd jbc
$ ls
dir htczftcn
74153 tzrz.hms
$ cd htczftcn
$ ls
dir nflgvsgz
$ cd nflgvsgz
$ ls
208092 nnrd.zrj
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd pffdg
$ ls
264811 htczftcn
$ cd ..
$ cd prwpzhb
$ ls
181249 fstwrdqp
dir jbc
140710 nflgvsgz
dir pffdg
103710 qlqfc.qbm
dir qtqpw
15917 sqgmfl
dir zhcs
171467 zls.tmj
$ cd jbc
$ ls
12337 tzrz.hms
$ cd ..
$ cd pffdg
$ ls
302369 cshb.fbd
251192 htczftcn.vnn
dir msdtpqqd
dir sgtqmfgq
$ cd msdtpqqd
$ ls
42614 mptlnbp
$ cd ..
$ cd sgtqmfgq
$ ls
81125 jbc.szn
$ cd ..
$ cd ..
$ cd qtqpw
$ ls
160846 dngdnvv.qdf
$ cd ..
$ cd zhcs
$ ls
166883 vtz.bvb
$ cd ..
$ cd ..
$ cd ..
$ cd gzlpvdhd
$ ls
dir ffvz
$ cd ffvz
$ ls
74736 jvb.ppb
$ cd ..
$ cd ..
$ cd htczftcn
$ ls
dir dqbml
149343 gqjgvz
112647 lbcgmm
dir lbm
192438 mpdzgzm
dir nflgvsgz
dir pffdg
dir qtqpw
149952 qtqpw.gdv
dir rcnwghg
134076 rvdsldpf.zqc
dir sglgqlp
dir wrfmf
$ cd dqbml
$ ls
dir bphwp
303757 gglsqjbz.ffb
dir htczftcn
dir hwm
56134 pml.pmq
dir rsv
108298 tzrz.hms
201663 wqqdrml.wsl
$ cd bphwp
$ ls
94931 dngdnvv.qdf
90517 jsgl
118142 pzl
7387 tzrz.hms
$ cd ..
$ cd htczftcn
$ ls
300063 ctfgqld
dir htczftcn
dir jhldlsc
dir nflgvsgz
125403 pffdg
25617 pffdg.zdg
dir qddqn
dir tpmbzslr
$ cd htczftcn
$ ls
dir zzpnff
$ cd zzpnff
$ ls
79133 ssznrqlz.llw
$ cd ..
$ cd ..
$ cd jhldlsc
$ ls
dir swcbqqd
$ cd swcbqqd
$ ls
11202 htczftcn.cjs
111869 htczftcn.nvb
$ cd ..
$ cd ..
$ cd nflgvsgz
$ ls
37140 bffzwn.gqj
dir glmvgr
233206 lpclj
79112 lpqh.ldp
254611 qtqpw
dir rmbwlbt
206666 tgbdwgn
$ cd glmvgr
$ ls
115043 nflgvsgz.jgl
$ cd ..
$ cd rmbwlbt
$ ls
dir pffdg
$ cd pffdg
$ ls
92779 tzrz.hms
$ cd ..
$ cd ..
$ cd ..
$ cd qddqn
$ ls
dir jbc
$ cd jbc
$ ls
268367 cdcs
$ cd ..
$ cd ..
$ cd tpmbzslr
$ ls
dir dbfcp
dir lgsdbjz
$ cd dbfcp
$ ls
23450 nflgvsgz.nsl
$ cd ..
$ cd lgsdbjz
$ ls
248980 cqzqzb.nfh
248463 tzrz.hms
$ cd ..
$ cd ..
$ cd ..
$ cd hwm
$ ls
174410 jbc.rvr
310669 tzrz.hms
$ cd ..
$ cd rsv
$ ls
dir rsdnfh
$ cd rsdnfh
$ ls
276060 dngdnvv.qdf
137576 zsznp.ccq
$ cd ..
$ cd ..
$ cd ..
$ cd lbm
$ ls
201564 pffdg.rpv
$ cd ..
$ cd nflgvsgz
$ ls
dir jbc
dir svmmm
dir zfjdnbs
$ cd jbc
$ ls
dir jbc
dir mzt
dir qzth
dir scwdmwj
$ cd jbc
$ ls
71570 hhdt
dir ldzjsrm
27263 qtqpw.tcg
$ cd ldzjsrm
$ ls
217073 mlmwjq
172121 nflgvsgz
39275 pzrrlgt
$ cd ..
$ cd ..
$ cd mzt
$ ls
130917 tzrz.hms
$ cd ..
$ cd qzth
$ ls
280896 dngdnvv.qdf
6736 jbc.mtm
dir nfsbdfv
293220 nvzjz
dir pffdg
88075 ppmr
$ cd nfsbdfv
$ ls
58157 bzmwfgf.wwp
dir gmhbnffd
65369 gmq.zvb
dir htczftcn
dir qmc
278485 tvs.csj
$ cd gmhbnffd
$ ls
195493 lbcgmm
264234 mvqbqprp
268782 rtqts.zls
$ cd ..
$ cd htczftcn
$ ls
dir lnhjgl
$ cd lnhjgl
$ ls
80056 ffsrvl
$ cd ..
$ cd ..
$ cd qmc
$ ls
29571 hqftnv.vwn
$ cd ..
$ cd ..
$ cd pffdg
$ ls
dir bfdmm
244334 ppf
dir rggmf
$ cd bfdmm
$ ls
296551 nflgvsgz.bch
77180 tzrz.hms
$ cd ..
$ cd rggmf
$ ls
187569 dngdnvv.qdf
$ cd ..
$ cd ..
$ cd ..
$ cd scwdmwj
$ ls
dir fhwnjp
191201 gztswt.cvn
dir jsbdjv
dir nflgvsgz
dir pffdg
55401 qtqpw.hfv
$ cd fhwnjp
$ ls
200583 tqrqsmwt
$ cd ..
$ cd jsbdjv
$ ls
46882 fgjhsb.szs
156238 qtqpw.ctw
$ cd ..
$ cd nflgvsgz
$ ls
216012 nrfchlbs.wlw
75316 qtqpw
218733 vzldr
$ cd ..
$ cd pffdg
$ ls
75020 htczftcn.trw
6370 snnvrrwb.qmm
281520 vwstfbzg.jgq
$ cd ..
$ cd ..
$ cd ..
$ cd svmmm
$ ls
dir bgh
22016 czchmpc
294397 dngdnvv.qdf
14175 gdhtprt
dir nclpsp
dir pffdg
dir qtqpw
dir rwhq
138882 smqdrdjs
174171 vqjztp.zlr
$ cd bgh
$ ls
172183 fhsfhhjn
209572 phpdrzm
$ cd ..
$ cd nclpsp
$ ls
41222 bzmwfgf.wwp
134164 dqbqvg
dir dqtgwjn
dir htczftcn
210868 htczftcn.cjp
dir jbc
185752 lfrdq.wrm
dir pwvbnc
dir qhrtrsvm
235340 rljlr.lfs
$ cd dqtgwjn
$ ls
dir lbft
118196 tpl.qgw
83985 wbjmdmjm
$ cd lbft
$ ls
187172 vrd
$ cd ..
$ cd ..
$ cd htczftcn
$ ls
210604 hzlf
154916 nflgvsgz
115688 pffdg.ptz
$ cd ..
$ cd jbc
$ ls
122033 bzmwfgf.wwp
105912 dngdnvv.qdf
16049 nflgvsgz
43497 slmwmtfn
69357 tcsc.fgf
$ cd ..
$ cd pwvbnc
$ ls
10200 pfvsnqp.fwr
$ cd ..
$ cd qhrtrsvm
$ ls
193675 djmhdr.vcc
108939 qtqpw
$ cd ..
$ cd ..
$ cd pffdg
$ ls
dir dbtmdvq
$ cd dbtmdvq
$ ls
127568 vhnqsm.ghq
$ cd ..
$ cd ..
$ cd qtqpw
$ ls
dir crpzfdn
$ cd crpzfdn
$ ls
135177 lpzrl.qvj
dir qtldnjtd
$ cd qtldnjtd
$ ls
88481 rlbzbjt.rrz
$ cd ..
$ cd ..
$ cd ..
$ cd rwhq
$ ls
87944 bzmwfgf.wwp
70798 dngdnvv.qdf
dir hgqbmgch
dir lrvncpvz
dir nflgvsgz
$ cd hgqbmgch
$ ls
293841 bzmwfgf.wwp
286937 lwpf
dir smfbjhw
dir smqh
103844 vmpqmzf.dnf
$ cd smfbjhw
$ ls
186167 crgrnf.dns
dir htczftcn
$ cd htczftcn
$ ls
11324 gssn.rlt
46905 tzrz.hms
$ cd ..
$ cd ..
$ cd smqh
$ ls
dir pffdg
dir zbg
$ cd pffdg
$ ls
3570 bzmwfgf.wwp
3335 fvpd.bct
$ cd ..
$ cd zbg
$ ls
108877 bzmwfgf.wwp
310302 drhsdtcv.rrw
152250 wfvvsg
$ cd ..
$ cd ..
$ cd ..
$ cd lrvncpvz
$ ls
206419 nflgvsgz.tvr
$ cd ..
$ cd nflgvsgz
$ ls
286461 tzrz.hms
$ cd ..
$ cd ..
$ cd ..
$ cd zfjdnbs
$ ls
dir htczftcn
dir nflgvsgz
dir scvzpf
$ cd htczftcn
$ ls
dir jznspqtr
dir tpz
$ cd jznspqtr
$ ls
86738 hqftnv.vwn
$ cd ..
$ cd tpz
$ ls
126506 nflgvsgz.qnh
$ cd ..
$ cd ..
$ cd nflgvsgz
$ ls
248446 gwjgdb.vrr
$ cd ..
$ cd scvzpf
$ ls
dir fpbbjmjf
173634 gbpql
141796 jzncpqb.pgc
69394 rpvnchs
65500 tzrz.hms
$ cd fpbbjmjf
$ ls
224020 hhrjc
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd pffdg
$ ls
101444 clwdmcz.thc
58211 dngdnvv.qdf
dir mnj
dir ncwh
153413 nflgvsgz
dir qtqpw
141829 rrfs.ffn
$ cd mnj
$ ls
298654 qtqpw
$ cd ..
$ cd ncwh
$ ls
133042 bmthlszz.mtr
dir nflgvsgz
dir nrsqtdz
201720 wqhnfz
$ cd nflgvsgz
$ ls
dir bqqmlffw
115991 hsljpqpf
dir htczftcn
$ cd bqqmlffw
$ ls
49001 wltpcszs.bvj
$ cd ..
$ cd htczftcn
$ ls
264620 sfdssh.dnj
260432 vgvzjl
$ cd ..
$ cd ..
$ cd nrsqtdz
$ ls
258978 htczftcn
dir jbc
dir nsqlmlqp
28767 pffdg.blw
172773 tzrz.hms
$ cd jbc
$ ls
dir ztphfs
$ cd ztphfs
$ ls
dir gpps
$ cd gpps
$ ls
74744 bzmwfgf.wwp
$ cd ..
$ cd ..
$ cd ..
$ cd nsqlmlqp
$ ls
dir zvwvdzlv
$ cd zvwvdzlv
$ ls
218727 hsjm.qgm
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd qtqpw
$ ls
171370 sdmhwctq.gzr
$ cd ..
$ cd ..
$ cd qtqpw
$ ls
dir csqvzqdc
131580 jbc.ppb
126635 jbc.sbm
302398 pbjd
74429 vnpj
dir zhmp
$ cd csqvzqdc
$ ls
150923 jbc.grw
dir lthhrqnn
240950 pffdg.qbt
dir rgzqq
$ cd lthhrqnn
$ ls
123194 czl
17546 pffdg
$ cd ..
$ cd rgzqq
$ ls
156566 jbc.hpw
$ cd ..
$ cd ..
$ cd zhmp
$ ls
291659 dngdnvv.qdf
309738 nflgvsgz.wmc
$ cd ..
$ cd ..
$ cd rcnwghg
$ ls
108285 hvhlggsn
308801 sgstjfqq.hln
$ cd ..
$ cd sglgqlp
$ ls
dir gnvnlrz
dir nchq
dir nlrbnwp
dir zpg
$ cd gnvnlrz
$ ls
62071 lgqrm
dir pvt
dir srdqwtcs
$ cd pvt
$ ls
dir fpfddfw
dir jbc
dir jzrb
$ cd fpfddfw
$ ls
257231 rgccj.dwc
$ cd ..
$ cd jbc
$ ls
118252 dsvsmgm.hdm
$ cd ..
$ cd jzrb
$ ls
157243 gcrfg.svt
86860 pblts.jtd
$ cd ..
$ cd ..
$ cd srdqwtcs
$ ls
267482 bzzghfpq.gmh
dir cbd
dir gwqzndrt
288249 hhdmlslr
286213 lwmhd
dir rfvmgch
121131 vbm.rbp
$ cd cbd
$ ls
238535 jpbzwvd.rrw
246606 wgl.gfg
$ cd ..
$ cd gwqzndrt
$ ls
dir twtpbh
262912 vcmv.qcs
$ cd twtpbh
$ ls
245819 dngdnvv.qdf
295823 ghrnmd
308384 pffdg.ptr
231669 sqhnt.grn
$ cd ..
$ cd ..
$ cd rfvmgch
$ ls
306719 cwr.jsm
6449 hqftnv.vwn
$ cd ..
$ cd ..
$ cd ..
$ cd nchq
$ ls
137003 qtqpw
267253 zrgvq
146047 zww.nrr
$ cd ..
$ cd nlrbnwp
$ ls
91151 tzrz.hms
$ cd ..
$ cd zpg
$ ls
68248 bzmwfgf.wwp
$ cd ..
$ cd ..
$ cd wrfmf
$ ls
dir cdlwfjhp
16673 dsctg
304187 jbc
dir lchrdvm
dir nflgvsgz
dir qtqpw
dir rgdc
306410 tzrz.hms
dir zqzzg
$ cd cdlwfjhp
$ ls
dir clshzcrc
dir lplgpg
$ cd clshzcrc
$ ls
191491 tzrz.hms
$ cd ..
$ cd lplgpg
$ ls
169864 cmhrmh.pjp
$ cd ..
$ cd ..
$ cd lchrdvm
$ ls
149068 chwbr.spd
250029 hqftnv.vwn
23399 jbc
69746 nflgvsgz.nmp
dir pldctfcf
dir vngv
251416 zhf.qtz
$ cd pldctfcf
$ ls
297722 bcpwcn
276738 cspls
dir gghvnc
80690 htczftcn
dir pffdg
97610 qfjs.gps
dir tvc
106070 tzrz.hms
$ cd gghvnc
$ ls
93770 dngdnvv.qdf
$ cd ..
$ cd pffdg
$ ls
180916 bzmwfgf.wwp
$ cd ..
$ cd tvc
$ ls
11724 gtgzwsq
$ cd ..
$ cd ..
$ cd vngv
$ ls
92840 qtqpw.gcl
$ cd ..
$ cd ..
$ cd nflgvsgz
$ ls
dir htczftcn
dir lcjqzrwm
54961 lfn.rmz
dir plvbmb
dir vdfwfg
$ cd htczftcn
$ ls
dir gflz
dir mpp
292374 rzm
$ cd gflz
$ ls
dir qpdn
$ cd qpdn
$ ls
258037 ddqb.jhd
$ cd ..
$ cd ..
$ cd mpp
$ ls
248628 pffdg.spt
$ cd ..
$ cd ..
$ cd lcjqzrwm
$ ls
249155 mbz.gsq
291857 nngm.nft
100136 zwvwlg.hrs
$ cd ..
$ cd plvbmb
$ ls
dir nnrnwp
163552 pffdg
$ cd nnrnwp
$ ls
289041 bzmwfgf.wwp
29165 nvcwzfpr
$ cd ..
$ cd ..
$ cd vdfwfg
$ ls
264391 hqftnv.vwn
309071 htczftcn.mrd
dir wtqrrvvr
$ cd wtqrrvvr
$ ls
230331 swhpd
$ cd ..
$ cd ..
$ cd ..
$ cd qtqpw
$ ls
292434 hbjlsrw
$ cd ..
$ cd rgdc
$ ls
dir hqldlpg
$ cd hqldlpg
$ ls
188809 rvjwsmnz.hqt
$ cd ..
$ cd ..
$ cd zqzzg
$ ls
250923 qtqpw.zrb
$ cd ..
$ cd ..
$ cd ..
$ cd qcqg
$ ls
309875 tzrz.hms
$ cd ..
$ cd qtqpw
$ ls
dir rcnp
$ cd rcnp
$ ls
131725 bzmwfgf.wwp
46663 chwfd
$ cd ..
$ cd ..
$ cd qzcdscbp
$ ls
dir mtqt
$ cd mtqt
$ ls
27367 llbt.pth
dir mcrddwgp
$ cd mcrddwgp
$ ls
77221 bzmwfgf.wwp
37941 lrwlhz
dir tcmrv
85568 tzrz.hms
$ cd tcmrv
$ ls
dir hprvr
$ cd hprvr
$ ls
59831 qbchdjw.gjg
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd rfgvg
$ ls
dir qlg
$ cd qlg
$ ls
142825 dngdnvv.qdf
$ cd ..
$ cd ..
$ cd rzb
$ ls
250575 dngdnvv.qdf
dir jbc
dir lbg
187509 plblzt.zzz
dir qwjlvqdp
237529 rrrqcl.pvt
dir rsjg
$ cd jbc
$ ls
253304 lpdndfn
$ cd ..
$ cd lbg
$ ls
dir fml
$ cd fml
$ ls
106624 shm.fgh
$ cd ..
$ cd ..
$ cd qwjlvqdp
$ ls
dir htczftcn
$ cd htczftcn
$ ls
dir gnnzlzwd
272143 jbc.ldg
dir sztdtpjt
$ cd gnnzlzwd
$ ls
218355 tzrz.hms
$ cd ..
$ cd sztdtpjt
$ ls
53466 tzrz.hms
$ cd ..
$ cd ..
$ cd ..
$ cd rsjg
$ ls
101889 cct.sfg'''

        s = advent2022.Day07.Solution(text.splitlines())

        s.buildTree()
        s.calculateTotalSize(s.root)
        print('\n')
        
        minSize = s.findPart2()
        print('Min size: ' + str(minSize))
        self.assertEqual(minSize, 5883165)

    def test_day01_part1(self):
        text = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
        s = advent2022.Day01.Solution(text.splitlines())
        s.parseInput()
        result = s.findMax()
        print('max is ' + str(result))

        self.assertEqual(24000, result)

    def test_day01_part1_puzzle(self):
        text = '''4601
1583
2995
5319
3352
1722
4331
5840
3339
5341
3415
1297
1610
2703

5928
1266
6405
4354
2815
1621
3545
1733
2162
1155
3674
4055
4262
2115

25873
16103
17042

6479
1521
6902
6331
6146
1591
2063
2149
1463
1865
2598
6893
3617

1431
8935
8134
8885
8698
8884
7982
3617
7079

34031
8383

3697
1199
3703
1322
5679
1627
5910
1092
6445
2371
3672
2281
2710
5111

17480

58355

3711
2406
2101
1406
5376
2149
4608
6768
6322
3792
4249
2342
2014

6197
6908
8484
3901
3001
7880
5165
2536

3964
4229
4898
4544
3535
6329
1573
4988
1424

57606

16325

6038
11538
13026
12734
6077

4696
3914
2375
1188
1247
1594
1843
5297
6053
1114
3179
5968
1430
4268
2514

6684
2321
3946
1746
7583
10379
3696
10110

5834
5944
9336
9638
3373
4279
9942

7208
7801
3771
8183
1824
8217
1545
3041
7369
5980

8368
6180
3100
4801
4430
6758
3023
3394

2545
4992
3347
5830
3764
3237
2431
3406
1408
5601
6548
4625

32334

1112
5471
10983
8298
4342
4221
7807

5733
2012
5928
3503
2785
4867
1515
4819
3569
3353
5997
4921
5498
3234
5588

11040
5547
12070
2168
7603
7245
4966

13027
12518
15381
3251
14935

15858
29295

2476
4289
10350
3953
10089
6953
5555
3007

61732

5567
4895
6095
4880
2945
6022
2129
5010
4100
3554
3410
1820

9902
33605

15331
15615
5062
15073

5940
2252
1233
2582
3624
2754
2304
3189
4060
3862
5164
1487
2776
1807
3385

6798
2385
3755
10299
11500
6478
1911

1469
9309
1785
17145

3363
3210
3285
4491
5992
2927
4098
2133
3191
2810
4694

31006
1582

4356
6146
2051
6503
9487
9244
4808
7761
7108

1771
6062
7135
5575
3278
1221
2547
7266
5444
7395

10634
1196

1361

2810
3106
8654
9455
3778
4219
8882
9387
5128

7114
1441
6146
4752
2388
6420
7350
1624
6050
5469
6751

5570
4674

2074
3476
4064
9446
2889
4871
6298
2970
8588

3482
8492
2226
4951
6733
5463
3183
4807
4806

6974
10251
4637
9558
5153
4665

6860
6949
1524
4201
4397
2278
4909
1353
2074
1920
7439
1040

4135
1411
5536
8004
3090
1036
6613
6353
6810

3932
4743
1615
3201
3791
6357
2511
3440
2290
4741
2844
3121
3641
3497

4549
5142
4438
2945
4576
4871
4795
6007
4884
1031
2111
4388
4705
5725
3425

45444

6688
9460
2727
6989
6789
12460

7310
5910
7822
7627
7600
4793
3152
5747
5197
8006

23983
33879

1020
4783
5117
3628
3065
6131
5543
1576
1159
3721
3182
1409
2738
5084

42750

8509
4370
1042
5664

59445

1589
5133
6413
6578
3301
8256
7749
4321
8190
5025

27739
18609

5447
4022
4069
1437
2811
6929
2754
1108
7390
3995
3480
3225

4240
6959
3289
8063
4751
4896
4611
6256
1105
1334
7598

27831

1821
5333
7853
6574
7985
3972
2306
1875
1857
6386

12780
2513
22939

9625
3785
8050
7432
11772
10914

1387
3439
4644
3880
1878
3911
5329
1480
5779
2083
3886
5525
3930
4813
2570

15763
2839
14258
1460

6193
3397
3222
3262
3735
2406
5588
2068
2862
3271
1401
3957
5690
4632

15070
5164
8902
9580
4271

4494
5665
7242
7687
7031
6135
2670
3315
6146
8085

2625
24285

4414
5985
2681
7036
6486
2501
4408
8582
5150
4295

1082
1497
5638
4643
1413
5969
1515
4016
4856
3287
3122
2948
3711
5031
4692

6445
2261
2132
3517
2461
2767
2071
2176
6357
1304
6034
1346

1318
4719
2054
1433
6514
3729
4329
1026
1502
2611
1363
6379
3617

1885
7519
2849
5167
3136
4819
8018
4110
2666
6098
4943

6575
1624
6004
4178
7453
5979
6736
3883
7109
1271
1175

9494
12633
11576
3547

4653
6777
4497
2246
4666
4675
4440
7227
3808
2425
6014
7305

2538
6155
4321
6239
6279
1445
5592

4920
5435
1392
4122
10513
6359
1574
7222

9013
2150
8377
8884
4108
5427
1605
6907

7861
10554
1210
1346
5296
4419
9147

1858
2956
2070
10271
5810
2632
9429
3941

4306
4972
6216
6345
3971
3920
6295
3552
1399
5425
5218
4512
3376
4460

4107
4484
5148
5456
7902
2185
3439
7199
9514

11030
12096

2886
1561
14057
7480
12186

8600
4085
11755
4564
1697
6345
10176

2538
10138
8328
10621
13322
13907

5450
3403
5776
5967
3873
2761
5992
2251
2278
4673
3442
2720
2556
4848
5967

2806
8228
9047
10630
4367
4917
4084
7893

2842
18343
1497
19962

3985
10986
1431
1569
8053
8987
6474

5733
2237
6183
1642
1005
4389
1889
2385
2470
6338
2200
3399
3659
4092

6579
5872
4229
1081
2254
1229
5218
4267
6906
2818
1084
3655
2294

1882
5005
3805
2088
6809
4982
1935
6789
1961
1842
5988
2859
3965

2313
1021
5090
1309
5110
3142
4102
2919
6010
3079
5786
3701
2659
5728

4251
1899
4119
8941
6677
2161
2119
2772
3122

7821
6113
5150
3486
2072
4089
2820
3161
7589
1787
5988

10582
8240
1934
1504
9070
1186
7766
1066

6700
6181
3238
1940
1229
3688
1375
5873
2328
6384
7446
7246

5542
6771
1964
4532
3011
2300
1451
6726
4595
2926
5237
5020
6129

15008
4409
6769
2211

11825
8947
17411
2893

8460
11664
2304
6865
2132
9174

15540
16925
12015
7621

1439
11886
3028

4604
1057
5342
4723
7773
3373
7488
8028
3246
6355
1939

2921
4447
3472
5175
5909
5936
5263
3993
1589
3906
4865
3156
2010

10089

5964
7650
4692
1537
3281
3162
1064
4567
3910
2229
3566

15533
17311
11818
6179

4583
4577
3573
1379
3761
1048
4799
4275
3515
5637
5435
3801
5933
1926

11841
16030
3213

4307
7300
1237
5513
6799
2402
2554

67023

1573
6798
3002
7536
2373
5994
10122

1149
1836
7129
6621
7432
2468
4028
6560
5127
3781
7035
5845

13729
10212
10942
10087
10080
6493

6850
5969
3370
5400
6433
4762
5702
6193
1836
1507
2637
3051
1394

5465
10565
4923
1671
9789
9150
6466
8013

31283

2001
6032
6765
3896
7593
3175
3447
1718

6062
7630
6302
4448
1014
4756
4696
4069
5663
2181
6153

9228
1871
11739
10894

7435
6290
3249
9358
9196
8951
5023
4910
9686

3823
4247
7159

4630
3352
7700
7752
3343
4577
2448
10326

10002
28943

2592
4430
4077
2126
4628
6466
5919
7019
2667
2573
7038
3153

2837
12151
9774
1574
3046
13079

6949

5306
7432
4274
6835
7057
5695
4727
5581
6516
3903
3138

4083
4247
1806
2753
3612
3509
5498
2160
5814
1502
5760
4663
1354
1592

59040

3738
7624
4539
8649
9418
5495
1178
8389

4458
5283
2572
3530
6228
4711
2621
2131
6363
5611
3236
2314
2547
1905

3744
1413
2997

2214
4673
4481
5827
3752
5489
5301
7568
6869
2928
2900

11668
7579
2324
7245
14362

1191
5622
2764
3241
3690
3627
2637
4043
3012
2773
4276
1127
3649

5327
6535
4821
5531
3037
4700
6287
6476
2266
7550

3054
5023
1296
4394
5649
1822
6609
7038
5836
6571
6918

9473
5377
8449
4839
3118
7861

8784
3880
5133
6131
2114
5196
10405
1040

5003
5888
6058
6910
3155
3278
1159
3863
4565
1181
2716
6431
3014

7633
4984
1297
4524
5183
3717
12038

5908
7784
11211
7635
2060
5502
9179

6537
6895
3455
4799
5557
3497
4467
1694
5227
1663
2377
3538
4529

9371
2421
9789
7373
6459
6405
7775
8218

2077
8589
3417
7811
10255
4325
7168

5963
2806
3512
2369
5721
3852
3022
3764
6152
1158
6460
4694
1909
2655

7789
3030
3621
6269
3149
6405
2288
3512
5674
1301

6120
2629
6348
7105
3459
6678
5903
4519
3074
2086
3927

2924
12290
1873
5613
3098
8641

24464
37206

7180
13271
4832
10691
9084

4915
1440
1841
1476
7124
1692
7480
4583
1896
3475
5424

6864
3187
4680
5159
4314
3148
1060
7290
2080
8308

2412
16405
15203
5606
9411

13201
6242
11906
15782
12558

5319
7968
6732
9702

7203
3571
7241
8764
3466
6032
6608
6898
7189
2749

6184
7590
4976
4289
8553
8238
5844
8314

3264
2924
2586
1234
3126
5269
6147
6029
2384
6440
6161
1708
2928
2336

24565
31964

11118
10621
1430
3312
1135
6740
9456

16874
4385
8675
4237

1537
4313
5552
2195
3530
2433
3056
3693
1151
4297
2017
4917
3823
3388
1580

5795
2642
3822
1824
2366
3800
2020
4065
2758
2677
3951
5175
4433
1199
3212

4183
2822
6355
4427
6384
2931
4892
3148
5802
3885
4892
5233
4269
4286

3711
5430
6115
5561
5066
2796
3886
1960
6083
4657

11662
12901
6891
3897

1086
4333
1477
1046
5670
3996
1909
3544
5143
1387
6319
3084
3136
6084

36111
14790

6552
8491

6636
9718
15736
1619

9531
7507
7311
5991
6901
12139
10580

10956
7878
9100
11884
2906
10388

7767
4040
5872
1060
2299
1008
3597
2749
5025

1550

5364
7108
8661
8894
9240
10008
4243

46695

4195
2850
2978
4995
2944
5773
3669
3662
4471
6343
4258
1252
6408
5995

9482
11898
9022
8167
9232

2647
1990
2948
5314
2341
3828
2513
2091
4173

9640
2690
8774
11619
11201
2429
7216

3433
5914
5223
4879
1349
4692
2906
3761
4416
4813
2751
4474
2057
1675

9803
8986
3617
2175
1412
8370

7671
6448
6759
1857

25790
14495

1872
6441
4585
4053
4142
5844
2089
3387
2660
5890
6499
3769
2710

23432
16915

1351
2656
6557
1149
5054
1681
6871
2643
3158
1617
4087
6498
4993

5494
10055
2730
5800
2923
8037
3448
1527

5803
18165
21951

4766
3809
4678
3184
9687
7825
7222
6638
2016

1801
1717
4955
6088
1848
4033
7023
3551
5970
1415
7027
7411

25450
11523
22548

1566
4742
3947
2708
2019
3479
4735
6002
7042
1828
7071
1535

14218
5232
10228
3340
7975

8837
3510
10363
11854
2821
7627
10186

1102
3749
1436
1561
3098
3849
3726
2041
1100
1532
5473
4643
5922
4739
1216

4408
7369
1369
4742
7109
4368
3468
2777
3296
6999
5777
5019

3750
12190

15694
12690
14834
15532
1955

8702
1209
3012
3074
8390
6779
6117
2544
3900
6374

4126
5772
7149
3949
2371
2374
2469
7839
7898
2871
5808

1108

9610
4374
10275
2595
9413
8906
6402
1551

6560
8632
5064
2152
3443
4229

13104
24831
17968

4648
5332
4866
1048
4089
4710
1406
2544
5319
4685
4622
6080
5899
3266

5694
12879
4015
16066
1600

11186
31873

3871
6382
5076
3606
4283
7913
11124

9959
14807
17825
5880

3914
14183

8104
8322
10254
3957
1410
9402
2012

1130
4640
5738
3860
1510
3067
5021
5321
2820
1269
3433
5216
5585
1344

5975
9879
4969
9796
1404
6772
3240
1954

12512
13741
6425
13234
10597
12414

2031
2255
3306
1831
1601
1959
4452
5054
4967
5392
4040
4989
4385
5838
5043

3165
10185
10580
1626
5436
9644
10842

5139
8090
1045
5867
5987
8488
2409

1045
2843
3543
3224
2855
3318
4192
4600
5773
4074
4705
4716
1798
5274
2443

6325
7878
4932
7543
8073
2113
5481
8138
2151
1296

6007
2506
2346
3631
1526
4875
3099
5253
6281
2057
3209
2622
2930
4926

2901
4561
2361
4474
8508
6515
5024
2201
4402
6922

4219
24714
17196

38164

1900
5727
3935
5498
6165
4621
3347
4387
5982
4213
1742
1302
2452
3923

9558
7131
15662
9101
13730

6474
2222
6539
3747
5995
5573
6288
4684
5121
2226
1722
1117
1020

3565
3489

18395
20407

57158

19992

3636
4392
4584
5421
3159
5817
2303
1013
1758
1802
4630
4261
1524
1639

4652
1967
4765
4946
3023
2732
2749
5258
5935
6428
3053
6328
2389
5681

5450
1993
2824
3596
2658
8545
6577
3024
4001
1780

7902
6187

1349
6028
3307
1964
5116
2308
6108
4286
1689
3324
3728
4946
4267
3801
3806

14183
29320

32460
25012

3317
5545
7302
4936
7934
6094
7971
2497
8130
3752

4195
2147
7770
4214
4737
7962
5942
4478
3816
7508
6693

26013
8614
19828

1144
2361
4371
4246
3442
1693
5137
5806
2434
1413
3135
4028
4757
6005

2351
4927
3004
3384
1545
2172
3407
4120
3954
1806
2342
5847
5228
1005

11490
7855
9775
10577
3232
5211

8316
2984
13490
15716
7433

11288
14551
10056
14839
7241

4573
2731
3358
4850
6352
5419
1021
6611
6489
3794
6089'''
        
        s = advent2022.Day01.Solution(text.splitlines())
        s.parseInput()
        result = s.findMax()

        print('\n')
        print('max is ' + str(result))

        self.assertEqual(68923, result)

    def test_day01_part2(self):
        text = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
        
        s = advent2022.Day01.Solution(text.splitlines())
        s.parseInput()
        result = s.sumTop3()

        print('\n')
        print('sum of top 3 is ' + str(result))

        self.assertEqual(45000, result)

    def test_day01_part2_puzzle(self):
        text = '''4601
1583
2995
5319
3352
1722
4331
5840
3339
5341
3415
1297
1610
2703

5928
1266
6405
4354
2815
1621
3545
1733
2162
1155
3674
4055
4262
2115

25873
16103
17042

6479
1521
6902
6331
6146
1591
2063
2149
1463
1865
2598
6893
3617

1431
8935
8134
8885
8698
8884
7982
3617
7079

34031
8383

3697
1199
3703
1322
5679
1627
5910
1092
6445
2371
3672
2281
2710
5111

17480

58355

3711
2406
2101
1406
5376
2149
4608
6768
6322
3792
4249
2342
2014

6197
6908
8484
3901
3001
7880
5165
2536

3964
4229
4898
4544
3535
6329
1573
4988
1424

57606

16325

6038
11538
13026
12734
6077

4696
3914
2375
1188
1247
1594
1843
5297
6053
1114
3179
5968
1430
4268
2514

6684
2321
3946
1746
7583
10379
3696
10110

5834
5944
9336
9638
3373
4279
9942

7208
7801
3771
8183
1824
8217
1545
3041
7369
5980

8368
6180
3100
4801
4430
6758
3023
3394

2545
4992
3347
5830
3764
3237
2431
3406
1408
5601
6548
4625

32334

1112
5471
10983
8298
4342
4221
7807

5733
2012
5928
3503
2785
4867
1515
4819
3569
3353
5997
4921
5498
3234
5588

11040
5547
12070
2168
7603
7245
4966

13027
12518
15381
3251
14935

15858
29295

2476
4289
10350
3953
10089
6953
5555
3007

61732

5567
4895
6095
4880
2945
6022
2129
5010
4100
3554
3410
1820

9902
33605

15331
15615
5062
15073

5940
2252
1233
2582
3624
2754
2304
3189
4060
3862
5164
1487
2776
1807
3385

6798
2385
3755
10299
11500
6478
1911

1469
9309
1785
17145

3363
3210
3285
4491
5992
2927
4098
2133
3191
2810
4694

31006
1582

4356
6146
2051
6503
9487
9244
4808
7761
7108

1771
6062
7135
5575
3278
1221
2547
7266
5444
7395

10634
1196

1361

2810
3106
8654
9455
3778
4219
8882
9387
5128

7114
1441
6146
4752
2388
6420
7350
1624
6050
5469
6751

5570
4674

2074
3476
4064
9446
2889
4871
6298
2970
8588

3482
8492
2226
4951
6733
5463
3183
4807
4806

6974
10251
4637
9558
5153
4665

6860
6949
1524
4201
4397
2278
4909
1353
2074
1920
7439
1040

4135
1411
5536
8004
3090
1036
6613
6353
6810

3932
4743
1615
3201
3791
6357
2511
3440
2290
4741
2844
3121
3641
3497

4549
5142
4438
2945
4576
4871
4795
6007
4884
1031
2111
4388
4705
5725
3425

45444

6688
9460
2727
6989
6789
12460

7310
5910
7822
7627
7600
4793
3152
5747
5197
8006

23983
33879

1020
4783
5117
3628
3065
6131
5543
1576
1159
3721
3182
1409
2738
5084

42750

8509
4370
1042
5664

59445

1589
5133
6413
6578
3301
8256
7749
4321
8190
5025

27739
18609

5447
4022
4069
1437
2811
6929
2754
1108
7390
3995
3480
3225

4240
6959
3289
8063
4751
4896
4611
6256
1105
1334
7598

27831

1821
5333
7853
6574
7985
3972
2306
1875
1857
6386

12780
2513
22939

9625
3785
8050
7432
11772
10914

1387
3439
4644
3880
1878
3911
5329
1480
5779
2083
3886
5525
3930
4813
2570

15763
2839
14258
1460

6193
3397
3222
3262
3735
2406
5588
2068
2862
3271
1401
3957
5690
4632

15070
5164
8902
9580
4271

4494
5665
7242
7687
7031
6135
2670
3315
6146
8085

2625
24285

4414
5985
2681
7036
6486
2501
4408
8582
5150
4295

1082
1497
5638
4643
1413
5969
1515
4016
4856
3287
3122
2948
3711
5031
4692

6445
2261
2132
3517
2461
2767
2071
2176
6357
1304
6034
1346

1318
4719
2054
1433
6514
3729
4329
1026
1502
2611
1363
6379
3617

1885
7519
2849
5167
3136
4819
8018
4110
2666
6098
4943

6575
1624
6004
4178
7453
5979
6736
3883
7109
1271
1175

9494
12633
11576
3547

4653
6777
4497
2246
4666
4675
4440
7227
3808
2425
6014
7305

2538
6155
4321
6239
6279
1445
5592

4920
5435
1392
4122
10513
6359
1574
7222

9013
2150
8377
8884
4108
5427
1605
6907

7861
10554
1210
1346
5296
4419
9147

1858
2956
2070
10271
5810
2632
9429
3941

4306
4972
6216
6345
3971
3920
6295
3552
1399
5425
5218
4512
3376
4460

4107
4484
5148
5456
7902
2185
3439
7199
9514

11030
12096

2886
1561
14057
7480
12186

8600
4085
11755
4564
1697
6345
10176

2538
10138
8328
10621
13322
13907

5450
3403
5776
5967
3873
2761
5992
2251
2278
4673
3442
2720
2556
4848
5967

2806
8228
9047
10630
4367
4917
4084
7893

2842
18343
1497
19962

3985
10986
1431
1569
8053
8987
6474

5733
2237
6183
1642
1005
4389
1889
2385
2470
6338
2200
3399
3659
4092

6579
5872
4229
1081
2254
1229
5218
4267
6906
2818
1084
3655
2294

1882
5005
3805
2088
6809
4982
1935
6789
1961
1842
5988
2859
3965

2313
1021
5090
1309
5110
3142
4102
2919
6010
3079
5786
3701
2659
5728

4251
1899
4119
8941
6677
2161
2119
2772
3122

7821
6113
5150
3486
2072
4089
2820
3161
7589
1787
5988

10582
8240
1934
1504
9070
1186
7766
1066

6700
6181
3238
1940
1229
3688
1375
5873
2328
6384
7446
7246

5542
6771
1964
4532
3011
2300
1451
6726
4595
2926
5237
5020
6129

15008
4409
6769
2211

11825
8947
17411
2893

8460
11664
2304
6865
2132
9174

15540
16925
12015
7621

1439
11886
3028

4604
1057
5342
4723
7773
3373
7488
8028
3246
6355
1939

2921
4447
3472
5175
5909
5936
5263
3993
1589
3906
4865
3156
2010

10089

5964
7650
4692
1537
3281
3162
1064
4567
3910
2229
3566

15533
17311
11818
6179

4583
4577
3573
1379
3761
1048
4799
4275
3515
5637
5435
3801
5933
1926

11841
16030
3213

4307
7300
1237
5513
6799
2402
2554

67023

1573
6798
3002
7536
2373
5994
10122

1149
1836
7129
6621
7432
2468
4028
6560
5127
3781
7035
5845

13729
10212
10942
10087
10080
6493

6850
5969
3370
5400
6433
4762
5702
6193
1836
1507
2637
3051
1394

5465
10565
4923
1671
9789
9150
6466
8013

31283

2001
6032
6765
3896
7593
3175
3447
1718

6062
7630
6302
4448
1014
4756
4696
4069
5663
2181
6153

9228
1871
11739
10894

7435
6290
3249
9358
9196
8951
5023
4910
9686

3823
4247
7159

4630
3352
7700
7752
3343
4577
2448
10326

10002
28943

2592
4430
4077
2126
4628
6466
5919
7019
2667
2573
7038
3153

2837
12151
9774
1574
3046
13079

6949

5306
7432
4274
6835
7057
5695
4727
5581
6516
3903
3138

4083
4247
1806
2753
3612
3509
5498
2160
5814
1502
5760
4663
1354
1592

59040

3738
7624
4539
8649
9418
5495
1178
8389

4458
5283
2572
3530
6228
4711
2621
2131
6363
5611
3236
2314
2547
1905

3744
1413
2997

2214
4673
4481
5827
3752
5489
5301
7568
6869
2928
2900

11668
7579
2324
7245
14362

1191
5622
2764
3241
3690
3627
2637
4043
3012
2773
4276
1127
3649

5327
6535
4821
5531
3037
4700
6287
6476
2266
7550

3054
5023
1296
4394
5649
1822
6609
7038
5836
6571
6918

9473
5377
8449
4839
3118
7861

8784
3880
5133
6131
2114
5196
10405
1040

5003
5888
6058
6910
3155
3278
1159
3863
4565
1181
2716
6431
3014

7633
4984
1297
4524
5183
3717
12038

5908
7784
11211
7635
2060
5502
9179

6537
6895
3455
4799
5557
3497
4467
1694
5227
1663
2377
3538
4529

9371
2421
9789
7373
6459
6405
7775
8218

2077
8589
3417
7811
10255
4325
7168

5963
2806
3512
2369
5721
3852
3022
3764
6152
1158
6460
4694
1909
2655

7789
3030
3621
6269
3149
6405
2288
3512
5674
1301

6120
2629
6348
7105
3459
6678
5903
4519
3074
2086
3927

2924
12290
1873
5613
3098
8641

24464
37206

7180
13271
4832
10691
9084

4915
1440
1841
1476
7124
1692
7480
4583
1896
3475
5424

6864
3187
4680
5159
4314
3148
1060
7290
2080
8308

2412
16405
15203
5606
9411

13201
6242
11906
15782
12558

5319
7968
6732
9702

7203
3571
7241
8764
3466
6032
6608
6898
7189
2749

6184
7590
4976
4289
8553
8238
5844
8314

3264
2924
2586
1234
3126
5269
6147
6029
2384
6440
6161
1708
2928
2336

24565
31964

11118
10621
1430
3312
1135
6740
9456

16874
4385
8675
4237

1537
4313
5552
2195
3530
2433
3056
3693
1151
4297
2017
4917
3823
3388
1580

5795
2642
3822
1824
2366
3800
2020
4065
2758
2677
3951
5175
4433
1199
3212

4183
2822
6355
4427
6384
2931
4892
3148
5802
3885
4892
5233
4269
4286

3711
5430
6115
5561
5066
2796
3886
1960
6083
4657

11662
12901
6891
3897

1086
4333
1477
1046
5670
3996
1909
3544
5143
1387
6319
3084
3136
6084

36111
14790

6552
8491

6636
9718
15736
1619

9531
7507
7311
5991
6901
12139
10580

10956
7878
9100
11884
2906
10388

7767
4040
5872
1060
2299
1008
3597
2749
5025

1550

5364
7108
8661
8894
9240
10008
4243

46695

4195
2850
2978
4995
2944
5773
3669
3662
4471
6343
4258
1252
6408
5995

9482
11898
9022
8167
9232

2647
1990
2948
5314
2341
3828
2513
2091
4173

9640
2690
8774
11619
11201
2429
7216

3433
5914
5223
4879
1349
4692
2906
3761
4416
4813
2751
4474
2057
1675

9803
8986
3617
2175
1412
8370

7671
6448
6759
1857

25790
14495

1872
6441
4585
4053
4142
5844
2089
3387
2660
5890
6499
3769
2710

23432
16915

1351
2656
6557
1149
5054
1681
6871
2643
3158
1617
4087
6498
4993

5494
10055
2730
5800
2923
8037
3448
1527

5803
18165
21951

4766
3809
4678
3184
9687
7825
7222
6638
2016

1801
1717
4955
6088
1848
4033
7023
3551
5970
1415
7027
7411

25450
11523
22548

1566
4742
3947
2708
2019
3479
4735
6002
7042
1828
7071
1535

14218
5232
10228
3340
7975

8837
3510
10363
11854
2821
7627
10186

1102
3749
1436
1561
3098
3849
3726
2041
1100
1532
5473
4643
5922
4739
1216

4408
7369
1369
4742
7109
4368
3468
2777
3296
6999
5777
5019

3750
12190

15694
12690
14834
15532
1955

8702
1209
3012
3074
8390
6779
6117
2544
3900
6374

4126
5772
7149
3949
2371
2374
2469
7839
7898
2871
5808

1108

9610
4374
10275
2595
9413
8906
6402
1551

6560
8632
5064
2152
3443
4229

13104
24831
17968

4648
5332
4866
1048
4089
4710
1406
2544
5319
4685
4622
6080
5899
3266

5694
12879
4015
16066
1600

11186
31873

3871
6382
5076
3606
4283
7913
11124

9959
14807
17825
5880

3914
14183

8104
8322
10254
3957
1410
9402
2012

1130
4640
5738
3860
1510
3067
5021
5321
2820
1269
3433
5216
5585
1344

5975
9879
4969
9796
1404
6772
3240
1954

12512
13741
6425
13234
10597
12414

2031
2255
3306
1831
1601
1959
4452
5054
4967
5392
4040
4989
4385
5838
5043

3165
10185
10580
1626
5436
9644
10842

5139
8090
1045
5867
5987
8488
2409

1045
2843
3543
3224
2855
3318
4192
4600
5773
4074
4705
4716
1798
5274
2443

6325
7878
4932
7543
8073
2113
5481
8138
2151
1296

6007
2506
2346
3631
1526
4875
3099
5253
6281
2057
3209
2622
2930
4926

2901
4561
2361
4474
8508
6515
5024
2201
4402
6922

4219
24714
17196

38164

1900
5727
3935
5498
6165
4621
3347
4387
5982
4213
1742
1302
2452
3923

9558
7131
15662
9101
13730

6474
2222
6539
3747
5995
5573
6288
4684
5121
2226
1722
1117
1020

3565
3489

18395
20407

57158

19992

3636
4392
4584
5421
3159
5817
2303
1013
1758
1802
4630
4261
1524
1639

4652
1967
4765
4946
3023
2732
2749
5258
5935
6428
3053
6328
2389
5681

5450
1993
2824
3596
2658
8545
6577
3024
4001
1780

7902
6187

1349
6028
3307
1964
5116
2308
6108
4286
1689
3324
3728
4946
4267
3801
3806

14183
29320

32460
25012

3317
5545
7302
4936
7934
6094
7971
2497
8130
3752

4195
2147
7770
4214
4737
7962
5942
4478
3816
7508
6693

26013
8614
19828

1144
2361
4371
4246
3442
1693
5137
5806
2434
1413
3135
4028
4757
6005

2351
4927
3004
3384
1545
2172
3407
4120
3954
1806
2342
5847
5228
1005

11490
7855
9775
10577
3232
5211

8316
2984
13490
15716
7433

11288
14551
10056
14839
7241

4573
2731
3358
4850
6352
5419
1021
6611
6489
3794
6089'''
       
        s = advent2022.Day01.Solution(text.splitlines())
        s.parseInput()
        result = s.sumTop3()

        print('\n')
        print('sum of top 3 is ' + str(result))

    def test_day02_part1(self):
        text = '''A Y
B X
C Z'''
        s = advent2022.Day02.Solution(text.splitlines())
        score = s.scorePart1()
        print('\n')        
        print('score is ' + str(score))

        self.assertEqual(15, score)

    def test_day02_part1_puzzle(self):
        text = '''A X
B Y
B Y
C X
B X
C Z
C Z
A Z
A Z
B Y
C Z
A Z
C Z
C X
B Z
C Z
C Z
C Z
B Y
C Z
C Z
C Z
A Z
A Y
B Z
B Z
A Y
B X
C Z
C Z
A Z
A Z
C Z
A Y
A X
A Z
A Z
B X
B Z
B X
A Z
B X
B Z
B Z
C Z
A Z
A Z
A Z
C Z
B Z
A Z
A Y
A Y
B Y
B Y
B Z
A Z
B Z
A Z
B Z
C Z
B Y
A Z
B Y
A Z
A Z
A Z
C Z
A Y
A Z
C Z
C Z
A Z
A X
B Y
C Z
A Z
A Z
C X
C Z
B X
C X
B X
A Z
C Z
C Z
A Y
A Z
B X
C X
A Z
A Z
C Z
C Z
B Y
C Z
A Z
A Z
A Y
B X
B Y
A Z
C Z
A Z
A Z
A Z
C X
C Y
C Z
B X
B X
B X
A Z
A X
C Z
A Z
B Y
B X
A Y
B X
A Z
C Z
C Z
A X
A Z
C Z
B Z
B X
A Z
C Z
C Z
C X
C Z
C Z
C Z
A Y
B X
A Y
A Z
B Z
B Z
C Z
B Z
B Z
B X
A Z
C Z
A Z
A Y
C Z
A Z
C X
A Z
A Z
A Y
A Y
A Z
C Z
B Y
A X
A Z
A Y
C Z
A Z
B X
A Z
B Y
A X
C X
B X
A Y
A Z
B Z
A Z
A Z
B X
A X
C Z
B X
B Y
A Z
B X
C Z
A Z
C Z
B X
A Z
A Y
A Z
A Z
B X
B X
B Z
A Z
B Y
C Z
B Z
C Z
C Z
B X
B X
A Z
C Z
C Z
A X
B X
B X
A Y
C Z
A Z
A Y
B X
A Z
A Z
B X
A Z
C Z
B X
B Z
B Y
B X
A Y
C Z
C Z
C Z
A X
C Z
A Z
C Z
C Y
C Z
C Z
C Z
B X
A Z
B X
B Z
A Z
C Z
B Y
B Y
B Z
C Z
C Z
C Z
B Z
B Y
A Z
B X
B Z
C Z
A Z
B Y
B Y
A X
C Z
B Y
A Y
B Y
B X
B Y
B Y
A Y
B Y
C X
A Y
A Y
C Z
A Z
A Y
C Z
A Z
A Z
C Z
C Z
C Z
B X
B Y
A Y
A Y
B Z
A Z
B Y
B X
B Y
A Y
A Y
A Z
B Z
C Z
C Z
C Z
A Z
C Z
A Z
A Z
A Z
A Z
C Z
B Y
C Z
B X
C Z
A X
A Z
B X
C Y
C X
A X
A X
A Z
A Z
B X
A Y
B Z
A Z
B Z
A Z
C Z
C X
C Z
C Z
C X
C Z
C Z
C X
C Z
B Z
A Z
B Y
A Z
C Z
B X
C Z
B Z
B Y
A Z
B Y
A Y
B X
B Z
B Z
A Z
B Z
C Z
C Z
A Y
A Z
A X
A Y
C Z
B X
A Z
C X
A Z
A Z
A Z
A Z
C Y
B Y
B Y
A X
C Z
A X
A Z
A Y
C X
A Y
A Y
A Z
C X
C Z
B Z
B X
A Z
C Z
C Z
B Z
B X
C Z
C Z
A Y
B Z
A X
B Y
A Z
C X
B X
C Z
B Y
A X
A Z
B Y
A Y
A Z
B Z
A Y
B Y
A Z
B Y
B X
B Z
A Z
B Y
B Z
A Y
A Z
C Z
B X
C Z
B X
C Z
B Z
C Z
C Z
B Z
A Y
A Y
C Z
B Z
A Z
A X
C Z
A Z
C Z
A Z
A X
A Z
A Z
A Y
B Z
B X
C X
B Y
C Z
B X
B Z
B X
A Z
A Z
A Z
B Z
B Y
A Z
B Y
C Z
B Z
A Z
A Y
C Z
A Z
B Y
B X
B Y
B X
C Z
C Y
A Z
C Z
C Z
A Z
C X
B Z
A Y
B Y
B Y
B Y
C Z
B Z
A Z
B Y
A Z
A Z
C Z
B Y
B Y
A X
A Z
A Z
C Z
A Z
C Z
C Z
A X
B Z
A Z
A Z
C Z
C Z
B Y
B Y
A Z
A Y
A Z
B Y
B Z
A Y
B Z
A Z
A Z
A Y
C Z
A Y
C Z
B X
A Z
A Z
C Z
A Y
C Z
A Z
A Y
A Y
C Z
A Z
A Y
B X
A Y
B X
A Z
A Z
A Y
B Y
B Y
B X
C Z
C Z
B Y
B X
C Z
B Y
C Z
B Y
B X
C Z
A Y
B Z
C X
A Y
C Z
C Z
C X
A Y
A Z
B X
C Z
A Z
B Y
C Z
B X
B Z
C Z
C Z
C Z
A Z
B X
C Z
A Z
A Y
B Y
C Z
A X
C Z
A Y
C X
A Y
B Y
C Z
B X
A Z
C Z
C Z
B Z
B Y
A Z
A Z
A Y
C Z
A Y
A X
A Y
B Z
C Z
C Z
A Z
A Z
C Z
A Y
C Z
C Z
B Z
C Z
C Z
A Z
C Z
B Z
C Z
B X
A Y
A Y
A Z
C X
C Z
C Y
C Z
C Z
C Z
B Z
A Z
C Z
C Z
A Y
B Y
B X
B X
C Z
A Z
B Y
C Z
C Z
B X
C Z
C Z
A Y
A Y
A Z
A Y
B Y
C Z
A X
A Y
C Z
A Z
C Z
C Z
A X
A Z
C Z
B Z
A Z
A Z
B Y
B X
A Z
A Z
B Z
C Z
C Z
A Y
A Z
B Z
B Z
C Z
B Z
A Y
B X
A Z
B X
C Z
A Z
A Y
C Z
C Z
A Z
A Z
A Z
A Z
A Z
B X
C Z
C Z
C Z
A Z
A Z
A Z
A Z
B X
C Z
B X
C Z
A Z
C Z
A X
A Y
A Z
C Z
B Y
C Z
C Z
B Z
C Z
B X
C Z
B X
A Z
A Z
B Y
B X
C Z
C Z
C Z
C Y
C X
B Y
B Y
C Z
A Z
A Z
C Y
C Z
B Y
C X
A Z
B X
A Z
C Z
C Z
A Z
C X
A Z
B Z
B Y
A X
C Z
A Z
B X
A Z
B Y
C Z
B X
C Z
B Y
C Z
A X
C Z
A Z
C Z
A Y
A Y
C Z
C Z
B X
B Z
A Z
C Z
A Z
C Z
A Y
B X
C Z
A Z
B X
C Z
C Z
B Y
C Z
C Z
C Y
B Y
B X
C Z
B Y
A Z
A Z
B X
B Y
B Y
B Y
B Y
B Z
C Z
C Z
A Z
C Z
C X
C Z
B Z
C X
C X
A Z
A Z
B Y
B Z
B Y
C Z
A Y
A Z
B Y
B Y
B X
A Z
A Z
A Z
C Z
C Z
C Z
B Z
A X
A Z
A Y
C Z
A Z
A Z
B Z
B Y
B Y
A X
C Z
C Z
B X
A Z
B Y
A Z
B Z
A Z
C Z
C X
A Y
A Z
C Z
C Z
C Z
A Z
C Z
C Z
B Y
A Z
A Z
A Z
A Y
C Z
A Z
C Z
B Z
A Z
C Z
C X
B Z
C X
B X
C Z
B Z
A Y
C Z
C Z
B X
B Y
B Y
A Z
B X
A Y
A Y
A Z
B Z
C Z
C Z
B Z
A Z
C Z
B Y
C X
B Z
C Z
B Z
C Y
C Z
A Y
A Z
C Z
A Z
A Z
C Z
C Z
C Z
B Z
A Z
C Z
C X
A Z
A Z
B X
B Y
C Z
A Y
A Z
C Z
B Z
C Z
A Y
A Y
C Z
A Z
A Z
B X
A Y
B Y
C Z
C Z
B Y
A Z
A Y
C X
C Z
C Z
A Z
C Z
A Y
C Z
A Z
A Z
C Z
A Z
A X
C Z
C Z
A Z
B Z
B Z
B X
A Z
B X
A Y
A Z
C Z
C Z
A Y
B Z
C Z
A Z
A Z
C X
B Z
B Y
B Y
A Y
B X
B X
C Z
B X
A Z
B X
A Z
C Z
C Z
A Z
B Y
C Z
C X
C Z
C Z
A Z
B X
C Z
C Z
A Y
C Z
C Z
B X
B X
B X
A Z
B Y
C Z
A Z
C Z
C Z
B Y
C Z
A Z
C Z
B Y
B Z
C Z
C Z
C X
C Z
B Z
C Z
B Y
B X
A Z
A Y
B X
A Y
B Y
A Z
C Z
C Z
C Z
B X
C Z
B X
A Z
B X
B Y
A Z
C Z
C Z
C Z
A Y
B Y
A Y
C Z
A Z
C Z
C Z
A Z
A Y
C Z
B X
A Y
A Z
C Z
B Y
C Z
A Z
C Z
B Y
C Z
C Z
B Y
C Z
C Z
B X
C Z
B Y
C Z
B Y
A Z
C Z
B Y
A Z
C Z
C Z
B Y
B X
B Z
A Z
A Y
A Z
A Y
C Z
C Z
B X
C Z
B Y
C Z
C X
C Z
A Y
A Z
C Z
C Z
C Z
A Z
B Y
C Z
C Z
A Z
B Y
C Z
A Y
B Z
B X
A Y
B Y
C Z
A Y
C Z
B Y
B Y
C Z
C Z
B Y
B X
C Z
B X
B Z
B Y
C Z
C Z
C Z
A Z
A X
A Z
B Z
A Z
C Z
A Z
C Z
C Z
A Z
A Z
B Z
C Z
C Z
C Z
A Z
B Y
A Z
A Y
C Z
B X
B X
A Y
C Z
C Z
B X
B Z
C X
B X
B Y
A Z
A Y
A Z
C Z
B X
C Z
B Z
C Z
A Y
C Z
A Y
C Z
B Y
B Z
C Z
C Z
C Z
C Z
C Z
A Z
B Y
C Z
C X
B Y
C X
B Y
B Z
B Y
A Z
A Z
B X
C Y
A Z
C Z
B X
B X
A Z
A Z
B Y
C Z
B Y
B Z
A Y
A Z
C Z
C Z
B X
A Z
A Z
A Z
C Z
C X
C Z
C Z
C Z
C Z
A Z
B Y
C Z
C Z
C Z
B Z
C Z
B X
C Z
A Z
A Z
C Z
C Y
B Y
A Z
A Y
B Z
A Y
B Y
C Z
A Y
C Z
A Z
C Z
B X
C Z
A Z
A Z
B Z
A Z
B Z
A Z
B Y
C Z
B Z
B Y
C Z
A Z
A Z
B X
B X
A Y
A Z
B Y
A Y
A Z
C Z
A X
C Z
A Z
A Z
C Z
A Z
B X
A Z
A Y
A Y
B Y
A Z
A Z
A Z
B Y
B Y
A Z
A Z
C Z
C Z
A Y
B X
B X
C Z
A Y
C Z
C Z
C Z
A Y
C Z
C X
C Z
B Y
A Z
B Y
A Z
C Z
A Y
C Z
A Y
B Z
B X
B Y
B X
B Y
B X
A Y
C Z
C Z
B Z
C Z
C X
B X
A X
A Z
A Z
B Y
C Z
C Z
B Y
C Z
C Z
B Y
A Z
B Z
C X
C Z
C Z
B Y
C X
C Z
B Z
A Z
C Z
B X
A Z
C Z
A Z
C Z
B X
B Z
C Z
C Z
C Z
A Z
B Y
A Y
A Z
C Z
C Z
C Z
B Y
A Z
C Z
C Z
A Z
B Z
B Y
C Z
A Y
A Z
A Z
C Z
C Z
C Z
C Z
A Z
C Z
C Z
A Y
A Y
A Z
C Z
A Z
A Z
B X
A Y
A Z
A Y
C Z
B Z
A Y
A Z
B X
C Z
A Z
A Z
A Y
B Y
C Z
C Z
A Z
B X
A Y
A Z
C Z
C Z
B Y
C Z
A Z
B Y
C Z
C Z
B Y
C X
A Z
C Z
C Z
C Z
C Z
A Z
B Y
A Y
B Y
B Z
C Z
A Z
B Z
C Z
A X
C Z
C X
A Z
A Z
A X
A Z
A Z
A Z
A Z
B X
A Z
A Z
A Z
C Z
C Z
C Z
C Z
A Z
A Y
B X
C Z
B Y
A Y
A Z
C Z
C Z
C Z
B Y
A Z
B Z
C Z
B X
B Z
B Z
B Y
C Z
C X
B Y
A Y
C X
C Z
C Z
B Y
A Z
C Z
A Z
A Z
C Z
C Z
C Z
C Z
B Z
C Z
B X
C Z
B X
B Z
A Z
B Y
C Z
A Z
C Z
A Z
A Y
A Z
C Z
B X
C Z
C Z
A Z
A Z
C Z
C Z
A Z
C Z
A Y
C Z
C Z
A Z
A X
A Z
C Z
A Z
C Z
C Z
A Z
B X
C Z
C Z
C X
A Z
A Z
A X
B X
C Z
C Z
A Z
B X
C X
A Z
C Z
B Y
C Z
A Z
C Z
A Y
A Z
C Z
C Z
B X
A Z
B Y
A Z
C Z
C X
B Z
C Z
A X
A Y
C Z
C Z
C X
B Z
A Z
A Z
B Z
A Y
C X
A Z
C Z
A Z
C Z
A Z
A Z
A Z
C Z
A Z
C Z
B X
A Y
A Z
C Z
B Y
C Z
A Y
C Z
C Z
C Z
C Z
A Z
A Z
B Z
C Z
A Y
C X
C Z
C Y
B Y
C X
A Y
C Z
C Z
B Z
B Y
B Z
A Z
B Y
C Z
C Z
B X
B Y
B Z
A Z
A Z
C Z
B X
A Z
B Y
C Z
C Z
B X
C Z
A X
C Z
B X
A Y
A Z
B Y
C Z
C Z
A Y
A Z
C Z
C Z
A Z
C Z
C Z
C Z
B X
C Z
B Y
B Y
C Z
B Z
C Z
C X
C Z
B X
A Z
B Z
B Z
B Z
C Z
A X
C Z
B X
A Z
A Z
A Z
A Y
C Z
C Z
C Z
C X
A Y
A Z
A Z
C Z
C Z
A Z
B X
C Z
B Y
A X
C X
B Y
B Y
A Y
C X
C Z
B X
A Z
A Z
B Z
A Y
C Z
C Z
A Z
C Z
C Z
A Y
C Z
C Z
B Y
C Z
C Z
A Z
A Z
B Z
A Z
C Z
C Z
C Z
C X
C Z
A Z
C Z
C Z
C Z
C X
C Z
C Z
A Z
B Y
C Z
B X
A Z
C Z
C Y
A Z
A Y
A Z
C X
C X
A Y
B X
A Y
B Y
B Z
B Y
B Y
B Y
B Y
B Y
B Y
B Y
B X
B Z
A Y
A Y
A Y
B Y
A Y
B X
C X
A Z
C Z
A Z
A X
C Z
C Z
B Z
C Z
B Z
B Z
A Z
A Y
A Z
B X
B Z
C Y
A Z
A Z
A Z
C Z
C Z
C Z
C Z
A Z
C Y
A Y
C X
C Z
B Y
C Z
A Z
A X
A Z
B Z
C Z
B X
B X
A Z
C Z
B X
C Z
C Z
A X
C Z
A Z
C Z
C Z
B Z
B Y
B X
B Z
A X
A Y
C Z
A X
A Y
B Y
A Y
C Z
C Z
B X
C Z
B Z
C Z
B Y
C Z
A Z
A Y
B Z
B Z
A Z
A Z
A Z
A Y
C Z
C X
A Z
A X
B Y
B X
A Z
C Z
A Z
A Z
C Z
B Z
B Z
B Y
B Y
A Y
C Z
A Z
A Z
C Z
A Z
C Z
C Z
B X
B Y
C Z
C Z
B X
C X
C Z
A Y
C X
B X
A Z
A Z
A Y
B Y
A Z
B Z
C Z
C Z
A Z
B X
A X
B Y
A Z
B Z
A Z
B Y
C Z
A Z
A Y
C Z
A Y
C Z
C Z
A Z
C Z
C Z
A Z
A Y
C Z
A Z
B Z
A Y
A Z
C Z
C Z
A Y
C Z
A Y
A Z
C X
B X
B Z
B Z
B Z
B Z
B Y
B X
A Z
C Z
B Z
C Z
C Z
C X
A Z
A Z
B X
C Z
A Y
C Z
B Z
A Z
C X
C Z
C Z
B Y
C Z
B Z
A Z
A X
C Z
B X
A Z
B Y
C Y
C X
C Z
A Z
B Z
A Z
B Y
C Z
C Z
A Z
C Z
C Z
C Z
C Z
B Z
C Z
B X
B Y
A Z
B Y
B Y
A Z
C Z
C Z
B Y
B Y
B Y
B Y
B Z
B X
A Z
B Y
B X
A Z
A Y
B X
B X
C Z
C X
B Y
C Z
C Z
A Z
C X
C Z
A Z
B Y
A Z
A Z
A X
C Z
B Y
A Z
C Z
C Z
A Z
B Y
B Y
B Z
B Z
B X
A X
A Z
A Z
C X
B Y
A Y
B Z
A Z
B Y
C Z
C Z
B X
C Z
C Z
A Z
C Z
A Z
A Z
C Z
C Z
C Z
B X
B Z
A Y
B X
C Z
A Z
C Z
A Y
B Y
A X
C Z
A Y
A Z
A Z
A Z
B Z
C Z
C Z
C Z
C Z
C Z
B Z
B X
C Z
A Z
C Z
A X
B Z
C Z
C Z
A Z
A Z
B Y
C Z
A Z
C Z
B Y
A Z
A Y
A Y
C X
C Z
A Z
B Y
C Z
C X
C Z
A Y
A Z
A Z
B X
C Z
B X
B Y
A Y
A Y
B Z
A Y
A Z
B Z
A Z
A X
B Z
C Z
C X
C Z
C Z
C Z
C Z
C X
C Z
A Z
A Z
B X
A Z
A Z
A Z
C Z
A Z
C Y
B Y
B Y
C Z
A Y
B Z
C Z
C Z
C Z
A Z
C Z
A Z
B Z
B Y
A Y
C Z
A Z
A Y
C Z
C Z
A Y
B Y
C Z
A Z
A Y
A Z
B X
C X
C Z
C Z
A Y
A Z
B X
C Z
A Z
C Z
C Z
A Z
C Z
B X
A Z
A Z
B Y
C Z
B X
C Z
C X
A Z
B X
C X
C Z
C Z
A Z
B Y
A Y
C Z
B Z
B Y
C X
B X
C Z
C Y
A Z
A Z
C Z
B X
A Z
C Z
B Y
B X
B Z
B X
A Y
C Z
C Z
C Y
A Z
A Y
C Z
B X
A Z
A Z
B Z
B Z
B X
A Y
A Z
C Z
A Z
A X
A Y
C Z
C Z
B Y
A Z
C Z
B Z
A Z
B Y
C Z
B Y
A Z
B Z
A Z
B Y
B Z
C Z
C Z
A Y
C Z
A Z
B X
C Z
B X
B X
A Z
C Z
B Z
A Z
C Z
C Z
C Z
C Z
A Z
C Z
B Z
C Z
A Z
B X
C Z
A Z
C Z
C Z
A Y
A Y
C Z
A Y
A X
C Z
A Z
A Z
B Z
A Z
A X
C Z
B Y
A Y
B Y
A Y
C Z
C Z
B X
A Z
B X
B Z
B Z
A Y
C X
A Y
C Z
B Y
A Z
A Z
C Z
A Z
A Z
B Y
C X
B X
A Z
A X
C Z
A Z
B Y
A Z
C Z
C Z
A Z
B X
B Z
A X
A Y
A Y
B Y
B Z
B X
B Z
C X
B Z
C Z
C Z
B X
B Y
B X
B Z
B Z
C Z
A Z
A X
B X
C Z
A Z
B Y
B Y
C X
A Z
B X
A X
C Z
B Y
A Y
B Y
A Y
B Z
C Z
C Z
C Z
B Y
B Y
A Y
C Z
C Y
B Z
A Z
C Z
C Y
B X
B X
A Z
B Y
A Z
B X
A Z
B Y
B Y
C Z
C Z
A Z
B Y
C Z
C Y
C Z
C Z
A Y
B X
C Y
A Y
B X
C Z
C Z
C Z
B Z
B Y
A Z
A Y
A Z
C Z
C Z
B Y
C Z
C Z
A Z
B Z
C Z
A Z
A Z
A Z
A Y
C X
B Y
B Y
A Y
C Z
B Y
B X
B Z
C Z
C Z
A Y
A Z
A Z
B Z
C Z
C Z
B Y
C Z
A Z
C Z
C Z
C X
B X
B Y
C Z
A Z
A Y
C Z
C Z
C Z
A Z
A Y
C Z
A Z
A Y
A Y
C Z
B X
C Z
C X
B Y
A Z
B Y
C Z
B X
A Z
A Y
C Z
A Z
C Z
A Z
C Z
C Z
A Y
A Z
A Z
B Z
A Z
A Z
C Z
A X
A Y
C X
A Z
A Z
B Z
B Y
A Z
C Z
B Z
C Z
A Z
C Z
B X
C Z
B Z
B Z
C Z
B Z
A Z
A Z
C Z
A Z
C X
C Z
A Y
A Z
A X
A Z
B Z
B Z
C Z
C X
A Y
C Z
A Z
A Z
A X
C Z
C Z
C X
B Z
B X
B Z
B Y
C Z
A Z
A Y
A Y
B X
A Y
A Y
C Z
C Z
B Z
A Z
B Z
C Z
A Z
B Y
B Y
C Z
A Z
C Z
A Z
B Y
A Z
C Z
B X
C Z
A Z
C Z
A Y
B Y
A Y
B Z
A Y
C Z
A Z
C Z
B X
B X
B Y
B X
C Z
A X
B Y
B Z
C Z
A Y
C Z
B Z
C Z
A Z
C X
C Z
A Z
A Y
C Z
C Z
B Y
C Z
B Y
C Z
C Z
B Z
A Z
C Z
B Y
B X
A Z
C Z
C Z
A Z
C Z
C Z
B Y
A Z
B X
C Z
B Y
B X
A Z
C Z
A Z
C Z
A Z
C Z
B Y
C Z
A Z
B X
C Z
A Y
A Y
A Z
A Y
A Z
A X
C Z
B X
B Z
C Z
A Z
C X
A Z
A Z
A Z
C Z
A Z
C Z'''
        s = advent2022.Day02.Solution(text.splitlines())
        score = s.scorePart1()
        print('\n')        
        print('score is ' + str(score))

        self.assertEqual(12794, score)

    def test_day02_part2(self):
        text = '''A Y
B X
C Z'''
        s = advent2022.Day02.Solution(text.splitlines())
        score = s.scorePart2()
        print('\n')        
        print('score is ' + str(score))

        self.assertEqual(12, score)

    def test_day02_part2_puzzle(self):
        text = '''A X
B Y
B Y
C X
B X
C Z
C Z
A Z
A Z
B Y
C Z
A Z
C Z
C X
B Z
C Z
C Z
C Z
B Y
C Z
C Z
C Z
A Z
A Y
B Z
B Z
A Y
B X
C Z
C Z
A Z
A Z
C Z
A Y
A X
A Z
A Z
B X
B Z
B X
A Z
B X
B Z
B Z
C Z
A Z
A Z
A Z
C Z
B Z
A Z
A Y
A Y
B Y
B Y
B Z
A Z
B Z
A Z
B Z
C Z
B Y
A Z
B Y
A Z
A Z
A Z
C Z
A Y
A Z
C Z
C Z
A Z
A X
B Y
C Z
A Z
A Z
C X
C Z
B X
C X
B X
A Z
C Z
C Z
A Y
A Z
B X
C X
A Z
A Z
C Z
C Z
B Y
C Z
A Z
A Z
A Y
B X
B Y
A Z
C Z
A Z
A Z
A Z
C X
C Y
C Z
B X
B X
B X
A Z
A X
C Z
A Z
B Y
B X
A Y
B X
A Z
C Z
C Z
A X
A Z
C Z
B Z
B X
A Z
C Z
C Z
C X
C Z
C Z
C Z
A Y
B X
A Y
A Z
B Z
B Z
C Z
B Z
B Z
B X
A Z
C Z
A Z
A Y
C Z
A Z
C X
A Z
A Z
A Y
A Y
A Z
C Z
B Y
A X
A Z
A Y
C Z
A Z
B X
A Z
B Y
A X
C X
B X
A Y
A Z
B Z
A Z
A Z
B X
A X
C Z
B X
B Y
A Z
B X
C Z
A Z
C Z
B X
A Z
A Y
A Z
A Z
B X
B X
B Z
A Z
B Y
C Z
B Z
C Z
C Z
B X
B X
A Z
C Z
C Z
A X
B X
B X
A Y
C Z
A Z
A Y
B X
A Z
A Z
B X
A Z
C Z
B X
B Z
B Y
B X
A Y
C Z
C Z
C Z
A X
C Z
A Z
C Z
C Y
C Z
C Z
C Z
B X
A Z
B X
B Z
A Z
C Z
B Y
B Y
B Z
C Z
C Z
C Z
B Z
B Y
A Z
B X
B Z
C Z
A Z
B Y
B Y
A X
C Z
B Y
A Y
B Y
B X
B Y
B Y
A Y
B Y
C X
A Y
A Y
C Z
A Z
A Y
C Z
A Z
A Z
C Z
C Z
C Z
B X
B Y
A Y
A Y
B Z
A Z
B Y
B X
B Y
A Y
A Y
A Z
B Z
C Z
C Z
C Z
A Z
C Z
A Z
A Z
A Z
A Z
C Z
B Y
C Z
B X
C Z
A X
A Z
B X
C Y
C X
A X
A X
A Z
A Z
B X
A Y
B Z
A Z
B Z
A Z
C Z
C X
C Z
C Z
C X
C Z
C Z
C X
C Z
B Z
A Z
B Y
A Z
C Z
B X
C Z
B Z
B Y
A Z
B Y
A Y
B X
B Z
B Z
A Z
B Z
C Z
C Z
A Y
A Z
A X
A Y
C Z
B X
A Z
C X
A Z
A Z
A Z
A Z
C Y
B Y
B Y
A X
C Z
A X
A Z
A Y
C X
A Y
A Y
A Z
C X
C Z
B Z
B X
A Z
C Z
C Z
B Z
B X
C Z
C Z
A Y
B Z
A X
B Y
A Z
C X
B X
C Z
B Y
A X
A Z
B Y
A Y
A Z
B Z
A Y
B Y
A Z
B Y
B X
B Z
A Z
B Y
B Z
A Y
A Z
C Z
B X
C Z
B X
C Z
B Z
C Z
C Z
B Z
A Y
A Y
C Z
B Z
A Z
A X
C Z
A Z
C Z
A Z
A X
A Z
A Z
A Y
B Z
B X
C X
B Y
C Z
B X
B Z
B X
A Z
A Z
A Z
B Z
B Y
A Z
B Y
C Z
B Z
A Z
A Y
C Z
A Z
B Y
B X
B Y
B X
C Z
C Y
A Z
C Z
C Z
A Z
C X
B Z
A Y
B Y
B Y
B Y
C Z
B Z
A Z
B Y
A Z
A Z
C Z
B Y
B Y
A X
A Z
A Z
C Z
A Z
C Z
C Z
A X
B Z
A Z
A Z
C Z
C Z
B Y
B Y
A Z
A Y
A Z
B Y
B Z
A Y
B Z
A Z
A Z
A Y
C Z
A Y
C Z
B X
A Z
A Z
C Z
A Y
C Z
A Z
A Y
A Y
C Z
A Z
A Y
B X
A Y
B X
A Z
A Z
A Y
B Y
B Y
B X
C Z
C Z
B Y
B X
C Z
B Y
C Z
B Y
B X
C Z
A Y
B Z
C X
A Y
C Z
C Z
C X
A Y
A Z
B X
C Z
A Z
B Y
C Z
B X
B Z
C Z
C Z
C Z
A Z
B X
C Z
A Z
A Y
B Y
C Z
A X
C Z
A Y
C X
A Y
B Y
C Z
B X
A Z
C Z
C Z
B Z
B Y
A Z
A Z
A Y
C Z
A Y
A X
A Y
B Z
C Z
C Z
A Z
A Z
C Z
A Y
C Z
C Z
B Z
C Z
C Z
A Z
C Z
B Z
C Z
B X
A Y
A Y
A Z
C X
C Z
C Y
C Z
C Z
C Z
B Z
A Z
C Z
C Z
A Y
B Y
B X
B X
C Z
A Z
B Y
C Z
C Z
B X
C Z
C Z
A Y
A Y
A Z
A Y
B Y
C Z
A X
A Y
C Z
A Z
C Z
C Z
A X
A Z
C Z
B Z
A Z
A Z
B Y
B X
A Z
A Z
B Z
C Z
C Z
A Y
A Z
B Z
B Z
C Z
B Z
A Y
B X
A Z
B X
C Z
A Z
A Y
C Z
C Z
A Z
A Z
A Z
A Z
A Z
B X
C Z
C Z
C Z
A Z
A Z
A Z
A Z
B X
C Z
B X
C Z
A Z
C Z
A X
A Y
A Z
C Z
B Y
C Z
C Z
B Z
C Z
B X
C Z
B X
A Z
A Z
B Y
B X
C Z
C Z
C Z
C Y
C X
B Y
B Y
C Z
A Z
A Z
C Y
C Z
B Y
C X
A Z
B X
A Z
C Z
C Z
A Z
C X
A Z
B Z
B Y
A X
C Z
A Z
B X
A Z
B Y
C Z
B X
C Z
B Y
C Z
A X
C Z
A Z
C Z
A Y
A Y
C Z
C Z
B X
B Z
A Z
C Z
A Z
C Z
A Y
B X
C Z
A Z
B X
C Z
C Z
B Y
C Z
C Z
C Y
B Y
B X
C Z
B Y
A Z
A Z
B X
B Y
B Y
B Y
B Y
B Z
C Z
C Z
A Z
C Z
C X
C Z
B Z
C X
C X
A Z
A Z
B Y
B Z
B Y
C Z
A Y
A Z
B Y
B Y
B X
A Z
A Z
A Z
C Z
C Z
C Z
B Z
A X
A Z
A Y
C Z
A Z
A Z
B Z
B Y
B Y
A X
C Z
C Z
B X
A Z
B Y
A Z
B Z
A Z
C Z
C X
A Y
A Z
C Z
C Z
C Z
A Z
C Z
C Z
B Y
A Z
A Z
A Z
A Y
C Z
A Z
C Z
B Z
A Z
C Z
C X
B Z
C X
B X
C Z
B Z
A Y
C Z
C Z
B X
B Y
B Y
A Z
B X
A Y
A Y
A Z
B Z
C Z
C Z
B Z
A Z
C Z
B Y
C X
B Z
C Z
B Z
C Y
C Z
A Y
A Z
C Z
A Z
A Z
C Z
C Z
C Z
B Z
A Z
C Z
C X
A Z
A Z
B X
B Y
C Z
A Y
A Z
C Z
B Z
C Z
A Y
A Y
C Z
A Z
A Z
B X
A Y
B Y
C Z
C Z
B Y
A Z
A Y
C X
C Z
C Z
A Z
C Z
A Y
C Z
A Z
A Z
C Z
A Z
A X
C Z
C Z
A Z
B Z
B Z
B X
A Z
B X
A Y
A Z
C Z
C Z
A Y
B Z
C Z
A Z
A Z
C X
B Z
B Y
B Y
A Y
B X
B X
C Z
B X
A Z
B X
A Z
C Z
C Z
A Z
B Y
C Z
C X
C Z
C Z
A Z
B X
C Z
C Z
A Y
C Z
C Z
B X
B X
B X
A Z
B Y
C Z
A Z
C Z
C Z
B Y
C Z
A Z
C Z
B Y
B Z
C Z
C Z
C X
C Z
B Z
C Z
B Y
B X
A Z
A Y
B X
A Y
B Y
A Z
C Z
C Z
C Z
B X
C Z
B X
A Z
B X
B Y
A Z
C Z
C Z
C Z
A Y
B Y
A Y
C Z
A Z
C Z
C Z
A Z
A Y
C Z
B X
A Y
A Z
C Z
B Y
C Z
A Z
C Z
B Y
C Z
C Z
B Y
C Z
C Z
B X
C Z
B Y
C Z
B Y
A Z
C Z
B Y
A Z
C Z
C Z
B Y
B X
B Z
A Z
A Y
A Z
A Y
C Z
C Z
B X
C Z
B Y
C Z
C X
C Z
A Y
A Z
C Z
C Z
C Z
A Z
B Y
C Z
C Z
A Z
B Y
C Z
A Y
B Z
B X
A Y
B Y
C Z
A Y
C Z
B Y
B Y
C Z
C Z
B Y
B X
C Z
B X
B Z
B Y
C Z
C Z
C Z
A Z
A X
A Z
B Z
A Z
C Z
A Z
C Z
C Z
A Z
A Z
B Z
C Z
C Z
C Z
A Z
B Y
A Z
A Y
C Z
B X
B X
A Y
C Z
C Z
B X
B Z
C X
B X
B Y
A Z
A Y
A Z
C Z
B X
C Z
B Z
C Z
A Y
C Z
A Y
C Z
B Y
B Z
C Z
C Z
C Z
C Z
C Z
A Z
B Y
C Z
C X
B Y
C X
B Y
B Z
B Y
A Z
A Z
B X
C Y
A Z
C Z
B X
B X
A Z
A Z
B Y
C Z
B Y
B Z
A Y
A Z
C Z
C Z
B X
A Z
A Z
A Z
C Z
C X
C Z
C Z
C Z
C Z
A Z
B Y
C Z
C Z
C Z
B Z
C Z
B X
C Z
A Z
A Z
C Z
C Y
B Y
A Z
A Y
B Z
A Y
B Y
C Z
A Y
C Z
A Z
C Z
B X
C Z
A Z
A Z
B Z
A Z
B Z
A Z
B Y
C Z
B Z
B Y
C Z
A Z
A Z
B X
B X
A Y
A Z
B Y
A Y
A Z
C Z
A X
C Z
A Z
A Z
C Z
A Z
B X
A Z
A Y
A Y
B Y
A Z
A Z
A Z
B Y
B Y
A Z
A Z
C Z
C Z
A Y
B X
B X
C Z
A Y
C Z
C Z
C Z
A Y
C Z
C X
C Z
B Y
A Z
B Y
A Z
C Z
A Y
C Z
A Y
B Z
B X
B Y
B X
B Y
B X
A Y
C Z
C Z
B Z
C Z
C X
B X
A X
A Z
A Z
B Y
C Z
C Z
B Y
C Z
C Z
B Y
A Z
B Z
C X
C Z
C Z
B Y
C X
C Z
B Z
A Z
C Z
B X
A Z
C Z
A Z
C Z
B X
B Z
C Z
C Z
C Z
A Z
B Y
A Y
A Z
C Z
C Z
C Z
B Y
A Z
C Z
C Z
A Z
B Z
B Y
C Z
A Y
A Z
A Z
C Z
C Z
C Z
C Z
A Z
C Z
C Z
A Y
A Y
A Z
C Z
A Z
A Z
B X
A Y
A Z
A Y
C Z
B Z
A Y
A Z
B X
C Z
A Z
A Z
A Y
B Y
C Z
C Z
A Z
B X
A Y
A Z
C Z
C Z
B Y
C Z
A Z
B Y
C Z
C Z
B Y
C X
A Z
C Z
C Z
C Z
C Z
A Z
B Y
A Y
B Y
B Z
C Z
A Z
B Z
C Z
A X
C Z
C X
A Z
A Z
A X
A Z
A Z
A Z
A Z
B X
A Z
A Z
A Z
C Z
C Z
C Z
C Z
A Z
A Y
B X
C Z
B Y
A Y
A Z
C Z
C Z
C Z
B Y
A Z
B Z
C Z
B X
B Z
B Z
B Y
C Z
C X
B Y
A Y
C X
C Z
C Z
B Y
A Z
C Z
A Z
A Z
C Z
C Z
C Z
C Z
B Z
C Z
B X
C Z
B X
B Z
A Z
B Y
C Z
A Z
C Z
A Z
A Y
A Z
C Z
B X
C Z
C Z
A Z
A Z
C Z
C Z
A Z
C Z
A Y
C Z
C Z
A Z
A X
A Z
C Z
A Z
C Z
C Z
A Z
B X
C Z
C Z
C X
A Z
A Z
A X
B X
C Z
C Z
A Z
B X
C X
A Z
C Z
B Y
C Z
A Z
C Z
A Y
A Z
C Z
C Z
B X
A Z
B Y
A Z
C Z
C X
B Z
C Z
A X
A Y
C Z
C Z
C X
B Z
A Z
A Z
B Z
A Y
C X
A Z
C Z
A Z
C Z
A Z
A Z
A Z
C Z
A Z
C Z
B X
A Y
A Z
C Z
B Y
C Z
A Y
C Z
C Z
C Z
C Z
A Z
A Z
B Z
C Z
A Y
C X
C Z
C Y
B Y
C X
A Y
C Z
C Z
B Z
B Y
B Z
A Z
B Y
C Z
C Z
B X
B Y
B Z
A Z
A Z
C Z
B X
A Z
B Y
C Z
C Z
B X
C Z
A X
C Z
B X
A Y
A Z
B Y
C Z
C Z
A Y
A Z
C Z
C Z
A Z
C Z
C Z
C Z
B X
C Z
B Y
B Y
C Z
B Z
C Z
C X
C Z
B X
A Z
B Z
B Z
B Z
C Z
A X
C Z
B X
A Z
A Z
A Z
A Y
C Z
C Z
C Z
C X
A Y
A Z
A Z
C Z
C Z
A Z
B X
C Z
B Y
A X
C X
B Y
B Y
A Y
C X
C Z
B X
A Z
A Z
B Z
A Y
C Z
C Z
A Z
C Z
C Z
A Y
C Z
C Z
B Y
C Z
C Z
A Z
A Z
B Z
A Z
C Z
C Z
C Z
C X
C Z
A Z
C Z
C Z
C Z
C X
C Z
C Z
A Z
B Y
C Z
B X
A Z
C Z
C Y
A Z
A Y
A Z
C X
C X
A Y
B X
A Y
B Y
B Z
B Y
B Y
B Y
B Y
B Y
B Y
B Y
B X
B Z
A Y
A Y
A Y
B Y
A Y
B X
C X
A Z
C Z
A Z
A X
C Z
C Z
B Z
C Z
B Z
B Z
A Z
A Y
A Z
B X
B Z
C Y
A Z
A Z
A Z
C Z
C Z
C Z
C Z
A Z
C Y
A Y
C X
C Z
B Y
C Z
A Z
A X
A Z
B Z
C Z
B X
B X
A Z
C Z
B X
C Z
C Z
A X
C Z
A Z
C Z
C Z
B Z
B Y
B X
B Z
A X
A Y
C Z
A X
A Y
B Y
A Y
C Z
C Z
B X
C Z
B Z
C Z
B Y
C Z
A Z
A Y
B Z
B Z
A Z
A Z
A Z
A Y
C Z
C X
A Z
A X
B Y
B X
A Z
C Z
A Z
A Z
C Z
B Z
B Z
B Y
B Y
A Y
C Z
A Z
A Z
C Z
A Z
C Z
C Z
B X
B Y
C Z
C Z
B X
C X
C Z
A Y
C X
B X
A Z
A Z
A Y
B Y
A Z
B Z
C Z
C Z
A Z
B X
A X
B Y
A Z
B Z
A Z
B Y
C Z
A Z
A Y
C Z
A Y
C Z
C Z
A Z
C Z
C Z
A Z
A Y
C Z
A Z
B Z
A Y
A Z
C Z
C Z
A Y
C Z
A Y
A Z
C X
B X
B Z
B Z
B Z
B Z
B Y
B X
A Z
C Z
B Z
C Z
C Z
C X
A Z
A Z
B X
C Z
A Y
C Z
B Z
A Z
C X
C Z
C Z
B Y
C Z
B Z
A Z
A X
C Z
B X
A Z
B Y
C Y
C X
C Z
A Z
B Z
A Z
B Y
C Z
C Z
A Z
C Z
C Z
C Z
C Z
B Z
C Z
B X
B Y
A Z
B Y
B Y
A Z
C Z
C Z
B Y
B Y
B Y
B Y
B Z
B X
A Z
B Y
B X
A Z
A Y
B X
B X
C Z
C X
B Y
C Z
C Z
A Z
C X
C Z
A Z
B Y
A Z
A Z
A X
C Z
B Y
A Z
C Z
C Z
A Z
B Y
B Y
B Z
B Z
B X
A X
A Z
A Z
C X
B Y
A Y
B Z
A Z
B Y
C Z
C Z
B X
C Z
C Z
A Z
C Z
A Z
A Z
C Z
C Z
C Z
B X
B Z
A Y
B X
C Z
A Z
C Z
A Y
B Y
A X
C Z
A Y
A Z
A Z
A Z
B Z
C Z
C Z
C Z
C Z
C Z
B Z
B X
C Z
A Z
C Z
A X
B Z
C Z
C Z
A Z
A Z
B Y
C Z
A Z
C Z
B Y
A Z
A Y
A Y
C X
C Z
A Z
B Y
C Z
C X
C Z
A Y
A Z
A Z
B X
C Z
B X
B Y
A Y
A Y
B Z
A Y
A Z
B Z
A Z
A X
B Z
C Z
C X
C Z
C Z
C Z
C Z
C X
C Z
A Z
A Z
B X
A Z
A Z
A Z
C Z
A Z
C Y
B Y
B Y
C Z
A Y
B Z
C Z
C Z
C Z
A Z
C Z
A Z
B Z
B Y
A Y
C Z
A Z
A Y
C Z
C Z
A Y
B Y
C Z
A Z
A Y
A Z
B X
C X
C Z
C Z
A Y
A Z
B X
C Z
A Z
C Z
C Z
A Z
C Z
B X
A Z
A Z
B Y
C Z
B X
C Z
C X
A Z
B X
C X
C Z
C Z
A Z
B Y
A Y
C Z
B Z
B Y
C X
B X
C Z
C Y
A Z
A Z
C Z
B X
A Z
C Z
B Y
B X
B Z
B X
A Y
C Z
C Z
C Y
A Z
A Y
C Z
B X
A Z
A Z
B Z
B Z
B X
A Y
A Z
C Z
A Z
A X
A Y
C Z
C Z
B Y
A Z
C Z
B Z
A Z
B Y
C Z
B Y
A Z
B Z
A Z
B Y
B Z
C Z
C Z
A Y
C Z
A Z
B X
C Z
B X
B X
A Z
C Z
B Z
A Z
C Z
C Z
C Z
C Z
A Z
C Z
B Z
C Z
A Z
B X
C Z
A Z
C Z
C Z
A Y
A Y
C Z
A Y
A X
C Z
A Z
A Z
B Z
A Z
A X
C Z
B Y
A Y
B Y
A Y
C Z
C Z
B X
A Z
B X
B Z
B Z
A Y
C X
A Y
C Z
B Y
A Z
A Z
C Z
A Z
A Z
B Y
C X
B X
A Z
A X
C Z
A Z
B Y
A Z
C Z
C Z
A Z
B X
B Z
A X
A Y
A Y
B Y
B Z
B X
B Z
C X
B Z
C Z
C Z
B X
B Y
B X
B Z
B Z
C Z
A Z
A X
B X
C Z
A Z
B Y
B Y
C X
A Z
B X
A X
C Z
B Y
A Y
B Y
A Y
B Z
C Z
C Z
C Z
B Y
B Y
A Y
C Z
C Y
B Z
A Z
C Z
C Y
B X
B X
A Z
B Y
A Z
B X
A Z
B Y
B Y
C Z
C Z
A Z
B Y
C Z
C Y
C Z
C Z
A Y
B X
C Y
A Y
B X
C Z
C Z
C Z
B Z
B Y
A Z
A Y
A Z
C Z
C Z
B Y
C Z
C Z
A Z
B Z
C Z
A Z
A Z
A Z
A Y
C X
B Y
B Y
A Y
C Z
B Y
B X
B Z
C Z
C Z
A Y
A Z
A Z
B Z
C Z
C Z
B Y
C Z
A Z
C Z
C Z
C X
B X
B Y
C Z
A Z
A Y
C Z
C Z
C Z
A Z
A Y
C Z
A Z
A Y
A Y
C Z
B X
C Z
C X
B Y
A Z
B Y
C Z
B X
A Z
A Y
C Z
A Z
C Z
A Z
C Z
C Z
A Y
A Z
A Z
B Z
A Z
A Z
C Z
A X
A Y
C X
A Z
A Z
B Z
B Y
A Z
C Z
B Z
C Z
A Z
C Z
B X
C Z
B Z
B Z
C Z
B Z
A Z
A Z
C Z
A Z
C X
C Z
A Y
A Z
A X
A Z
B Z
B Z
C Z
C X
A Y
C Z
A Z
A Z
A X
C Z
C Z
C X
B Z
B X
B Z
B Y
C Z
A Z
A Y
A Y
B X
A Y
A Y
C Z
C Z
B Z
A Z
B Z
C Z
A Z
B Y
B Y
C Z
A Z
C Z
A Z
B Y
A Z
C Z
B X
C Z
A Z
C Z
A Y
B Y
A Y
B Z
A Y
C Z
A Z
C Z
B X
B X
B Y
B X
C Z
A X
B Y
B Z
C Z
A Y
C Z
B Z
C Z
A Z
C X
C Z
A Z
A Y
C Z
C Z
B Y
C Z
B Y
C Z
C Z
B Z
A Z
C Z
B Y
B X
A Z
C Z
C Z
A Z
C Z
C Z
B Y
A Z
B X
C Z
B Y
B X
A Z
C Z
A Z
C Z
A Z
C Z
B Y
C Z
A Z
B X
C Z
A Y
A Y
A Z
A Y
A Z
A X
C Z
B X
B Z
C Z
A Z
C X
A Z
A Z
A Z
C Z
A Z
C Z'''
        s = advent2022.Day02.Solution(text.splitlines())
        score = s.scorePart2()
        print('\n')        
        print('score is ' + str(score))

        self.assertEqual(14979, score)

    def test_day03_part1(self):
        text = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
        s = advent2022.Day03.Solution(text.splitlines())

        print('\n')
        sum = s.findPart1()
        print('sum is ' + str(sum))
        self.assertEqual(157, sum)

    def test_day03_part1_puzzle(self):
        text = '''lvcNpRHDCnTLCJlL
RFZggsMrjTFGCJmdmd
srsBZgBqwBqRZbzqtHpzzDNtHDqV
CCTPpCvlpzzZQQQflrzbQDttTJcgcggJcHtcddtdhT
nMLBRnGsFFLznRFRLMMNBnNLDRDdhScJccctdSccJJgDDHhH
GVBGVBsLjsrrvfzpjpfQ
dzVRSPVVBVDSPzDBQVSQFFlrclMplpMJMtPJlJvHZCMt
TjmGmbhjTnTmwhmrvvrHcZvCHZMl
fnLwwqfwfqjghHwGThwfTGGBFVDFFsszSRVzRBsdBDgFsV
CCWFCcdDWwcWFpSvggnzRRQszngJwT
mGtqqLrqfmmLNtNrgTjgJzNQlvJTvznJ
tnhVbhMLLZZrnWHPSHDBWbWBFd
nQhvgnCQjSSSTTSMCsLDsfPfDlsPJMWLzL
qrqBFFBbrVRLszLfsqdqPW
bNFFRbBcFZNrZRRRbprNpFrHSwznTnvSwgHvzCSSSjnCQwgz
tnnZZVmwmqtvVdZqnddQQHHTHQLsFTnsPrrgrQ
MzMflMGpzGzPGPgjLgHrGj
zPfhMJDDMJfzlhcRJvVwcVtwVcmcbqqtbv
GVzrBVcPVfGrzVVBcQJlGGRCZSSRtSdRnGLJ
wbjvHWbLvhFppjZdtwZRNddtJwlR
pvMmbpFFbqqqvWHMFvzrLDMMrMTTrVTPzVzc
qPmgpmwpwqWWPHdjdTNStzNLMztSWtMNtz
lVFfJrFJbbcsvcRVRZzQCzQNSZTZ
DGbvFSDGbDjnqgjwmGdq
DMnpnpwwnpmRRmcRBDnDwpbRQHssHqhHCHHSsQddHZQQcqqs
JlZjjlJgNSddfsgQdf
GvrWvzNjvPVLDpbPZwBP
drQDzHsHrdZWqDSSPwmmJDDbvbSJ
hphBhCMFlBtBtGTJMJsscPwTjMJv
tlBCGFgVFNpGClFFVGGtFBZrdZQznfdQQrRWVRQdRsVf
NjdCLdjzzlNdjwBBtZqpqPJQbN
CsDWcHcGHtcBbJPpbP
mGHSssSgSsHFSgGrSgmlLzCdldllrCVCLdnfnT
rDLLzRmbcLJRtRSvSBdZtSTp
MFswshwgsCsjghgFBsGssjlZpfpvdSHfTdCZTSpHtfddTH
llwlwGjMPMQQnBMswsFgglPVcWcDcbWqLWbbLJVDzrqnVr
pqmmcSTLfSSSMFlf
rHWtPWnHtlrlDntzWwtBFdzCFMRCfjRQFfgMRMjC
PWWHDVZPDDJVlWHncGGbqqTVvVmpGTmm
wLBtWhGWJBdMmZMs
jgvNCFvvGppGnmNJ
DDRQTgcvjTPFqGHhRVhLRSVL
tPPwLpBpDpgLSPvgQCvsLPjdjNZrJZsdZjsrsnZNjbZc
lMWzWMBhmMhRGfVRffHmMjJcJjrNNZnjJcWjNqJnZJ
mFMzhTmBGfHTwgPgtptFpPgP
qCcqJQHslgtsQsCZmPWNSRNZTPBBCN
nnLpjjnvwwvDnrGwFvbFjwPgPWRTPrrPShNhmmNSRRPN
bnwdDLjnzGgvFqdJQcqVfQVqHt
DfCzDCCTDLDBCsdjzwdrHjbRgjGH
MSStMScccJtPptJNJZtJJSrFdwPGjFFHHwsggrwdwRdP
nStlpVlhhNSshZlcNZnMcctpBChWBQLqCWqmqvmBCBmQBqmL
RfLHNvfLfLZQBtRZsBfffjVqGvqpGSmJpgrJpjGjrp
FDbPCMzbTTDDPmzrVzqppJBrBj
DPcWPWDhlbCcWBsQZZfHtdwf
fbHfPfHHfPZWgZfSGpqNBqdBBjpjdPBJqv
rnVNCwwrhhDrmmvcmjdDqcmB
hFRrslFRNhFzVthllRCRCCwnQtSGfQgZZbbSWQLSSTZWbQTt
nmVqTFCmTVbnvVCnqwFrffjhZLffhNrNJF
StBHWDgMBpHMBHDzLjffjWwZJNNfNZjL
wBBcDcgzdVbbQcnQlq
MfGCtqGDhjDqHhrjGCcJZZBwHRcspZsBsHRc
PFFpLFSpzVdSTPgnzzdPPZBRcZBwBJRcWJBmJW
vdTTzVpNVpfCChMGqMvr
VtZzBzhtlrhznFlBfgrfZgFrPjGRMGjRTmSjRjRTHjfRHmRv
DQpnsbJCsNNnpNNJsDQdCDcRmHPGTHTHRSmRmHjvjHSpSS
cQbnQdNLdJJQJJJDJWnFwzgwBthrgZBwBgFLZV
VhRRgmhpFjFFBDVPGPWQPzvvMMWfjf
qcnbnCbfLqJrCnrcdbbLrGSlzWsQvsWWzvWGdMWGQl
bnfbwrcwCrHqnHcZhFBTBVRDFmpBHB
lrtqltJJJqSTWJqVHRnsRhphdbfbzBdhsRsd
vSZCgZMMLSNvCQLPLDPNgZgnznzBfsGGnQnQGdnsfhsfzb
CMFLgmPgFFNMFDDCgLLcrWrjTTjtmSJqlWTTwWSr
LdjljBdZMFdZFLLLgPvWzQRzCsCmCVssmFSW
TJttwDhnnTlWsQzSQQDvWm
HtcnfctJwtwrHhrwhfHhJpjNLMZBMgZLrBlbbLNPNj
qqhNchPdpqTTNqpDmmvvGzVfzfmvdH
cwccjsFwFjnwGwQDfVVVVv
FbWjcRsLLFngBrjpbJqCJZTbJZNClq
lhznMTSzSnjhQGtVPQBdGB
msfNDDJLWslJgfNgCrmLdtGQFVvdGQPZVttBFP
RCrJJJDrJRsfgmbsrNsrlDMTSMHcjqwzScjMqqTjbbSc
nNgsvNWDRvgnRNVCFddTNZTNZQCTFZ
lffHJfHSPmSfvLlbLmpZrCTFTtrTQHqtTrCCrq
cpzblplpbvMzWnsDDB
CgtvQvJvMtWttvwftCdWvDQrfsFcrqnlcnqZZFRcRqsnhF
HzLzVBNLjHqnhzFlWFlr
NmBjLbVVbmbTLpTjBNVLHNdCtTSWQvCgdwSwJtWQwdSD
lncHcnlccVSLNSQNslncLcrZJCrgPfJZDrggJCCvZPHC
jRqqRmmqFwRFppfPPppPBfpWBvZf
wmMqjtTdjFwGGdtNhQbVfhntcNLVbL
HFBgMjpbpddMpbHdgHLLRNwhwFLDtNSRDLLD
zsCnfqZflrlnhhrtwNgggNNL
CGqnQzlqlWWMWgVBGg
pQnvzjztpzpCmtzzjzpnBHrJNGlqggMMqgqlNWgfNNqNCP
sVTSwddRRDVShwRwRTWgPNqMGQMGNqMWslsg
hDSTQhcQcHrtcBmZHv
QRmQfvQpWpswfZWWvNbhlMglgFbZDldlbL
rzHqtcnqqVjqjGcHdLdFdCFdCbLDnMCh
DGcGGSPDpWTsSfpv
llfMHTmvHlfZlFZRzgQzsFBLtLzFGF
wrWNJrdJhRmhGmNh
DWrrJjwPjCdPDwdmwnrTZnZZcqZfnqbvZfHvql
mPmVJJmNZJmlVBPPrZpWcFWbGWbjgqNbdqjSjg
nMhzwRhwvhMDMgWHRdGHgccggd
sMvnhQshMwwvdvMMCwBtlZtplZpTmPBVZVlC
ltlRzpncRglplzhFwFwzZZMWLWZBqnDVZLDVZQQQ
SJcdvJscNSsGcSGCSJmsTQDTVZQTLTQQWCTTMQCW
sPdJmcvsJvGJmdJmfpwftfrlztrRlPfP
LdPrWcMCWCfPdMJgdFsbRRHsRSHRHHcFpH
hVVTQmQTnRFLFsmzps
qthVVwZqlQLQhNttDDDWrffDJJJDrgNP
BTjTNjtlPrBjjrljbnMFfhVWFFhlMWMfHdll
mzcgZvDggDDCJCZLvsLJLcmVqWVSVqFLfdHHMWVWWWffnF
cmmcmzQDZQJmZCnDRgQCTTwjpTtwRjrbNjpPpwrj
rMbchQphhCSbGnzSbl
qFtgvTTqFFFFJGzWJG
NZjGqGBNjNHQrhpPNHQr
LnLmbtTtTwtLcVfFFLtPrfPrfqqqsqhSvrhrhh
BzJWzZRZJzJvlZJCZgZZpJHCqQDhNQPDqDDrjNsjPPNrhSCN
lpJWZzJpgHWdWMgHlJMZzgpJLGVLGGvwVwtmcGbvGMGVvncn
WdBgdqRgWqHmNNwsGgcQ
ptPVbPbSbMJrmsVzRzhwmcGQ
SSbvrJbJtCDZfTqdRfCdBZ
WDNNWvPpvNJRRbGLsGMnnbmG
qgFdBwgVdjwdtjjdBgMgGmLQsnZrnZssGswsmLrw
FqTCTtqjdjVqgCqSMJMTvPThTJMNDh
brSSSpZjVVWdfVrHPhRBggNNGwHr
fDlLzFCLMvnMMJLNHNCBQwNhRgwRPP
MJqMmfzDvFtLDtmsVsZZTsSScWcsbq
CSZlllhSdnDrrDdJjqjzbSGzGvwbfHMb
gTNvVNLQtsFpQHqfwfBfVMfHzf
QgNmWTtmTcmmdmrZRvnlPl
SmzfvfjvjbjLNJjD
cFhWMhGHTPhccMQQGBTFGwbVVwdbddJDvVJLvDDHvd
GFMBGcWTWhcGrhFZTTchQsSfgtmnnRvnmnnRgRCrRS
ZTQHVZsZSQpQQGBMGqfBRbRB
CwtLDtNFcPnllwnqvMgbvGVfVfBG
VClLWWFPPhlhctsTrrSpWpmszjZj
HChzPltNnnHtnpqSpHpFpSfSvS
mJmQssZJLdTQLcbjlGLGfSgMbqwwSFSMSFMMqMwS
JdBLlGTjLjjjjdmmBPnRzCBRNPhPtPWPtr
FPLHMHqqPMgFLLggsMghTJhwtDSSJDltJvtwdvST
WQfmjQZsjfZNQCrZCNZQQWQBCSClvdwTSClwSwlTJvtwJdbT
BpmzrWcpBrfmpsGPGFqPRgzqVPLM
bHjccpHwGHJTfPlffPwr
VtChMZVhhStZdfTCfJvcPRCTJn
sLNLZcdNZZqZqqVqSNWtjQDGHssHGHgQHDBgmsDg
CdWgCpddwgClFlmmVTBbRtRtbntBVVds
vcJGhPLPhJvChLhMLfccrvfvsVVbsGBTTBnVbRzBVstsGnbz
vJJHhjcCLPPjQPHLrSZmpgmqwlWZZgZZQm
VpTFCFtrjCdJdjHVFnSjszSllDjsDzgvzl
fhmhZBMtfZfGBNfNcmsbZnzSlRsRggslsbnv
qPLPhMcLhPfNWPpFrdFdFTtJ
nlgQJhJFlncMzMWZMFvw
mDdsDfHjHsjHdjTLfpDsbDcNzzwcRbZNZPMcCPWMRPMc
sqqdwffHjTmdmpffmLddTTGDnSJtJBShVVhrGVJtShrlBBnJ
CrcMcMDBCmLlZdSd
qPjGjnQPqWjgZmTdlFwTmqLJ
bnPnnzHjbPznzVpdpVDcvprr
TCScMQcQCrssJPQhQs
VpfnqqfdVVwpqvqwGbDPPsjgPShDSsJhlnSl
qffdmGpfwfbfvVqpfwwfbdqRMTSTWNMWTmZLTzTCZTMLWC
QQPpPbPbDNplSJrCCj
VdMzffgnRmVdfVWRvlrCTjRlNBvrrlrr
mGgNdthhGgMWWtsFcHcHwqLqtH
HrPFVqVppVpDjFDrVbCpDFJSLsmwjhjGLLmthJLJLmZs
WWgRdMdRMnQnRzWvPSssPWssJmhsshtG
MnfvMlnQccvfMlcTRMQdRfpHPDDDpPrDTbTBNbHbHDCq
GWWRsSwLhWsRsSbsPttThZqrNBJJBgPNCJCCqNMNgP
HpVDTHzfFDpFfzHzFVcrBZCggMJBvNrNgcNNrM
jlVpVpVVQDHdFVlmmmQTlzpjjGstWLsSbsnnnStWLRhnht
prLMDDjNCLZbdFLGngdLBv
VQHmhWSSzhWHmPJRJhSmVHJPFvgTbtnTbBtGqbQnbdqgTFqG
RzwzzhwhwNCvvfpc
wQgmZnhmWVtwQmnnnQbQhzwsFcRPrFPvRJhPlPPBBBFvJv
DdjqMMGLLMMGqTGdMqdMLdBBJsJPJBJJrrBFcqRlPlqr
DsddsfMsWgfzftZb
lcqlFSFwBBPlNwPlvSlQfWsVLTQjzjWVfLsWVq
HMMbMHMtJHgFzzFrVVtfFQ
RMFpCDDFcCNBcZvP
gwDrClhppDDPwPhnmPlwDrlDjMFfMTjMTjJmRHHJBJRMJHGj
LbbZBSvSLVRHffHJHJGZ
WztdtLsSvNQStbbtzdStthWhnwnPBDclgwwnrwllCC
MnMMBppMBDWMhpnCDBgCBmRbstvPvvbGltSPVGlVPWVv
TrrddJHjNcTqrrqdFcqZwSvLSlGGPbtFRbLvFVSRPG
JTccqTcwNQcTJrZwNJcJqHwJBQDfhCBCpCQpmpDfMRfCfBpn
njVcjHfGjVjpTCpMWprW
tsSsQDvSqQshDhtmWpnQnmMmbrpdzM
FNhsDDLNLnNllBqfRJGBVHBPHRRBZZ
hFVdlFSFlfZdRhgWgdWnnnfGpMNfnLMQzQQjMD
RsrJRHsvBcvHBHjDMMpDQDjjzDHj
BcCmBqvrbbqJgmFZtWdRVSVV
FzzdDJrJCFSFRqLlwsgspsBCpL
HQdWhMZMVwqLMllw
bbQtcvZcmHtNPZcWthWRvrdrRzrSDfRSrzjJjR
bTFZzHjZNJHzLggsJgbdsWcdcShWCwsSSdvGvv
VDBmntntfCBGGGGhRc
fMnnPDfmDlmnMPmtmttnVlHzZzNLbFbLbhzJJjMgJFbb
GzgJGPRrMSgTgpgH
hcvWhBdhcfPFvmFQvwfbHMsMMbpDpTDSSHsHpd
LmcvFFlcWQlFlfPnRZPVCJzJClCz
DdCHCHrmHRgghTHH
pFVZFwfssMsgghML
tSnphvhtctSSQNDqNdmrWGvq
rqmtRmGmcWrRRQprRRnfbGMMlPGGPblwMbTP
BHHhVZSvDNdhvBVhshbzfPbTmDfnwPwzPgbl
ddvBsSSdsLdshLsLpmWqcWrCCrtFpQ
wZPCwdPCHrnLQCGZDcPRqllzqqBzjlqc
gMmgnJspsvTmWNVWNpTNWNcDcqVjqDcclhSzllRSDzqR
JnWsgMnngmttFWWMdrwCZwHfZfdfGdFd
wwgNgrsWvbfBrqqsWbjDCDDDCDCmFbSmLDLlSC
QdpdzQTVdzRMTVVzcHTQLnlFmZHPSChCmlDPPHnP
dRMLVttzzVtTVQVqrrrgBtsvWWwtNw
vtBvntlqMvfnTfPDPhdRNbhdTFzF
QLWcmrrcgmCgCcsgcQWlWWrrDjjzzjsdFDdRhPNDhhhzDzPF
GGWHcCQcCCSlmmBVMGVBfMqwJtqv
cfqfhDRwhqZgRgRzRvcfhBSrsBnrDBBJWrnrWrSmmr
VCTVjGCTCjFddQntmrsVsJvrtrrW
PFQGpFbvPRMNqgRq
MmDgZZGMjZGfZRFztzCtCjzSrF
cBNpPJpBdNntcBHBccJlsSVVzzSwlCRrCnzsFw
PPBJLPPBBLPHBNQgqfMQtmTftGGvhq
bbZnbnVVgVSnbgZtntZrltsprpMCJvpqdJmsCMMmvvCq
BjDcjLLDzNjLDcjDzhcDNLLLHdpmpHJsqsMMNfCHfJpspqvp
dFLTFBcBzjFLgTbQtRgTVTlZ
nqNnrBRjLnjLZCqGGlqSGWlWDS
mTJTTcTJJfJfhhhwMbQDPWCQFCRlbDCSDDPl
dhMcRgJmgRrBrrrNgrLZ
GvJvJSGZFrGmmbmCrWnhjncLctcWttVqjLBB
wDlTzwlHTncRTqnRBt
gspglgzDzdPDfpgfdDzsgMPGvZJBrrbZGJNFmCFvmFvFvM
RLjMZZzfvNLBdjQfBfQdhRfSTVlcVqGbGcLGlbmqLVccmm
FggHCwsggrWWtCHJDDHtWrTNNlqSnlTlnGVTmWGcbcbm
PtpttrwsJssPsdRQvphZNzdMBh
NqqpZBHqTBpPNpPpGwwMPGTJjjLjQljGmtLfftllbJQfGf
nHczcrSFnVWSlrltrgJmjLLQ
SvzcDDVVFzdzhndCFSvnhcDspRDRDMPpMHRNPPZqppwM
FRSbVCSFFCDMFjRMjSSVFSWggMmWtWngJWttWmmJctnt
BPwcQQcQqQmWHfgrfwrh
PPlBQdNQvdLzzvclczdNRSbpLSbRbDjFZFFZVsFs
wtrrVhBbpcZSSjBfSfmm
MDWTvTMGMRCDCTQWsvfrRjjFfHlFmjlmLlHl
gQrTQvQDssdNWGsTstcbptwVPqcbpNqttP
jtGSwGQczrzjtGzrcsJwMRqMVMwRVMWFvVTWFV
DhLgnDLndDHmLvWqpTHqHHVNqF
LhdmPhfgZnZDlPCPmDfljQtGsJtBsWjGJzJSWBjC
zHDjcjBjTfjjfGpf
NNFTnNwPNNdqnJdFnqqTgmgftfftrWCZGbmrpWttmW
FLJqVNVNhnwnTRsRQBlQzShs
HJGJGJzzHHQHfJHsnNsGMbccMrTgbr
vddSCCjdmVvDDmvmBVbbBchcrrcscMTTnscn
VjWdFCVVMWWmjdSVFSVpqwwZttfJJltJZqltppLw
SnmPBPBnMLnPBsSgSDqRNRRccDfNcNQQRg
lZVWtWVzCjvZzCCGzDwbwRwtqJwJNTtDfD
zCzHZFFFfdLnBfFf
NRBFpNNJgNbWbJLRpRbWNtNpZllCZdjjZfjPVljTVCZQltlV
sDqHmsHcDrwHhMDlfCQfVBjDPCTd
MnGGcqwhhsrchcmGpzRJSSGGJWJzbJBR
LBzjQQzcjWvHWLnVDdnHRffHDCVR
rmJSrPJJsbNZssGSPrFpddfGwDRRpVjVpCGdCp
mPsrmsNTrPNLTjQlWQhqLc
MSDFszbhbRRTRdwhtw
PWmCZCmZVvGqMcjmJRpdTTtdLpqwdlll
MWGmmCVHvMSBDSNbbHHS
mBwSBSfSPHZCLPZSWwfPppTndVpdVncFgcgPpP
rhQJjzQjrltJzGqCrGJTvgqRpnTgFgcFTVFqFR
QbhGMJrhzrhQGQCsjwMDNWBDSZBZwSBLmM
bQfDPgDQbQNGPgflWfvMZcRMMFmcvMfZ
BLqSssjnzpBwszqwzFCNMvzWvRvzCCZFvc
BpNpjnNHnSpssqLqrBLLHjdhTPPDgbggllldhTPdrrQh
CvCMqNWVVqqPvNvvChhhdSnFHwBdWwhfdS
gqTZGGjlmclrZjlmSndSDwfFhhDBHm
tRrZpgrcctbbltRpgtqCVJCvPsRvsvPCQPCLPz
dTjRdWDBRzvjfzTfvTJPtJttsSLqHsSQJw
hrJNmbnFNZrbhlCsqltqcQcQSQqwPL
pVNhFgZphZmjzvjGDJWzVJ
gWzQhCWbQnCCFgCJnFQnWCzwjrHjjHGTwHGrhLwjjjtStL
splcpqDNDqqcZqRlspwHbjVrjjHTrwSbtVNV
BpMslDqDmRDRsBRBJPPnbzCfvQgmCWJb
tRtgRQWCwlTglHZHTglCtTdbbfvhWpbSBbhWzzbfGpfhbb
cqZVMJmLqmNrsJMDbzGrGSvzGBhvvG
mmnJPMZcclFRdnQtCQ
QVQVqfFzVVQQrQwZsCTrBtTrccTtctcJRRjT
vNNPnvGbBtWBLvBf
mMHbfDfHdHGmnhDDqZFDzVSQzF
NNlTNFCRTrfllTZsPWSsFPfzJdVQVpDQVszQVtpbzJMVbJ
LNHjNHjmLLjNqvGgvVQJQDVLbDVDpdQQzQ
nqmqGHjwgHvgwGHjGgccNTSWrrlCZrFfPSFFCP
qWzCQqhPCHjHmqJhqvqmjRgSFMTFggMFTFVRVVTgTm
SptGsDlnGfnDLgTMTwgRFFFs
bBcntZdpGZZcctlGtDfnDnBCSWqJvQhqjqzjhJqJQCQWPd
SjZJrSSDShddqLvPqzzdwq
nTssfRpQQmQCHlPBBgGmwVGzwm
TWQsbCRQFHFWQRTpzRHRsRrMtDrjhjbtMbccrttJjJht
cCChVMwPPMHCPCCPrvJnntdTJSvTtdrSRt
FGfFDBhGGlfGGfWJWdbSRSnRNbTvdn
fGpGlDmBhflgfDFmmfFpcVzMzqZZzcCPQVZzqP
SmgtSjGPjppBjbqqWTCZDQTHHHTg
VsFfCzLvsMfzNfNRhVMslzlHqrWrQDQcqDqTrLWHcrWJJW
dsRdsNCvNMVpwPdnnGbbPb'''
        s = advent2022.Day03.Solution(text.splitlines())

        print('\n')
        sum = s.findPart1()
        print('sum is ' + str(sum))
        self.assertEqual(7997, sum)

    def test_day03_part2(self):
        text = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
        s = advent2022.Day03.Solution(text.splitlines())

        print('\n')
        groups = s.findGroupBadges()
        print(groups)

        result = s.findPart2()
        self.assertEqual(70, result)

    def test_day03_part2_puzzle(self):
        text = '''lvcNpRHDCnTLCJlL
RFZggsMrjTFGCJmdmd
srsBZgBqwBqRZbzqtHpzzDNtHDqV
CCTPpCvlpzzZQQQflrzbQDttTJcgcggJcHtcddtdhT
nMLBRnGsFFLznRFRLMMNBnNLDRDdhScJccctdSccJJgDDHhH
GVBGVBsLjsrrvfzpjpfQ
dzVRSPVVBVDSPzDBQVSQFFlrclMplpMJMtPJlJvHZCMt
TjmGmbhjTnTmwhmrvvrHcZvCHZMl
fnLwwqfwfqjghHwGThwfTGGBFVDFFsszSRVzRBsdBDgFsV
CCWFCcdDWwcWFpSvggnzRRQszngJwT
mGtqqLrqfmmLNtNrgTjgJzNQlvJTvznJ
tnhVbhMLLZZrnWHPSHDBWbWBFd
nQhvgnCQjSSSTTSMCsLDsfPfDlsPJMWLzL
qrqBFFBbrVRLszLfsqdqPW
bNFFRbBcFZNrZRRRbprNpFrHSwznTnvSwgHvzCSSSjnCQwgz
tnnZZVmwmqtvVdZqnddQQHHTHQLsFTnsPrrgrQ
MzMflMGpzGzPGPgjLgHrGj
zPfhMJDDMJfzlhcRJvVwcVtwVcmcbqqtbv
GVzrBVcPVfGrzVVBcQJlGGRCZSSRtSdRnGLJ
wbjvHWbLvhFppjZdtwZRNddtJwlR
pvMmbpFFbqqqvWHMFvzrLDMMrMTTrVTPzVzc
qPmgpmwpwqWWPHdjdTNStzNLMztSWtMNtz
lVFfJrFJbbcsvcRVRZzQCzQNSZTZ
DGbvFSDGbDjnqgjwmGdq
DMnpnpwwnpmRRmcRBDnDwpbRQHssHqhHCHHSsQddHZQQcqqs
JlZjjlJgNSddfsgQdf
GvrWvzNjvPVLDpbPZwBP
drQDzHsHrdZWqDSSPwmmJDDbvbSJ
hphBhCMFlBtBtGTJMJsscPwTjMJv
tlBCGFgVFNpGClFFVGGtFBZrdZQznfdQQrRWVRQdRsVf
NjdCLdjzzlNdjwBBtZqpqPJQbN
CsDWcHcGHtcBbJPpbP
mGHSssSgSsHFSgGrSgmlLzCdldllrCVCLdnfnT
rDLLzRmbcLJRtRSvSBdZtSTp
MFswshwgsCsjghgFBsGssjlZpfpvdSHfTdCZTSpHtfddTH
llwlwGjMPMQQnBMswsFgglPVcWcDcbWqLWbbLJVDzrqnVr
pqmmcSTLfSSSMFlf
rHWtPWnHtlrlDntzWwtBFdzCFMRCfjRQFfgMRMjC
PWWHDVZPDDJVlWHncGGbqqTVvVmpGTmm
wLBtWhGWJBdMmZMs
jgvNCFvvGppGnmNJ
DDRQTgcvjTPFqGHhRVhLRSVL
tPPwLpBpDpgLSPvgQCvsLPjdjNZrJZsdZjsrsnZNjbZc
lMWzWMBhmMhRGfVRffHmMjJcJjrNNZnjJcWjNqJnZJ
mFMzhTmBGfHTwgPgtptFpPgP
qCcqJQHslgtsQsCZmPWNSRNZTPBBCN
nnLpjjnvwwvDnrGwFvbFjwPgPWRTPrrPShNhmmNSRRPN
bnwdDLjnzGgvFqdJQcqVfQVqHt
DfCzDCCTDLDBCsdjzwdrHjbRgjGH
MSStMScccJtPptJNJZtJJSrFdwPGjFFHHwsggrwdwRdP
nStlpVlhhNSshZlcNZnMcctpBChWBQLqCWqmqvmBCBmQBqmL
RfLHNvfLfLZQBtRZsBfffjVqGvqpGSmJpgrJpjGjrp
FDbPCMzbTTDDPmzrVzqppJBrBj
DPcWPWDhlbCcWBsQZZfHtdwf
fbHfPfHHfPZWgZfSGpqNBqdBBjpjdPBJqv
rnVNCwwrhhDrmmvcmjdDqcmB
hFRrslFRNhFzVthllRCRCCwnQtSGfQgZZbbSWQLSSTZWbQTt
nmVqTFCmTVbnvVCnqwFrffjhZLffhNrNJF
StBHWDgMBpHMBHDzLjffjWwZJNNfNZjL
wBBcDcgzdVbbQcnQlq
MfGCtqGDhjDqHhrjGCcJZZBwHRcspZsBsHRc
PFFpLFSpzVdSTPgnzzdPPZBRcZBwBJRcWJBmJW
vdTTzVpNVpfCChMGqMvr
VtZzBzhtlrhznFlBfgrfZgFrPjGRMGjRTmSjRjRTHjfRHmRv
DQpnsbJCsNNnpNNJsDQdCDcRmHPGTHTHRSmRmHjvjHSpSS
cQbnQdNLdJJQJJJDJWnFwzgwBthrgZBwBgFLZV
VhRRgmhpFjFFBDVPGPWQPzvvMMWfjf
qcnbnCbfLqJrCnrcdbbLrGSlzWsQvsWWzvWGdMWGQl
bnfbwrcwCrHqnHcZhFBTBVRDFmpBHB
lrtqltJJJqSTWJqVHRnsRhphdbfbzBdhsRsd
vSZCgZMMLSNvCQLPLDPNgZgnznzBfsGGnQnQGdnsfhsfzb
CMFLgmPgFFNMFDDCgLLcrWrjTTjtmSJqlWTTwWSr
LdjljBdZMFdZFLLLgPvWzQRzCsCmCVssmFSW
TJttwDhnnTlWsQzSQQDvWm
HtcnfctJwtwrHhrwhfHhJpjNLMZBMgZLrBlbbLNPNj
qqhNchPdpqTTNqpDmmvvGzVfzfmvdH
cwccjsFwFjnwGwQDfVVVVv
FbWjcRsLLFngBrjpbJqCJZTbJZNClq
lhznMTSzSnjhQGtVPQBdGB
msfNDDJLWslJgfNgCrmLdtGQFVvdGQPZVttBFP
RCrJJJDrJRsfgmbsrNsrlDMTSMHcjqwzScjMqqTjbbSc
nNgsvNWDRvgnRNVCFddTNZTNZQCTFZ
lffHJfHSPmSfvLlbLmpZrCTFTtrTQHqtTrCCrq
cpzblplpbvMzWnsDDB
CgtvQvJvMtWttvwftCdWvDQrfsFcrqnlcnqZZFRcRqsnhF
HzLzVBNLjHqnhzFlWFlr
NmBjLbVVbmbTLpTjBNVLHNdCtTSWQvCgdwSwJtWQwdSD
lncHcnlccVSLNSQNslncLcrZJCrgPfJZDrggJCCvZPHC
jRqqRmmqFwRFppfPPppPBfpWBvZf
wmMqjtTdjFwGGdtNhQbVfhntcNLVbL
HFBgMjpbpddMpbHdgHLLRNwhwFLDtNSRDLLD
zsCnfqZflrlnhhrtwNgggNNL
CGqnQzlqlWWMWgVBGg
pQnvzjztpzpCmtzzjzpnBHrJNGlqggMMqgqlNWgfNNqNCP
sVTSwddRRDVShwRwRTWgPNqMGQMGNqMWslsg
hDSTQhcQcHrtcBmZHv
QRmQfvQpWpswfZWWvNbhlMglgFbZDldlbL
rzHqtcnqqVjqjGcHdLdFdCFdCbLDnMCh
DGcGGSPDpWTsSfpv
llfMHTmvHlfZlFZRzgQzsFBLtLzFGF
wrWNJrdJhRmhGmNh
DWrrJjwPjCdPDwdmwnrTZnZZcqZfnqbvZfHvql
mPmVJJmNZJmlVBPPrZpWcFWbGWbjgqNbdqjSjg
nMhzwRhwvhMDMgWHRdGHgccggd
sMvnhQshMwwvdvMMCwBtlZtplZpTmPBVZVlC
ltlRzpncRglplzhFwFwzZZMWLWZBqnDVZLDVZQQQ
SJcdvJscNSsGcSGCSJmsTQDTVZQTLTQQWCTTMQCW
sPdJmcvsJvGJmdJmfpwftfrlztrRlPfP
LdPrWcMCWCfPdMJgdFsbRRHsRSHRHHcFpH
hVVTQmQTnRFLFsmzps
qthVVwZqlQLQhNttDDDWrffDJJJDrgNP
BTjTNjtlPrBjjrljbnMFfhVWFFhlMWMfHdll
mzcgZvDggDDCJCZLvsLJLcmVqWVSVqFLfdHHMWVWWWffnF
cmmcmzQDZQJmZCnDRgQCTTwjpTtwRjrbNjpPpwrj
rMbchQphhCSbGnzSbl
qFtgvTTqFFFFJGzWJG
NZjGqGBNjNHQrhpPNHQr
LnLmbtTtTwtLcVfFFLtPrfPrfqqqsqhSvrhrhh
BzJWzZRZJzJvlZJCZgZZpJHCqQDhNQPDqDDrjNsjPPNrhSCN
lpJWZzJpgHWdWMgHlJMZzgpJLGVLGGvwVwtmcGbvGMGVvncn
WdBgdqRgWqHmNNwsGgcQ
ptPVbPbSbMJrmsVzRzhwmcGQ
SSbvrJbJtCDZfTqdRfCdBZ
WDNNWvPpvNJRRbGLsGMnnbmG
qgFdBwgVdjwdtjjdBgMgGmLQsnZrnZssGswsmLrw
FqTCTtqjdjVqgCqSMJMTvPThTJMNDh
brSSSpZjVVWdfVrHPhRBggNNGwHr
fDlLzFCLMvnMMJLNHNCBQwNhRgwRPP
MJqMmfzDvFtLDtmsVsZZTsSScWcsbq
CSZlllhSdnDrrDdJjqjzbSGzGvwbfHMb
gTNvVNLQtsFpQHqfwfBfVMfHzf
QgNmWTtmTcmmdmrZRvnlPl
SmzfvfjvjbjLNJjD
cFhWMhGHTPhccMQQGBTFGwbVVwdbddJDvVJLvDDHvd
GFMBGcWTWhcGrhFZTTchQsSfgtmnnRvnmnnRgRCrRS
ZTQHVZsZSQpQQGBMGqfBRbRB
CwtLDtNFcPnllwnqvMgbvGVfVfBG
VClLWWFPPhlhctsTrrSpWpmszjZj
HChzPltNnnHtnpqSpHpFpSfSvS
mJmQssZJLdTQLcbjlGLGfSgMbqwwSFSMSFMMqMwS
JdBLlGTjLjjjjdmmBPnRzCBRNPhPtPWPtr
FPLHMHqqPMgFLLggsMghTJhwtDSSJDltJvtwdvST
WQfmjQZsjfZNQCrZCNZQQWQBCSClvdwTSClwSwlTJvtwJdbT
BpmzrWcpBrfmpsGPGFqPRgzqVPLM
bHjccpHwGHJTfPlffPwr
VtChMZVhhStZdfTCfJvcPRCTJn
sLNLZcdNZZqZqqVqSNWtjQDGHssHGHgQHDBgmsDg
CdWgCpddwgClFlmmVTBbRtRtbntBVVds
vcJGhPLPhJvChLhMLfccrvfvsVVbsGBTTBnVbRzBVstsGnbz
vJJHhjcCLPPjQPHLrSZmpgmqwlWZZgZZQm
VpTFCFtrjCdJdjHVFnSjszSllDjsDzgvzl
fhmhZBMtfZfGBNfNcmsbZnzSlRsRggslsbnv
qPLPhMcLhPfNWPpFrdFdFTtJ
nlgQJhJFlncMzMWZMFvw
mDdsDfHjHsjHdjTLfpDsbDcNzzwcRbZNZPMcCPWMRPMc
sqqdwffHjTmdmpffmLddTTGDnSJtJBShVVhrGVJtShrlBBnJ
CrcMcMDBCmLlZdSd
qPjGjnQPqWjgZmTdlFwTmqLJ
bnPnnzHjbPznzVpdpVDcvprr
TCScMQcQCrssJPQhQs
VpfnqqfdVVwpqvqwGbDPPsjgPShDSsJhlnSl
qffdmGpfwfbfvVqpfwwfbdqRMTSTWNMWTmZLTzTCZTMLWC
QQPpPbPbDNplSJrCCj
VdMzffgnRmVdfVWRvlrCTjRlNBvrrlrr
mGgNdthhGgMWWtsFcHcHwqLqtH
HrPFVqVppVpDjFDrVbCpDFJSLsmwjhjGLLmthJLJLmZs
WWgRdMdRMnQnRzWvPSssPWssJmhsshtG
MnfvMlnQccvfMlcTRMQdRfpHPDDDpPrDTbTBNbHbHDCq
GWWRsSwLhWsRsSbsPttThZqrNBJJBgPNCJCCqNMNgP
HpVDTHzfFDpFfzHzFVcrBZCggMJBvNrNgcNNrM
jlVpVpVVQDHdFVlmmmQTlzpjjGstWLsSbsnnnStWLRhnht
prLMDDjNCLZbdFLGngdLBv
VQHmhWSSzhWHmPJRJhSmVHJPFvgTbtnTbBtGqbQnbdqgTFqG
RzwzzhwhwNCvvfpc
wQgmZnhmWVtwQmnnnQbQhzwsFcRPrFPvRJhPlPPBBBFvJv
DdjqMMGLLMMGqTGdMqdMLdBBJsJPJBJJrrBFcqRlPlqr
DsddsfMsWgfzftZb
lcqlFSFwBBPlNwPlvSlQfWsVLTQjzjWVfLsWVq
HMMbMHMtJHgFzzFrVVtfFQ
RMFpCDDFcCNBcZvP
gwDrClhppDDPwPhnmPlwDrlDjMFfMTjMTjJmRHHJBJRMJHGj
LbbZBSvSLVRHffHJHJGZ
WztdtLsSvNQStbbtzdStthWhnwnPBDclgwwnrwllCC
MnMMBppMBDWMhpnCDBgCBmRbstvPvvbGltSPVGlVPWVv
TrrddJHjNcTqrrqdFcqZwSvLSlGGPbtFRbLvFVSRPG
JTccqTcwNQcTJrZwNJcJqHwJBQDfhCBCpCQpmpDfMRfCfBpn
njVcjHfGjVjpTCpMWprW
tsSsQDvSqQshDhtmWpnQnmMmbrpdzM
FNhsDDLNLnNllBqfRJGBVHBPHRRBZZ
hFVdlFSFlfZdRhgWgdWnnnfGpMNfnLMQzQQjMD
RsrJRHsvBcvHBHjDMMpDQDjjzDHj
BcCmBqvrbbqJgmFZtWdRVSVV
FzzdDJrJCFSFRqLlwsgspsBCpL
HQdWhMZMVwqLMllw
bbQtcvZcmHtNPZcWthWRvrdrRzrSDfRSrzjJjR
bTFZzHjZNJHzLggsJgbdsWcdcShWCwsSSdvGvv
VDBmntntfCBGGGGhRc
fMnnPDfmDlmnMPmtmttnVlHzZzNLbFbLbhzJJjMgJFbb
GzgJGPRrMSgTgpgH
hcvWhBdhcfPFvmFQvwfbHMsMMbpDpTDSSHsHpd
LmcvFFlcWQlFlfPnRZPVCJzJClCz
DdCHCHrmHRgghTHH
pFVZFwfssMsgghML
tSnphvhtctSSQNDqNdmrWGvq
rqmtRmGmcWrRRQprRRnfbGMMlPGGPblwMbTP
BHHhVZSvDNdhvBVhshbzfPbTmDfnwPwzPgbl
ddvBsSSdsLdshLsLpmWqcWrCCrtFpQ
wZPCwdPCHrnLQCGZDcPRqllzqqBzjlqc
gMmgnJspsvTmWNVWNpTNWNcDcqVjqDcclhSzllRSDzqR
JnWsgMnngmttFWWMdrwCZwHfZfdfGdFd
wwgNgrsWvbfBrqqsWbjDCDDDCDCmFbSmLDLlSC
QdpdzQTVdzRMTVVzcHTQLnlFmZHPSChCmlDPPHnP
dRMLVttzzVtTVQVqrrrgBtsvWWwtNw
vtBvntlqMvfnTfPDPhdRNbhdTFzF
QLWcmrrcgmCgCcsgcQWlWWrrDjjzzjsdFDdRhPNDhhhzDzPF
GGWHcCQcCCSlmmBVMGVBfMqwJtqv
cfqfhDRwhqZgRgRzRvcfhBSrsBnrDBBJWrnrWrSmmr
VCTVjGCTCjFddQntmrsVsJvrtrrW
PFQGpFbvPRMNqgRq
MmDgZZGMjZGfZRFztzCtCjzSrF
cBNpPJpBdNntcBHBccJlsSVVzzSwlCRrCnzsFw
PPBJLPPBBLPHBNQgqfMQtmTftGGvhq
bbZnbnVVgVSnbgZtntZrltsprpMCJvpqdJmsCMMmvvCq
BjDcjLLDzNjLDcjDzhcDNLLLHdpmpHJsqsMMNfCHfJpspqvp
dFLTFBcBzjFLgTbQtRgTVTlZ
nqNnrBRjLnjLZCqGGlqSGWlWDS
mTJTTcTJJfJfhhhwMbQDPWCQFCRlbDCSDDPl
dhMcRgJmgRrBrrrNgrLZ
GvJvJSGZFrGmmbmCrWnhjncLctcWttVqjLBB
wDlTzwlHTncRTqnRBt
gspglgzDzdPDfpgfdDzsgMPGvZJBrrbZGJNFmCFvmFvFvM
RLjMZZzfvNLBdjQfBfQdhRfSTVlcVqGbGcLGlbmqLVccmm
FggHCwsggrWWtCHJDDHtWrTNNlqSnlTlnGVTmWGcbcbm
PtpttrwsJssPsdRQvphZNzdMBh
NqqpZBHqTBpPNpPpGwwMPGTJjjLjQljGmtLfftllbJQfGf
nHczcrSFnVWSlrltrgJmjLLQ
SvzcDDVVFzdzhndCFSvnhcDspRDRDMPpMHRNPPZqppwM
FRSbVCSFFCDMFjRMjSSVFSWggMmWtWngJWttWmmJctnt
BPwcQQcQqQmWHfgrfwrh
PPlBQdNQvdLzzvclczdNRSbpLSbRbDjFZFFZVsFs
wtrrVhBbpcZSSjBfSfmm
MDWTvTMGMRCDCTQWsvfrRjjFfHlFmjlmLlHl
gQrTQvQDssdNWGsTstcbptwVPqcbpNqttP
jtGSwGQczrzjtGzrcsJwMRqMVMwRVMWFvVTWFV
DhLgnDLndDHmLvWqpTHqHHVNqF
LhdmPhfgZnZDlPCPmDfljQtGsJtBsWjGJzJSWBjC
zHDjcjBjTfjjfGpf
NNFTnNwPNNdqnJdFnqqTgmgftfftrWCZGbmrpWttmW
FLJqVNVNhnwnTRsRQBlQzShs
HJGJGJzzHHQHfJHsnNsGMbccMrTgbr
vddSCCjdmVvDDmvmBVbbBchcrrcscMTTnscn
VjWdFCVVMWWmjdSVFSVpqwwZttfJJltJZqltppLw
SnmPBPBnMLnPBsSgSDqRNRRccDfNcNQQRg
lZVWtWVzCjvZzCCGzDwbwRwtqJwJNTtDfD
zCzHZFFFfdLnBfFf
NRBFpNNJgNbWbJLRpRbWNtNpZllCZdjjZfjPVljTVCZQltlV
sDqHmsHcDrwHhMDlfCQfVBjDPCTd
MnGGcqwhhsrchcmGpzRJSSGGJWJzbJBR
LBzjQQzcjWvHWLnVDdnHRffHDCVR
rmJSrPJJsbNZssGSPrFpddfGwDRRpVjVpCGdCp
mPsrmsNTrPNLTjQlWQhqLc
MSDFszbhbRRTRdwhtw
PWmCZCmZVvGqMcjmJRpdTTtdLpqwdlll
MWGmmCVHvMSBDSNbbHHS
mBwSBSfSPHZCLPZSWwfPppTndVpdVncFgcgPpP
rhQJjzQjrltJzGqCrGJTvgqRpnTgFgcFTVFqFR
QbhGMJrhzrhQGQCsjwMDNWBDSZBZwSBLmM
bQfDPgDQbQNGPgflWfvMZcRMMFmcvMfZ
BLqSssjnzpBwszqwzFCNMvzWvRvzCCZFvc
BpNpjnNHnSpssqLqrBLLHjdhTPPDgbggllldhTPdrrQh
CvCMqNWVVqqPvNvvChhhdSnFHwBdWwhfdS
gqTZGGjlmclrZjlmSndSDwfFhhDBHm
tRrZpgrcctbbltRpgtqCVJCvPsRvsvPCQPCLPz
dTjRdWDBRzvjfzTfvTJPtJttsSLqHsSQJw
hrJNmbnFNZrbhlCsqltqcQcQSQqwPL
pVNhFgZphZmjzvjGDJWzVJ
gWzQhCWbQnCCFgCJnFQnWCzwjrHjjHGTwHGrhLwjjjtStL
splcpqDNDqqcZqRlspwHbjVrjjHTrwSbtVNV
BpMslDqDmRDRsBRBJPPnbzCfvQgmCWJb
tRtgRQWCwlTglHZHTglCtTdbbfvhWpbSBbhWzzbfGpfhbb
cqZVMJmLqmNrsJMDbzGrGSvzGBhvvG
mmnJPMZcclFRdnQtCQ
QVQVqfFzVVQQrQwZsCTrBtTrccTtctcJRRjT
vNNPnvGbBtWBLvBf
mMHbfDfHdHGmnhDDqZFDzVSQzF
NNlTNFCRTrfllTZsPWSsFPfzJdVQVpDQVszQVtpbzJMVbJ
LNHjNHjmLLjNqvGgvVQJQDVLbDVDpdQQzQ
nqmqGHjwgHvgwGHjGgccNTSWrrlCZrFfPSFFCP
qWzCQqhPCHjHmqJhqvqmjRgSFMTFggMFTFVRVVTgTm
SptGsDlnGfnDLgTMTwgRFFFs
bBcntZdpGZZcctlGtDfnDnBCSWqJvQhqjqzjhJqJQCQWPd
SjZJrSSDShddqLvPqzzdwq
nTssfRpQQmQCHlPBBgGmwVGzwm
TWQsbCRQFHFWQRTpzRHRsRrMtDrjhjbtMbccrttJjJht
cCChVMwPPMHCPCCPrvJnntdTJSvTtdrSRt
FGfFDBhGGlfGGfWJWdbSRSnRNbTvdn
fGpGlDmBhflgfDFmmfFpcVzMzqZZzcCPQVZzqP
SmgtSjGPjppBjbqqWTCZDQTHHHTg
VsFfCzLvsMfzNfNRhVMslzlHqrWrQDQcqDqTrLWHcrWJJW
dsRdsNCvNMVpwPdnnGbbPb'''
        s = advent2022.Day03.Solution(text.splitlines())

        print('\n')
        groups = s.findGroupBadges()
        print(groups)

        result = s.findPart2()
        self.assertEqual(2545, result)

    def test_day04_part1(self):
        text = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''
        s = advent2022.Day04.Solution(text.splitlines())

        print('\n')
        c = s.countFullyContained()
        print(c)

        self.assertEqual(2, c)

    def test_day04_part1_puzzle(self):
        text = '''222-65,22-66
91-94,63-91
6-88,5-31
85-86,64-86
40-65,40-65
25-82,24-94
68-69,68-92
60-91,89-92
3-72,3-73
44-85,84-85
15-72,14-72
84-92,84-92
10-84,3-10
32-62,31-61
14-98,98-99
24-78,24-61
2-5,5-89
58-95,58-59
39-93,92-93
11-82,81-82
12-37,13-58
53-92,52-91
1-19,3-18
90-91,91-98
20-72,19-71
91-91,1-92
71-90,71-93
77-94,77-94
48-76,48-76
48-58,48-53
3-42,2-14
3-4,3-94
4-9,7-8
14-97,77-97
66-66,17-65
12-99,13-98
29-74,30-74
30-93,29-92
43-44,42-46
7-9,8-81
21-77,1-89
85-92,86-91
56-72,73-73
16-75,17-42
2-85,1-85
97-97,13-98
3-94,3-33
55-91,1-99
14-21,14-15
1-3,2-98
43-57,43-56
9-95,8-10
18-80,81-92
19-72,19-71
17-94,62-86
45-59,46-60
73-88,46-87
63-82,82-86
63-88,87-98
20-28,20-56
76-76,70-75
36-73,35-73
85-91,85-90
4-82,4-85
2-2,1-98
27-71,27-81
13-79,13-14
32-43,33-42
53-97,98-99
41-62,42-66
23-78,23-77
6-92,6-91
1-86,1-85
3-89,84-90
5-79,78-80
51-73,50-72
48-81,49-82
32-33,33-88
4-97,4-97
13-88,14-65
33-74,32-75
26-48,48-78
1-46,16-33
2-6,6-67
5-93,5-93
5-6,4-22
68-83,38-84
10-70,18-69
10-77,70-76
4-94,3-93
22-95,21-99
32-72,31-92
30-75,29-74
3-96,95-95
96-96,61-81
52-77,53-77
1-2,1-94
4-96,3-98
29-58,30-56
31-49,30-60
33-79,27-80
10-51,8-11
8-36,8-36
36-93,36-92
9-60,10-15
48-80,79-87
39-41,40-49
48-87,64-87
30-34,2-57
81-82,13-81
3-15,15-99
37-72,38-72
10-85,5-84
6-79,78-93
75-80,76-84
55-72,55-55
8-66,9-9
54-64,63-99
6-77,7-48
2-64,1-32
31-91,90-90
19-66,18-94
58-75,26-76
58-60,1-59
90-90,87-91
5-91,5-91
67-67,3-66
13-81,31-36
31-61,23-60
18-92,17-91
85-86,15-86
10-68,9-11
52-85,12-84
7-27,26-26
43-50,21-50
25-75,74-75
7-7,6-24
1-63,42-62
11-12,11-66
25-94,93-93
13-48,31-47
3-58,59-59
1-54,1-1
5-5,5-96
59-70,7-71
18-19,18-81
9-96,10-84
33-41,33-38
1-99,1-98
69-83,68-78
19-82,8-81
2-23,3-24
57-90,57-98
75-83,74-76
68-68,16-69
2-86,1-33
5-92,6-14
51-76,52-75
25-72,24-46
9-76,10-50
5-51,23-52
19-83,20-93
33-69,44-70
22-69,23-69
55-61,40-62
2-16,16-81
66-98,66-96
27-85,28-86
43-93,88-94
19-83,32-82
2-92,26-52
87-87,45-93
40-81,97-99
4-97,98-98
19-95,6-20
52-96,53-53
2-34,2-97
62-83,63-66
9-74,8-81
53-83,53-83
35-73,11-72
9-97,10-95
9-51,10-50
25-27,26-35
45-60,45-46
12-65,28-65
40-92,40-91
5-5,4-98
72-91,90-91
16-87,17-91
97-97,18-96
77-78,75-79
22-48,32-47
70-70,35-69
45-98,99-99
65-83,83-92
2-95,4-88
5-10,10-46
4-84,50-85
58-58,15-59
11-80,3-22
46-48,3-47
29-80,30-30
34-96,5-95
65-97,32-96
26-31,30-46
12-12,12-77
26-92,26-92
29-92,29-90
26-27,27-30
4-30,3-29
29-57,1-28
99-99,42-97
92-97,78-98
3-90,46-91
44-76,43-75
24-28,10-25
1-95,1-52
3-3,3-61
39-94,40-93
41-86,75-94
28-28,26-27
21-94,21-97
12-41,41-54
4-49,3-5
75-90,44-75
4-83,78-82
5-93,93-94
33-90,89-90
12-32,13-98
41-99,98-99
4-67,3-38
95-95,11-95
7-46,7-46
11-18,18-24
7-92,12-57
60-91,90-91
86-94,86-95
11-58,57-57
7-10,10-97
1-46,3-46
1-52,1-2
16-94,74-93
7-98,18-97
8-76,8-74
37-92,54-91
63-86,88-96
4-55,47-58
70-92,91-95
73-77,71-77
3-99,5-99
56-58,56-57
53-73,13-74
88-97,97-97
52-63,51-60
13-94,14-91
2-93,3-99
42-75,67-75
38-39,38-88
8-93,92-97
13-32,17-31
3-17,16-53
1-1,3-95
5-88,4-87
76-89,47-77
5-54,4-55
45-95,90-96
81-89,36-88
31-36,32-60
87-99,10-88
17-89,47-88
26-94,25-99
43-90,42-43
59-87,59-80
34-43,37-41
1-54,1-53
2-91,2-3
40-95,46-95
8-14,14-55
38-52,51-69
16-62,15-63
30-55,31-74
46-59,10-74
35-81,80-88
10-86,10-98
18-68,18-68
5-50,5-92
48-98,99-99
6-71,4-72
6-6,6-43
27-39,26-36
15-15,14-82
91-98,29-92
46-51,50-52
5-99,5-98
4-91,4-92
82-83,81-85
68-78,21-68
32-70,69-93
25-59,25-60
40-52,40-40
28-68,93-94
13-99,50-98
10-33,10-11
11-46,8-11
20-32,19-31
9-63,3-62
24-92,92-97
57-68,68-69
39-91,39-91
57-97,49-83
2-58,21-92
14-99,15-98
42-90,43-51
51-51,20-51
29-43,39-43
8-91,7-99
11-75,11-76
33-98,34-97
99-99,28-97
35-82,11-35
80-82,45-81
52-56,53-55
29-77,28-93
6-95,1-94
12-77,12-13
28-90,27-29
71-74,72-77
4-97,4-97
40-85,39-60
36-38,25-38
25-35,24-28
20-57,51-54
80-81,3-81
18-98,97-98
82-94,71-83
5-95,6-87
16-78,3-79
3-74,4-75
14-87,13-42
93-93,8-94
7-20,9-21
6-76,6-7
4-98,69-99
67-95,94-94
66-87,79-86
45-94,45-46
9-13,10-46
71-84,8-83
3-56,4-82
35-89,36-61
54-77,53-55
46-95,46-94
9-19,7-19
18-19,19-42
37-54,53-54
14-91,14-90
9-35,9-36
20-20,20-45
96-97,25-83
11-55,10-10
10-95,11-89
30-34,30-86
30-37,35-38
70-71,53-71
6-12,6-10
4-34,34-95
48-79,48-72
5-99,6-6
60-77,78-94
64-64,13-63
13-31,14-30
7-23,8-24
87-92,88-93
34-81,35-74
7-58,8-77
3-98,3-99
7-94,94-95
3-12,2-88
21-97,22-72
13-77,95-97
15-77,15-16
67-82,68-83
28-28,25-56
51-52,33-52
12-90,12-90
24-72,25-99
1-56,3-55
40-84,39-84
8-9,8-86
31-71,31-72
76-90,64-75
19-90,91-91
42-70,45-69
51-93,80-92
21-36,22-37
96-99,97-97
83-99,1-98
40-43,34-61
1-97,2-96
1-92,1-91
11-92,9-73
57-57,56-66
13-71,12-75
70-89,70-71
12-24,16-24
10-35,56-63
18-85,51-76
20-46,1-45
4-64,4-64
48-52,48-50
84-85,17-85
48-64,63-64
19-28,27-29
4-16,3-17
29-66,2-28
8-88,55-70
60-84,61-85
8-69,8-69
15-67,3-68
42-95,96-99
21-55,22-54
64-70,19-71
17-82,17-81
4-80,3-81
7-95,7-73
12-34,4-33
3-95,63-96
1-96,93-94
45-50,36-49
63-89,45-64
8-96,9-87
93-93,1-92
10-11,10-11
2-6,6-99
40-41,40-68
4-91,3-90
4-68,66-68
37-84,36-85
15-85,29-86
77-79,53-78
50-81,80-81
51-66,50-72
53-53,29-54
42-78,5-77
35-53,36-76
17-17,18-18
4-79,4-79
23-38,23-38
46-81,80-80
26-93,25-37
59-61,20-60
82-96,82-94
16-40,17-21
5-95,5-98
26-26,26-64
32-40,32-75
3-55,6-54
28-86,28-86
4-87,4-96
4-88,24-99
4-66,5-5
9-61,8-89
48-70,48-70
36-37,14-37
21-49,21-50
57-62,14-35
8-62,8-66
14-96,11-97
13-44,43-44
12-87,11-86
2-24,25-97
3-83,2-98
10-80,10-80
4-94,2-4
1-77,20-77
28-79,17-79
8-82,7-7
6-87,77-82
4-93,3-65
94-94,38-95
74-92,74-93
13-68,12-69
41-51,41-42
22-93,21-23
7-12,13-64
58-87,51-88
18-66,19-91
1-70,71-71
9-17,8-37
3-32,4-97
54-90,27-91
1-94,3-93
3-99,4-70
16-92,16-91
22-57,22-57
4-78,31-53
28-94,28-29
19-48,16-18
48-68,49-67
23-39,22-24
12-87,23-95
36-47,37-46
66-69,66-68
35-94,36-93
13-22,2-20
41-53,52-54
4-51,3-96
52-52,5-53
20-85,19-84
4-78,3-79
86-98,15-97
68-85,68-87
2-55,3-54
27-63,11-64
75-83,52-83
18-75,19-74
7-88,8-87
1-86,1-92
6-43,38-44
71-71,70-71
6-43,24-83
15-53,15-63
69-97,69-69
9-99,12-13
31-41,41-42
11-53,10-57
46-67,14-70
24-35,25-36
13-91,23-90
62-67,68-70
62-99,63-68
10-84,51-85
5-98,1-98
16-97,81-98
51-92,41-52
15-88,14-93
3-92,2-93
44-74,44-74
4-95,94-96
51-62,25-63
28-69,11-68
3-82,3-78
5-95,5-98
25-96,25-99
9-9,9-66
17-18,1-18
2-86,4-85
4-9,9-92
2-98,2-98
61-96,60-98
1-89,35-50
89-89,25-90
1-99,1-33
53-73,52-74
30-55,29-90
97-98,70-91
66-69,65-66
31-83,82-83
2-67,67-95
77-78,77-96
30-98,30-98
94-94,28-95
37-83,8-82
14-46,28-30
75-80,12-81
19-68,18-19
65-85,96-99
62-63,3-63
19-95,97-97
54-79,55-78
12-98,97-99
83-98,41-84
68-88,34-69
25-25,20-25
2-66,8-99
84-85,21-85
52-98,53-87
32-55,31-54
4-51,6-90
46-86,47-47
75-75,10-76
30-38,29-49
5-96,4-5
49-49,49-93
8-67,39-65
6-51,5-70
38-70,39-69
2-98,2-3
51-53,50-59
56-92,57-91
11-90,11-52
19-99,20-98
54-77,52-55
6-93,1-6
62-80,58-62
27-82,26-97
10-79,9-78
18-99,18-99
7-87,7-84
44-44,45-86
89-91,6-90
15-98,15-95
56-59,54-60
61-89,2-82
30-78,12-96
10-84,1-10
61-62,46-62
5-74,5-6
29-33,30-32
81-95,95-99
51-98,50-85
6-79,49-78
47-52,12-61
4-58,3-89
75-94,31-76
43-49,42-44
3-4,4-47
44-98,98-98
67-72,66-72
2-38,3-38
3-5,4-47
5-95,5-95
34-97,35-78
66-68,67-98
28-32,29-35
44-68,31-44
28-53,27-55
16-73,17-67
12-49,49-97
34-76,75-75
38-96,37-43
15-20,20-79
15-22,22-35
3-25,4-55
6-90,6-89
17-74,18-75
15-60,14-61
6-29,29-81
23-66,11-24
37-90,90-90
1-24,2-57
42-78,41-79
94-99,74-95
95-97,2-30
13-61,56-60
23-82,24-83
56-56,31-57
58-91,57-99
13-25,14-24
46-54,47-77
47-74,73-74
23-48,22-82
79-80,81-81
16-33,6-76
54-70,55-70
44-67,45-66
2-4,3-97
24-94,19-94
33-77,49-93
13-35,35-73
28-84,28-83
6-89,7-90
40-80,42-80
39-84,65-83
83-83,59-84
20-46,30-46
31-34,32-46
12-13,13-67
35-75,34-74
20-20,20-89
13-70,5-60
25-25,24-24
84-87,83-86
26-58,26-58
6-96,5-7
4-78,5-79
15-15,15-27
7-79,3-80
62-64,24-63
68-69,32-71
27-68,28-41
43-43,11-44
27-82,83-83
54-70,26-69
16-16,17-70
27-34,33-35
33-97,96-97
4-5,4-39
43-43,43-92
27-33,1-28
23-91,23-58
9-51,8-10
4-6,5-76
5-34,33-95
97-98,46-98
20-53,52-65
7-72,6-96
32-79,93-95
21-86,20-85
47-82,46-84
9-96,8-86
10-93,11-75
11-12,11-77
7-56,6-55
3-7,7-43
54-84,55-55
3-95,3-97
18-55,37-56
40-68,39-91
56-87,56-85
12-34,13-35
7-62,8-63
95-95,54-95
7-94,6-94
14-92,13-99
18-42,42-53
75-96,76-95
5-78,4-6
93-94,14-94
25-91,25-92
96-98,97-99
82-84,82-85
37-39,38-42
11-48,7-49
64-66,65-90
10-46,9-45
35-92,34-52
6-94,9-93
12-96,95-96
16-86,63-67
5-96,5-96
54-59,19-60
3-92,3-52
26-54,27-53
28-97,28-93
98-98,83-97
64-98,13-99
79-84,80-86
5-98,4-97
2-23,22-35
7-11,7-87
31-94,32-59
25-41,17-42
28-94,76-95
6-93,5-94
73-94,74-93
6-44,17-44
2-99,22-46
1-73,1-72
25-71,25-72
35-36,6-36
6-66,5-66
92-95,92-95
53-75,52-75
5-55,3-97
12-76,43-75
5-49,13-48
32-32,8-37
18-96,19-19
17-59,17-60
1-17,2-95
37-82,83-83
39-79,39-39
25-81,25-86
11-52,51-51
91-91,30-91
43-58,44-57
1-98,2-98
31-62,31-62
6-13,6-13
65-92,13-91
3-6,5-95
21-88,14-21
48-75,47-74
70-93,30-92
37-58,58-89
14-24,14-23
31-60,58-83
4-95,1-56
47-79,98-98
36-65,37-38
6-18,19-75
14-50,98-99
44-94,45-93
37-39,38-56
39-57,38-40
7-36,6-90
81-83,28-82
15-86,15-77
70-86,2-44
8-23,7-23
28-31,29-78
5-67,4-66
31-31,14-32
45-95,13-96
11-39,40-40
6-95,21-94
35-35,35-66
4-97,4-98
2-97,96-97
14-14,13-50
3-62,2-54
3-98,54-98
24-87,23-86
29-84,28-78
42-45,41-55
8-32,10-33
35-39,35-77
10-89,23-59
10-82,6-98
52-84,83-84
65-73,60-72
7-75,74-91
50-77,76-93
1-94,2-95
98-98,21-97
19-79,18-24
3-87,86-88
47-47,41-48
28-95,29-96
71-85,70-72
60-98,61-75
3-7,7-96
22-23,22-50
90-92,38-91
83-89,57-88
6-86,7-87
3-98,28-99
52-62,15-62
23-98,24-24
38-86,87-94
10-43,16-42
17-25,18-76
60-62,16-63
66-89,66-88
42-80,21-79
6-91,6-93
8-41,41-41
80-87,79-99
88-88,14-89
35-76,23-75
8-51,7-88
2-99,41-71
6-8,7-99
18-83,18-19
69-91,50-68
28-43,28-29
57-76,9-58
56-58,52-57
13-64,14-81
6-84,5-83
95-97,61-77
9-11,10-12
46-65,46-66
18-83,17-83
86-88,57-87
15-74,79-99
5-99,98-99
13-16,14-69
23-92,22-98
70-96,69-98
9-12,9-13
10-12,11-52
21-70,20-87
44-88,44-84
84-86,10-85
30-92,30-91
10-26,25-79
42-59,41-42
39-72,33-99
19-66,39-66
21-23,2-80
23-23,22-23
73-99,72-97
4-72,3-5
22-75,21-76
24-53,52-52
40-56,55-64
17-85,18-84
15-18,14-85
8-71,3-8
1-99,3-95
41-41,40-96
60-67,37-68
9-26,10-91
30-92,73-92
44-85,45-86
13-75,42-75
11-11,64-83
7-98,7-99
53-57,37-54
71-72,8-71
86-86,7-86
14-32,15-54
13-20,12-12
68-93,72-94
3-68,3-4
4-98,17-97
15-94,41-83
23-72,23-72
26-86,2-27
36-81,37-55
10-94,9-93
32-84,31-83
44-95,14-45
3-62,3-62
46-78,45-66
96-98,3-97
91-92,31-92
50-57,20-58
1-64,3-64
48-80,35-48
69-90,69-91
62-68,40-67
74-76,74-76
42-81,43-82
16-58,58-59
88-89,1-89
68-69,69-90
57-73,57-68
58-83,58-94
2-60,88-94
14-18,13-20
68-82,81-83
77-79,26-78
20-36,19-99
12-87,13-89
54-88,64-87
12-85,12-86
1-88,87-89
43-64,64-81
38-97,37-48
12-73,57-74
25-52,26-53
22-22,21-37
75-97,74-76
13-54,14-32
16-47,16-48
9-93,10-92
50-50,49-88
10-10,10-76
94-94,2-95
33-93,63-92
46-46,16-47
90-97,1-91
24-63,26-63
38-84,19-62
28-96,95-98
56-56,49-58
6-83,19-82
31-87,77-88
4-97,3-99
13-86,14-85
90-90,23-90
8-25,26-26
17-60,18-89
10-61,11-62
13-59,50-59
52-73,34-73
94-97,33-95
20-93,19-97
6-6,6-94
7-81,6-89
4-95,4-95
9-65,65-66
37-72,71-75
57-96,56-72
23-77,76-76
7-89,6-88
1-86,85-86
42-44,43-93
18-59,27-58
19-88,18-95
1-74,3-73
22-67,54-66
23-28,23-27
6-73,6-73
4-85,3-5
46-95,46-96
5-92,4-86
22-61,21-61
70-84,56-95
8-9,8-85
18-42,41-41
12-97,96-97
67-73,40-74
13-74,13-81
3-36,4-98
8-96,5-6
9-89,9-84
67-85,68-84
68-69,45-69
34-66,66-71
50-83,13-82
31-74,32-83
1-3,3-83
4-88,4-4
12-93,9-94
70-98,30-98'''
        s = advent2022.Day04.Solution(text.splitlines())

        print('\n')
        c = s.countFullyContained()
        print(c)

        self.assertEqual(584, c)

    def test_day04_part2(self):
        text = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''
        s = advent2022.Day04.Solution(text.splitlines())

        print('\n')
        c = s.countOverlap()
        print(c)

        self.assertEqual(4, c)

    def test_day04_part2_puzzle(self):
        text = '''22-65,22-66
91-94,63-91
6-88,5-31
85-86,64-86
40-65,40-65
25-82,24-94
68-69,68-92
60-91,89-92
3-72,3-73
44-85,84-85
15-72,14-72
84-92,84-92
10-84,3-10
32-62,31-61
14-98,98-99
24-78,24-61
2-5,5-89
58-95,58-59
39-93,92-93
11-82,81-82
12-37,13-58
53-92,52-91
1-19,3-18
90-91,91-98
20-72,19-71
91-91,1-92
71-90,71-93
77-94,77-94
48-76,48-76
48-58,48-53
3-42,2-14
3-4,3-94
4-9,7-8
14-97,77-97
66-66,17-65
12-99,13-98
29-74,30-74
30-93,29-92
43-44,42-46
7-9,8-81
21-77,1-89
85-92,86-91
56-72,73-73
16-75,17-42
2-85,1-85
97-97,13-98
3-94,3-33
55-91,1-99
14-21,14-15
1-3,2-98
43-57,43-56
9-95,8-10
18-80,81-92
19-72,19-71
17-94,62-86
45-59,46-60
73-88,46-87
63-82,82-86
63-88,87-98
20-28,20-56
76-76,70-75
36-73,35-73
85-91,85-90
4-82,4-85
2-2,1-98
27-71,27-81
13-79,13-14
32-43,33-42
53-97,98-99
41-62,42-66
23-78,23-77
6-92,6-91
1-86,1-85
3-89,84-90
5-79,78-80
51-73,50-72
48-81,49-82
32-33,33-88
4-97,4-97
13-88,14-65
33-74,32-75
26-48,48-78
1-46,16-33
2-6,6-67
5-93,5-93
5-6,4-22
68-83,38-84
10-70,18-69
10-77,70-76
4-94,3-93
22-95,21-99
32-72,31-92
30-75,29-74
3-96,95-95
96-96,61-81
52-77,53-77
1-2,1-94
4-96,3-98
29-58,30-56
31-49,30-60
33-79,27-80
10-51,8-11
8-36,8-36
36-93,36-92
9-60,10-15
48-80,79-87
39-41,40-49
48-87,64-87
30-34,2-57
81-82,13-81
3-15,15-99
37-72,38-72
10-85,5-84
6-79,78-93
75-80,76-84
55-72,55-55
8-66,9-9
54-64,63-99
6-77,7-48
2-64,1-32
31-91,90-90
19-66,18-94
58-75,26-76
58-60,1-59
90-90,87-91
5-91,5-91
67-67,3-66
13-81,31-36
31-61,23-60
18-92,17-91
85-86,15-86
10-68,9-11
52-85,12-84
7-27,26-26
43-50,21-50
25-75,74-75
7-7,6-24
1-63,42-62
11-12,11-66
25-94,93-93
13-48,31-47
3-58,59-59
1-54,1-1
5-5,5-96
59-70,7-71
18-19,18-81
9-96,10-84
33-41,33-38
1-99,1-98
69-83,68-78
19-82,8-81
2-23,3-24
57-90,57-98
75-83,74-76
68-68,16-69
2-86,1-33
5-92,6-14
51-76,52-75
25-72,24-46
9-76,10-50
5-51,23-52
19-83,20-93
33-69,44-70
22-69,23-69
55-61,40-62
2-16,16-81
66-98,66-96
27-85,28-86
43-93,88-94
19-83,32-82
2-92,26-52
87-87,45-93
40-81,97-99
4-97,98-98
19-95,6-20
52-96,53-53
2-34,2-97
62-83,63-66
9-74,8-81
53-83,53-83
35-73,11-72
9-97,10-95
9-51,10-50
25-27,26-35
45-60,45-46
12-65,28-65
40-92,40-91
5-5,4-98
72-91,90-91
16-87,17-91
97-97,18-96
77-78,75-79
22-48,32-47
70-70,35-69
45-98,99-99
65-83,83-92
2-95,4-88
5-10,10-46
4-84,50-85
58-58,15-59
11-80,3-22
46-48,3-47
29-80,30-30
34-96,5-95
65-97,32-96
26-31,30-46
12-12,12-77
26-92,26-92
29-92,29-90
26-27,27-30
4-30,3-29
29-57,1-28
99-99,42-97
92-97,78-98
3-90,46-91
44-76,43-75
24-28,10-25
1-95,1-52
3-3,3-61
39-94,40-93
41-86,75-94
28-28,26-27
21-94,21-97
12-41,41-54
4-49,3-5
75-90,44-75
4-83,78-82
5-93,93-94
33-90,89-90
12-32,13-98
41-99,98-99
4-67,3-38
95-95,11-95
7-46,7-46
11-18,18-24
7-92,12-57
60-91,90-91
86-94,86-95
11-58,57-57
7-10,10-97
1-46,3-46
1-52,1-2
16-94,74-93
7-98,18-97
8-76,8-74
37-92,54-91
63-86,88-96
4-55,47-58
70-92,91-95
73-77,71-77
3-99,5-99
56-58,56-57
53-73,13-74
88-97,97-97
52-63,51-60
13-94,14-91
2-93,3-99
42-75,67-75
38-39,38-88
8-93,92-97
13-32,17-31
3-17,16-53
1-1,3-95
5-88,4-87
76-89,47-77
5-54,4-55
45-95,90-96
81-89,36-88
31-36,32-60
87-99,10-88
17-89,47-88
26-94,25-99
43-90,42-43
59-87,59-80
34-43,37-41
1-54,1-53
2-91,2-3
40-95,46-95
8-14,14-55
38-52,51-69
16-62,15-63
30-55,31-74
46-59,10-74
35-81,80-88
10-86,10-98
18-68,18-68
5-50,5-92
48-98,99-99
6-71,4-72
6-6,6-43
27-39,26-36
15-15,14-82
91-98,29-92
46-51,50-52
5-99,5-98
4-91,4-92
82-83,81-85
68-78,21-68
32-70,69-93
25-59,25-60
40-52,40-40
28-68,93-94
13-99,50-98
10-33,10-11
11-46,8-11
20-32,19-31
9-63,3-62
24-92,92-97
57-68,68-69
39-91,39-91
57-97,49-83
2-58,21-92
14-99,15-98
42-90,43-51
51-51,20-51
29-43,39-43
8-91,7-99
11-75,11-76
33-98,34-97
99-99,28-97
35-82,11-35
80-82,45-81
52-56,53-55
29-77,28-93
6-95,1-94
12-77,12-13
28-90,27-29
71-74,72-77
4-97,4-97
40-85,39-60
36-38,25-38
25-35,24-28
20-57,51-54
80-81,3-81
18-98,97-98
82-94,71-83
5-95,6-87
16-78,3-79
3-74,4-75
14-87,13-42
93-93,8-94
7-20,9-21
6-76,6-7
4-98,69-99
67-95,94-94
66-87,79-86
45-94,45-46
9-13,10-46
71-84,8-83
3-56,4-82
35-89,36-61
54-77,53-55
46-95,46-94
9-19,7-19
18-19,19-42
37-54,53-54
14-91,14-90
9-35,9-36
20-20,20-45
96-97,25-83
11-55,10-10
10-95,11-89
30-34,30-86
30-37,35-38
70-71,53-71
6-12,6-10
4-34,34-95
48-79,48-72
5-99,6-6
60-77,78-94
64-64,13-63
13-31,14-30
7-23,8-24
87-92,88-93
34-81,35-74
7-58,8-77
3-98,3-99
7-94,94-95
3-12,2-88
21-97,22-72
13-77,95-97
15-77,15-16
67-82,68-83
28-28,25-56
51-52,33-52
12-90,12-90
24-72,25-99
1-56,3-55
40-84,39-84
8-9,8-86
31-71,31-72
76-90,64-75
19-90,91-91
42-70,45-69
51-93,80-92
21-36,22-37
96-99,97-97
83-99,1-98
40-43,34-61
1-97,2-96
1-92,1-91
11-92,9-73
57-57,56-66
13-71,12-75
70-89,70-71
12-24,16-24
10-35,56-63
18-85,51-76
20-46,1-45
4-64,4-64
48-52,48-50
84-85,17-85
48-64,63-64
19-28,27-29
4-16,3-17
29-66,2-28
8-88,55-70
60-84,61-85
8-69,8-69
15-67,3-68
42-95,96-99
21-55,22-54
64-70,19-71
17-82,17-81
4-80,3-81
7-95,7-73
12-34,4-33
3-95,63-96
1-96,93-94
45-50,36-49
63-89,45-64
8-96,9-87
93-93,1-92
10-11,10-11
2-6,6-99
40-41,40-68
4-91,3-90
4-68,66-68
37-84,36-85
15-85,29-86
77-79,53-78
50-81,80-81
51-66,50-72
53-53,29-54
42-78,5-77
35-53,36-76
17-17,18-18
4-79,4-79
23-38,23-38
46-81,80-80
26-93,25-37
59-61,20-60
82-96,82-94
16-40,17-21
5-95,5-98
26-26,26-64
32-40,32-75
3-55,6-54
28-86,28-86
4-87,4-96
4-88,24-99
4-66,5-5
9-61,8-89
48-70,48-70
36-37,14-37
21-49,21-50
57-62,14-35
8-62,8-66
14-96,11-97
13-44,43-44
12-87,11-86
2-24,25-97
3-83,2-98
10-80,10-80
4-94,2-4
1-77,20-77
28-79,17-79
8-82,7-7
6-87,77-82
4-93,3-65
94-94,38-95
74-92,74-93
13-68,12-69
41-51,41-42
22-93,21-23
7-12,13-64
58-87,51-88
18-66,19-91
1-70,71-71
9-17,8-37
3-32,4-97
54-90,27-91
1-94,3-93
3-99,4-70
16-92,16-91
22-57,22-57
4-78,31-53
28-94,28-29
19-48,16-18
48-68,49-67
23-39,22-24
12-87,23-95
36-47,37-46
66-69,66-68
35-94,36-93
13-22,2-20
41-53,52-54
4-51,3-96
52-52,5-53
20-85,19-84
4-78,3-79
86-98,15-97
68-85,68-87
2-55,3-54
27-63,11-64
75-83,52-83
18-75,19-74
7-88,8-87
1-86,1-92
6-43,38-44
71-71,70-71
6-43,24-83
15-53,15-63
69-97,69-69
9-99,12-13
31-41,41-42
11-53,10-57
46-67,14-70
24-35,25-36
13-91,23-90
62-67,68-70
62-99,63-68
10-84,51-85
5-98,1-98
16-97,81-98
51-92,41-52
15-88,14-93
3-92,2-93
44-74,44-74
4-95,94-96
51-62,25-63
28-69,11-68
3-82,3-78
5-95,5-98
25-96,25-99
9-9,9-66
17-18,1-18
2-86,4-85
4-9,9-92
2-98,2-98
61-96,60-98
1-89,35-50
89-89,25-90
1-99,1-33
53-73,52-74
30-55,29-90
97-98,70-91
66-69,65-66
31-83,82-83
2-67,67-95
77-78,77-96
30-98,30-98
94-94,28-95
37-83,8-82
14-46,28-30
75-80,12-81
19-68,18-19
65-85,96-99
62-63,3-63
19-95,97-97
54-79,55-78
12-98,97-99
83-98,41-84
68-88,34-69
25-25,20-25
2-66,8-99
84-85,21-85
52-98,53-87
32-55,31-54
4-51,6-90
46-86,47-47
75-75,10-76
30-38,29-49
5-96,4-5
49-49,49-93
8-67,39-65
6-51,5-70
38-70,39-69
2-98,2-3
51-53,50-59
56-92,57-91
11-90,11-52
19-99,20-98
54-77,52-55
6-93,1-6
62-80,58-62
27-82,26-97
10-79,9-78
18-99,18-99
7-87,7-84
44-44,45-86
89-91,6-90
15-98,15-95
56-59,54-60
61-89,2-82
30-78,12-96
10-84,1-10
61-62,46-62
5-74,5-6
29-33,30-32
81-95,95-99
51-98,50-85
6-79,49-78
47-52,12-61
4-58,3-89
75-94,31-76
43-49,42-44
3-4,4-47
44-98,98-98
67-72,66-72
2-38,3-38
3-5,4-47
5-95,5-95
34-97,35-78
66-68,67-98
28-32,29-35
44-68,31-44
28-53,27-55
16-73,17-67
12-49,49-97
34-76,75-75
38-96,37-43
15-20,20-79
15-22,22-35
3-25,4-55
6-90,6-89
17-74,18-75
15-60,14-61
6-29,29-81
23-66,11-24
37-90,90-90
1-24,2-57
42-78,41-79
94-99,74-95
95-97,2-30
13-61,56-60
23-82,24-83
56-56,31-57
58-91,57-99
13-25,14-24
46-54,47-77
47-74,73-74
23-48,22-82
79-80,81-81
16-33,6-76
54-70,55-70
44-67,45-66
2-4,3-97
24-94,19-94
33-77,49-93
13-35,35-73
28-84,28-83
6-89,7-90
40-80,42-80
39-84,65-83
83-83,59-84
20-46,30-46
31-34,32-46
12-13,13-67
35-75,34-74
20-20,20-89
13-70,5-60
25-25,24-24
84-87,83-86
26-58,26-58
6-96,5-7
4-78,5-79
15-15,15-27
7-79,3-80
62-64,24-63
68-69,32-71
27-68,28-41
43-43,11-44
27-82,83-83
54-70,26-69
16-16,17-70
27-34,33-35
33-97,96-97
4-5,4-39
43-43,43-92
27-33,1-28
23-91,23-58
9-51,8-10
4-6,5-76
5-34,33-95
97-98,46-98
20-53,52-65
7-72,6-96
32-79,93-95
21-86,20-85
47-82,46-84
9-96,8-86
10-93,11-75
11-12,11-77
7-56,6-55
3-7,7-43
54-84,55-55
3-95,3-97
18-55,37-56
40-68,39-91
56-87,56-85
12-34,13-35
7-62,8-63
95-95,54-95
7-94,6-94
14-92,13-99
18-42,42-53
75-96,76-95
5-78,4-6
93-94,14-94
25-91,25-92
96-98,97-99
82-84,82-85
37-39,38-42
11-48,7-49
64-66,65-90
10-46,9-45
35-92,34-52
6-94,9-93
12-96,95-96
16-86,63-67
5-96,5-96
54-59,19-60
3-92,3-52
26-54,27-53
28-97,28-93
98-98,83-97
64-98,13-99
79-84,80-86
5-98,4-97
2-23,22-35
7-11,7-87
31-94,32-59
25-41,17-42
28-94,76-95
6-93,5-94
73-94,74-93
6-44,17-44
2-99,22-46
1-73,1-72
25-71,25-72
35-36,6-36
6-66,5-66
92-95,92-95
53-75,52-75
5-55,3-97
12-76,43-75
5-49,13-48
32-32,8-37
18-96,19-19
17-59,17-60
1-17,2-95
37-82,83-83
39-79,39-39
25-81,25-86
11-52,51-51
91-91,30-91
43-58,44-57
1-98,2-98
31-62,31-62
6-13,6-13
65-92,13-91
3-6,5-95
21-88,14-21
48-75,47-74
70-93,30-92
37-58,58-89
14-24,14-23
31-60,58-83
4-95,1-56
47-79,98-98
36-65,37-38
6-18,19-75
14-50,98-99
44-94,45-93
37-39,38-56
39-57,38-40
7-36,6-90
81-83,28-82
15-86,15-77
70-86,2-44
8-23,7-23
28-31,29-78
5-67,4-66
31-31,14-32
45-95,13-96
11-39,40-40
6-95,21-94
35-35,35-66
4-97,4-98
2-97,96-97
14-14,13-50
3-62,2-54
3-98,54-98
24-87,23-86
29-84,28-78
42-45,41-55
8-32,10-33
35-39,35-77
10-89,23-59
10-82,6-98
52-84,83-84
65-73,60-72
7-75,74-91
50-77,76-93
1-94,2-95
98-98,21-97
19-79,18-24
3-87,86-88
47-47,41-48
28-95,29-96
71-85,70-72
60-98,61-75
3-7,7-96
22-23,22-50
90-92,38-91
83-89,57-88
6-86,7-87
3-98,28-99
52-62,15-62
23-98,24-24
38-86,87-94
10-43,16-42
17-25,18-76
60-62,16-63
66-89,66-88
42-80,21-79
6-91,6-93
8-41,41-41
80-87,79-99
88-88,14-89
35-76,23-75
8-51,7-88
2-99,41-71
6-8,7-99
18-83,18-19
69-91,50-68
28-43,28-29
57-76,9-58
56-58,52-57
13-64,14-81
6-84,5-83
95-97,61-77
9-11,10-12
46-65,46-66
18-83,17-83
86-88,57-87
15-74,79-99
5-99,98-99
13-16,14-69
23-92,22-98
70-96,69-98
9-12,9-13
10-12,11-52
21-70,20-87
44-88,44-84
84-86,10-85
30-92,30-91
10-26,25-79
42-59,41-42
39-72,33-99
19-66,39-66
21-23,2-80
23-23,22-23
73-99,72-97
4-72,3-5
22-75,21-76
24-53,52-52
40-56,55-64
17-85,18-84
15-18,14-85
8-71,3-8
1-99,3-95
41-41,40-96
60-67,37-68
9-26,10-91
30-92,73-92
44-85,45-86
13-75,42-75
11-11,64-83
7-98,7-99
53-57,37-54
71-72,8-71
86-86,7-86
14-32,15-54
13-20,12-12
68-93,72-94
3-68,3-4
4-98,17-97
15-94,41-83
23-72,23-72
26-86,2-27
36-81,37-55
10-94,9-93
32-84,31-83
44-95,14-45
3-62,3-62
46-78,45-66
96-98,3-97
91-92,31-92
50-57,20-58
1-64,3-64
48-80,35-48
69-90,69-91
62-68,40-67
74-76,74-76
42-81,43-82
16-58,58-59
88-89,1-89
68-69,69-90
57-73,57-68
58-83,58-94
2-60,88-94
14-18,13-20
68-82,81-83
77-79,26-78
20-36,19-99
12-87,13-89
54-88,64-87
12-85,12-86
1-88,87-89
43-64,64-81
38-97,37-48
12-73,57-74
25-52,26-53
22-22,21-37
75-97,74-76
13-54,14-32
16-47,16-48
9-93,10-92
50-50,49-88
10-10,10-76
94-94,2-95
33-93,63-92
46-46,16-47
90-97,1-91
24-63,26-63
38-84,19-62
28-96,95-98
56-56,49-58
6-83,19-82
31-87,77-88
4-97,3-99
13-86,14-85
90-90,23-90
8-25,26-26
17-60,18-89
10-61,11-62
13-59,50-59
52-73,34-73
94-97,33-95
20-93,19-97
6-6,6-94
7-81,6-89
4-95,4-95
9-65,65-66
37-72,71-75
57-96,56-72
23-77,76-76
7-89,6-88
1-86,85-86
42-44,43-93
18-59,27-58
19-88,18-95
1-74,3-73
22-67,54-66
23-28,23-27
6-73,6-73
4-85,3-5
46-95,46-96
5-92,4-86
22-61,21-61
70-84,56-95
8-9,8-85
18-42,41-41
12-97,96-97
67-73,40-74
13-74,13-81
3-36,4-98
8-96,5-6
9-89,9-84
67-85,68-84
68-69,45-69
34-66,66-71
50-83,13-82
31-74,32-83
1-3,3-83
4-88,4-4
12-93,9-94
70-98,30-98'''
        s = advent2022.Day04.Solution(text.splitlines())

        print('\n')
        c = s.countOverlap()
        print(c)

        self.assertEqual(933, c)

    def test_day05_part1(self):
        text = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''
        s = advent2022.Day05.Solution(text.splitlines())

        print('\n')
        s.readStacks()
        s.readInstructions()
        s.executeInstructionsPart1(s.instructions)
        print(s.stacks)
        self.assertEqual('CMZ', s.result(s.stacks))

    def test_day05_part1_puzzle(self):
        text = '''        [M]     [B]             [N]
[T]     [H]     [V] [Q]         [H]
[Q]     [N]     [H] [W] [T]     [Q]
[V]     [P] [F] [Q] [P] [C]     [R]
[C]     [D] [T] [N] [N] [L] [S] [J]
[D] [V] [W] [R] [M] [G] [R] [N] [D]
[S] [F] [Q] [Q] [F] [F] [F] [Z] [S]
[N] [M] [F] [D] [R] [C] [W] [T] [M]
 1   2   3   4   5   6   7   8   9 

move 1 from 8 to 7
move 1 from 2 to 7
move 6 from 9 to 8
move 1 from 9 to 1
move 1 from 9 to 1
move 3 from 3 to 6
move 3 from 3 to 9
move 1 from 9 to 2
move 5 from 7 to 9
move 9 from 1 to 6
move 3 from 4 to 9
move 2 from 9 to 2
move 1 from 4 to 2
move 1 from 3 to 9
move 8 from 9 to 4
move 14 from 6 to 7
move 1 from 3 to 2
move 5 from 4 to 2
move 5 from 5 to 7
move 4 from 2 to 1
move 2 from 4 to 9
move 1 from 4 to 3
move 3 from 5 to 7
move 1 from 8 to 6
move 2 from 8 to 7
move 2 from 1 to 2
move 1 from 9 to 7
move 2 from 1 to 3
move 5 from 6 to 5
move 4 from 5 to 7
move 3 from 8 to 4
move 20 from 7 to 1
move 11 from 7 to 5
move 1 from 6 to 9
move 3 from 9 to 2
move 12 from 1 to 9
move 2 from 8 to 3
move 4 from 2 to 8
move 8 from 2 to 1
move 4 from 8 to 9
move 1 from 2 to 5
move 12 from 9 to 7
move 4 from 4 to 9
move 4 from 9 to 5
move 13 from 5 to 4
move 4 from 4 to 7
move 1 from 7 to 9
move 2 from 9 to 5
move 9 from 1 to 2
move 1 from 8 to 3
move 5 from 4 to 2
move 1 from 3 to 6
move 7 from 2 to 8
move 6 from 1 to 6
move 6 from 8 to 7
move 6 from 2 to 1
move 3 from 9 to 3
move 7 from 3 to 7
move 4 from 4 to 9
move 1 from 8 to 9
move 1 from 3 to 9
move 1 from 2 to 4
move 1 from 9 to 6
move 5 from 1 to 9
move 1 from 4 to 9
move 2 from 9 to 1
move 8 from 6 to 7
move 4 from 9 to 7
move 2 from 5 to 2
move 2 from 1 to 9
move 14 from 7 to 4
move 22 from 7 to 2
move 2 from 7 to 4
move 3 from 7 to 5
move 9 from 4 to 7
move 6 from 2 to 4
move 8 from 4 to 3
move 14 from 2 to 9
move 2 from 3 to 9
move 3 from 2 to 9
move 4 from 4 to 2
move 1 from 4 to 5
move 1 from 1 to 4
move 5 from 7 to 8
move 1 from 1 to 3
move 4 from 5 to 2
move 6 from 3 to 9
move 1 from 3 to 4
move 4 from 8 to 9
move 2 from 4 to 6
move 4 from 5 to 3
move 1 from 7 to 6
move 1 from 8 to 5
move 3 from 3 to 1
move 33 from 9 to 5
move 5 from 2 to 1
move 1 from 3 to 5
move 1 from 7 to 6
move 18 from 5 to 1
move 1 from 2 to 8
move 6 from 5 to 4
move 1 from 8 to 7
move 2 from 4 to 1
move 4 from 1 to 2
move 19 from 1 to 2
move 4 from 6 to 8
move 4 from 1 to 8
move 14 from 2 to 9
move 5 from 2 to 4
move 1 from 8 to 2
move 8 from 2 to 5
move 5 from 8 to 4
move 4 from 9 to 7
move 1 from 8 to 1
move 16 from 5 to 4
move 15 from 4 to 5
move 1 from 9 to 5
move 5 from 7 to 6
move 2 from 7 to 6
move 1 from 1 to 9
move 7 from 6 to 7
move 1 from 8 to 5
move 1 from 1 to 9
move 12 from 5 to 7
move 7 from 5 to 9
move 12 from 7 to 2
move 1 from 7 to 4
move 7 from 4 to 7
move 2 from 9 to 4
move 5 from 4 to 9
move 8 from 2 to 3
move 4 from 2 to 4
move 9 from 4 to 8
move 6 from 3 to 5
move 8 from 7 to 3
move 1 from 4 to 3
move 7 from 8 to 9
move 4 from 5 to 4
move 6 from 3 to 1
move 4 from 3 to 4
move 1 from 3 to 6
move 6 from 4 to 9
move 1 from 6 to 5
move 17 from 9 to 4
move 3 from 7 to 3
move 1 from 7 to 9
move 2 from 5 to 3
move 2 from 1 to 3
move 2 from 8 to 9
move 1 from 5 to 1
move 14 from 4 to 5
move 2 from 3 to 2
move 1 from 7 to 6
move 10 from 9 to 4
move 12 from 9 to 4
move 9 from 4 to 5
move 1 from 2 to 9
move 13 from 5 to 9
move 2 from 5 to 1
move 1 from 2 to 9
move 3 from 4 to 2
move 12 from 4 to 7
move 8 from 5 to 7
move 1 from 1 to 9
move 1 from 6 to 4
move 1 from 5 to 4
move 1 from 4 to 8
move 5 from 3 to 4
move 10 from 9 to 6
move 3 from 6 to 2
move 7 from 6 to 5
move 6 from 5 to 4
move 1 from 8 to 5
move 1 from 1 to 4
move 2 from 7 to 2
move 5 from 4 to 9
move 2 from 5 to 8
move 1 from 1 to 3
move 2 from 1 to 7
move 6 from 7 to 9
move 9 from 9 to 8
move 1 from 1 to 3
move 4 from 2 to 7
move 11 from 7 to 3
move 11 from 8 to 6
move 7 from 3 to 1
move 4 from 7 to 2
move 3 from 2 to 9
move 8 from 1 to 5
move 2 from 7 to 5
move 2 from 2 to 9
move 2 from 3 to 9
move 11 from 4 to 7
move 7 from 9 to 5
move 6 from 6 to 5
move 2 from 2 to 9
move 1 from 2 to 3
move 6 from 9 to 4
move 3 from 9 to 1
move 4 from 3 to 5
move 6 from 7 to 1
move 2 from 6 to 3
move 2 from 9 to 2
move 3 from 3 to 2
move 3 from 6 to 8
move 2 from 7 to 5
move 20 from 5 to 6
move 8 from 5 to 1
move 1 from 5 to 9
move 2 from 8 to 4
move 1 from 8 to 7
move 16 from 1 to 8
move 8 from 8 to 9
move 4 from 2 to 4
move 1 from 1 to 5
move 1 from 5 to 4
move 3 from 8 to 4
move 14 from 4 to 6
move 5 from 8 to 7
move 6 from 7 to 8
move 29 from 6 to 2
move 3 from 9 to 8
move 21 from 2 to 3
move 1 from 8 to 3
move 6 from 9 to 4
move 8 from 3 to 5
move 7 from 8 to 4
move 7 from 3 to 9
move 3 from 7 to 2
move 12 from 4 to 8
move 2 from 3 to 1
move 2 from 9 to 1
move 1 from 6 to 7
move 1 from 7 to 6
move 1 from 6 to 3
move 3 from 1 to 8
move 2 from 4 to 1
move 4 from 6 to 1
move 5 from 2 to 7
move 1 from 1 to 2
move 5 from 1 to 2
move 2 from 8 to 1
move 1 from 4 to 5
move 9 from 8 to 4
move 3 from 7 to 9
move 7 from 5 to 7
move 2 from 5 to 9
move 4 from 9 to 2
move 3 from 3 to 2
move 5 from 2 to 7
move 2 from 8 to 2
move 2 from 7 to 3
move 1 from 8 to 6
move 2 from 1 to 2
move 1 from 6 to 7
move 1 from 8 to 1
move 12 from 7 to 1
move 5 from 2 to 7
move 7 from 4 to 2
move 2 from 4 to 1
move 5 from 3 to 8
move 7 from 1 to 9
move 4 from 7 to 1
move 7 from 1 to 5
move 12 from 9 to 2
move 27 from 2 to 4
move 3 from 8 to 9
move 6 from 2 to 5
move 6 from 1 to 8
move 1 from 7 to 6
move 9 from 5 to 2
move 3 from 9 to 2
move 13 from 4 to 5
move 10 from 2 to 7
move 1 from 9 to 8
move 11 from 5 to 7
move 1 from 8 to 7
move 1 from 2 to 6
move 13 from 4 to 3
move 23 from 7 to 4
move 1 from 6 to 9
move 1 from 2 to 4
move 7 from 3 to 5
move 1 from 9 to 8
move 19 from 4 to 1
move 2 from 4 to 1
move 1 from 7 to 6
move 1 from 4 to 5
move 1 from 5 to 7
move 11 from 5 to 1
move 2 from 5 to 4
move 2 from 6 to 9
move 3 from 8 to 2
move 2 from 8 to 1
move 3 from 2 to 1
move 1 from 9 to 5
move 6 from 1 to 3
move 1 from 9 to 7
move 2 from 7 to 5
move 2 from 8 to 6
move 1 from 3 to 2
move 2 from 8 to 5
move 1 from 2 to 1
move 3 from 4 to 1
move 3 from 5 to 1
move 2 from 5 to 1
move 2 from 6 to 9
move 1 from 9 to 6
move 1 from 4 to 5
move 1 from 9 to 8
move 1 from 8 to 6
move 8 from 1 to 6
move 7 from 1 to 8
move 9 from 1 to 6
move 1 from 5 to 3
move 3 from 8 to 4
move 11 from 3 to 4
move 1 from 3 to 6
move 10 from 6 to 8
move 13 from 1 to 6
move 3 from 4 to 5
move 7 from 8 to 6
move 3 from 8 to 5
move 6 from 5 to 3
move 22 from 6 to 9
move 4 from 3 to 6
move 4 from 9 to 5
move 1 from 1 to 5
move 2 from 3 to 4
move 2 from 1 to 5
move 1 from 9 to 2
move 5 from 8 to 3
move 2 from 9 to 2
move 11 from 6 to 9
move 3 from 2 to 7
move 1 from 6 to 7
move 12 from 9 to 8
move 4 from 7 to 1
move 12 from 4 to 8
move 2 from 4 to 7
move 1 from 1 to 8
move 1 from 5 to 1
move 19 from 8 to 4
move 4 from 5 to 1
move 1 from 7 to 4
move 1 from 7 to 1
move 3 from 3 to 4
move 2 from 8 to 4
move 1 from 5 to 7
move 1 from 7 to 9
move 8 from 1 to 8
move 1 from 1 to 4
move 1 from 3 to 9
move 1 from 3 to 5
move 1 from 5 to 2
move 7 from 8 to 7
move 16 from 4 to 7
move 1 from 7 to 4
move 3 from 8 to 2
move 14 from 7 to 4
move 1 from 5 to 8
move 5 from 7 to 5
move 16 from 4 to 5
move 3 from 5 to 4
move 3 from 2 to 1
move 1 from 7 to 9
move 11 from 4 to 2
move 3 from 8 to 6
move 2 from 1 to 8
move 1 from 4 to 9
move 18 from 5 to 1
move 1 from 8 to 7
move 3 from 7 to 9
move 18 from 9 to 3
move 3 from 6 to 9
move 7 from 1 to 6
move 1 from 8 to 4
move 1 from 4 to 9
move 3 from 6 to 4
move 5 from 9 to 2
move 2 from 4 to 7
move 7 from 2 to 8
move 1 from 7 to 3
move 2 from 6 to 8
move 1 from 9 to 5
move 1 from 6 to 8
move 1 from 4 to 8
move 1 from 5 to 3
move 1 from 7 to 5
move 8 from 8 to 7
move 10 from 2 to 6
move 1 from 9 to 3
move 6 from 6 to 2
move 5 from 6 to 2
move 7 from 2 to 7
move 12 from 1 to 6
move 2 from 2 to 1
move 1 from 2 to 5
move 4 from 7 to 6
move 12 from 3 to 1
move 2 from 7 to 2
move 9 from 3 to 8
move 1 from 2 to 6
move 1 from 5 to 4
move 9 from 6 to 5
move 1 from 7 to 6
move 1 from 4 to 9
move 9 from 6 to 7
move 7 from 8 to 3
move 6 from 3 to 1
move 4 from 8 to 3
move 5 from 3 to 1
move 1 from 9 to 8
move 2 from 8 to 9
move 5 from 5 to 7
move 14 from 7 to 8
move 1 from 9 to 4
move 2 from 2 to 1
move 3 from 5 to 3
move 2 from 3 to 1
move 1 from 4 to 6
move 6 from 8 to 6
move 6 from 8 to 3
move 3 from 6 to 1
move 2 from 8 to 9
move 19 from 1 to 6
move 3 from 9 to 3
move 6 from 3 to 4
move 6 from 6 to 2
move 4 from 3 to 9
move 1 from 7 to 9
move 2 from 5 to 7
move 5 from 9 to 6
move 6 from 7 to 2
move 11 from 2 to 5
move 2 from 7 to 4
move 4 from 4 to 3
move 2 from 4 to 8
move 12 from 1 to 2
move 1 from 8 to 2
move 8 from 5 to 7
move 2 from 4 to 9
move 2 from 7 to 1
move 4 from 2 to 3
move 1 from 8 to 6
move 1 from 1 to 5
move 2 from 9 to 1
move 2 from 7 to 3
move 2 from 5 to 2
move 1 from 5 to 7
move 2 from 7 to 8
move 1 from 5 to 7
move 5 from 3 to 4
move 3 from 1 to 7
move 1 from 2 to 4
move 15 from 6 to 1
move 4 from 4 to 1
move 4 from 2 to 3
move 8 from 3 to 2
move 5 from 2 to 4
move 1 from 8 to 6
move 1 from 8 to 9
move 1 from 3 to 1
move 3 from 7 to 3
move 5 from 7 to 6
move 4 from 2 to 9
move 6 from 2 to 6
move 4 from 9 to 6
move 12 from 1 to 5
move 6 from 4 to 1
move 1 from 3 to 6
move 4 from 5 to 8
move 7 from 5 to 3
move 3 from 8 to 2
move 1 from 2 to 3
move 1 from 9 to 5
move 1 from 4 to 5
move 1 from 8 to 5
move 8 from 6 to 9
move 10 from 1 to 4
move 3 from 6 to 1
move 9 from 3 to 6
move 1 from 3 to 8
move 1 from 2 to 4
move 6 from 9 to 1
move 1 from 1 to 4
move 10 from 1 to 6
move 1 from 8 to 6
move 13 from 6 to 7
move 1 from 2 to 1
move 1 from 9 to 6
move 9 from 7 to 5
move 1 from 9 to 4
move 3 from 7 to 1
move 3 from 5 to 6
move 10 from 4 to 7
move 5 from 6 to 5
move 3 from 4 to 5
move 13 from 6 to 9
move 7 from 5 to 3
move 6 from 3 to 2
move 5 from 6 to 4
move 4 from 2 to 8'''
        s = advent2022.Day05.Solution(text.splitlines())

        print('\n')
        s.readStacks()
        s.readInstructions()
        s.executeInstructionsPart1(s.instructions)
        result = s.result(s.stacks)
        self.assertEqual('FRDSQRRCD', result)

    def test_day05_part2(self):
        text = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''
        s = advent2022.Day05.Solution(text.splitlines())

        print('\n')
        s.readStacks()
        s.readInstructions()
        s.executeInstructionsPart2(s.instructions)
        print(s.stacks)
        self.assertEqual('MCD', s.result(s.stacks))

    def test_day05_part2_puzzle(self):
        text = '''        [M]     [B]             [N]
[T]     [H]     [V] [Q]         [H]
[Q]     [N]     [H] [W] [T]     [Q]
[V]     [P] [F] [Q] [P] [C]     [R]
[C]     [D] [T] [N] [N] [L] [S] [J]
[D] [V] [W] [R] [M] [G] [R] [N] [D]
[S] [F] [Q] [Q] [F] [F] [F] [Z] [S]
[N] [M] [F] [D] [R] [C] [W] [T] [M]
 1   2   3   4   5   6   7   8   9 

move 1 from 8 to 7
move 1 from 2 to 7
move 6 from 9 to 8
move 1 from 9 to 1
move 1 from 9 to 1
move 3 from 3 to 6
move 3 from 3 to 9
move 1 from 9 to 2
move 5 from 7 to 9
move 9 from 1 to 6
move 3 from 4 to 9
move 2 from 9 to 2
move 1 from 4 to 2
move 1 from 3 to 9
move 8 from 9 to 4
move 14 from 6 to 7
move 1 from 3 to 2
move 5 from 4 to 2
move 5 from 5 to 7
move 4 from 2 to 1
move 2 from 4 to 9
move 1 from 4 to 3
move 3 from 5 to 7
move 1 from 8 to 6
move 2 from 8 to 7
move 2 from 1 to 2
move 1 from 9 to 7
move 2 from 1 to 3
move 5 from 6 to 5
move 4 from 5 to 7
move 3 from 8 to 4
move 20 from 7 to 1
move 11 from 7 to 5
move 1 from 6 to 9
move 3 from 9 to 2
move 12 from 1 to 9
move 2 from 8 to 3
move 4 from 2 to 8
move 8 from 2 to 1
move 4 from 8 to 9
move 1 from 2 to 5
move 12 from 9 to 7
move 4 from 4 to 9
move 4 from 9 to 5
move 13 from 5 to 4
move 4 from 4 to 7
move 1 from 7 to 9
move 2 from 9 to 5
move 9 from 1 to 2
move 1 from 8 to 3
move 5 from 4 to 2
move 1 from 3 to 6
move 7 from 2 to 8
move 6 from 1 to 6
move 6 from 8 to 7
move 6 from 2 to 1
move 3 from 9 to 3
move 7 from 3 to 7
move 4 from 4 to 9
move 1 from 8 to 9
move 1 from 3 to 9
move 1 from 2 to 4
move 1 from 9 to 6
move 5 from 1 to 9
move 1 from 4 to 9
move 2 from 9 to 1
move 8 from 6 to 7
move 4 from 9 to 7
move 2 from 5 to 2
move 2 from 1 to 9
move 14 from 7 to 4
move 22 from 7 to 2
move 2 from 7 to 4
move 3 from 7 to 5
move 9 from 4 to 7
move 6 from 2 to 4
move 8 from 4 to 3
move 14 from 2 to 9
move 2 from 3 to 9
move 3 from 2 to 9
move 4 from 4 to 2
move 1 from 4 to 5
move 1 from 1 to 4
move 5 from 7 to 8
move 1 from 1 to 3
move 4 from 5 to 2
move 6 from 3 to 9
move 1 from 3 to 4
move 4 from 8 to 9
move 2 from 4 to 6
move 4 from 5 to 3
move 1 from 7 to 6
move 1 from 8 to 5
move 3 from 3 to 1
move 33 from 9 to 5
move 5 from 2 to 1
move 1 from 3 to 5
move 1 from 7 to 6
move 18 from 5 to 1
move 1 from 2 to 8
move 6 from 5 to 4
move 1 from 8 to 7
move 2 from 4 to 1
move 4 from 1 to 2
move 19 from 1 to 2
move 4 from 6 to 8
move 4 from 1 to 8
move 14 from 2 to 9
move 5 from 2 to 4
move 1 from 8 to 2
move 8 from 2 to 5
move 5 from 8 to 4
move 4 from 9 to 7
move 1 from 8 to 1
move 16 from 5 to 4
move 15 from 4 to 5
move 1 from 9 to 5
move 5 from 7 to 6
move 2 from 7 to 6
move 1 from 1 to 9
move 7 from 6 to 7
move 1 from 8 to 5
move 1 from 1 to 9
move 12 from 5 to 7
move 7 from 5 to 9
move 12 from 7 to 2
move 1 from 7 to 4
move 7 from 4 to 7
move 2 from 9 to 4
move 5 from 4 to 9
move 8 from 2 to 3
move 4 from 2 to 4
move 9 from 4 to 8
move 6 from 3 to 5
move 8 from 7 to 3
move 1 from 4 to 3
move 7 from 8 to 9
move 4 from 5 to 4
move 6 from 3 to 1
move 4 from 3 to 4
move 1 from 3 to 6
move 6 from 4 to 9
move 1 from 6 to 5
move 17 from 9 to 4
move 3 from 7 to 3
move 1 from 7 to 9
move 2 from 5 to 3
move 2 from 1 to 3
move 2 from 8 to 9
move 1 from 5 to 1
move 14 from 4 to 5
move 2 from 3 to 2
move 1 from 7 to 6
move 10 from 9 to 4
move 12 from 9 to 4
move 9 from 4 to 5
move 1 from 2 to 9
move 13 from 5 to 9
move 2 from 5 to 1
move 1 from 2 to 9
move 3 from 4 to 2
move 12 from 4 to 7
move 8 from 5 to 7
move 1 from 1 to 9
move 1 from 6 to 4
move 1 from 5 to 4
move 1 from 4 to 8
move 5 from 3 to 4
move 10 from 9 to 6
move 3 from 6 to 2
move 7 from 6 to 5
move 6 from 5 to 4
move 1 from 8 to 5
move 1 from 1 to 4
move 2 from 7 to 2
move 5 from 4 to 9
move 2 from 5 to 8
move 1 from 1 to 3
move 2 from 1 to 7
move 6 from 7 to 9
move 9 from 9 to 8
move 1 from 1 to 3
move 4 from 2 to 7
move 11 from 7 to 3
move 11 from 8 to 6
move 7 from 3 to 1
move 4 from 7 to 2
move 3 from 2 to 9
move 8 from 1 to 5
move 2 from 7 to 5
move 2 from 2 to 9
move 2 from 3 to 9
move 11 from 4 to 7
move 7 from 9 to 5
move 6 from 6 to 5
move 2 from 2 to 9
move 1 from 2 to 3
move 6 from 9 to 4
move 3 from 9 to 1
move 4 from 3 to 5
move 6 from 7 to 1
move 2 from 6 to 3
move 2 from 9 to 2
move 3 from 3 to 2
move 3 from 6 to 8
move 2 from 7 to 5
move 20 from 5 to 6
move 8 from 5 to 1
move 1 from 5 to 9
move 2 from 8 to 4
move 1 from 8 to 7
move 16 from 1 to 8
move 8 from 8 to 9
move 4 from 2 to 4
move 1 from 1 to 5
move 1 from 5 to 4
move 3 from 8 to 4
move 14 from 4 to 6
move 5 from 8 to 7
move 6 from 7 to 8
move 29 from 6 to 2
move 3 from 9 to 8
move 21 from 2 to 3
move 1 from 8 to 3
move 6 from 9 to 4
move 8 from 3 to 5
move 7 from 8 to 4
move 7 from 3 to 9
move 3 from 7 to 2
move 12 from 4 to 8
move 2 from 3 to 1
move 2 from 9 to 1
move 1 from 6 to 7
move 1 from 7 to 6
move 1 from 6 to 3
move 3 from 1 to 8
move 2 from 4 to 1
move 4 from 6 to 1
move 5 from 2 to 7
move 1 from 1 to 2
move 5 from 1 to 2
move 2 from 8 to 1
move 1 from 4 to 5
move 9 from 8 to 4
move 3 from 7 to 9
move 7 from 5 to 7
move 2 from 5 to 9
move 4 from 9 to 2
move 3 from 3 to 2
move 5 from 2 to 7
move 2 from 8 to 2
move 2 from 7 to 3
move 1 from 8 to 6
move 2 from 1 to 2
move 1 from 6 to 7
move 1 from 8 to 1
move 12 from 7 to 1
move 5 from 2 to 7
move 7 from 4 to 2
move 2 from 4 to 1
move 5 from 3 to 8
move 7 from 1 to 9
move 4 from 7 to 1
move 7 from 1 to 5
move 12 from 9 to 2
move 27 from 2 to 4
move 3 from 8 to 9
move 6 from 2 to 5
move 6 from 1 to 8
move 1 from 7 to 6
move 9 from 5 to 2
move 3 from 9 to 2
move 13 from 4 to 5
move 10 from 2 to 7
move 1 from 9 to 8
move 11 from 5 to 7
move 1 from 8 to 7
move 1 from 2 to 6
move 13 from 4 to 3
move 23 from 7 to 4
move 1 from 6 to 9
move 1 from 2 to 4
move 7 from 3 to 5
move 1 from 9 to 8
move 19 from 4 to 1
move 2 from 4 to 1
move 1 from 7 to 6
move 1 from 4 to 5
move 1 from 5 to 7
move 11 from 5 to 1
move 2 from 5 to 4
move 2 from 6 to 9
move 3 from 8 to 2
move 2 from 8 to 1
move 3 from 2 to 1
move 1 from 9 to 5
move 6 from 1 to 3
move 1 from 9 to 7
move 2 from 7 to 5
move 2 from 8 to 6
move 1 from 3 to 2
move 2 from 8 to 5
move 1 from 2 to 1
move 3 from 4 to 1
move 3 from 5 to 1
move 2 from 5 to 1
move 2 from 6 to 9
move 1 from 9 to 6
move 1 from 4 to 5
move 1 from 9 to 8
move 1 from 8 to 6
move 8 from 1 to 6
move 7 from 1 to 8
move 9 from 1 to 6
move 1 from 5 to 3
move 3 from 8 to 4
move 11 from 3 to 4
move 1 from 3 to 6
move 10 from 6 to 8
move 13 from 1 to 6
move 3 from 4 to 5
move 7 from 8 to 6
move 3 from 8 to 5
move 6 from 5 to 3
move 22 from 6 to 9
move 4 from 3 to 6
move 4 from 9 to 5
move 1 from 1 to 5
move 2 from 3 to 4
move 2 from 1 to 5
move 1 from 9 to 2
move 5 from 8 to 3
move 2 from 9 to 2
move 11 from 6 to 9
move 3 from 2 to 7
move 1 from 6 to 7
move 12 from 9 to 8
move 4 from 7 to 1
move 12 from 4 to 8
move 2 from 4 to 7
move 1 from 1 to 8
move 1 from 5 to 1
move 19 from 8 to 4
move 4 from 5 to 1
move 1 from 7 to 4
move 1 from 7 to 1
move 3 from 3 to 4
move 2 from 8 to 4
move 1 from 5 to 7
move 1 from 7 to 9
move 8 from 1 to 8
move 1 from 1 to 4
move 1 from 3 to 9
move 1 from 3 to 5
move 1 from 5 to 2
move 7 from 8 to 7
move 16 from 4 to 7
move 1 from 7 to 4
move 3 from 8 to 2
move 14 from 7 to 4
move 1 from 5 to 8
move 5 from 7 to 5
move 16 from 4 to 5
move 3 from 5 to 4
move 3 from 2 to 1
move 1 from 7 to 9
move 11 from 4 to 2
move 3 from 8 to 6
move 2 from 1 to 8
move 1 from 4 to 9
move 18 from 5 to 1
move 1 from 8 to 7
move 3 from 7 to 9
move 18 from 9 to 3
move 3 from 6 to 9
move 7 from 1 to 6
move 1 from 8 to 4
move 1 from 4 to 9
move 3 from 6 to 4
move 5 from 9 to 2
move 2 from 4 to 7
move 7 from 2 to 8
move 1 from 7 to 3
move 2 from 6 to 8
move 1 from 9 to 5
move 1 from 6 to 8
move 1 from 4 to 8
move 1 from 5 to 3
move 1 from 7 to 5
move 8 from 8 to 7
move 10 from 2 to 6
move 1 from 9 to 3
move 6 from 6 to 2
move 5 from 6 to 2
move 7 from 2 to 7
move 12 from 1 to 6
move 2 from 2 to 1
move 1 from 2 to 5
move 4 from 7 to 6
move 12 from 3 to 1
move 2 from 7 to 2
move 9 from 3 to 8
move 1 from 2 to 6
move 1 from 5 to 4
move 9 from 6 to 5
move 1 from 7 to 6
move 1 from 4 to 9
move 9 from 6 to 7
move 7 from 8 to 3
move 6 from 3 to 1
move 4 from 8 to 3
move 5 from 3 to 1
move 1 from 9 to 8
move 2 from 8 to 9
move 5 from 5 to 7
move 14 from 7 to 8
move 1 from 9 to 4
move 2 from 2 to 1
move 3 from 5 to 3
move 2 from 3 to 1
move 1 from 4 to 6
move 6 from 8 to 6
move 6 from 8 to 3
move 3 from 6 to 1
move 2 from 8 to 9
move 19 from 1 to 6
move 3 from 9 to 3
move 6 from 3 to 4
move 6 from 6 to 2
move 4 from 3 to 9
move 1 from 7 to 9
move 2 from 5 to 7
move 5 from 9 to 6
move 6 from 7 to 2
move 11 from 2 to 5
move 2 from 7 to 4
move 4 from 4 to 3
move 2 from 4 to 8
move 12 from 1 to 2
move 1 from 8 to 2
move 8 from 5 to 7
move 2 from 4 to 9
move 2 from 7 to 1
move 4 from 2 to 3
move 1 from 8 to 6
move 1 from 1 to 5
move 2 from 9 to 1
move 2 from 7 to 3
move 2 from 5 to 2
move 1 from 5 to 7
move 2 from 7 to 8
move 1 from 5 to 7
move 5 from 3 to 4
move 3 from 1 to 7
move 1 from 2 to 4
move 15 from 6 to 1
move 4 from 4 to 1
move 4 from 2 to 3
move 8 from 3 to 2
move 5 from 2 to 4
move 1 from 8 to 6
move 1 from 8 to 9
move 1 from 3 to 1
move 3 from 7 to 3
move 5 from 7 to 6
move 4 from 2 to 9
move 6 from 2 to 6
move 4 from 9 to 6
move 12 from 1 to 5
move 6 from 4 to 1
move 1 from 3 to 6
move 4 from 5 to 8
move 7 from 5 to 3
move 3 from 8 to 2
move 1 from 2 to 3
move 1 from 9 to 5
move 1 from 4 to 5
move 1 from 8 to 5
move 8 from 6 to 9
move 10 from 1 to 4
move 3 from 6 to 1
move 9 from 3 to 6
move 1 from 3 to 8
move 1 from 2 to 4
move 6 from 9 to 1
move 1 from 1 to 4
move 10 from 1 to 6
move 1 from 8 to 6
move 13 from 6 to 7
move 1 from 2 to 1
move 1 from 9 to 6
move 9 from 7 to 5
move 1 from 9 to 4
move 3 from 7 to 1
move 3 from 5 to 6
move 10 from 4 to 7
move 5 from 6 to 5
move 3 from 4 to 5
move 13 from 6 to 9
move 7 from 5 to 3
move 6 from 3 to 2
move 5 from 6 to 4
move 4 from 2 to 8'''
        s = advent2022.Day05.Solution(text.splitlines())

        print('\n')
        s.readStacks()
        s.readInstructions()
        s.executeInstructionsPart2(s.instructions)
        result = s.result(s.stacks)
        self.assertEqual('HRFTQVWNN', result)

    def test_day06_part1(self):
        s = advent2022.Day06.Solution()
        text = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb'''
        print('\n')
        result = s.resultOption1(text, 4)
        print(result)
        self.assertEqual(7, result)

    def test_day06_part1_puzzle(self):
        s = advent2022.Day06.Solution()
        text = '''vftfrfcrfrpptffhnnnsznzgngqgsssczcjcdcssmgmtmnmqnmmfttbdttqtggmgpmmqrqzrzttptpdtpddqfdffgjgzjzczjcjjvttvmmrwmrwwjtwjttnccgbcbjbgjjcvvsqshszhzvhvsstjjljcczmzjmzzdtzzhfhvvvflljtllfqqdmmmhmfhffzhhtgtssqppgcppfjjrnngwwrvrvqvpppcspsrrsqqqlmmpcmcjmmjhmhzzpnnggmjjrprptpccdggcrrwfwggsfggbbqlqflqqcsqqccqzqbbnbmmlzllnhnwwsjsgstgttfdtffzfvzvbzzrlzlppcsctcncrncnjnfnqnvngnzzscslsppdqdbbthhqvqfvqqvccvdcddsllnwnqwwsccjmcjmmfmppnzpzffslffjrfjftftrffwcwppfsftssdwdzzffnwndnvnggbbfbgfbbfmbbjzzdqdtqtfqqpzzqpzpllvrrbqqbcqqzvznzmmwcwtwftwfwtftvtddhldldblbzlbzlllcjjwllvcllqplqplpzlzqzsqzsznnqwnqqrcqqnrrhmmqbqqlbqqrhrrdgrrsqssnwsnswsgsfsbbdhbdbqqtsqsbsmmbtmmghhcththrrnvvnlvvdvwwjwmwbmmvtvztzmtmrmprpvvmbmrbrsbbpsbbtccwgccbctbccjrjcjtccrrdnnwwqrwwjpjtptcpcfpfvfjjtqtnqqvzqqfhfrftrrgqgbqqtwwthwhqwqjqmmlglnlrnlrnnshsmspmmfnnqwqgwqqprpbbjbhjbbfqftfwwjhhcpcgcpcvppgfgcfgffbzbfzbzqzccmppndppspbssnbbpdpjpgpngpnggtztjzjdjhjmmwrmmqhhcvvvltvllvmvpvlplwplpmllgpllczlzpzczwzswwqgqbqppcjjhjddgccfmmctcjcscczzzjzwzjjsccdmdppdrdccmttjpttqvqdqtdqtqhqchhhtbbddmhhwdhdwdjdccnhcnndpdldvldlvddbjdbjbppjbpbssqnqnmmmclcggrmmdnnwmwddvjvdvrvzzglzlnnllhqqrbbcvvdtttdvvnfnqqstszsjsrscspszppfjjfttgqttdpdbbbvnndbdcdqdrdhhdhhdjjjzzhqqrcrvccrvrtvtnvnpppccpdpccjgjmjzzbsbgsbstsbbtdttrqtrrsrdrdcdjcddbcbjcbjbwbbslbbbbnmmtsmmrwrnwwqtqzqpprhrzhrhhldddrpdrpdpwdpwdpwwlmmzssbwswppldlmddphhnfhhczhhqrrdgdjjdttztftzffdvddqnqvvlbbncnffssbnbfnnzbnznhzhdzzrqzzptzppsnsnzntzzfwfzzvrzrbzrbzrbzrrqqltqlqppbwppmvpmvpmmbnnbhbmbdmbbhmmngmgmhgmghhvttzzfvfggrrchrrbffzjzlzsllbqqhqrrmqrrlzzsqzqqmhhmnmtntstnsnhsnnwwpdphhgjhjccbcqcjcbjbttmssqffjzjmzmqqrbbfnffcbfcfzfrzztftntbntttlddvwdvdcdhcdhdbbjfjzjwpbcvlqvcwjrcjssdfmgwrhrjvhpgqsbtzqqdwjrqsjplqjdzdcrtvqlcrfpcgwpjnbpcmbwnwbzhcvjvzzpvqnzdqdgpfrvdpfdmpprmzmghdfjjzfqjqcbplwntzmsrpqclgrqzhlsgwffqqntswnjsmrcpjlsvdrmcwdgqzsbsbvhbszqgwqffcgbqmjrfjdvbpwbrzwbjgvvjchwfscrhrtzbghjlcnsqqhdgqtdcqrrpsbzqvjwptblszrtffhwcvbngnsdjgpscfzwrncwlpfqgwdzffsqmjcbrlffftpvhjchmgmgqvjnpfsjnfzddqjsfqcpjgfrfgrtlmtfqphjfmdcvmghrdqvbbbhlstgpcgmqnwpdjwbrdbntbpncnztmnmzmsjzrwjmccqslngrvbjcjjgcvnvhsslfhwpwtjjcwgzqpdvqrlbttnnwdphztmwcdlvlqggrdprmzdfpbfhmsgqznzjhdqpmhfphqcvbfqmhnfpcvstrhdbtmljnnhqtfnpdwnszfrflsbbqjsvbvggzfhlcljwlrlfnlwlzzllzbqftlwzqsvwlldslnfnnbhlwmhqhrjlqzpdsjlhjncpwtnpnqvjtzzjnmdntmbjbcwphplbcwdfcqbhhnjnjsfplgwbrqpqmghnzvdprtlmgvwhdgpdwfvdtqtnqdvbntmsrhftwvrgwcbvhnwmhfggdzfgbdfqsbngmvjgssclqlhqggwndzzhcrzrmnzggnvbbbpzfdjtnlvlnprjtlljhtdqjlddmjdswjrwhwdbbbrmpwsgpfgnplbtzfzlvgnfrvvnbjtsglbzmtmcjbbjclmjgtdrrbpbbqzqnvrgqssfrwhrtpsbgsvnnfbmqgbvhshmpqtqljlpwptqzprdbgnzmlgtrvgnmmfhtccsvbmsfnlnzwhrmcnwmmhgwclghgmspwjvbgqrbbhhrglstdntwnvcgdcmwgbwrwhsqzsdnqsvmcbzrvtztspshrfmqbtrdtnsqdllqzdcbmvbdswzrrzchqgpgmhvjgwgnpqfwcmchsnqssnnslzwtwvbqjfbhlbdjzjrqjvsshcvcbwhsvvwtmjwjfgszmvfzclbqjhnczqcznprwzjnlgmdgbfjnrqfgvstcldnttbjmhsqgqlmzqtsqngvmdvrwcjtfljzdmnndnrbqnlqtmsqngflwsghzzsfcdnttpblqqhmtgnqmcdfmclsvgnsfpnnfssqzjtdsjbjnnmqhfctlddtwrqlpczlzvhddrtjfwgqhfcvchzqgfhdbfpbvtqcjvchqmwhvwjrbtcjgbfqjdsbfpgjrzvlgqwphshnqrvqsppgsnfswvrzpwmdfmmwntnsddzppffjvbnshhqgwclvtpjzvlbdzblhhmhrmjrpmltglsdffnstsdqwjhnjccqhbdrgnwmpwczflfvsbznpphgpbfzffbcdnbrqbwddlhvgqsdmdhmlzbdztrrswsbvdgptvhhcdtwzqqhzqpswwvftppwvwhrspfqwppjbdlhcchlftjhrpwhtvqhmwwtcbfhgbqzvzdlwlzwcsqgvmmsnhrfmwwpcrjlsgzmgdqstlwbzrzbqfnpqffmjqbqqzcnsqrfstnwjflwlpfgcjwjdvtjslrcpgwsvrbvjtzqvnjlqrvvwjhzbzqqjhcrbdtwqjbtmwfrmcgnbdcrhrvlcgrgtglpfmvpgwbzccddlrbsjzwbgwthhdmjjtpchtsbnnpgqfcpmsrgvqwhcdqzmtzlzbfdgmvtqzzdcrnhtlcwnmhdjtwdsrfnlmwpnfwdrptclvwrnwrnntwwqvfmjgswbtqcvmbfbgstvsntndzhjjnjfblqdqrgchchtgdwtvlqzrlpsqgbltjzjngdscdczwzhnlszpdnvnbrmfmjpdzvjfgvtwtpwdjjfgspbvtdjrwzncdpbsthgcwvvdbbvpvqdqpzjmlzhtjmjwmzsmrcstrsvbccqhppwrtmslggqbgglgrgffrbwzmbghfqclwwgssgghqjgfjgvwjhhwnntnrnhmfslqpmwzlggsbmrjjgfzfpjlvmshfsdjtshdlfzvjtlqwjbbgmnjhrhtpbgvcsjvwzlqvfchhpfwsbhcztmdgfzgsmszwfbvvgmgpqsrbzvtpmpqdvhgrjmmspnswjrjnjqfgjwsfbzhwhtlfwjfdhgsvcwqlbznqlnhsmzwltfwclcwgjdbhqvjbbchmcpptmpdqzwpfwrbmchpbqndtmdrwtcvlmrrnvhnpzwqcwwgmcblzvnzbzsspwchtqvjmphqtzgwdzqlbvgdjbssdjwljhlsjwzrdvqtrzcdwszqgfdwgnqdrmssqqhtblqzdhtqtqmlbbfhzvlbrphcjhzpvvshjffnsjcbgvngnsjmfdbgfzphjc'''
        print('\n')
        result = s.resultOption1(text, 4)
        print(result)
        self.assertEqual(1640, result)

    def test_day06_part2(self):
        s = advent2022.Day06.Solution()
        self.assertEqual(19, s.resultOption1('''mjqjpqmgbljsphdztnvjfqwrcgsmlb''', 14))
        self.assertEqual(23, s.resultOption1('''bvwbjplbgvbhsrlpgdmjqwftvncz''', 14))
        self.assertEqual(23, s.resultOption1('''nppdvjthqldpwncqszvftbrmjlhg''', 14))
        self.assertEqual(29, s.resultOption1('''nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg''', 14))
        self.assertEqual(26, s.resultOption1('''zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw''', 14))

    def test_day06_part2_puzzle(self):
        s = advent2022.Day06.Solution()
        text = '''vftfrfcrfrpptffhnnnsznzgngqgsssczcjcdcssmgmtmnmqnmmfttbdttqtggmgpmmqrqzrzttptpdtpddqfdffgjgzjzczjcjjvttvmmrwmrwwjtwjttnccgbcbjbgjjcvvsqshszhzvhvsstjjljcczmzjmzzdtzzhfhvvvflljtllfqqdmmmhmfhffzhhtgtssqppgcppfjjrnngwwrvrvqvpppcspsrrsqqqlmmpcmcjmmjhmhzzpnnggmjjrprptpccdggcrrwfwggsfggbbqlqflqqcsqqccqzqbbnbmmlzllnhnwwsjsgstgttfdtffzfvzvbzzrlzlppcsctcncrncnjnfnqnvngnzzscslsppdqdbbthhqvqfvqqvccvdcddsllnwnqwwsccjmcjmmfmppnzpzffslffjrfjftftrffwcwppfsftssdwdzzffnwndnvnggbbfbgfbbfmbbjzzdqdtqtfqqpzzqpzpllvrrbqqbcqqzvznzmmwcwtwftwfwtftvtddhldldblbzlbzlllcjjwllvcllqplqplpzlzqzsqzsznnqwnqqrcqqnrrhmmqbqqlbqqrhrrdgrrsqssnwsnswsgsfsbbdhbdbqqtsqsbsmmbtmmghhcththrrnvvnlvvdvwwjwmwbmmvtvztzmtmrmprpvvmbmrbrsbbpsbbtccwgccbctbccjrjcjtccrrdnnwwqrwwjpjtptcpcfpfvfjjtqtnqqvzqqfhfrftrrgqgbqqtwwthwhqwqjqmmlglnlrnlrnnshsmspmmfnnqwqgwqqprpbbjbhjbbfqftfwwjhhcpcgcpcvppgfgcfgffbzbfzbzqzccmppndppspbssnbbpdpjpgpngpnggtztjzjdjhjmmwrmmqhhcvvvltvllvmvpvlplwplpmllgpllczlzpzczwzswwqgqbqppcjjhjddgccfmmctcjcscczzzjzwzjjsccdmdppdrdccmttjpttqvqdqtdqtqhqchhhtbbddmhhwdhdwdjdccnhcnndpdldvldlvddbjdbjbppjbpbssqnqnmmmclcggrmmdnnwmwddvjvdvrvzzglzlnnllhqqrbbcvvdtttdvvnfnqqstszsjsrscspszppfjjfttgqttdpdbbbvnndbdcdqdrdhhdhhdjjjzzhqqrcrvccrvrtvtnvnpppccpdpccjgjmjzzbsbgsbstsbbtdttrqtrrsrdrdcdjcddbcbjcbjbwbbslbbbbnmmtsmmrwrnwwqtqzqpprhrzhrhhldddrpdrpdpwdpwdpwwlmmzssbwswppldlmddphhnfhhczhhqrrdgdjjdttztftzffdvddqnqvvlbbncnffssbnbfnnzbnznhzhdzzrqzzptzppsnsnzntzzfwfzzvrzrbzrbzrbzrrqqltqlqppbwppmvpmvpmmbnnbhbmbdmbbhmmngmgmhgmghhvttzzfvfggrrchrrbffzjzlzsllbqqhqrrmqrrlzzsqzqqmhhmnmtntstnsnhsnnwwpdphhgjhjccbcqcjcbjbttmssqffjzjmzmqqrbbfnffcbfcfzfrzztftntbntttlddvwdvdcdhcdhdbbjfjzjwpbcvlqvcwjrcjssdfmgwrhrjvhpgqsbtzqqdwjrqsjplqjdzdcrtvqlcrfpcgwpjnbpcmbwnwbzhcvjvzzpvqnzdqdgpfrvdpfdmpprmzmghdfjjzfqjqcbplwntzmsrpqclgrqzhlsgwffqqntswnjsmrcpjlsvdrmcwdgqzsbsbvhbszqgwqffcgbqmjrfjdvbpwbrzwbjgvvjchwfscrhrtzbghjlcnsqqhdgqtdcqrrpsbzqvjwptblszrtffhwcvbngnsdjgpscfzwrncwlpfqgwdzffsqmjcbrlffftpvhjchmgmgqvjnpfsjnfzddqjsfqcpjgfrfgrtlmtfqphjfmdcvmghrdqvbbbhlstgpcgmqnwpdjwbrdbntbpncnztmnmzmsjzrwjmccqslngrvbjcjjgcvnvhsslfhwpwtjjcwgzqpdvqrlbttnnwdphztmwcdlvlqggrdprmzdfpbfhmsgqznzjhdqpmhfphqcvbfqmhnfpcvstrhdbtmljnnhqtfnpdwnszfrflsbbqjsvbvggzfhlcljwlrlfnlwlzzllzbqftlwzqsvwlldslnfnnbhlwmhqhrjlqzpdsjlhjncpwtnpnqvjtzzjnmdntmbjbcwphplbcwdfcqbhhnjnjsfplgwbrqpqmghnzvdprtlmgvwhdgpdwfvdtqtnqdvbntmsrhftwvrgwcbvhnwmhfggdzfgbdfqsbngmvjgssclqlhqggwndzzhcrzrmnzggnvbbbpzfdjtnlvlnprjtlljhtdqjlddmjdswjrwhwdbbbrmpwsgpfgnplbtzfzlvgnfrvvnbjtsglbzmtmcjbbjclmjgtdrrbpbbqzqnvrgqssfrwhrtpsbgsvnnfbmqgbvhshmpqtqljlpwptqzprdbgnzmlgtrvgnmmfhtccsvbmsfnlnzwhrmcnwmmhgwclghgmspwjvbgqrbbhhrglstdntwnvcgdcmwgbwrwhsqzsdnqsvmcbzrvtztspshrfmqbtrdtnsqdllqzdcbmvbdswzrrzchqgpgmhvjgwgnpqfwcmchsnqssnnslzwtwvbqjfbhlbdjzjrqjvsshcvcbwhsvvwtmjwjfgszmvfzclbqjhnczqcznprwzjnlgmdgbfjnrqfgvstcldnttbjmhsqgqlmzqtsqngvmdvrwcjtfljzdmnndnrbqnlqtmsqngflwsghzzsfcdnttpblqqhmtgnqmcdfmclsvgnsfpnnfssqzjtdsjbjnnmqhfctlddtwrqlpczlzvhddrtjfwgqhfcvchzqgfhdbfpbvtqcjvchqmwhvwjrbtcjgbfqjdsbfpgjrzvlgqwphshnqrvqsppgsnfswvrzpwmdfmmwntnsddzppffjvbnshhqgwclvtpjzvlbdzblhhmhrmjrpmltglsdffnstsdqwjhnjccqhbdrgnwmpwczflfvsbznpphgpbfzffbcdnbrqbwddlhvgqsdmdhmlzbdztrrswsbvdgptvhhcdtwzqqhzqpswwvftppwvwhrspfqwppjbdlhcchlftjhrpwhtvqhmwwtcbfhgbqzvzdlwlzwcsqgvmmsnhrfmwwpcrjlsgzmgdqstlwbzrzbqfnpqffmjqbqqzcnsqrfstnwjflwlpfgcjwjdvtjslrcpgwsvrbvjtzqvnjlqrvvwjhzbzqqjhcrbdtwqjbtmwfrmcgnbdcrhrvlcgrgtglpfmvpgwbzccddlrbsjzwbgwthhdmjjtpchtsbnnpgqfcpmsrgvqwhcdqzmtzlzbfdgmvtqzzdcrnhtlcwnmhdjtwdsrfnlmwpnfwdrptclvwrnwrnntwwqvfmjgswbtqcvmbfbgstvsntndzhjjnjfblqdqrgchchtgdwtvlqzrlpsqgbltjzjngdscdczwzhnlszpdnvnbrmfmjpdzvjfgvtwtpwdjjfgspbvtdjrwzncdpbsthgcwvvdbbvpvqdqpzjmlzhtjmjwmzsmrcstrsvbccqhppwrtmslggqbgglgrgffrbwzmbghfqclwwgssgghqjgfjgvwjhhwnntnrnhmfslqpmwzlggsbmrjjgfzfpjlvmshfsdjtshdlfzvjtlqwjbbgmnjhrhtpbgvcsjvwzlqvfchhpfwsbhcztmdgfzgsmszwfbvvgmgpqsrbzvtpmpqdvhgrjmmspnswjrjnjqfgjwsfbzhwhtlfwjfdhgsvcwqlbznqlnhsmzwltfwclcwgjdbhqvjbbchmcpptmpdqzwpfwrbmchpbqndtmdrwtcvlmrrnvhnpzwqcwwgmcblzvnzbzsspwchtqvjmphqtzgwdzqlbvgdjbssdjwljhlsjwzrdvqtrzcdwszqgfdwgnqdrmssqqhtblqzdhtqtqmlbbfhzvlbrphcjhzpvvshjffnsjcbgvngnsjmfdbgfzphjc'''
        print('\n')
        result = s.resultOption1(text, 14)
        print(result)
        self.assertEqual(3613, result)


