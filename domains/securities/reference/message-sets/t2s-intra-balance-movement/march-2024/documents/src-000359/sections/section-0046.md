---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Status Advice - camt.067.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Status Advice - camt.067.001

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Status Advice - camt.067.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P392** Intra-balance Movement Status Advice - camt.067.001

**P393** Description

**P394** In this example, an accepted status is sent as a response to the setting-up of a Settlement Restriction on Cash Balance requested by Party A (PBPTYBICXXX). Party A requested the blocking of 50000 EUR, using the restriction type ‘BLKA’, within its account ‘9000000123’. The Intended Settlement Date for the restriction is on the 9th of January 2015.

**P395** Message instance

**P396** <Document>

**P397**        <IntraBalMvmntStsAdvc>

**P398** 		<Id>

**P399** 			<Id>NONREF</Id>

**P400** 		</Id>

**P401** 		<TxId>

**P402** 			<AcctOwnrTxId>REF0123</AcctOwnrTxId>

**P403** 			<MktInfrstrctrTxId>T1390</MktInfrstrctrTxId>

**P404** 		</TxId>

**P405** 		<PrcgSts>

**P406** 			<AckdAccptd>

**P407** 				<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P408** 			</AckdAccptd>

**P409** 		</PrcgSts>

**P410** 		<CshAcct>

**P411** 			<Id>

**P412** 				<Othr>

**P413** 					<Id>9000000123</Id>

**P414** 				</Othr>

**P415** 			</Id>

**P416**               </CshAcct>

**P417**               <CshAcctOwnr>

**P418** 	              <Id>

**P419** 		              <Id>

**P420** 			              <AnyBIC>PBPTYBICXXX</AnyBIC>

**P421** 		              </Id>

**P422** 	              </Id>

**P423**               </CshAcctOwnr>

**P424**               <UndrlygIntraBal>

**P425** 	              <SttlmAmt>

**P426** 				<AmtWthCcy Ccy="EUR">50000</AmtWthCcy>

**P427** 			</SttlmAmt>

**P428** 			<SttlmDt>

**P429** 				<Dt>2015-01-09</Dt>

**P430** 			</SttlmDt>

**P431** 			<BalFr>

**P432** 				<Tp>

**P433** 					<Prtry>

**P434** 						<Id>DLVR</Id>

**P435** 						<Issr>T2S</Issr>

**P436** 						<SchmeNm>RT</SchmeNm>

**P437** 					</Prtry>

**P438** 				</Tp>

**P439** 			</BalFr>

**P440** 			<BalTo>

**P441** 				<Tp>

**P442** 					<Prtry>

**P443** 						<Id>BLKA</Id>

**P444** 						<Issr>T2S</Issr>

**P445** 						<SchmeNm>RT</SchmeNm>

**P446** 					</Prtry>

**P447** 				</Tp>

**P448** 			</BalTo>

**P449**               </UndrlygIntraBal>

**P450** 	</IntraBalMvmntStsAdvc>

**P451** </Document>

