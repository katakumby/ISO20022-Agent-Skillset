---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "IntraPositionMovementConfirmation semt.015.001.10"]
content_origin: "source-transcription"
---

# IntraPositionMovementConfirmation semt.015.001.10

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / IntraPositionMovementConfirmation semt.015.001.10.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1032** IntraPositionMovementConfirmation semt.015.001.10

**P1033** Description

**P1034** On the 15 January 2019,the account servicer, Dresdner Bank London (DRESGB2L), sends to its customers Dresdner Bank Frankfurt (DRESDEFF) an Intra-Position Movement Confirmation (semt.015.001.06). It is used to confirm the previously requested securities movement.

**P1035** Business Data

**P1036** Transaction Identification: FRTJ123REG1

**P1037** Safekeeping Account: 222S

**P1038** Financial Instrument: GB0987654321

**P1039** Position moved: 4,000,000 from the available to the restricted balance

**P1040** Settlement Date: 15/01/2019

**P1041** Message Instance

**P1042** <IntraPosMvmntConf>

**P1043** 	<AddtlParams>

**P1044** 		<AcctOwnrTxId>FRTJ123REG1</AcctOwnrTxId>

**P1045** 	</AddtlParams>

**P1046** 	<SfkpgAcct>

**P1047** 		<Id>222S</Id>

**P1048** 	</SfkpgAcct>

**P1049** 	<FinInstrmId>

**P1050** 		<ISIN>GB0987654321</ISIN>

**P1051** 	</FinInstrmId>

**P1052** 	<IntraPosDtls>

**P1053** 		<SttldQty>

**P1054** 			<FaceAmt>4000000</FaceAmt>

**P1055** 		</SttldQty>

**P1056** 		<SttlmDt>

**P1057** 			<Dt>2019-01-15</Dt>

**P1058** 		</SttlmDt>

**P1059** 		<BalFr>

**P1060** 			 <Tp>

**P1061** 				<Cd>AVAI</Cd>

**P1062** 		 	</Tp>

**P1063** 		</BalFr>

**P1064** 		<BalTo>

**P1065** 			<Tp>

**P1066** 				<Cd>RSTR</Cd>

**P1067** 			</Tp>

**P1068** 		</BalTo>

**P1069** 	</IntraPosDtls>

**P1070** </IntraPosMvmntConf>

