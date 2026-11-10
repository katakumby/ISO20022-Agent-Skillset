---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Query Response - camt.079.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Query Response - camt.079.001

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Query Response - camt.079.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P786** Intra-balance Movement Query Response - camt.079.001

**P787** Description

**P788** In this example an Intra-Balance Movement Query Response containing 4 instructions matching the query criteria corresponding to query reference ‘ID0Q0F001122’ is depicted. This message is sent as a response to an Intra-Balance Movement Query requesting all movements where the dedicated cash account is ‘9000000123’ and the Restriction Reference is ‘567459’.

**P789** Message instance

**P790** <Document>

**P791**        <IntraBalMvmntQryRspn>

**P792** 		<Id>

**P793** 			<Id>NONREF</Id>

**P794** 		</Id>

**P795** 		<Pgntn>

**P796** 			<PgNb>1</PgNb>

**P797** 			<LastPgInd>true</LastPgInd>

**P798** 		</Pgntn>

**P799** 		<RptGnlDtls>

**P800** 			<QryRef>ID0Q0F001122</QryRef>

**P801** 			<QryTp>FULL</QryTp>

**P802** 			<ActvtyInd>true</ActvtyInd>

**P803** 		</RptGnlDtls>

**P804** 		<RptOrErr>

**P805** 			<Mvmnts>

**P806** 			      <CshAcct>

**P807** 				      <Id>

**P808** 						<Othr>

**P809** 							<Id>9000000123</Id>

**P810** 						</Othr>

**P811** 				      </Id>

**P812** 				</CshAcct>

**P813** 				<Mvmnt>

**P814** 					<CshAcctOwnr>

**P815** 						<Id>

**P816** 							<Id>

**P817** 								<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P818** 							</Id>

**P819** 						</Id>

**P820** 						<RspnsblPtyId>

**P821** 							<Id>

**P822** 								<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P823** 							</Id>

**P824** 						</RspnsblPtyId>

**P825** 					</CshAcctOwnr>

**P826** 					<StsAndRsn>

**P827** 						<PrcgSts>

**P828** 							<AckdAccptd>

**P829** 								<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P830** 							</AckdAccptd>

**P831** 						</PrcgSts>

**P832** 						<Sttld/>

**P833** 					</StsAndRsn>

**P834** 					<AcctOwnrTxId>ACCTOWNREF001</AcctOwnrTxId>												<MktInfrstrctrTxId>T2SREF00001234</MktInfrstrctrTxId>

**P835** 					<MvmntDtls>

**P836** 						<BalFr>

**P837** 							<Tp>

**P838** 								<Prtry>

**P839** 									<Id>DLVR</Id>

**P840** 									<Issr>T2S</Issr>

**P841** 									<SchmeNm>RT</SchmeNm>

**P842** 								</Prtry>

**P843** 							</Tp>

**P844** 						</BalFr>

**P845** 						<BalTo>

**P846** 							<Tp>

**P847** 								<Prtry>

**P848** 									<Id>BLK7</Id>

**P849** 									<Issr>T2S</Issr>

**P850** 									<SchmeNm>RT</SchmeNm>

**P851** 								</Prtry>

**P852** 							</Tp>

**P853** 						</BalTo>

**P854** 						<SttlmAmt>

**P855** 							<AmtWthCcy Ccy="EUR">100000</AmtWthCcy>

**P856** 						</SttlmAmt>

**P857** 						<SttldAmt>

**P858** 							<AmtWthCcy Ccy="EUR">100000</AmtWthCcy>

**P859** 						</SttldAmt>

**P860** 						<IntnddSttlmDt>

**P861** 							<Dt>2015-01-13</Dt>

**P862** 						</IntnddSttlmDt>

**P863** 						<FctvSttlmDt>

**P864** 							<Dt>2015-01-13</Dt>

**P865** 						</FctvSttlmDt>

**P866** 						<StsDt>2015-01-13T16:00:01</StsDt>

**P867** 						<CshSubBalId>

**P868** 							<Id>567459</Id>

**P869** 						</CshSubBalId>

**P870** 						<Prty>

**P871** 							<Nmrc>0002</Nmrc>

**P872** 						</Prty>

**P873** 						<MsgOrgtr>

**P874** 							<Id>

**P875** 								<Id>

**P876** 									<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P877** 								</Id>

**P878** 							</Id>

**P879** 							<RspnsblPtyId>

**P880** 								<Id>

**P881** 									<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P882** 								</Id>

**P883** 							</RspnsblPtyId>

**P884** 						</MsgOrgtr>

**P885** 						<CreDtTm>2015-01-09T11:20:23</CreDtTm>

**P886** 					</MvmntDtls>

**P887** 				</Mvmnt>

**P888** 				<Mvmnt>

**P889** 					<CshAcctOwnr>

**P890** 						<Id>

**P891** 							<Id>

**P892** 								<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P893** 							</Id>

**P894** 						</Id>

**P895** 						<RspnsblPtyId>

**P896** 							<Id>

**P897** 								<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P898** 							</Id>

**P899** 						</RspnsblPtyId>

**P900** 					</CshAcctOwnr>

**P901** 					<StsAndRsn>

**P902** 						<PrcgSts>

**P903** 							<AckdAccptd>

**P904** 								<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P905** 							</AckdAccptd>

**P906** 						</PrcgSts>

**P907** 						<Sttld/>

**P908** 					</StsAndRsn>

**P909** 					<AcctOwnrTxId>ACCTOWNREF002</AcctOwnrTxId>

**P910** 					<MktInfrstrctrTxId>T2SREF00005432</MktInfrstrctrTxId>

**P911** 					<MvmntDtls>

**P912** 						<BalFr>

**P913** 							<Tp>

**P914** 								<Prtry>

**P915** 									<Id>DLVR</Id>

**P916** 									<Issr>T2S</Issr>

**P917** 									<SchmeNm>RT</SchmeNm>

**P918** 								</Prtry>

**P919** 							</Tp>

**P920** 						</BalFr>

**P921** 						<BalTo>

**P922** 							<Tp>

**P923** 								<Prtry>

**P924** 									<Id>BLK7</Id>

**P925** 									<Issr>T2S</Issr>

**P926** 									<SchmeNm>RT</SchmeNm>

**P927** 								</Prtry>

**P928** 							</Tp>

**P929** 						</BalTo>

**P930** 						<SttlmAmt>

**P931** 							<AmtWthCcy Ccy="EUR">50000</AmtWthCcy>

**P932** 						</SttlmAmt>

**P933** 						<SttldAmt>

**P934** 							<AmtWthCcy Ccy="EUR">50000</AmtWthCcy>

**P935** 						</SttldAmt>

**P936** 						<IntnddSttlmDt>

**P937** 							<Dt>2015-01-15</Dt>

**P938** 						</IntnddSttlmDt>

**P939** 						<FctvSttlmDt>

**P940** 							<Dt>2015-01-15</Dt>

**P941** 						</FctvSttlmDt>

**P942** 						<StsDt>2015-01-15T11:50:12</StsDt>

**P943** 						<CshSubBalId>

**P944** 							<Id>567459</Id>

**P945** 						</CshSubBalId>

**P946** 						<Prty>

**P947** 							<Nmrc>0002</Nmrc>

**P948** 						</Prty>

**P949** 						<MsgOrgtr>

**P950** 							<Id>

**P951** 								<Id>

**P952** 									<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P953** 								</Id>

**P954** 							</Id>

**P955** 							<RspnsblPtyId>

**P956** 								<Id>

**P957** 									<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P958** 								</Id>

**P959** 							</RspnsblPtyId>

**P960** 						</MsgOrgtr>

**P961** 						<CreDtTm>2015-01-14T10:30:54</CreDtTm>

**P962** 					</MvmntDtls>

**P963** 				</Mvmnt>

**P964** 				<Mvmnt>

**P965** 					<CshAcctOwnr>

**P966** 						<Id>

**P967** 							<Id>

**P968** 								<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P969** 							</Id>

**P970** 						</Id>

**P971** 						<RspnsblPtyId>

**P972** 							<Id>

**P973** 								<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P974** 							</Id>

**P975** 						</RspnsblPtyId>

**P976** 					</CshAcctOwnr>

**P977** 					<StsAndRsn>

**P978** 						<PrcgSts>

**P979** 							<AckdAccptd>

**P980** 								<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P981** 							</AckdAccptd>

**P982** 						</PrcgSts>

**P983** 						<Sttld/>

**P984** 					</StsAndRsn>

**P985** 					<AcctOwnrTxId>ACCTOWNREF003</AcctOwnrTxId>

**P986** 					<MktInfrstrctrTxId>T2SREF00007893</MktInfrstrctrTxId>

**P987** 					<MvmntDtls>

**P988** 						<BalFr>

**P989** 							<Tp>

**P990** 								<Prtry>

**P991** 									<Id>BLK7</Id>

**P992** 									<Issr>T2S</Issr>

**P993** 									<SchmeNm>RT</SchmeNm>

**P994** 								</Prtry>

**P995** 							</Tp>

**P996** 						</BalFr>

**P997** 						<BalTo>

**P998** 							<Tp>

**P999** 								<Prtry>

**P1000** 									<Id>DLVR</Id>

**P1001** 									<Issr>T2S</Issr>

**P1002** 									<SchmeNm>RT</SchmeNm>

**P1003** 								</Prtry>

**P1004** 							</Tp>

**P1005** 						</BalTo>

**P1006** 						<SttlmAmt>

**P1007** 							<AmtWthCcy Ccy="EUR">20000</AmtWthCcy>

**P1008** 						</SttlmAmt>

**P1009** 						<SttldAmt>

**P1010** 							<AmtWthCcy Ccy="EUR">20000</AmtWthCcy>

**P1011** 						</SttldAmt>

**P1012** 						<IntnddSttlmDt>

**P1013** 							<Dt>2015-01-16</Dt>

**P1014** 						</IntnddSttlmDt>

**P1015** 						<FctvSttlmDt>

**P1016** 							<Dt>2015-01-16</Dt>

**P1017** 						</FctvSttlmDt>

**P1018** 						<StsDt>2015-01-16T15:10:32</StsDt>

**P1019** 						<CshSubBalId>

**P1020** 							<Id>567459</Id>

**P1021** 						</CshSubBalId>

**P1022** 						<Prty>

**P1023** 							<Nmrc>0001</Nmrc>

**P1024** 						</Prty>

**P1025** 						<MsgOrgtr>

**P1026** 							<Id>

**P1027** 								<Id>

**P1028** 									<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P1029** 								</Id>

**P1030** 							</Id>

**P1031** 							<RspnsblPtyId>

**P1032** 								<Id>

**P1033** 									<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P1034** 								</Id>

**P1035** 							</RspnsblPtyId>

**P1036** 						</MsgOrgtr>

**P1037** 						<CreDtTm>2015-01-16T09:42:38</CreDtTm>

**P1038** 					</MvmntDtls>

**P1039** 				</Mvmnt>

**P1040** 				<Mvmnt>

**P1041** 					<CshAcctOwnr>

**P1042** 						<Id>

**P1043** 							<Id>

**P1044** 								<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P1045** 							</Id>

**P1046** 						</Id>

**P1047** 						<RspnsblPtyId>

**P1048** 							<Id>

**P1049** 								<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P1050** 							</Id>

**P1051** 						</RspnsblPtyId>

**P1052** 					</CshAcctOwnr>

**P1053** 					<StsAndRsn>

**P1054** 						<PrcgSts>

**P1055** 							<AckdAccptd>

**P1056** 								<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P1057** 							</AckdAccptd>

**P1058** 						</PrcgSts>

**P1059** 						<Sttld/>

**P1060** 					</StsAndRsn>

**P1061** 					<AcctOwnrTxId>ACCTOWNREF006</AcctOwnrTxId>

**P1062** 					<MktInfrstrctrTxId>T2SREF00009571</MktInfrstrctrTxId>

**P1063** 					<MvmntDtls>

**P1064** 						<BalFr>

**P1065** 							<Tp>

**P1066** 								<Prtry>

**P1067** 									<Id>DVLR</Id>

**P1068** 									<Issr>T2S</Issr>

**P1069** 									<SchmeNm>RT</SchmeNm>

**P1070** 								</Prtry>

**P1071** 							</Tp>

**P1072** 						</BalFr>

**P1073** 						<BalTo>

**P1074** 							<Tp>

**P1075** 								<Prtry>

**P1076** 									<Id>BLK7</Id>

**P1077** 									<Issr>T2S</Issr>

**P1078** 									<SchmeNm>RT</SchmeNm>

**P1079** 								</Prtry>

**P1080** 							</Tp>

**P1081** 						</BalTo>

**P1082** 						<SttlmAmt>

**P1083** 							<AmtWthCcy Ccy="EUR">35000</AmtWthCcy>

**P1084** 						</SttlmAmt>

**P1085** 						<SttldAmt>

**P1086** 							<AmtWthCcy Ccy="EUR">35000</AmtWthCcy>

**P1087** 						</SttldAmt>

**P1088** 						<IntnddSttlmDt>

**P1089** 							<Dt>2015-01-21</Dt>

**P1090** 						</IntnddSttlmDt>

**P1091** 						<FctvSttlmDt>

**P1092** 							<Dt>2015-01-21</Dt>

**P1093** 						</FctvSttlmDt>

**P1094** 						<StsDt>2015-01-21T17:20:51</StsDt>

**P1095** 						<CshSubBalId>

**P1096** 							<Id>567459</Id>

**P1097** 						</CshSubBalId>

**P1098** 						<Prty>

**P1099** 							<Nmrc>0004</Nmrc>

**P1100** 						</Prty>

**P1101** 						<MsgOrgtr>

**P1102** 							<Id>

**P1103** 								<Id>

**P1104** 									<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P1105** 								</Id>

**P1106** 							</Id>

**P1107** 							<RspnsblPtyId>

**P1108** 								<Id>

**P1109** 									<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P1110** 								</Id>

**P1111** 							</RspnsblPtyId>

**P1112** 						</MsgOrgtr>

**P1113** 						<CreDtTm>2015-01-20T08:41:05</CreDtTm>

**P1114** 					</MvmntDtls>

**P1115** 				</Mvmnt>

**P1116** 			</Mvmnts>

**P1117** 		</RptOrErr>

**P1118** 	</IntraBalMvmntQryRspn>

**P1119** </Document>

