---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Cancellation Request - camt.074.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Cancellation Request - camt.074.001

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Cancellation Request - camt.074.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P641** Intra-balance Movement Cancellation Request - camt.074.001

**P642** Description

**P643** In this example Party A (PBPTYBICXXX), has requested the cancellation of the Intra-balance movement with an account owner transaction id, ‘REF0123’. The Market Infrastructure transaction Identification of the 'to be' cancelled Intra-balance movement is ‘T1390’ and refers to a Cash Blocking Settlement Restriction for 50000 EUR, using the restriction type “BLKA” sent by the Party A within its account ‘1000000123’ and Intended Settlement Date on the 9th of January 2015.

**P644** In this example, Party A specifies both references (AcctOwnrTxId and MktInfrstrctrTxId) to refer the Settlement Restriction willing to cancel.

**P645** Message instance

**P648** <Document>

**P649**        <IntraBalMvmntCxlReq>

**P650** 		<Id>

**P651** 			<Id>MSG410</Id>

**P652** 		</Id>

**P653** 		<TxId>

**P654** 			<AcctOwnrTxId>REF0123</AcctOwnrTxId>

**P655** 			<MktInfrstrctrTxId>T1390</MktInfrstrctrTxId>

**P656** 		</TxId>

**P657** 		<CshAcct>

**P658** 			<Id>

**P659** 				<Othr>

**P660** 					<Id>1000000123</Id>

**P661** 				</Othr>

**P662** 			</Id>

**P663** 		</CshAcct>

**P664** 		<CshAcctOwnr>

**P665** 			<Id>

**P666** 				<Id>

**P667** 					<AnyBIC>PRTYABICXXX</AnyBIC>

**P668** 				</Id>

**P669** 			</Id>

**P670** 		</CshAcctOwnr>

**P671** 		<UndrlygIntraBal>

**P672** 			<SttlmAmt>

**P673** 				<AmtWthCcy Ccy="EUR">50000</AmtWthCcy>

**P674** 			</SttlmAmt>

**P675** 			<SttlmDt>

**P676** 				<Dt>2015-01-09</Dt>

**P677** 			</SttlmDt>

**P678** 			<BalFr>

**P679** 				<Tp>

**P680** 					<Prtry>

**P681** 						<Id>DLVR</Id>

**P682** 						<Issr>T2S</Issr>

**P683** 						<SchmeNm>RT</SchmeNm>

**P684** 					</Prtry>

**P685** 				</Tp>

**P686** 			</BalFr>

**P687** 			<BalTo>

**P688** 				<Tp>

**P689** 					<Prtry>

**P690** 						<Id>BLKA</Id>

**P691** 						<Issr>T2S</Issr>

**P692** 						<SchmeNm>RT</SchmeNm>

**P693** 					</Prtry>

**P694** 				</Tp>

**P695** 			</BalTo>

**P696** 		</UndrlygIntraBal>

**P697** 	</IntraBalMvmntCxlReq>

**P698** </Document>

