---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Confirmation - camt.068.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Confirmation - camt.068.001

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Confirmation - camt.068.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P452** Intra-balance Movement Confirmation - camt.068.001

**P453** Description

**P454** In this example, the confirmation of the full settlement of the blocking set-up by Party A (PBPTYBICXXX) is presented. Party A requested the blocking of 50000 EUR, using the restriction type ‘BLKA’, within its cash account ‘9000000123’. T2S (in the case of this example) confirms the blocking and assigns it the reference T222.

**P455** Message instance

**P456** <Document>

**P457**        <IntraBalMvmntConf>

**P458** 		<Id>

**P459** 			<Id>NONREF</Id>

**P460** 		</Id>

**P461** 		<AddtlParams>

**P462** 			<AcctOwnrTxId>REF0123</AcctOwnrTxId>

**P463** 			<MktInfrstrctrTxId>T1390</MktInfrstrctrTxId>

**P464** 		</AddtlParams>

**P465** 		<CshAcct>

**P466** 			<Id>

**P467** 				<Othr>

**P468** 					<Id>9000000123</Id>

**P469** 				</Othr>

**P470** 			</Id>

**P471**               </CshAcct>

**P472**               <CshAcctOwnr>

**P473** 	              <Id>

**P474** 		              <Id>

**P475** 			              <AnyBIC>PBPTYBICXXX</AnyBIC>

**P476** 		              </Id>

**P477** 	              </Id>

**P478**               </CshAcctOwnr>

**P479** 		 <IntraBal>

**P480** 			<SttldAmt>

**P481** 				<AmtWthCcy Ccy="EUR">50000</AmtWthCcy>

**P482** 			</SttldAmt>

**P483** 			<SttlmDt>

**P484** 				<DtTm>2015-01-09T20:20:02</DtTm>

**P485** 			</SttlmDt>

**P486** 			<BalFr>

**P487** 				<Tp>

**P488** 					<Prtry>

**P489** 						<Id>DLVR</Id>

**P490** 						<Issr>T2S</Issr>

**P491** 						<SchmeNm>RT</SchmeNm>

**P492** 					</Prtry>

**P493** 				</Tp>

**P494** 			</BalFr>

**P495** 			<BalTo>

**P496** 				<Tp>

**P497** 					<Prtry>

**P498** 						<Id>BLKA</Id>

**P499** 						<Issr>T2S</Issr>

**P500** 						<SchmeNm>RT</SchmeNm>

**P501** 					</Prtry>

**P502** 				</Tp>

**P503** 			</BalTo>

**P504**               <CshSubBalId>

**P505** 	              <Id>T222</Id>

**P506**               </CshSubBalId>

**P507** 		 </IntraBal>

**P508** 	</IntraBalMvmntConf>

**P509** </Document>

