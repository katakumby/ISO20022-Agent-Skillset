---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "IntraPositionMovementStatusAdvice semt.014.001.09"]
content_origin: "source-transcription"
---

# IntraPositionMovementStatusAdvice semt.014.001.09

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / IntraPositionMovementStatusAdvice semt.014.001.09.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P990** IntraPositionMovementStatusAdvice semt.014.001.09

**P991** Description

**P992** On the 15 January 2019, the account servicer, Dresdner Bank London (DRESGB2L), advises the account owner Dresdner Bank Frankfurt (DRESDEFF) of the status of the previously requested Intra-Position Movement Instruction. This is done with the IntraPositionMovementStatusAdvice (semt.014.001.05).

**P993** Business Data

**P994** Account Owner Transaction Identification: FRTJ123REG1

**P995** Processing Status: Acknowledged/Accepted (no specific reason

**P996** Safekeeping Account: 222s

**P997** Financial Instrument: GB0987654321

**P998** Face Amount: 4,000,000

**P999** Settlement Date: 15/01/2019

**P1000** Position moved: 4,000,000 from the available to the restricted balance

**P1001** Message Instance

**P1002** <IntraPosMvmntStsAdvc>

**P1003** 	<TxId>

**P1004** 		<AcctOwnrTxId>FRTJ123REG1</AcctOwnrTxId>

**P1005** 	</TxId>

**P1006** 	<PrcgSts>

**P1007** 		<AckdAccptd>

**P1008** 			<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P1009** 		</AckdAccptd>

**P1010** 	</PrcgSts>

**P1011** 	<TxDtls>

**P1012** 		<SfkpgAcct>

**P1013** 			<Id>222S</Id>

**P1014** 		</SfkpgAcct>

**P1015** 		<FinInstrmId>

**P1016** 			<ISIN>GB0987654321</ISIN>

**P1017** 		</FinInstrmId>

**P1018** 		<SttlmQty>

**P1019** 			<FaceAmt>4000000</FaceAmt>

**P1020** 		</SttlmQty>

**P1021** 		<SttlmDt>

**P1022** 			<Dt>2019-01-15</Dt>

**P1023** 		</SttlmDt>

**P1024** 		<BalFr>

**P1025** 			<Cd>AVAI</Cd>

**P1026** 		</BalFr>

**P1027** 		<BalTo>

**P1028** 			<Cd>RSTR</Cd>

**P1029** 		</BalTo>

**P1030** 	</TxDtls>

**P1031** </IntraPosMvmntStsAdvc>

