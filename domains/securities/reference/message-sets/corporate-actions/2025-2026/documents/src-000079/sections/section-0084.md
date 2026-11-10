---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionMovementPreliminaryAdvice seev.035.00x.17 – 2"]
content_origin: "source-transcription"
---

# CorporateActionMovementPreliminaryAdvice seev.035.00x.17 – 2

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path Business Examples / CorporateActionMovementPreliminaryAdvice seev.035.00x.17 – 2.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P989** CorporateActionMovementPreliminaryAdvice seev.035.00x.17 – 2

**P990** Description

**P991** This example describes a CorporateActionMovementPreliminaryAdvice sent by an account servicer to pre-advice the account owner about an upcoming reversal of the movements which were previously confirmed by a confirmation message.

**P992** The reason indicated for the reversal is that the payment currency was incorrect. The reversal movement pre-advice provides the opposite movements that were previously confirmed in the confirmation that is, credits in the confirmation are shown as debits in this reversal pre-advice and conversely.

**P993** The CorporateActionMovementPreliminaryAdvice sample message illustrates a reversal preliminary advice based on the confirmation illustrated in the example 1 of the CorporateActionMovementConfirmation section.

**P994** The corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash.

**P995** Business Data

**P996** Issue name

**P997** Glaxo Holdings

**P998** ISIN GB0007123466

**P999** Terms

**P1000** Final dividend of GBP 0,017 per share, OR one ordinary share for every 37 shares held. Elections cannot be made on holdings of less than 37 shares.

**P1001** Elections which give rise to fractional entitlements will be rounded down to the nearest whole multiple of 37 shares; the full cash dividend of GBP 0,017 per share will be paid on the remainder of the holding.

**P1002** Relative dates

**P1003** Ex date - 01 September 2010

**P1004** Record date - 07 September 2010

**P1005** Dividend payment date - 02 October 2010

**P1006** Response deadline date - 23 September 2010

**P1007** Transaction description

**P1008** A/C 98-0112441-05 has an underlying balance of 80,000 shares.

**P1009** Message Instance (with application header)

**P1010** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P1011** 	<Fr>

**P1012** 		<FIId>

**P1013** 			<FinInstnId>

**P1014** 				<BICFI>ABCDBEBBXXX</BICFI>

**P1015** 			</FinInstnId>

**P1016** 		</FIId>

**P1017** 	</Fr>

**P1018** 	<To>

**P1019** 		<FIId>

**P1020** 			<FinInstnId>

**P1021** 				<BICFI>WXYZFRPP666</BICFI>

**P1022** 			</FinInstnId>

**P1023** 		</FIId>

**P1024** 	</To>

**P1025** 	<BizMsgIdr>LOCCUS00000000245</BizMsgIdr>

**P1026** 	<MsgDefIdr>seev.035.001.17</MsgDefIdr>

**P1027** 	<CreDt>2010-10-06T15:30:00Z</CreDt>

**P1028** </AppHdr>

**P1029** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.035.001.17" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P1030** 	<CorpActnMvmntPrlimryAdvc>

**P1031** 		<MvmntPrlimryAdvcGnlInf>

**P1032** 			<Tp>REPL</Tp>

**P1033** 			<Fctn>CAPA</Fctn>

**P1034** 		</MvmntPrlimryAdvcGnlInf>

**P1035** 		<PrvsMvmntPrlimryAdvcId>

**P1036** 			<Id>LOCCUS0000000076</Id>

**P1037** 		</PrvsMvmntPrlimryAdvcId>

**P1038** 		<NtfctnId>

**P1039** 			<Id>LOCCUS000000001</Id>

**P1040** 		</NtfctnId>

**P1041** 		<MvmntConfId>

**P1042** 			<Id>LOCCUS000000391</Id>

**P1043** 		</MvmntConfId>

**P1044** 		<InstrId>

**P1045** 			<Id>GLOCUS0000000001</Id>

**P1046** 		</InstrId>

**P1047** 		<RvslRsn>

**P1048** 			<Rsn>

**P1049** 				<Cd>IPCU</Cd>

**P1050** 			</Rsn>

**P1051** 		</RvslRsn>

**P1052** 		<CorpActnGnlInf>

**P1053** 			<CorpActnEvtId>DIVGLAX123</CorpActnEvtId>

**P1054** 			<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P1055** 			<EvtTp>

**P1056** 				<Cd>DVOP</Cd>

**P1057** 			</EvtTp>

**P1058** 			<MndtryVlntryEvtTp>

**P1059** 				<Cd>CHOS</Cd>

**P1060** 			</MndtryVlntryEvtTp>

**P1061** 			<UndrlygScty>

**P1062** 				<FinInstrmId>

**P1063** 					<ISIN>GB0007123466</ISIN>

**P1064** 					<Desc>GLAXO HOLDINGS</Desc>

**P1065** 				</FinInstrmId>

**P1066** 			</UndrlygScty>

**P1067** 		</CorpActnGnlInf>

**P1068** 		<AcctDtls>

**P1069** 			<AcctsListAndBalDtls>

**P1070** 				<SfkpgAcct>98-0112441-05</SfkpgAcct>

**P1071** 				<Bal>

**P1072** 					<TtlElgblBal>

**P1073** 						<Bal>

**P1074** 							<QtyChc>

**P1075** 								<SgndQty>

**P1076** 									<ShrtLngPos>LONG</ShrtLngPos>

**P1077** 									<Qty>

**P1078** 										<Unit>80000</Unit>

**P1079** 									</Qty>

**P1080** 								</SgndQty>

**P1081** 							</QtyChc>

**P1082** 						</Bal>

**P1083** 					</TtlElgblBal>

**P1084** 				</Bal>

**P1085** 			</AcctsListAndBalDtls>

**P1086** 		</AcctDtls>

**P1087** 		<CorpActnMvmntDtls>

**P1088** 			<OptnNb>002</OptnNb>

**P1089** 			<OptnTp>

**P1090** 				<Cd>SECU</Cd>

**P1091** 			</OptnTp>

**P1092** 			<FrctnDspstn>

**P1093** 				<Cd>CINL</Cd>

**P1094** 			</FrctnDspstn>

**P1095** 			<DfltPrcgOrStgInstr>

**P1096** 				<DfltOptnInd>false</DfltOptnInd>

**P1097** 			</DfltPrcgOrStgInstr>

**P1098** 			<DtDtls>

**P1099** 				<MktDdln>

**P1100** 					<Dt>

**P1101** 						<Dt>2010-09-24</Dt>

**P1102** 					</Dt>

**P1103** 				</MktDdln>

**P1104** 				<RspnDdln>

**P1105** 					<Dt>

**P1106** 						<DtTm>2010-09-23T15:00:00</DtTm>

**P1107** 					</Dt>

**P1108** 				</RspnDdln>

**P1109** 			</DtDtls>

**P1110** 			<SctiesMvmntDtls>

**P1111** 				<SctyDtls>

**P1112** 					<FinInstrmId>

**P1113** 						<ISIN>GB0007633421</ISIN>

**P1114** 						<Desc>GLAXO WELLCOME</Desc>

**P1115** 					</FinInstrmId>

**P1116** 				</SctyDtls>

**P1117** 				<CdtDbtInd>DBIT</CdtDbtInd>

**P1118** 				<EntitldQty>

**P1119** 					<Qty>

**P1120** 						<Unit>2162</Unit>

**P1121** 					</Qty>

**P1122** 				</EntitldQty>

**P1123** 				<DtDtls>

**P1124** 					<PmtDt>

**P1125** 						<Dt>2010-10-02</Dt>

**P1126** 					</PmtDt>

**P1127** 				</DtDtls>

**P1128** 				<RateDtls>

**P1129** 					<AddtlQtyForExstgScties>

**P1130** 						<QtyToQty>

**P1131** 							<Qty1>1</Qty1>

**P1132** 							<Qty2>37</Qty2>

**P1133** 						</QtyToQty>

**P1134** 					</AddtlQtyForExstgScties>

**P1135** 				</RateDtls>

**P1136** 			</SctiesMvmntDtls>

**P1137** 			<CshMvmntDtls>

**P1138** 				<CdtDbtInd>DBIT</CdtDbtInd>

**P1139** 				<AmtDtls>

**P1140** 					<CshInLieuOfShr Ccy="GBP">0.10</CshInLieuOfShr>

**P1141** 					<EntitldAmt Ccy="GBP">0.10</EntitldAmt>

**P1142** 				</AmtDtls>

**P1143** 				<DtDtls>

**P1144** 					<PmtDt>

**P1145** 						<Dt>2010-10-02</Dt>

**P1146** 					</PmtDt>

**P1147** 					<ValDt>

**P1148** 						<Dt>2010-10-02</Dt>

**P1149** 					</ValDt>

**P1150** 				</DtDtls>

**P1151** 			</CshMvmntDtls>

**P1152** 		</CorpActnMvmntDtls>

**P1153** 	</CorpActnMvmntPrlimryAdvc>

**P1154** </Document>

**P1155**   


