---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionMovementConfirmation seev.036.00x.17"]
content_origin: "source-transcription"
---

# CorporateActionMovementConfirmation seev.036.00x.17

Source: [src-000079](../../../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Locator: heading path Business Examples / CorporateActionMovementConfirmation seev.036.00x.17.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1156** CorporateActionMovementConfirmation seev.036.00x.17

**P1157** Description

**P1158** This example describes a CorporateActionMovementConfirmation sent by an account servicer on payment date and containing confirmation of the movements of a dividend option event.

**P1159** The CorporateActionMovementConfirmation sample message illustrates a confirmation based on the announced event illustrated in the example 1 of the CorporateActionNotification section and based on the instruction illustrated in the example 1 of the CorporateActionInstruction section.

**P1160** The corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash.

**P1161** Business Data

**P1162** Issue name

**P1163** Glaxo Holdings

**P1164** ISIN GB0007123466

**P1165** Terms

**P1166** Final dividend of GBP 0,017 per share, OR one ordinary share for every 37 shares held. Elections cannot be made on holdings of less than 37 shares.

**P1167** Elections which give rise to fractional entitlements will be rounded down to the nearest whole multiple of 37 shares; the full cash dividend of GBP 0,017 per share will be paid on the remainder of the holding.

**P1168** Relative dates

**P1169** Ex date - 01 September 2010

**P1170** Record date - 07 September 2010

**P1171** Dividend payment date - 02 October 2010

**P1172** Response deadline date - 23 September 2010

**P1173** Transaction description

**P1174** A/C 98-0112441-05 has an underlying balance of 80,000 shares.

**P1175** Message Instance (with application header)

**P1176** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P1177** 	<Fr>

**P1178** 		<FIId>

**P1179** 			<FinInstnId>

**P1180** 				<BICFI>ABCDBEBBXXX</BICFI>

**P1181** 			</FinInstnId>

**P1182** 		</FIId>

**P1183** 	</Fr>

**P1184** 	<To>

**P1185** 		<FIId>

**P1186** 			<FinInstnId>

**P1187** 				<BICFI>WXYZFRPP666</BICFI>

**P1188** 			</FinInstnId>

**P1189** 		</FIId>

**P1190** 	</To>

**P1191** 	<BizMsgIdr>LOCCUS00000000198</BizMsgIdr>

**P1192** 	<MsgDefIdr>seev.036.001.17</MsgDefIdr>

**P1193** 	<CreDt>2010-10-02T14:30:00Z</CreDt>

**P1194** </AppHdr>

**P1195** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.036.001.17" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P1196** </Document>

**P1197** 	<CorpActnMvmntConf>

**P1198** 		<NtfctnId>

**P1199** 			<Id>LOCCUS000000001</Id>

**P1200** 		</NtfctnId>

**P1201** 		<MvmntPrlimryAdvcId>

**P1202** 			<Id>LOCCUS0000000076</Id>

**P1203** 		</MvmntPrlimryAdvcId>

**P1204** 		<InstrId>

**P1205** 			<Id>GLOCUS0000000001</Id>

**P1206** 		</InstrId>

**P1207** 		<CorpActnGnlInf>

**P1208** 			<CorpActnEvtId>DIVGLAX125</CorpActnEvtId>

**P1209** 			<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P1210** 			<EvtTp>

**P1211** 				<Cd>DVOP</Cd>

**P1212** 			</EvtTp>

**P1213** 			<FinInstrmId>

**P1214** 				<ISIN>GB0007123466</ISIN>

**P1215** 				<Desc>GLAXO HOLDINGS</Desc>

**P1216** 			</FinInstrmId>

**P1217** 		</CorpActnGnlInf>

**P1218** 		<AcctDtls>

**P1219** 			<SfkpgAcct>98-0112441-05</SfkpgAcct>

**P1220** 			<Bal>

**P1221** 				<ConfdBal>

**P1222** 					<Bal>

**P1223** 						<ShrtLngPos>LONG</ShrtLngPos>

**P1224** 						<QtyChc>

**P1225** 							<Qty>

**P1226** 								<Unit>80000</Unit>

**P1227** 							</Qty>

**P1228** 						</QtyChc>

**P1229** 					</Bal>

**P1230** 				</ConfdBal>

**P1231** 				<TtlElgblBal>

**P1232** 					<Bal>

**P1233** 						<QtyChc>

**P1234** 							<SgndQty>

**P1235** 								<ShrtLngPos>LONG</ShrtLngPos>

**P1236** 								<Qty>

**P1237** 									<Unit>80000</Unit>

**P1238** 								</Qty>

**P1239** 							</SgndQty>

**P1240** 						</QtyChc>

**P1241** 					</Bal>

**P1242** 				</TtlElgblBal>

**P1243** 			</Bal>

**P1244** 		</AcctDtls>

**P1245** 		<CorpActnConfDtls>

**P1246** 			<OptnNb>

**P1247** 				<Nb>002</Nb>

**P1248** 			</OptnNb>

**P1249** 			<OptnTp>

**P1250** 				<Cd>SECU</Cd>

**P1251** 			</OptnTp>

**P1252** 			<SctiesMvmntDtls>

**P1253** 				<FinInstrmId>

**P1254** 					<ISIN>GB0007633421</ISIN>

**P1255** 					<Desc>GLAXO WELLCOME</Desc>

**P1256** 				</FinInstrmId>

**P1257** 				<CdtDbtInd>CRDT</CdtDbtInd>

**P1258** 				<PstngQty>

**P1259** 					<Qty>

**P1260** 						<Unit>2162</Unit>

**P1261** 					</Qty>

**P1262** 				</PstngQty>

**P1263** 				<FrctnDspstn>

**P1264** 					<Cd>CINL</Cd>

**P1265** 				</FrctnDspstn>

**P1266** 				<DtDtls>

**P1267** 					<PstngDt>2010-10-02</PstngDt>

**P1268** 				</DtDtls>

**P1269** 				<RateDtls>

**P1270** 					<AddtlQtyForExstgScties>

**P1271** 						<QtyToQty>

**P1272** 							<Qty1>1</Qty1>

**P1273** 							<Qty2>37</Qty2>

**P1274** 						</QtyToQty>

**P1275** 					</AddtlQtyForExstgScties>

**P1276** 				</RateDtls>

**P1277** 			</SctiesMvmntDtls>

**P1278** 			<CshMvmntDtls>

**P1279** 				<CdtDbtInd>CRDT</CdtDbtInd>

**P1280** 				<AmtDtls>

**P1281** 					<PstngAmt Ccy="GBP">0.10</PstngAmt>

**P1282** 					<CshInLieuOfShr Ccy="GBP">0.10</CshInLieuOfShr>

**P1283** 				</AmtDtls>

**P1284** 				<DtDtls>

**P1285** 					<PstngDt>

**P1286** <Dt>2010-10-02</Dt></PstngDt>

**P1287** 					<ValDt>2010-10-02</ValDt>

**P1288** 				</DtDtls>

**P1289** 			</CshMvmntDtls>

**P1290** 		</CorpActnConfDtls>

**P1291** 	</CorpActnMvmntConf>

**P1292** </Document>  


