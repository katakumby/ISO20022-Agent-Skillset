---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Modification Request Status Advice - camt.073.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Modification Request Status Advice - camt.073.001

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Modification Request Status Advice - camt.073.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P572** Intra-balance Movement Modification Request Status Advice - camt.073.001

**P573** Description

**P574** In this example, an accepted status advice as a response to the Amendment Instruction of a Settlement Restriction on Cash sent by Party A is presented.

**P575** Message instance

**P576** <Document>

**P577**        <IntraBalMvmntModReqStsAdvc>

**P578** 		<Id>

**P579** 			<Id>NONREF</Id>

**P580** 		</Id>

**P581** 		<ReqRef>DOC1234</ReqRef>

**P582** 		       <CshAcct>

**P583** 			       <Id>

**P584** 				       <Othr>

**P585** 					       <Id>1000000123</Id>

**P586** 				       </Othr>

**P587** 			       </Id>

**P588** 		</CshAcct>

**P589** 		<CshAcctOwnr>

**P590** 			<Id>

**P591** 				<Id>

**P592** 					<AnyBIC>PRTYABICXXX</AnyBIC>

**P593** 				</Id>

**P594** 			</Id>

**P595** 		</CshAcctOwnr>

**P596** 		<ReqDtls>

**P597** 			<Ref>

**P598** 				<AcctOwnrTxId>REF0123</AcctOwnrTxId>

**P599** 				<MktInfrstrctrTxId>T1390</MktInfrstrctrTxId>

**P600** 			</Ref>

**P601** 			<Prty>

**P602** 				<Nmrc>0003</Nmrc>

**P603** 			</Prty>

**P604** 		</ReqDtls>

**P605** 		<PrcgSts>

**P606** 			<AckdAccptd>

**P607** 				<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P608** 			</AckdAccptd>

**P609** 		</PrcgSts>

**P610** 		<UndrlygIntraBal>

**P611** 			<SttlmAmt>

**P612** 				<AmtWthCcy Ccy="EUR">50000</AmtWthCcy>

**P613** 			</SttlmAmt>

**P614** 			<SttlmDt>

**P615** 				<Dt>2015-01-09</Dt>

**P616** 			</SttlmDt>

**P617** 			<BalFr>

**P618** 				<Tp>

**P619** 					<Prtry>

**P620** 						<Id>DVLR</Id>

**P621** 						<Issr>T2S</Issr>

**P622** 						<SchmeNm>RT</SchmeNm>

**P623** 					</Prtry>

**P624** 				</Tp>

**P625** 			</BalFr>

**P626** 			<BalTo>

**P627** 				<Tp>

**P628** 					<Prtry>

**P629** 						<Id>BLKA</Id>

**P630** 						<Issr>T2S</Issr>

**P631** 						<SchmeNm>RT</SchmeNm>

**P632** 					</Prtry>

**P633** 				</Tp>

**P634** 			</BalTo>

**P635** 			<Prty>

**P636** 				<Nmrc>0004</Nmrc>

**P637** 			</Prty>

**P638** 		</UndrlygIntraBal>

**P639** 	</IntraBalMvmntModReqStsAdvc>

**P640** </Document>

