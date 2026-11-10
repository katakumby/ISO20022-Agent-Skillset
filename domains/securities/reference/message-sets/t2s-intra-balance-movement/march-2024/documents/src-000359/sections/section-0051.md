---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", " Intra-balance Movement Cancellation Request Status Advice - camt.075.001"]
content_origin: "source-transcription"
---

#  Intra-balance Movement Cancellation Request Status Advice - camt.075.001

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples /  Intra-balance Movement Cancellation Request Status Advice - camt.075.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P699**  Intra-balance Movement Cancellation Request Status Advice - camt.075.001

**P700** Description 

**P701** This example refers to the usage of a status advice message, sent by T2S, when the Cancellation Instruction of an Intra-balance movement is valid. A Cancellation Instruction of an Intra-balance movement is valid and accepted by T2S if it passes the business validation process.

**P702** Message instance

**P703** <Document>

**P704**        <IntraBalMvmntCxlReqStsAdvc>

**P705** 	       <Id>

**P706** 		       <Id>NONREF</Id>

**P707** 	       </Id>

**P708** 		<ReqRef>MSG410</ReqRef>

**P709** 		<TxId>

**P710** 			<AcctOwnrTxId>REF0123</AcctOwnrTxId>

**P711** 			<MktInfrstrctrTxId>T1390</MktInfrstrctrTxId>

**P712** 		</TxId>

**P713** 		<PrcgSts>

**P714** 			<AckdAccptd>

**P715** 				<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P716** 			</AckdAccptd>

**P717** 		</PrcgSts>

**P718** 		<CshAcct>

**P719** 			<Id>

**P720** 				<Othr>

**P721** 					<Id>1000000123</Id>

**P722** 				</Othr>

**P723** 			</Id>

**P724** 		</CshAcct>

**P725** 		<CshAcctOwnr>

**P726** 			<Id>

**P727** 				<Id>

**P728** 					<AnyBIC>PBPTYBICXXX</AnyBIC>

**P729** 				</Id>

**P730** 			</Id>

**P731** 		</CshAcctOwnr>

**P732** 		<UndrlygIntraBal>

**P733** 			<SttlmAmt>

**P734** 				<AmtWthCcy Ccy="EUR">50000</AmtWthCcy>

**P735** 			</SttlmAmt>

**P736** 			<SttlmDt>

**P737** 				<Dt>2015-01-09</Dt>

**P738** 			</SttlmDt>

**P739** 			<BalFr>

**P740** 				<Tp>

**P741** 					<Prtry>

**P742** 						<Id>DLVR</Id>

**P743** 						<Issr>T2S</Issr>

**P744** 						<SchmeNm>RT</SchmeNm>

**P745** 					</Prtry>

**P746** 				</Tp>

**P747** 			</BalFr>

**P748** 			<BalTo>

**P749** 				<Tp>

**P750** 					<Prtry>

**P751** 						<Id>BLKA</Id>

**P752** 						<Issr>T2S</Issr>

**P753** 						<SchmeNm>RT</SchmeNm>

**P754** 					</Prtry>

**P755** 				</Tp>

**P756** 			</BalTo>

**P757** 		</UndrlygIntraBal>

**P758** 	</IntraBalMvmntCxlReqStsAdvc>

**P759** </Document>

