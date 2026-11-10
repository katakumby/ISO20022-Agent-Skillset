---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Modification Report - camt.081.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Modification Report - camt.081.001

Source: [src-000359](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Modification Report - camt.081.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1150** Intra-balance Movement Modification Report - camt.081.001

**P1151** Description

**P1152** In this example a Statement of pending amendment instructions for all the Intra-Balance Movements executed on the 3rd of February 2015 within the Dedicated Cash Account ‘9000000123’ is depicted.

**P1153** Message instance

**P1154** <Document>

**P1155** 	<IntraBalMvmntModRpt>

**P1156** 		<Id>

**P1157** 			<Id>NONREF</Id> 

**P1158**   		</Id>

**P1159**  		<Pgntn>

**P1160**   			<PgNb>1</PgNb> 

**P1161** 			<LastPgInd>true</LastPgInd> 

**P1162**   		</Pgntn>

**P1163** 		<RptGnlDtls>

**P1164** 			<RptId>T6678</RptId> 

**P1165** 			<RptPrd>

**P1166** 				<FrDtTmToDtTm>

**P1167**   					<FrDtTm>2015-02-03T06:20:15</FrDtTm> 

**P1168**  					<ToDtTm>2015-02-03T06:20:16</ToDtTm> 

**P1169**  				</FrDtTmToDtTm>

**P1170**  			</RptPrd>

**P1171**  			<Frqcy>

**P1172**   				<Cd>DAIL</Cd> 

**P1173**  			</Frqcy>

**P1174**  			<UpdTp>

**P1175**  				<Cd>DELT</Cd> 

**P1176**   			</UpdTp>

**P1177**   			<ActvtyInd>true</ActvtyInd> 

**P1178**   		</RptGnlDtls>

**P1179** 		<RptOrErr>

**P1180** 			<Mods>

**P1181** 				<CshAcct>

**P1182** 					<Id>

**P1183** 						<Othr>

**P1184** 							<Id>9000000123</Id>

**P1185** 						</Othr>

**P1186** 					</Id>

**P1187** 				</CshAcct>

**P1188**  				<CshAcctOwnr>

**P1189** 					<Id>

**P1190** 						<Id>

**P1191** 							<AnyBIC>PBPTYBICXXX</AnyBIC>

**P1192** 						</Id>

**P1193** 					</Id>

**P1194** 				</CshAcctOwnr>

**P1195**  				<PrcgSts>

**P1196**  					<AckdAccptd>

**P1197**  						<NoSpcfdRsn>NORE</NoSpcfdRsn> 

**P1198**   					</AckdAccptd>

**P1199**   				</PrcgSts>

**P1200**  				<Mod>

**P1201**   					<ReqRef>DOC5522</ReqRef> 

**P1202**   					<StsDt>2015-02-03T17:30:47-05:00</StsDt> 

**P1203**  					<ReqDtls>

**P1204**  						<Ref>

**P1205**   							<MktInfrstrctrTxId>1395</MktInfrstrctrTxId> 

**P1206**   						</Ref>

**P1207**  						<Lkg>

**P1208**   							<Cd>UNLK</Cd> 

**P1209**   						</Lkg>

**P1210**  						<Lnkgs>

**P1211**  							<Ref>

**P1212**   							<SctiesSttlmTxId>REF1157</SctiesSttlmTxId> 

**P1213**  							</Ref>

**P1214**  							<RefOwnr>

**P1215**   								<AnyBIC>PBPTYBICXXX</AnyBIC> 

**P1216**   							</RefOwnr>

**P1217**   						</Lnkgs>

**P1218**   					</ReqDtls>

**P1219**  					<UndrlygIntraBal>

**P1220**  						<SttlmAmt>

**P1221**   							<AmtWthCcy Ccy="EUR">500000</AmtWthCcy> 

**P1222**   						</SttlmAmt>

**P1223**  						<SttlmDt>

**P1224**   							<Dt>2015-02-03</Dt> 

**P1225**   						</SttlmDt>

**P1226**  						<BalFr>

**P1227** 							<Tp>

**P1228**   								<Prtry>

**P1229**     									<Id>DVLR</Id> 

**P1230**       									<Issr>T2S</Issr> 

**P1231**       									<SchmeNm>RT</SchmeNm> 

**P1232**    								</Prtry>

**P1233**    							</Tp>

**P1234**   						</BalFr>

**P1235**   						<BalTo>

**P1236**  							<Tp>

**P1237**   								<Prtry>

**P1238**      									<Id>RSV1</Id> 

**P1239**       									<Issr>T2S</Issr> 

**P1240**       									<SchmeNm>RT</SchmeNm> 

**P1241**     								</Prtry>

**P1242**   							</Tp>

**P1243**   						</BalTo>

**P1244**   						<CshSubBalId>

**P1245**       							<Id>7452</Id> 

**P1246**    						</CshSubBalId>

**P1247**   						<Prty>

**P1248**       							<Nmrc>0003</Nmrc> 

**P1249**    						</Prty>

**P1250**   					</UndrlygIntraBal>

**P1251**   				</Mod>

**P1252**   			</Mods>

**P1253**  		</RptOrErr>

**P1254** 	</IntraBalMvmntModRpt>

**P1255** </Document>

